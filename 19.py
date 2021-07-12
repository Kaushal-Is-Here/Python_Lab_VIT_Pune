#Write a program with function, Find_vowel that prints and counts identified vowels, Write another function main, in main() function accept a string from user then pass accepted complete string or character by character string to the Find_vowel function and then count number of vowels and display identified vowels in that string.
s=input("Enter a String:")
vowels=0
for i in s:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            print(i,end=" ")
            vowels=vowels+1
print("\n Number of vowels are:")
print(vowels)   

#***************************************************** Output **************************************************************************/

# i i a e e 
# Number of vowels are:
# 5