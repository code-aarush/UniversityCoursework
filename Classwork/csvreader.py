class csvReader: 
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, "r")
        self.keys = []
        titles = self.f.readline()
        title = ""

        for i in range(len(titles)):
            if titles[i] != "," :
                title += titles[i]
            else:
                self.keys.append(title)
                title = ""
        self.keys.append(title)

    def next(self):
        
        values = []
        valueline = self.f.readline()
        value = "" 

        for i in range(len(valueline)):
            if valueline[i] != "," :
                value +=valueline[i]
            else:
                values.append(value)
                value = ""
        values.append(value)
        myDict = dict(zip(self.keys, values))
        print(myDict)
        
new_csvReader = csvReader("demo.csv")

for i in range(3):
    new_csvReader.next()
