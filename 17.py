#count frequncy of element


arr = [1, 2, 8, 3, 2, 2, 2, 5, 1];   
#Array fr will store frequencies of element  
fr = [None] * len(arr);  
visited = -1;  
   
for i in range(0, len(arr)):  
    count = 1;  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            count = count + 1;  
            #To avoid counting same element again  
            fr[j] = visited;  
              
    if(fr[i] != visited):  
        fr[i] = count;  
   

print(" Element | Frequency");  

for i in range(0, len(fr)):  
    if(fr[i] != visited):  
        print(str(arr[i]) + "    |    " + str(fr[i]));  

#***************************************************** Output **************************************************************************/
#Element | Frequency
#1    |    2
#2    |    4
#8    |    1
#3    |    1
#5    |    1