# Write a function in Python for PushS(List) and for PopS(List) for performing 
# Push and Pop operations with a stack of List containing integers.

def push(stack):
  value = int(input('Enter any integer no :'))
  stack.append(value)

def pop(stack):
  if len(stack)<=0:
    print('\n Stack Underflow')
  else:
    print('\nPoped value from stack :',stack.pop())

def display(stack):
  print('\n\nStack Elements : ')
  for x in stack:
    print(x, end=' ')

#implementation of function to show stack
stack=[]
while True:
  print('\n  STACK MENU')
  print('1. Push')
  print('2. Pop')
  print('3. Display ')
  print('4. Exit')
  choice = input('Enter your choice :')
  if choice=='1':
      push(stack)
  if choice=='2':
      pop(stack)
  if choice=='3':
      display(stack)
  if choice=='4':
      break



