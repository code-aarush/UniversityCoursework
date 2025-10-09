word = str(input("Input a word to count vowels and consonants: "))
v_counter = 0
c_counter = 0
for char in word :
    if char in ("a" , "e", "i", "o", "u") :
        v_counter += 1
    else: 
        c_counter += 1
    
print("There are", v_counter, "vowels and", c_counter, "consonants.")
