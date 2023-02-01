#TAKE 2 STRINGS FROM THE USER AND THEN REPLACE ALL THE A'S WITH a's 
# AND THEN CONCATENATE THE 2 STRINGS AND PRINT?
str=input()
b=input()
def func(c):
    d=''
    for i in c:
        if c=='A':
            d+='a'
        else:
            d+=i
    return(d)
#main code
str=func(str)
b=func(b)
print(str+b)
