try:
    A = int(input("enter a number: "))
    B = int(input("enter a number: "))
    calcul = A / B 
    B == 0
except ZeroDivisionError:  
    print("you can't divide by zero")
print(calcul)
 
