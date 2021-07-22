import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="EmployeeDetails"
)

cursorObject = mydb.cursor()


studentRecord = """INSERT INTO Employee (EmployeeID,EmployeeName,EmployeeDept,EmployeeSalary) VALUES('101','Rajesh','Production','20000')"""


cursorObject.execute(studentRecord)

mydb.commit()

print(cursorObject.rowcount, "details inserted")

mydb.close()

