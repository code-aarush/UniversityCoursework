def generate_purchase_report(data):
    i = 0
    colon_counter = 0
    names = []
    while i < len(data):
        if data[i] == ":":
            colon_counter += 1
            if colon_counter % 2 != 0 :
                name = ""
                while data[i] != "," :
                    name += data[i]
                    i += 1
                name = name.replace(":", "").replace("'", "").strip()
                    
                if name in names:
                    next
                else:
                    names.append(name)
        i += 1

    i = 0
    comma_counter = 0
    categories = []
    while i < len(data):
        if data[i] == ",":
            comma_counter += 1
            if comma_counter % 2 != 0:
                category = ""
                while data[i] != ":":
                    category += data[i]
                    i += 1
                category = category.replace(",", "").replace("'", "").strip()
                if category in categories:
                    next
                else:
                    categories.append(category)
        i += 1

    print(names)
    print(categories)

data = ''' [
{'name': 'Arun', 'electronics': 1200},
{'name': 'Diya', 'fashion': 750},
{'name': 'Arun', 'grocery': 300},
{'name': 'Rahul', 'electronics': 2200},
{'name': 'Diya', 'grocery': 450},
{'name': 'Arun', 'fashion': 900}
] '''

generate_purchase_report(data)