import csv
# with open(r'Employees.csv','w') as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerow(['EmpId','Emp Name','Salary'])
#     writer.writerow([1,'Ramesh',22001.00])
#     writer.writerow([2,'Rakesh',26501.00])

with open(r'Employees.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['EmpId','Emp Name','Salary'])
    writer.writerow([1,'Ramesh',22001.00])
    writer.writerow([2,'Rakesh',26501.00])



   
