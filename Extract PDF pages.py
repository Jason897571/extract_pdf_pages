import PyPDF2
import os


path1 = r"C:\Users\QB333LP\OneDrive - EY\Desktop\Amaranth\2020\5472"

file_list = os.listdir(path1)

for name in file_list:
    path2 = r"C:\Users\QB333LP\OneDrive - EY\Desktop\Amaranth\2020\5472\{name}".format(name=name)
    path3 = r"C:\Users\QB333LP\OneDrive - EY\Desktop\Amaranth\2020\signature\{name}".format(name=name)
    path3 = path3.replace("_5472"," signature page")
    file = PyPDF2.PdfFileReader(path2)

    pdfWriter = PyPDF2.PdfFileWriter()

    pdfWriter.addPage(file.getPage(0))

    with open(path3,"wb") as f:
        pdfWriter.write(f)
        f.close()
