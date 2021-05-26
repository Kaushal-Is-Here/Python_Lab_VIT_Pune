#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

/***********************************************Solution*******************************************************/

a = int(input("the number of student in div A :"))
b = int(input("the number of student in div B :"))
c = int(input("the number of student in div C :"))
s = a //2 + b//2 + c//2 + a % 2 + b % 2 + c % 2
print("total number of desk are required :" , s)

/***********************************************Output*******************************************************/

the number of student in div A :7
the number of student in div B :8
the number of student in div C :5
total number of desk are required : 11
