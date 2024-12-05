def is_even_odd():
    numbers =[2, 5, 11, 44, 55, 88]
    results = []
    for x in numbers:
        if x % 2 == 0:
            results.append("is even")
        else:
            results.append("is odd")
    return results
result = is_even_odd()
print(result) 