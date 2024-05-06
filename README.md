# FINALES_AutoBASS_tenant
**Auto**matic **B**attery **ASS**embling **T**enant

The AutoBASS tenant created for the use with FINALES.

# Related Documents and Links to FINALES

Documents related to the FINALES project and its broader context can be found on the
respective Wiki page of the project:
[https://github.com/BIG-MAP/FINALES2/wiki/General-Information](https://github.com/BIG-MAP/FINALES2/wiki/General-Information)

Links to FINALES:

1. FINALES latest version Github
[https://github.com/BIG-MAP/FINALES2](https://github.com/BIG-MAP/FINALES2)

1. FINALES v1.1.0 Zenodo
[10.5281/zenodo.10987727](10.5281/zenodo.10987727)

1. Schemas of FINALES v1.1.0
[https://github.com/BIG-MAP/FINALES2_schemas](https://github.com/BIG-MAP/FINALES2_schemas)

Further links:

1. Robotic cell assembly to accelerate battery research  
 _Bojing Zhang, Leon Merker, Alexey Sanin, and Helge S. Stein_  
[https://doi.org/10.1039/D2DD00046F](https://doi.org/10.1039/D2DD00046F)

1. Apples to Apples: Shift from Mass Ratio to Additive Molecules per Electrode Area to Optimize Li-Ion Batteries  
_Bojing Zhang, Leon Merker, Monika Vogler, Fuzhan Rahmanian, and Helge S. Stein_  
[10.26434/chemrxiv-2024-6nm0d-v2](10.26434/chemrxiv-2024-6nm0d-v2)


# Description

The AutoBASS tenant handels the request of the cell assembly. It includes one robot for the transport of the cell components, one for transport of the cell to the crimper and one for the disposal of the electrolyte. 

The transport robot is picking up component after component and stacks all in one place, whereas inbetween the electrode and seperator stacking electrolyte is disposed by the second robot. For increased stacking accuracy a foto is taken form each component before placing it and postion is corrected by image recogntion and edge dectection. After stacking all components the transportation robot picks up the cell an places it in the crimper, the crimper is then started automaticlly and the robots takes out the finished cells and drops it in the storage place.
AutoBASS is useable in the automated FINALES mode, where it looks for requests, assembles the cells and post the result, as well as in a manuall mode.

Details can be found in the respective paper.

# Acknowledgements

This project received funding from the European Union’s
[Horizon 2020 research and innovation programme](https://ec.europa.eu/programmes/horizon2020/en)
under grant agreement [No 957189](https://cordis.europa.eu/project/id/957189) (BIG-MAP).
The authors acknowledge BATTERY2030PLUS, funded by the European Union’s Horizon 2020
research and innovation program under grant agreement no. 957213.
This work contributes to the research performed at CELEST (Center for Electrochemical
Energy Storage Ulm-Karlsruhe) and was co-funded by the German Research Foundation (DFG)
under Project ID 390874152 (POLiS Cluster of Excellence).
