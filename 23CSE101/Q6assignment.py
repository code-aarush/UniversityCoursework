a = input("Enter a unique number 1: ")
b = input("Enter a unique number 2: ")
c = input("Enter a unique number 3: ")
if a > b and a > c :
    print("Largest number is", a)
elif b > a and b > c :
    print("Largest number is", b)
else: 
    print("Largest number is", c)
