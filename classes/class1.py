class student():
    name = "rakesh"
    website ="binarynote.com"
    expertise ="PHP, CSS, HTML,JavaScript,JQuery,WordPress and Now Python Django"

    def showMessage(self):
        print("This is a demo message from class ")

s = student()

print("Default Behaviour of Class Members in Python\n\n\nName : ",s.name)
print("website  : ", s.website)
print("Expertise :", s.expertise,"\n")
