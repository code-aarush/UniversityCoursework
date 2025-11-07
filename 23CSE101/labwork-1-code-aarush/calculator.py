# Create a simple calculator with basic math functionality

class Calculator :
    def __init__(self): # creates a dictionary filled with the methods to be called based on user input
        self.operations = {
            "+": self.addition,
            "-": self.subtraction,
            "*": self.multiplication,
            "/": self.quotientCalc,
            "%": self.remainderCalc
        }

    def addition(self, a, b): # add function 
        return a + b
    
    def subtraction(self, a, b): # subtract function
        return a - b
    
    def multiplication(self, a, b): # multiply function
        return a * b
    
    def quotientCalc(self, a, b): # quotient function
        return a / b
    
    def remainderCalc(self, a, b): # calculates remainder
        return a % b
    
    def calculate(self, a, b, oper):  # 5 line function replaces 5 condition if-else block
        func  = self.operations.get(oper) # fetches operation from user input || based on which method is fetched from dictionary
        if func: # encompasses the particular method to be called
            return func(a, b)
        else: 
            return "invalid operator"

newCalculator = Calculator() # creating instance 
a = int(input("Enter a number: ")) # number 1 input
b = int(input("Enter another number: ")) # number 2 input
oper = str(input("Enter operation (+,-,*,/,%): ")) # operation input

result = newCalculator.calculate(a, b, oper) # calling the calculate function
print("Result: ", result) # prints final result 
        