#import pandas as pd
import openpyxl
from openpyxl import load_workbook, worksheet, Workbook
from openpyxl.styles import Font, Color

wb = openpyxl.load_workbook('ProfileVV.xlsx')
target = wb['Variable vs Variable']
wb.copy_worksheet(target)
print(wb.sheetnames)
#apply font and color
ft=Font(color="FF0000")
ws=wb['Variable vs Variable Copy']
ws['K4'] = "%Pen"
ws['L4']="Index"
ws['K4'].font=ft
ws['L4'].font=ft


wb.save('ProfileVV1.xlsx')
for row in ws.iter_cols(min_col=10, max_col=10, min_row=4,max_row=30):
    for cell in row:
        print(cell.value)
