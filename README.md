# FINALES_AutoBASS_tenant
**Auto**matic **B**attery **ASS**embling **T**enant

The AutoBASS tenant created for the use with FINALES.

# Related Documents and Links to FINALES

Documents related to this project and its broader context can be found on the respective Wiki page of this project: [https://github.com/BIG-MAP/FINALES2/wiki/Links](https://github.com/BIG-MAP/FINALES2/wiki/Links)

Links to the other related tenants and FINALES:

1. FINALES 2 latest version Github
[https://github.com/BIG-MAP/FINALES2](https://github.com/BIG-MAP/FINALES2)

1. FINALES 2 used Version Zenodo
[10.5281/zenodo.10987727](10.5281/zenodo.10987727)

1. Schemas of FINALES 2
[https://github.com/BIG-MAP/FINALES2_schemas](https://github.com/BIG-MAP/FINALES2_schemas)

1. AutoBASS Paper
[https://doi.org/10.1039/D2DD00046F](https://doi.org/10.1039/D2DD00046F)

1. AutoBASS Paper 2
[10.26434/chemrxiv-2024-6nm0d-v2](10.26434/chemrxiv-2024-6nm0d-v2)


# Description

The AutoBASS tenant handels the request of the cell assembly. It includes one robot for the transport of the cell components, one for transport of the cell to the crimper and one for the disposal of the electrolyte. 

The transport robot is picking up component after component and stacks all in one place, whereas inbetween the electrode and seperator stacking electrolyte is disposed by the second robot. For increased stacking accuracy a foto is taken form each component before placing it and postion is corrected by image recogntion and edge dectection. After stacking all components the transportation robot picks up the cell an places it in the crimper, the crimper is then started automaticlly and the robots takes out the finished cells and drops it in the storage place.
AutoBASS is useable in the automated FINALES mode, where it looks for requests, assembles the cells and post the result, as well as in a manuall mode.

Details can be found in the respective paper.

## Acknowledgements

This project received funding from the European Union’s Horizon 2020 research and innovation program under grant agreement no. 957189 (BIG-MAP).
The authors acknowledge BATTERY2030PLUS, funded by the European Union’s Horizon 2020 research and innovation program under grant agreement no. 957213.
This work contributes to the research performed at CELEST (Center for Electrochemical Energy Storage Ulm-Karlsruhe) and was co-funded by the German Research Foundation (DFG) under Project ID 390874152 (POLiS Cluster of Excellence).
