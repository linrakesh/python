#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     13-04-2018
# Copyright:   (c) acer 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys          #module for terminating 
import glob
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter
def pdf_splitter(path,dest):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = dest+'\{}_page_{}.pdf'.format(fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

if __name__ == '__main__':
    #path = "Computer_Science.pdf"
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()  #source file name
    dest = filedialog.askdirectory()     # destination folder
    pdf_splitter(path,dest)