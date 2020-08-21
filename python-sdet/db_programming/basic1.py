# first install the connector using : python -m pip install mysql-connector-python
import mysql.connector
# con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
con = mysql.connector.connect(host="localhost",port="3306",user="utsav",passwd="MySqlPassword2020!",database="Employee")
cur = con.cursor(buffered=True)
# cur.execute("INSERT INTO Computer VALUES (1005,'Dell','Vostro',2013)");
cur.execute("Select * from employee_details")
print(cur.rowcount)

cur.close()
con.commit()
con.close()
