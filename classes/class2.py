class student():
    name = "rakesh"
    website ="binarynote.com"
    expertise ="PHP, CSS, HTML,JavaScript,JQuery,WordPress and Now Python Django"

    def setData(self,name,web,exp):
        self.name = name
        self.website = web
        self.expertise = exp
    
    def showData(self):
        print("Name : ",self.name)
        print("website  : ", self.website)
        print("Expertise :", self.expertise,"\n")

#object creation
s = student()  
s.showData()

# set new Data using another function
s.setData("Swarnima", 'swarnima.com','Python, Django, CSS, JavaScript')
s.showData()