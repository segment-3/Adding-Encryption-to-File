# Drew Rochford
# AIST 2120

#=======================================================================

#import statements and key
import os
import glob
import time
import json

key = 'enigma'

#=======================================================================

# Welcome User
print('---------------------------------'.center(40))
print('---     PDF Encryptinator     ---'.center(40))
print('---------------------------------'.center(40))
print()

#=======================================================================

#define the files that will be encrypted later on
def add_encryption(input_pdf, output_pdf, password):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    
# Create PDF File Reader and Writer objects
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)
    
# Copy each page from the Reader to Writer object 
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
        
# Apply Encryption to the Write object using the key so it can be changed
    pdf_writer.encrypt(password)
    
# Write output PDF files
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

#=======================================================================

# Prevents skipping the main body of code
if __name__ == '__main__' :

#=======================================================================
    
# Source and Destination Folders (Relative Paths)
    indir = './source'
    outdir = './destination'
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    print('-----------------------------------')
    print('Processing folder: '+indir)
    print('Visible files are:')
    for file in glob.glob(indir + '/*'):
        print(' - ' + os.path.basename(file))
        
#=======================================================================

# Fetching only PDFs using glob so only the PDFs get used
    pdfnames = glob.glob(indir + '/*.pdf')

#=======================================================================
    
    # A divider
    print('-----------------------------------')

#=======================================================================

# Get your program to time how long it takes to process a PDF document
# Get your program to store the PDF filename and processing time in a dictionary
    print('Processed files location' + outdir)
    print('Processed files:')
    timedict = {}
    for pdf in pdfnames:
        start = time.time()
        outfile = os.path.join(outdir,'encrypted_'+os.path.basename(pdf))
        print(' - ' + os.path.basename(outfile))
        add_encryption(pdf,outfile,key)
        end = time.time()
        runtime = end - start       
        timedict[pdf] = "{:.2f}".format(runtime)

#=======================================================================

# Write the JSON file out to the correct location   
    with open(os.path.join(outdir,"runningtime_json.txt"), "w") as outfile:
        json.dump(timedict, outfile)
        print('JSON file created')
    print('*** Mission complete ***')

#=======================================================================

# Exit Message
print()
print('---------------------------------'.center(40))
print('---          Complete         ---'.center(40))
print('---------------------------------'.center(40))

#-----------------------------------------------------------------------
