# Write a python code to accept Student Information and display Student Information and average marks 


 /***************************************************** SOLUTION **************************************************************************/

roll  =int(input("enter roll of student :")) 
print(roll)
name =input("enter name of student :")
print(name)
physics = int(input("enter marks of physics :"))
print(physics)
chemistry = int(input("enter marks of chemistry :"))
print(chemistry)
maths = int(input("enter marks of maths :"))
print(maths)
avg = float((physics+chemistry+maths)/3) 
print(" average of 3 subject :",avg)

/***************************************************** Output **************************************************************************/


enter roll of student :16
16
enter name of student :A
A
enter marks of physics :100
100
enter marks of chemistry :90
90
enter marks of maths :100
100
 average of 3 subject : 96.66666666666667

