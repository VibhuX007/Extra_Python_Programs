#TAKE LIST OF ELEMENTS FROM THE USER AND FIND THE SQUARE ROOT OF EACH NUMBER IN THE LIST AND STORE IT IN ANOTHER LIST 
# AND PRINT THAT LIST
import math
l=list(map(int,input().split()))
b=[]
for i in l:
    b.append(math.sqrt(i))
    
print(b)