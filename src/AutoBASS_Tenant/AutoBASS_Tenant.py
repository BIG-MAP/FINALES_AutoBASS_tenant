# import reference tenant from FINALES
# replace run, update_queue, run_method, post_result
# implement get_results, post_request

import requests
import importlib

from FINALES2.tenants.referenceTenant import Tenant
from FINALES2.schemas import GeneralMetaData, Quantity, ServerConfig, Method
from FINALES2.user_management.classes_user_manager import User
# from FINALES2_schemas.classes_common import * # Temp
# from FINALES2_schemas.classes_common.separator import Separator # Temp
# from FINALES2_schemas.classes_input.cell_assembly import AssemblyInput # Temp
from prepare_results import prepare_results
from run_method import run_method

from configuration.config import conf


# Prepare the tenant inputs
general_meta = GeneralMetaData(**conf["general_meta"])

FINALES_server_config = ServerConfig(**conf["FINALES_server_conf"])

# method = Method(**conf["methode"])
# chemical_1 = Chemical(SMILES="w", InChIKey="ww")
# formulation_component_1 = FormulationComponent(chemical=chemical_1, fraction=0.3, fraction_type="mol/mol")
# electrode_1 = Electrode(material=[formulation_component_1], mass_loading=3.1, size=0.79)
# electrode_2 = Electrode(material=[formulation_component_1], mass_loading=3.1, size=0.79)
# separator = Separator(material="Glasfiber", size=0.9)
# battery_chemistry_1 = BatteryChemistry(electrolyte=[formulation_component_1], anode=electrode_1, cathode=electrode_2)
# cell_1 = Cell(batteryChemistry=battery_chemistry_1, separator=separator, electrolyte_volume=30)
# assemblyInput_1 = AssemblyInput(cell_info=cell_1, batch_volume=30)

# config = assemblyInput_1.dict()
# print(config)

method = Method(**conf['method'])

# quantities = {}
quantities = Quantity(
    name="cell_assembly",
    methods={"autobass_assembly": method},
    is_active=True
)

AutoBASS_Tenant = Tenant(
    general_meta=general_meta,
    quantities={"cell_assembly": quantities},
    sleep_time_s=conf["sleep_time_s"],
    tenant_config=str(conf),
    run_method=run_method,
    prepare_results=prepare_results,
    FINALES_server_config=FINALES_server_config,
    end_run_time=conf["end_run_time"],
    operator=User(**conf["operator"]),
    tenant_user= User(**conf["tenant_user"]),
    tenant_uuid="Sauron"
)

AutoBASS_Tenant.run()

print("AutoBASS_Tenant quantities", AutoBASS_Tenant.quantities)
