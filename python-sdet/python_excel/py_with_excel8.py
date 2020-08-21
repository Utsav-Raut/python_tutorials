import openpyxl as xl
filepath=r'Employee.xlsx'
wb=xl.load_workbook(filepath)
ws=wb['Emp']
ws.append([4,'Ramesh',37, 'Scientist'])
wb.save(filepath)
