vowels = 'aeiou'

# take input from the user

str = input("Enter a string: ")

# make it suitable for caseless comparisions

str = str.casefold()

count = {}.fromkeys(vowels,0)

# count the vowels

for char in str:

    if char in count:

        count[char] += 1

print(count)
