import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="EmployeeDetails")

cursorObject = mydb.cursor()

cursorObject.execute('select * from Employee where EmployeeID >= 100');
result = cursorObject.fetchall()

for x in result:
    print(x)

mydb.close()