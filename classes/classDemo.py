class student:
    def read_data(self,name,fatherName,stream):
        self.name = name
        self.fatherName = fatherName
        self.stream = stream

    def show_data(self):
        print("Student Name ",self.name)
        print("father  Name ",self.fatherName)
        print("Stream Name ",self.stream)

s = student()
s.read_data('rakesh','jagdish','computer')
s.show_data()