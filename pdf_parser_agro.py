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

def show_num_pages(FILE):
    """
    Return the number of pages
    
    Args:
    =====
    FILE: str
    a filename or a path to a file
    
    Returns:
    ========
    
    
    """
    pdf_file_obj = open(FILE, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    return(type(pdf_reader.numPages))

print(show_num_pages(FILE))