import csv
with open(r'Customer.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    for record in reader:
        print(record)
    
# with open(r'Customer.csv', 'r') as csvfile:
#     reader=csv.DictReader(csvfile)
#     for record in reader:
#         print(record)
    