fibonacci = [0,1]
x = int(input("Enter the number of terms: "))
for i in range(1, x):
    fibonacci.append(fibonacci[i-1] + fibonacci[i])

print(fibonacci)
