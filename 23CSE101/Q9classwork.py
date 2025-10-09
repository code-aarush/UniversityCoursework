def isPalindrom(word):
    current_pointer = 0
    end_pointer = len(word) - 1
    for current_pointer in range(int(len(word)/2)):
        if word[current_pointer] != word[end_pointer - current_pointer]:
            return False
        if word[current_pointer] == word[end_pointer - current_pointer]:
            pal_flag = True

    if pal_flag == True:
        return pal_flag    
        
word = str(input("Enter a word to find if it is a palindrome: "))
print(isPalindrom(word))  
