__author__ = 'Qiusheng'

import arcpy
import os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
workspace = arcpy.GetParameterAsText(0)
clip_fc = arcpy.GetParameterAsText(1)
output_dir = arcpy.GetParameterAsText(2)
bool_composite = arcpy.GetParameterAsText(3)

f_ext = ".tif"

ras_composite = "Composite" + f_ext
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
fc_list = arcpy.ListRasters()
fc_count = len(fc_list)

if arcpy.Exists(output_dir) == False:
    arcpy.CreateFolder_management(os.path.split(output_dir)[0],os.path.split(output_dir)[1])

arcpy.env.mask = clip_fc

arcpy.SetProgressor("step","Clipping raster datasets...",0,fc_count,1)
i = 1
for fc in fc_list:
    arcpy.SetProgressorLabel("Clipping " + str(i) + "/" + str(fc_count) +": " + fc + "...")
    out_fc = os.path.join(output_dir,fc.split(".")[0] + f_ext)
    arcpy.env.snapRaster = fc
    out_ras = arcpy.sa.ExtractByMask(fc,clip_fc)
    out_ras = arcpy.sa.ApplyEnvironment(out_ras)
    out_ras.save(out_fc)
    arcpy.SetProgressorPosition()
    i+=1

if bool_composite.lower() == "true":
    arcpy.SetProgressorLabel("Composite rasters ...")
    arcpy.env.workspace = output_dir
    ras_list = arcpy.ListRasters()
    arcpy.CompositeBands_management(ras_list,ras_composite)

arcpy.AddMessage("Clipping raster datasets completed!")
