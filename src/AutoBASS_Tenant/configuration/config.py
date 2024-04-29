from datetime import datetime
from pathlib import Path

conf = {}

conf["workflow"] = [
    ("electrolyte_formulation", "pump_system"),
    ("cell_assembly", "autobass_assembly"),
    ("capacity", "cycling"),
    ("degradationEOL", "degradation_model")
    ] # list of tuples with (quantity, method)

conf["general_meta"] = {
    "name": "AutoBASS - the cell_assembly tenant",
    "description": "The tenant to assemble cells."
    }

conf["method"] = {
    "name": "autobass_assembly",
    "quantity": "cell_assembly",
    "parameters": ["cell_info", "batch_volume"], # e.g. ["temperature", "composition"],
    "limitations": {'cell_info': 
                    {'batteryChemistry': 
                     {'electrolyte': [[{'chemical': {'SMILES': 'w', 'InChIKey': 'ww'}, 'fraction': [{"minimum": 0.0, "maximum":1.0}], 'fraction_type': ['molPerMol']}]], 
                      'anode': {'material': [[{'chemical': {'SMILES': 'w', 'InChIKey': 'ww'}, 'fraction': [{"minimum": 0.0, "maximum":1.0}], 'fraction_type': ['molPerMol']}]], 
                                'mass_loading': [1.0, 1.1, 3.0, 3.1], 'size': [1.7663]}, 
                        'cathode': {'material': [[{'chemical': {'SMILES': 'w', 'InChIKey': 'ww'}, 'fraction': [{"minimum": 0.0, "maximum":1.0}], 'fraction_type': ['molPerMol']}]], 
                                'mass_loading': [1.0, 1.1, 3.0, 3.1], 'size': [1.5386]}, 
                        'separator': {'material': ['Glasfiber'], 'size': [2.0096]}, 
                        'electrolyte_volume': [{"minimum": 0.0, "maximum":80.0, 'step':5}]}, 'batch_volume': [{"minimum": 0.0, "maximum":64.0, 'step':1}]}  # e.g. {"temperature": {"minimum": 10, "maximum": 40}}
    }
}

conf["sleep_time_s"] = 1

conf["FINALES_server_conf"] = {
    "app_title": "FINALES",
    "app_description": "FINALES's description",
    "app_version": "2.0",
    "host": "192.168.31.131",
    "port": 8888
    }

conf["run_method"] = Path(__file__).resolve().parent.joinpath("run_method")

conf["prepare_results"] = Path(__file__).resolve().parent.joinpath("prepare_results")

conf["end_run_time"] = datetime(
    year=2023,
    month=8,
    day=30,
    hour=00,
    minute=00,
    second=00
    )

conf["operator"] = {
    "username": "Bojing",
    "password": "z91VIXquAXpC0iDHOqxT",
    "usergroups": ["BIG-MAP"]
    }

conf["tenant_user"] = {
    "username": "AutoBASS",
    "password": "z91VIXquAXpC0iDHOqxT",
    "usergroups": ["BIG-MAP"]
}