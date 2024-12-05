text = input("enter a string: ")
z = 0
vowels = ('a','e','i','o','u')

for char in text:
    if char in vowels:
        z += 1
print("count of vowels in the string is: " + str(z))
