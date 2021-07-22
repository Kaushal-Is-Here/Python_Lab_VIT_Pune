import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="EmployeeDetails"
)

mycursor = mydb.cursor()


studentRecord = """CREATE TABLE Employee (
                   EmployeeID INT NOT NULL,
                   EmployeeName  VARCHAR(20) NOT NULL,
                   EmployeeDept VARCHAR(50),
                   EmployeeSalary VARCHAR(50)
                   )"""


mycursor.execute("CREATE DATABASE 1stdatabase ")

mydb.close()