# Write a function in Python for PushS(List) and for PopS(List) for performing
# Push and Pop operations with a queue of List containing integers.


def insert_element(queue):
  value = int(input('Enter any integer no :'))
  queue.append(value)


def delete_element(queue):
  if len(queue) <= 0:
    print('\n Queue Underflow')
  else:
    print('\nDeleted Elment from from Queue :', queue.pop(0))


def display(queue):
  print('\n\nQueue Elements : ')
  for x in queue:
    print(x, end=' ')


#implementation of function to show queue
queue = []
while True:
  print('\n  QUEUE MENU')
  print('1. Insert Element')
  print('2. Delete Element')
  print('3. Display ')
  print('4. Exit')
  choice = input('Enter your choice :')
  if choice == '1':
      insert_element(queue)
  if choice == '2':
      delete_element(queue)
  if choice == '3':
      display(queue)
  if choice == '4':
      break
