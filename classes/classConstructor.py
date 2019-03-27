class student:
    def __init__(self,name,website,expertise):
        self.name = name
        self.website = website
        self.expertise = expertise

    def showdata(self):
        return 'Name : {} \nWebsite: {}  \nExpertise :{}'.format(self.name,self.website,self.expertise)
#object creation
#

s1 = student('rakehs','https://bianrynote.com','Django Specilist')  #calling constructor
print(s1.showdata())

#calling function using class itself and passing object as its parameter
print(student.showdata(s1))