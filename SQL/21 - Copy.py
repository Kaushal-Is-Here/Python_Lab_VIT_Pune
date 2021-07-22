# Assignment no 2. Write a Python program to interchange first and last elements in a list.

myList = [1, 7, 3, 90, 23, 4]
print("Initial List : ", myList)

length = len(myList)

temp = myList[0]
myList[0] = myList[length - 1]
myList[length - 1] = temp

print("List after Swapping : ", myList)

#***************************************************** Output **************************************************************************/

# Initial List :  [1, 7, 3, 90, 23, 4]
# List after Swapping :  [4, 7, 3, 90, 23, 1]