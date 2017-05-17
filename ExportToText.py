__author__ = 'Qiush'

import arcpy
import os

#infile = r"C:\Geog503A\lab7\airports.txt"
#fc = "airports.shp"

in_fc = arcpy.GetParameterAsText(0)
fields = arcpy.GetParameterAsText(1)
delimiter = arcpy.GetParameterAsText(2)
out_txt = arcpy.GetParameterAsText(3)

fields = fields.split(";")
arcpy.AddMessage(fields)

cursor = arcpy.da.SearchCursor(in_fc,fields)
num = len(fields)

f = open(out_txt,"w")

if len(delimiter) == 0:
	delimiter = " "

for row in cursor:
    line = ""
    for i in range(0,num):
        line = line + delimiter + fields[i] + "=" + str(row[i])
    line = line[1:] + "\n"
    f.write(line)
f.close()

