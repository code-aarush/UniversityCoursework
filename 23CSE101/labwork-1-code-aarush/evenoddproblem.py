num = int(input("Enter a number: "))
if num % 2 == 0 :
    num = num / 2
elif num % 2 == 1 :
    num = num * 3
else: 
    print("Invalid input")

print("The new number is :", int(num))