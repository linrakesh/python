def display(number, msg1="School", msg2="Place"):
    print('-----Times :', number, end=" ")
    print('-----Message 1 :', msg1*2)
    print('-----Message 2 :', msg2)
    print('----------------------')


display(2, 'DAV', 'Ghaziabad')
display(5)
display("SpringDales")
display(msg2="Modern", number=3)
display(msg2="Modern", msg1=24, number=3)
