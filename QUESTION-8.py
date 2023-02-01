# WRITE A PROGRAM FOR PRINT THE SQUARES OF ALL THE NUMBERS, EXCEPT THE FACTORS OF 3?
l=[int(i)for i in input().split()]
for i in l:
    if i%3!=0:
        print(i**2)