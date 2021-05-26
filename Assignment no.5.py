a = int(input("the number of student in div A :"))
b = int(input("the number of student in div B :"))
c = int(input("the number of student in div C :"))
s = a //2 + b//2 + c//2 + a % 2 + b % 2 + c % 2
print("total number of desk are required :" , s)
