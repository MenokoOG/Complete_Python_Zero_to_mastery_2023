"""PDF lesson, Menoko OG, 11-2023"""
import PyPDF2

with open("dummy.pdf", "rb") as file: # rb is read in binary, have to make sure with pdf files.
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    # print(reader.numPages)
    # print(reader.getPage(0))
    # print(page.rotate(180)) # this will produce error, there is no rotate method in the module.
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
