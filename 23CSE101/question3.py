speed_mph = 0 # initializing variables
speed_mps = 0 # initializing variables
def speedUnitConverter(speed_kmph, unit): # function to handle conversions
    if unit == "mps" :  # block to run when m/s is needed
        speed_mps = speed_kmph / 3.6 # formula
        print("Speed is: ", float(speed_mps), " m/s") # formatted output
    elif unit == "mph" : # block to run when mph is needed
        speed_mph = speed_kmph / 1.609 # formula
        print("Speed is: ", float(speed_mph), " mph") # formatted output
    else: 
        print("invalid input: [type the speed as numerical value] [unit has to be valid]") # input validation

speed_kmph = float(input("Enter speed in kmph to convert: ")) # speed in kmph to convert
unit = str(input("Do you want to convert to (mps) or (mph): ")) # unit to be converted to 
speedUnitConverter(speed_kmph, unit) # function call
