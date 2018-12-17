import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'module'))

import openpyxl


def main(event, context):
    print(sys.path)    
    wb = openpyxl.load_workbook(os.path.join(os.path.dirname(__file__), 'test.xlsx'))
    wb.save(os.path.join(os.path.dirname(__file__), 'test.xlsx'))
    return False

if __name__ == '__main__':
    event = {}
    context = {}
    main(event, context)
