operation = str(input("Do you want to find [square root] or [cube root]:")) # fetching the operation from user
num = float(input("Enter number to find square/cube root of: ")) # getting number
if operation == "square root" :
    sqrt = num ** (1/2)
    print("Square root is", sqrt)
elif operation == "cube root" : 
    cbrt = num ** (1/3)
    print("Cube root is", cbrt)