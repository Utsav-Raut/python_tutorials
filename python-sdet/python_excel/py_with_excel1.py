import openpyxl as xl
wb = xl.load_workbook(r'Employee.xlsx')
print(wb.sheetnames)
ws = wb['Emp']
print('Type of ws = ',type(ws))
