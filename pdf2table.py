import tabula
import pandas as pd
import numpy as np

def pdf2table(pdf_path,page_no)-> list:

    '''
    function will return list of tables
    '''

    # table=tabula.read_pdf('/content/UTCLResultsQ4FY23.pdf',pages=12)
    table=tabula.read_pdf(pdf_path,pages=page_no)

    return table

pdf_path=''
page_no=3
table_dataframe=pdf2table(pdf_path,page_no)[0]