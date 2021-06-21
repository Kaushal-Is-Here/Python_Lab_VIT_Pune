#  Write a Program to Calculate Grade of Student based on Marks obtained.

# /***************************************************** SOLUTION **************************************************************************/


print("Enter Marks Obtained in 5 Subjects: ")
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

tot = A+B+C+D+E
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")

    #***************************************************** Output **************************************************************************/
    
#Enter Marks Obtained in 5 Subjects: 
#90
#92
#95
#96
#98
#Your Grade is A1
