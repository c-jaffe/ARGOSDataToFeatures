# Name: Select_Example2.py
# Description: Select roads of Class 4 from major roads tin the gnatcatcher habitat study area
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "C:/Advanced_GIS/GISandPython/ArcPyDemo1/Data/SanDiego"
   
# Set local variables
in_features = "majorrds.shp"
out_feature_class = "C:/Advanced_GIS/GISandPython/ArcPyDemo1/Scratch/majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''
   
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)
