import mysql.connector 
con = mysql.connector.connect(host="localhost",port="3306",user="utsav",passwd="MySqlPassword2020!",database="Employee")
cur = con.cursor(buffered=True)
try:
    cur.execute("INSERT INTO Computer_1 VALUES (100)")
    con.commit()
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    con.close()
