#function to add element at the end of list
def add_element(queue,x):
    queue.append(x)
#function to remove last element from list    
def delete_element(queue):
    n = len(queue)
    if(n<=0):
        print("Queue empty....Deletion not possible")
    else:
        del(queue[0])

#function to display queue entry
def display(queue):
    if len(queue)<=0:
        print("Queue empty...........Nothing to display")
    for i in queue:
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
    
