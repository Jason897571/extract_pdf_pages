import PyPDF2
import os


path1 = "C:\pdf" # path for input PDF

file_list = os.listdir(path1) # To get the name list of PDF under path 1


for name in file_list:
    path2 = r"C:\pdf\{name}".format(name=name) # path for each pdf file
    path3 = r"C:\pdf\output\{name}".format(name=name) # path for output PDF
    path3 = path3.replace("_5472"," signature page") # rename the output PDF
    
    
    file = PyPDF2.PdfFileReader(path2) # to read each pdf
    pdfWriter = PyPDF2.PdfFileWriter() # to lunch pdfWriter 
    pdfWriter.addPage(file.getPage(0)) # to get the first page of each pdf

    
    with open(path3,"wb") as f: # to save pdf in under path 3
        pdfWriter.write(f) 
        f.close()
