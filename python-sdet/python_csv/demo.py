import csv
with open(r'demo.csv', 'r') as csvfile:
    reader=csv.reader(csvfile)
    for i in reader:
        header=i
    print(header)
    print(header[1:])
    print(len(header[1:]))
    print(header[0].split(':'))
    print(len(header[0].split(':')[1:]))

    