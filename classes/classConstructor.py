class student():
    name=""
    website=""
    expertise=""
    
    def __init__(self):
        self.name ="swarnima"
        self.website = "http://www.swarnima.com"
        self.expertise ="Django Specialist"

    def showData(self):
        print("Name : ",self.name)
        print("website  : ", self.website)
        print("Expertise :", self.expertise,"\n")

#object creation
#

s1 = student()  #calling constructor
s1.showData()

