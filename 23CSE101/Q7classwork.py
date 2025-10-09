word = str(input("Input a word to count vowels and consonants: "))
u_counter = 0
l_counter = 0
for char in word :
    if char.upper() == char :
        u_counter += 1
    elif char.lower() == char :
        l_counter += 1
    else: 
        print("invalid input")

print("There are", u_counter, "uppercase characters", l_counter, "lowercase characters.")
