word = str(input("Enter a word to compress: "))
current_counter = 1
new_str = ""
for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        current_counter += 1
    elif word[i] != word[i - 1]:
        new_str = str(new_str) + str(word[i - 1]) + str(current_counter)
        current_counter = 1
        current_char = word[i]
    
new_str = str(new_str) + str(current_char) + str(current_counter)
print(new_str)
