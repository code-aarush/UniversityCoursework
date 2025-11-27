class csvWriter: 
    def __init__(self, filename, columns):
        self.filename = filename
        self.column_names = columns

    def write_row(self, data):  
        row_values = []

        for col in self.column_names:
            value = data.get(col, "")
            value = str(value)
            row_values.append(value)

        line = ",".join(row_values)

        f = open(self.filename, "a")
        f.write(line + "\n")

data = [for i in range(10): {"Name": "S Aarush", "RollNo": "349", "Semester": "1" }]
new_csvWriter = csvWriter("demo.csv", ["Name", "RollNo", "Semester"])
new_csvWriter.write_row(data)

