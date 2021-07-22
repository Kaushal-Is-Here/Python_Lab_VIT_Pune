import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="EmployeeDetails"
    )

cursorObject = mydb.cursor()

studentRecord = "DELETE FROM Employee WHERE EmployeeSalary = 23000 "
cursorObject.execute(studentRecord)
mydb.commit()

print(cursorObject.rowcount, "details DELETED")

mydb.close()