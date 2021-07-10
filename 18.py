#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world


q1=input("Enter sequence of words : ")
q2=sorted(set(q1.split(" ")))
print(" ".join(q2))

#***************************************************** Output **************************************************************************/


#Enter sequence of words : hello world again
#again hello world