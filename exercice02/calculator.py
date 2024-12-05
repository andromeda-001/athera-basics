A = int(input("enter a number: "))
B = int(input("enter a number: "))
C = input(" + or - or / or * : ") 
if C == "+":
    calcul = A + B
    print(calcul)
elif C == "-":
    calcul = A - B
    print(calcul)
elif C == "/":
    calcul = A / B
    print(calcul) 
elif C == "*":
    calcul = A * B
    print(calcul)
else:
    print("invalid operator!")