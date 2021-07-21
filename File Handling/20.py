#1)	Write a function to read the content from a text file line by line and display the same on screen.

# f=open('MyCountry.txt')
# content=f.read()
# print(content)
# f.close()

#2)	Write a function to count the number of lines from a text file which is not starting with an alphabet "T".

# def line_count():
#     file = open("MyCountry.txt","r")
#     count=0
#     for line in file:
#         if line[0] not in 'T':
#             count+= 1
#     file.close()
#     print("No of lines not starting with 'T'=",count)

# line_count()

#***************************************************** Output **************************************************************************/

#No of lines not starting with 'T'= 5

# 3)	Write a function to find and display the occurrence of the word "the".

# def count_words():
#     file = open("MyCountry.txt","r")
#     count = 0
#     data = file.read()
#     words = data.split()
#     for word in words:
#         if word =="the" or word =="The":
#             count += 1
#     print(count)
#     file.close()

# count_words()

#***************************************************** Output **************************************************************************/

# 8

#4)	Write a function to write user given sentence at the end of file and display all the contents on the screen.

with open("MyCountry.txt", "a") as file_object:
    a=input("write sentense to add = ")
    
 
    file_object.write(a)
    f=open('MyCountry.txt')
    content=f.read()
    print(content)
    f.close()

#***************************************************** Output **************************************************************************/

# write sentense to add =  India is my country .

# India is a great country where people speak different languages.
# The national language is Hindi. 
# India is full of different religions and cultures but they live together. 
# Thatâ€™s the reasons India is famous for the common saying of â€œunity in diversityâ€œ.
# India is the seventh-largest country in the whole world.
# India has the second-largest population in the world.
# India is also known as Bharat, Hindustan and sometimes Aryavart.
# The great leaders and freedom fighters are from India. India is my country .