# WRITE A PROGRAM TO GET THE LIST OF ODD NUMBERS FROM THE LIST OF NUMBERS 
# GIVEN BY USER(USE LIST COMPREHENSION)
l=list(map(int,input().split()))
only_odd = [num for num in l if num % 2 == 1]
print(only_odd)