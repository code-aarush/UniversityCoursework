# Finding the square root and cube root of a quadratic equation

operation = str(input("ENTER 1 TO FIND SQUARE ROOT \nENTER 2 TO FIND CUBE ROOT : ")) # fetching the operation from user
num = float(input("Enter number to find square/cube root of: ")) # getting number
if operation == "1" : # finding square root 
    sqrt = num ** (1/2) # formula
    print("Square root is", sqrt) # output
elif operation == "2" : # finding cube root 
    cbrt = num ** (1/3) # formula
    print("Cube root is", cbrt) # output         