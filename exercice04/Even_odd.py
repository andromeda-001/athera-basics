def is_even_odd():
    number = int(input("enter a number: "))
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
result = is_even_odd()
print( "this number is " + result )
