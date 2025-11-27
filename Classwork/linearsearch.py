target = int(input("Enter the number to find: "))
arr = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr)) :
    if arr[i] == target :
        print(target, "found at: ", i)
        break
    if i == len(arr) - 1:
        print("not found")