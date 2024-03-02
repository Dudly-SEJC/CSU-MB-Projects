#splitting a pdf by certain pages
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'fifteen.pdf'
pdf = PdfFileReader(pdf_file_path)

pages = [1, 3, 4] #count starts at 0, where 0 = page 1
pdfwriter = PdfFileWriter()

for page_num in pages:
    pdfwriter.addPage(pdf.getPage(page_num))
#out is a variable
with open('output.pdf', 'wb') as out:
    pdfwriter.write(out)

print('PDF file has been split')