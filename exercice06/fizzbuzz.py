
for number in range(1, 51) : 
    if number % 5 == 0  and number % 3 == 0:
        print ("fizzbuz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print ("fizz")
    else:
        print(number)