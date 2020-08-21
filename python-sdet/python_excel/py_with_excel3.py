import openpyxl as xl
wb = xl.load_workbook(r'Employee.xlsx')
ws = wb['Emp']
cells = ws['A1':'C4']
for row in cells:
    for cell in row:
        print(cell.value, end = ' ')
    print()