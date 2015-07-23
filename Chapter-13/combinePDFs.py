#! python3
# combinePDFs.py - combines all PDFs in the current working directory into
# a single PDF (does NOT skip the first page of all the pdf files you merge)

import PyPDF2, os

#get all the pdf names in your cwd
pdfFiles = [] #empty list
for filename in os.listdir('.'): #returns list of every file in cwd
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

#sort alphabetically
pdfFiles.sort(key=str.lower)

print("The following files are being merged: " + str(pdfFiles))
        

pdfWriter = PyPDF2.PdfFileWriter() #create the pdfWriter object
    # Loop thru all PDF Files
for filename in pdfFiles: #loop through your newly created pdf file list
        #return a file object
    pdfFileObj = open(filename, 'rb') #rb is default read-only mode in binary format
        #create a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  #read the pdf file
        # Loop thru all pages (except first and add them)
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum) #get each page individually
        pdfWriter.addPage(pageObj) #add the page to pdfWriter object
    # Save resulting PDF in a file
pdfOutput = open('pdfs_joined.pdf', 'wb') #make PDF file in write-binary mode
pdfWriter.write(pdfOutput) #write the contents of pdfWriter object to pdf file
pdfOutput.close()

print('Hooray you are done!')
