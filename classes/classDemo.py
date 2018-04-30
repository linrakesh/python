class student():
    def read_data(self,name,fatherName,stream):
        name = self.name;
        fatherName = self.fatherName
        stream  = self.stream

    def show_data(self):
        print("Student Name ",self.name)
        print("father  Name ",self.fatherName)
        print("Stream Name ",self.stream)

student s;
s.read_data('rakesh','jagdish','computer')
s.show_data()