def prepare_results(*kwargs):
    """ Prepares the results for posting.
    Input:
    request: FINALES2.server.schemas.Request
    data: Any

    Output:
    formatted_result: FINALES2.server.schemas.Result

    
    """
    outputList:list = []
    resultFormatted:dict = {}
    request = request_info['request']
    batchNumber, cellNumber = _get_current_batch_and_cell_number()
    batchNumber = batchNumber+1
    for i in list(data.keys()):
        reqMethod = request['methods'][0]
        reqParameters = request['parameters'][reqMethod]
        cellNumber = cellNumber+1
        cellUUID = str(uuid.uuid4())
        requestCellInfo: dict = reqParameters['cell_info']
        anodeInfo = requestCellInfo.get("anode_info")
        if anodeInfo == None:
            anodeInfo = FormulationInfo(
                name="Gr",
                preparation_date="unknown",
                batch="1",
                location={
                "address": "KIT, HIU, Ulm",
                "detail_1": "AutoBASS",
                "detail_2": f"Tray_{i}"
                }
            )
        cathodeInfo = requestCellInfo.get("anode_info")
        if cathodeInfo == None:
            cathodeInfo = FormulationInfo(
                name="LNO",
                preparation_date="unknown",
                batch="1",
                location={
                "address": "KIT, HIU, Ulm",
                "detail_1": "AutoBASS",
                "detail_2": f"Tray_{i}"
                }
            )
        cellObj = Cell(
            battery_chemistry=BatteryChemistry(
                electrolyte=reqParameters['cell']['battery_chemistry']['electrolyte'],
                anode={
                        "material": [
                            {
                            "chemical": {
                                "SMILES": "[C]",
                                "InChIKey": "OKTJSMMVPCPJKN-UHFFFAOYSA-N"
                            },
                            "fraction": 1.0,
                            "fraction_type": "molPerMol"
                            }
                        ],
                        "mass_loading": 1.0,
                        "size": 1.7663
                },
                cathode={
                        "material": [
                            {
                            "chemical": {
                                "SMILES": "[Li+].[O-][Ni]=O",
                                "InChIKey": "VROAXDSNYPAOBJ-UHFFFAOYSA-N"
                            },
                            "fraction": 1.0,
                            "fraction_type": "molPerMol"
                            }
                        ],
                        "mass_loading": 1.0,
                        "size": 1.5386
                },
            ),
            separator={
                        "material": "Celgard(R) 2325",
                        "size": 2.0096
                    },
            electrolyte_volume=reqParameters['cell']['electrolyte_volume']
        )
        rating = _compute_rating(data[i]['time_consume'])
        cellOutput = AssemblyOutput(
            cell_info = {
            "cell_name": f'Cell_{cellNumber}',
            "uuid": cellUUID,
            "assembly_date": data[i]['sealing_time'].split('-')[0],
            "batch": f'Batch_{batchNumber}',
            "anode_info": anodeInfo.dict(),
            "cathode_info": cathodeInfo.dict(),
            "electrolyte_info": requestCellInfo['electrolyte_info'],
            "cell_location": {
                "address": "KIT, HIU, Ulm",
                "detail_1": "AutoBASS",
                "detail_2": f"Tray_{i}"
            }
        },
            cell = cellObj.dict(),
            manufacturing_img = data[i]['image'],
            meta = MethodMeta(success = bool(data[i]['success']), rating = rating),
            temperature = 300,
            sealing_time = data[i]['sealing_time']
        )
        outputList.append(cellOutput)
    autoBASSOutput = AutoBASSOutput(
        batch_output = outputList,
        batch_id = request_info['uuid']
    )
    dataPack = autoBASSOutput.dict()
    resultFormatted['data'] = dataPack
    request['method'] = request['methods']
    del request['methods']
    resultFormatted.update(request)
    resultFormatted['request_uuid'] = request_info['uuid']
    return resultFormatted

def _get_current_batch_and_cell_number() -> int:
    with open(FINALES_CELL_CONFIG) as infile:
        finalesAutoBASSConfig = json.load(infile)
    tasks:dict = finalesAutoBASSConfig['tasks']
    postedResults: list = []
    cellFinished:list = []
    for taskId in list(tasks.keys()):
        if tasks[taskId]['result_posted'] == 1:
            postedResults.append(taskId)
            cellFinished.append(tasks[taskId]['batch_volume'])
    return len(postedResults), sum(cellFinished)

def _compute_rating(consume_time:float) -> int:
    standardTime = 3.08 # in mins
    minusCoeffecient = 2.5
    rating = int(5-abs(consume_time-standardTime)*minusCoeffecient)
    return 1 if rating<1 else rating
    