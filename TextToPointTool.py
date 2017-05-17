__author__ = 'Qiusheng'

import arcpy
import os

infile = arcpy.GetParameterAsText(0)
out_path = arcpy.GetParameterAsText(1)
workspace = os.path.split(out_path)[0]
fc = os.path.split(out_path)[1]

arcpy.env.overwriteOutput = True
arcpy.env.workspace = workspace

pointList =[]

f = open(infile)
for line in f.readlines():
    list1 = line.split(", ")
    point = []
    for item in list1:
        subitem = item.split(": ")
        point.append(subitem[1].strip('\n'))
    pointList.append(point)

prj = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(workspace,fc,"Point",spatial_reference=prj)
arcpy.AddField_management(fc,"Name","string",field_length=50)
arcpy.AddField_management(fc,"LOCID","string",field_length=10)
arcpy.AddField_management(fc,"X","float")
arcpy.AddField_management(fc,"Y","float")

cursor = arcpy.da.InsertCursor(fc,["Id","NAME","LOCID","X","Y","SHAPE@X","SHAPE@Y"])

for point in pointList:
    id = int(point[0])
    name = point[1]
    locid = point[2]
    x = float(point[3])
    y = float(point[4])
    cursor.insertRow([id,name,locid,x,y,x,y])

del cursor