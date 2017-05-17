
import os
import sys
import arcpy
from arcpy.mapping import *

input_mxd = arcpy.GetParameterAsText(0)
out_pdf = arcpy.GetParameterAsText(1)
merge = arcpy.GetParameterAsText(2)
existing_pdf = arcpy.GetParameterAsText(3)

mxd = MapDocument(input_mxd)
mxd.dataDrivenPages.exportToPDF(out_pdf)

if merge:
    if arcpy.Exists(existing_pdf):
        existing_pdf_dir = os.path.split(existing_pdf)[0]
        existing_pdf_name = os.path.split(existing_pdf)[1]
        existing_pdf_name_tmp = "tmp_" + existing_pdf_name
        os.chdir(existing_pdf_dir)
        os.rename(existing_pdf_name,existing_pdf_name_tmp)
        pdf_doc = PDFDocumentCreate(existing_pdf)
        pdf_doc.appendPages(os.path.join(existing_pdf_dir,existing_pdf_name_tmp))
        pdf_doc.appendPages(out_pdf)
        pdf_doc.saveAndClose()
        os.remove(os.path.join(existing_pdf_dir,existing_pdf_name_tmp))

del mxd