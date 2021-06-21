#  Write a program to print all prime numbers within the given range.

# /***************************************************** SOLUTION **************************************************************************/


lower = 1
upper = 20

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
            
 #***************************************************** Output **************************************************************************/

# Prime numbers between 1 and 20 are:
#2
#3
#5
#7
#11
#13
#17
#19
