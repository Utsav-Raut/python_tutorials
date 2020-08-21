import csv
with open(r'Employees1.csv','w',newline='') as csvfile:
    fields=['EmpId','Emp Name','Salary']
    writer=csv.DictWriter(csvfile,fields)
    writer.writeheader()
    writer.writerow({'EmpId':1,'Emp Name':'Ramesh','Salary':22001.00})
    writer.writerow({'EmpId':2,'Emp Name':'Rakesh','Salary':26501.00})
   
