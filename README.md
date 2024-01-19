
    ## ArcGIS Python Toolbox - Layer to KMZ Converter

    This Python script is designed to be used as an ArcGIS Python Toolbox tool. It converts selected feature layers in specified layer groups to KMZ files.

    ### Usage:

    1. **Parameters:**
       - *Group Names:* Specify the target group names separated by ';'.
       - *Output Path:* Specify the folder to save the output KML files.

    2. **Run the Tool:**
       - Execute the script by running the Python Toolbox tool in ArcGIS.
       - Provide the required parameters.

    3. **Output:**
       - KMZ files will be generated in the specified output folder for each selected feature layer.

    ### Notes:

    - This tool assumes that you have an active ArcGIS project with an open map containing the desired layer groups.
    - The tool will create a folder for each specified group in the output path and save individual KMZ files inside those folders.

    ### Troubleshooting:

    - If an error occurs during the conversion of a layer, the tool will display a warning message in the ArcGIS tool dialog.

    For more details, refer to the script comments and the ArcGIS Python API documentation.

    Author: Mohamed Mokashifi
    Date: 19/1/2024
