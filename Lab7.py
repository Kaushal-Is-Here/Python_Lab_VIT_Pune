# """ By using list comprehension, write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]"""



row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
