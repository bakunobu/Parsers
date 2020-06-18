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
    num_pages: int
    the number of pages in a given pdf-file
    """
    
    pdf_file_obj = open(FILE, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    return(type(pdf_reader.numPages))

# testing
# print(show_num_pages(FILE))
"""
Doesn't work - returns an empty page
pdf_file_obj = open(FILE, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
page_obj = pdf_reader.getPage(22)
print(page_obj.extractText())
"""

# tabula-py
import tabula
import pandas as pd


out_file = 'test.csv'
start_page = 12
end_page = 21


columns = ['indicator',
           'all_2006',
           'all_2016',
           'companies_2006',
           'companies_2016',
           'farmers_and_IE_2006',
           'farmers_and_IE_2016', 
           'farmers_2006',
           'farmers_2016',
           'IE_2006',
           'IE_2016',
           'personal_2006',
           'personal_2016',
           'non_profit_2006',
           'non_profit_2016']


def page_index(* args):
    if len(args) == 1:
        return(args[0])
    else:
        return(f'{args[0]}-{args[1]}')

print(page_index(1, 3))

def pdf_to_csv_conv(params_dict):
    
    '''
    A parser that converts a pdf table to a csv file
    Adjusted for table 1 ('Main Results')
    
    Args:
    =====
    params_dict: dict
        
    Contains:
    =========
    PDF_FILE: str
    a filename or a path to a file
    
    start_page: str
    the first page to be converted (if only one page number
    is given, converts the exact page)
    
    end_page: str (optional)
    the last page to be converted
    
    output_file: str (optional)
    a filename or a path to a file  the information
    should be written to
    a default value is 'test.csv' in the same folder
    
    COLUMNS: list or tuple
    a list of column names
    
    Returns:
    None: None type
    Writes the data to the specified .csv file
    '''
    
    PDF_FILE = params_dict.get('PDF_FILE')
    start_page = params_dict.get('start_page')
    end_page = params_dict.get('end_page', '')
    output_file = params_dict.get('output_file', 'test.csv')
    COLUMNS = params_dict.get('COLUMNS')
    
    
    df = pd.DataFrame(columns=COLUMNS)
    ppages = page_index(start_page, end_page)
    
    tabula.convert_into(PDF_FILE, 'temp.csv', pages=ppages,
                        stream=True, output_format='csv')
