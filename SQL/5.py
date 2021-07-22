import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    mydb="EmployeeDetails")

cursorObject = mydb.cursor()

studentRecord = "UPDATE Employee SET EmployeeSalary = 23000 WHERE EmployeeName ='Rajesh'"

cursorObject.execute(studentRecord)

mydb.commit()

print(cursorObject.rowcount, "details updated")

mydb.close()