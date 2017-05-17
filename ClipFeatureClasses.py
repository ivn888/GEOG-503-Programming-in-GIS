__author__ = 'Qiusheng'

import arcpy
import os

workspace = arcpy.GetParameterAsText(0)
clip_fc = arcpy.GetParameterAsText(1)
output_dir = arcpy.GetParameterAsText(2)

arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
fc_list = arcpy.ListFeatureClasses()
if len(fc_list) == 0:
    arcpy.AddError(workspace + " has no feature classes.")
    quit()

desc = arcpy.Describe(clip_fc)
if desc.path == workspace:
    fc_list.remove(desc.file)
    if len(fc_list) == 0:
        arcpy.AddWarning(workspace + " has no feature classes.")
        quit()

if arcpy.Exists(output_dir) == False:
    arcpy.CreateFolder_management(os.path.split(output_dir)[0],os.path.split(output_dir)[1])

fcount = len(fc_list)
arcpy.SetProgressor("step","Clipping feature classes...",0,fcount,1)

for fc in fc_list:
    arcpy.SetProgressorLabel("Clipping " + fc + " ...")
    out_fc = os.path.join(output_dir,fc)
    arcpy.Clip_analysis(fc,clip_fc,out_fc)
    arcpy.SetProgressorPosition()
    
arcpy.AddMessage("Clipping multiple features completed.")