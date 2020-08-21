# //
# CREATE FUNCTION Increase_by_100 (NUMBER INT) RETURNS INT
# BEGIN
# RETURN NUMBER+100;
# END
# //
# import mysql.connector 
# con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
# cur = con.cursor()
# cur.execute('SELECT INCREASE_BY_100(%s)',[10])
# print(cur.fetchone())


CREATE PROCEDURE promotion_discount(IN DISCOUNT INT, INOUT PRICE INT)
BEGIN
SET PRICE=PRICE*(1-DISCOUNT/100);
END
import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
args=[10,1000]
res=cur.callproc('promotion_discount',args)
print(res)