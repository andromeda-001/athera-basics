import random

random_number = random.randint(1,6)
number_guess = int(input("guess a number: "))
while random_number != number_guess:
    if number_guess < random_number:
        print("too high! try again ")
        number_guess = int(input("guess a number: "))
    elif number_guess > random_number:
        print("too low! try again ")
        number_guess = int(input("guess a number: "))
        
print("barvoo")