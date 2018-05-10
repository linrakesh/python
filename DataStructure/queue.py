#function to add element at the end of list
def add_element(stack,x):
    stack.append(x)
#function to remove last element from list    
def delete_element(stack):
    n = len(stack)
    if(n<=0):
        print("Queue empty....Deletion not possible")
    else:
        del(stack[0])

#function to display stack entry
def display(stack):
    if len(stack)<=0:
        print("Queue empty...........Nothing to display")
    for i in stack:
        print(i,end=" ")
#main program starts from here 
x=[]
choice=0
while (choice!=4):
    print("\n\tQueue menu \n\n\t1. Add Element \n\t2. Delete Element \n\t3. Display \n\t4. Exit")
    choice = int(input("\n Enter your choice : "))
    
    if(choice==1):
        value = int(input("Enter value : "))
        add_element(x,value)
    if(choice==2):
        delete_element(x)
    if(choice==3):
        display(x)
    if(choice==4):
        print("You selected to close this program")
    
