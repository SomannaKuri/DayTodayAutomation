# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:56:57 2021

@author: somanna.kuri
"""
import glob # Its part of standard system library, not required to install it
from PyPDF2 import PdfFileReader # install using pip/conda install PyPDF2
totalPages = 0 # adding total number of pages from each file
k=0
files=list((glob.glob(r"C:\Users\somanna.kuri\Desktop\WebDevelopmentTraining\Samanvi\*.pdf")))
for i in files:
    pdf = PdfFileReader((open(i,"rb")))
    totalPages.append(pdf.getNumPages())
    totalPages +=pdf.getNumPages()
print("Total number of pages from above directory :")
