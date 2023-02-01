nums = []
print("Enter the size of list: ", end="")
total = int(input())
print("Enter", total, "Elements for the list: ", end="")
for i in range(total):
    nums.append(int(input()))

sum = 0
count = 0
for i in range(total):
    if nums[i]%2 == 0:
        sum = sum + nums[i]
        count = count+1

if count==0:
    print("\nEven number is not found in this list!")
else:
    print("\nSum of Even Numbers =", sum)