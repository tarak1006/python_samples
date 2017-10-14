from openpyxl import load_workbook
wb = load_workbook(filename = 'teachers.xlsx')
sheet_ranges = wb['range names']
for i in sheet_ranges:
    print(sheet_ranges['A18'])