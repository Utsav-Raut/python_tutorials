import mysql.connector as conn

# mydb = conn.connect(
#     host = "localhost",
#     user = "root",
#     password = "MySqlPassword2020!"
# )
# print(mydb)

# mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# ================================================

mydb = conn.connect(
    host = "localhost",
    user = "root",
    password = "MySqlPassword2020!",
    database = "ORG"
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM Worker')

for x in mycursor:
    print(x)