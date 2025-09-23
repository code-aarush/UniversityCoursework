operation = str(input("ENTER 1 TO FIND SQUARE ROOT \nENTER 2 TO FIND CUBE ROOT : ")) # fetching the operation from user
num = float(input("Enter number to find square/cube root of: ")) # getting number
if operation == "1" :
    sqrt = num ** (1/2)
    print("Square root is", sqrt)
elif operation == "2" : 
    cbrt = num ** (1/3)
    print("Cube root is", cbrt)             