import imapclient  # use pip install imapclient <-  easy for reading different email Server
import pyzmail # easy to read different part of EMail like subject / body /cc/bcc/to/from etc
from collections import Counter   

d=[]
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True) # email server for Gmail 
username=input("Enter your completer gmail User Name ")
Password=input("Enter your gmail passowrd")
imapObj.login(username,Password)   # login Method for your email
print("Dear", username," you are logged into your account")
imapObj.select_folder('[Gmail]/Spam', readonly=True)  # selecting different folder for phising email i used Spam
UIDs = imapObj.search(['ALL'])  # different filter for mailboxes  ALL/SEEN/UNSEEN it returns ids for the filter you have search
print( "No of emails in your [Gmail]/Spam' box=" ,len(UIDs))
print("Mail from\t\t"," Subject Line")
for i in UIDs:  # only 10 emails to be taken
    rawMessages = imapObj.fetch([i], ['BODY[]', 'FLAGS'])  # fetch the email message for particular UID
    message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]']) # Parse the raw email message.
    print(message.get_addresses('from'),message.get_subject()) # return the subject part of email 
    message.text_part != None    # check for text part of body message  Message can have html part also
    d.append(message.text_part.get_payload().decode(message.text_part.charset)+"\n")   # fetch the textpart
    #get_payload() method that returns the email’s body as a value of the bytes data type But this still isn’t a string value that we can use.
    #decode() method takes one argument: the message’s character encoding,
    #stored in the text_part.charset or html_part.charset attribute. This, finally, will return the string of the email’s body.
imapObj.logout()
print("Logged out successfully from server...")

with open("E:\email2.txt", 'w') as fp:
    for i in range(len(d)):
        fp.write(str(d[i]))


file = open("E:\email2.txt")
split_it=[]
for line in file:
       line=line.strip()
       split_it+=line.split()    # split() returns list of all the words in the string 
       
   
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
# most_common() produces k frequently encountered 
# input values and their respective counts.
print( "most common word found in EMails")
num=int(input("How many most common words you want to find"))
most_occur = Counter.most_common(num) 
for com in most_occur:
    print(com[0],"=>",com[1])