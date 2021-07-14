import Calu.sum , Calu.sub,Calu.mult, Calu.div,Calu.fact 

print("Enter: \n 1.Sum \n 2.Subtration \n 3.Multiplication \n 4.Division \n 5.Fatorial")

A=int(input("Enter Choice : "))

if A== 1:
    a=int(input("Enter First Number : "))
    b=int(input("Enter First Number : "))
    print(Calu.sum.sum(a,b))
elif A== 2:
    a=int(input("Enter First Number : "))
    b=int(input("Enter First Number : "))
    print(Calu.sub.sub(a,b))    
elif A== 3:
    a=int(input("Enter First Number : "))
    b=int(input("Enter First Number : "))
    print(Calu.mult.mult(a,b))    
elif A== 4:
    a=int(input("Enter First Number : "))
    b=int(input("Enter First Number : "))
    print(Calu.div.div(a,b))
elif A== 5:
    a=int(input("Enter First Number : "))
    print(Calu.fact.fact(a))  
else:
    print("Opps ! you did worong . Correct choice . ")     





