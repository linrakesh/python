import os

hostname ="https://binarynote.com"

for i in range(2, 255):
    response = os.system("ping -4t " + hostname)
    # and then check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')
