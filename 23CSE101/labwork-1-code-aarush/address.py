# Print the formatted address, taking individual lines as user input 

address = {
    "Name" : input("Enter address holder name: "), # identity
    "House number" : input("Enter your house/unit number: "), # could be an office address too
    "Building name" : input("Enter you building name: "), # presumption that independent house owners ignore this
    "Street name" : input("Enter the name your street: "), # assumption that there is direct street access
    "Area" : input("Enter your locality/neighbourhood/sector: "), # area
    "City" : input("Enter your city/town/municipality: "), # district
    "State" : input("Enter your state/province/region: "), # region
    "PIN CODE" : input("Input your zip/pin code: "), # zip/pin
    "Country" : input("Enter your country: "), # country
}

print("\nYour address is below: ")
for value in address.values():
    if value: # ignores if value is null
        print(value)