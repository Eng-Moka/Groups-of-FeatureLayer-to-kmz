import arcpy
import os

def Layer_to_kmz(Group_name, layers, output_path):
    # Group_name: Name of the layer group to be converted
    # layers: List of layers as objects
    # output_path: Folder to save the output KML files of layers
    for layer in layers:
        layer_path = f"{os.path.sep}".join((Group_name, layer.name))
        kml_name = "".join((layer.name, ".kmz"))
        kml_folder = f"{os.path.sep}".join((output_path, Group_name))
        if not os.path.exists(kml_folder):
            os.makedirs(kml_folder)
        kml_path = f"{os.path.sep}".join((kml_folder, kml_name))
        try:
            arcpy.conversion.LayerToKML(layer_path, kml_path)
            arcpy.AddMessage(f"Layer: {layer_path} successfully converted")
        except Exception as e:
            arcpy.AddWarning(f"Layer: {layer_path} NOT converted")
            arcpy.AddMessage(f"Error: {e}")
            continue

def all_group_of_current_activemap():
    # A function that returns all GroupLayers as a list of layer objects
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    map = aprx.activeMap
    groups = [layer for layer in map.listLayers() if layer.isGroupLayer]
    return groups

def all_featcuer_layers_of_group(group):
    # group: GroupLayer object
    feature_layers = [layer for layer in group.listLayers() if layer.isFeatureLayer]
    return feature_layers

def get_target_Layer_group(target_groups_name):
    all_groups_in_map = all_group_of_current_activemap()
    return [group for group in all_groups_in_map if group.name in target_groups_name]

def groups_layers_to_kmz(group_names, output_path):
    # group_names: String value of names for all selected groups separated by ';'
    # output_path: Folder to save output KML files of layers
    target_groups_name = group_names.replace("'", "").split(";")
    target_groups_object = get_target_Layer_group(target_groups_name)
    for group in target_groups_object:
        feature_layers = all_featcuer_layers_of_group(group)
        Layer_to_kmz(group.name, feature_layers, output_path)


if __name__ == '__main__':
    # 1st Get the Parameters
    groups_names = arcpy.GetParameterAsText(0)
    output_path = arcpy.GetParameterAsText(1)
    # 2nd Run the groups_layers_to_kmz Function
    groups_layers_to_kmz(groups_names, output_path)
