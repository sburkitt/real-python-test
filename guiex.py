from easygui import * 
from PyPDF2 import PdfFileReader, PdfFileWriter 

file = fileopenbox("","Select PDF for Rotation","*.pdf")
if file is None:
	exit()

#Rotation 
rotate = ('90', '180', '270')
message =('Rotate clockwise _ degrees')
degrees = buttonbox(message, "choose roation", rotate)

#output file
out = filesavebox("","save as", "*.pdf")
while file == out:
    msgbox("cannot overwrite orignal file", "choose another file")
    out = filesavebox("","save as", ".pdf")

if out is None:
    exit()

#read file/rotate 
newfile = PdfFileReader(open(file, "rb"))
out_pdf = PdfFileWriter()

for page_num in range(0, newfile.getNumPages()):
    page = newfile.getPage(page_num)
    page = page.rotateClockwise(int(degrees))
    output_pdf.addPage(page)

outfile = open(out,"wb")
out_pdf.write(outfile)
outfile.close()
    
                     