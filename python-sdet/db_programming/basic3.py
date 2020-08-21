import mysql.connector 
con = mysql.connector.connect(host="localhost",port="3306",user="utsav",passwd="MySqlPassword2020!",database="Employee")
cur = con.cursor(buffered=True)
list_of_age=[31, 39, 43]
for age in list_of_age:
    cur.execute("SELECT * FROM employee_details WHERE age=%(c_id)s",{"c_id":age})
    for i in cur:
        print(i)
cur.close()
con.close()
