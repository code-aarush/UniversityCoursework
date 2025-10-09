numbers = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
        }

def calculate(num):  
        func  = numbers.get(num) 
        if func: 
            return func
        else: 
            return "invalid operator"

num = str(input("Enter operation (0,1,2,3,4,5,6,7,8,9): "))
    
print(calculate(num))