import mysql.connector 
con = mysql.connector.connect(host="localhost",port="3306",user="utsav",passwd="MySqlPassword2020!",database="Employee")
cur = con.cursor(buffered=True)
cur.execute("Select * from employee_details")
# print(cur.fetchone())
# print(cur.fetchall())
# print(cur.fetchmany())
print(cur.fetchmany(2))
cur.close()
con.close()
