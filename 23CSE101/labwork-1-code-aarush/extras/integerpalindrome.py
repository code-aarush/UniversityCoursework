number = 1234321
counter = 0
new_number = 0
while number > 0 :
    number = number // 10
    counter += 1    

number_new = 1234321

print(counter)

for i in range(1, counter + 1) :
    end_num = number_new % 10
    print(end_num)
    new_number = new_number + (end_num * (10**i))

    