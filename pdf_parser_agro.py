# Use 2016 Russian Agricultural Census data
FILE = '/home/bakunobu/parsers/VSHP_2016_T1_k1(3).pdf'


# test module PyPDF2
import os
import sys
import re

import PyPDF2

'''
thanks to medium.com/@umerfarooq_26378/python-for-pdf-ef0fac2808b0
'''

pdf_file_obj = open(FILE, 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

print(pdf_reader.numPages)
