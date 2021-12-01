'''
Brianna Garland 
Fundamentals of Software Engineering 
Homework 7
______________________________________________________________________________________________________________________________
Using the mbox.txt file, find the lines that start with From: and determine how many unique sender email addresses are included in this file, e.g. 

        From: cwen@iupui.edu

Also count the total number of email messages sent by each unique user.  Only print the number of unique senders and the email address and number of 
emails sent by the address that sent the most email messages.

Hints:

You can identify senders by looking for lines that start with "From: <senderEmail>".  
Store the sender's email and the total number of emails sent in a dict().    
Dictionaries raise a KeyError exception if you specify a key that is not found in the dictionary, but dict.get(key,default=None) can be used to simplify your code. E.g. 
      d = dict()

      #  d['unknown key']  raises a KeyError exception

      d.get('unknown key', 0) # adds 'unknown key' to dictionary d with value 0

      d.get(key, 0) += 1  # adds key to the dictionary with value 0 if key is not already in the dictionary and then adds 1

                                    # or increments the value if key is already in the dictionary

You can track the max emails and sender either as you read the file or wait until the entire file has been read and then find the max after reading the file.

Verify that your script responds properly when encountering empty files, non-existent files, or files that contain no relevant "From:" lines.  You may want to debug your program with mbox-short.txt but verify that it works properly with mbox.txt as well.

Also be sure to keep your try/except blocks small for readability.  You may want to use the try:/except:/else: form of the statement.
'''
from pathlib import Path
import os

def emails(fileName):
    print("In email ")
    uniSenders =[]
    inde=0
    count=0
    maxs = 1
    inputFile=[]
    filer = open(fileName)
    numArr=[]

    #reads in each line of the txt file as an element in a list 
    with filer as f:
        inputFile = list(f)
    #Looping through the list 
    for i in range(len(inputFile)):
        if 'Date:' in inputFile[i]:
            print("line says sender")
            temp = inputFile[i].split()
            sender = temp[1]
            if sender not in uniSenders: #Finding unique Senders
                uniSenders.append(sender)
                numArr.append(1) 
            else: #Adding one to their number of send emails 
                numArr[uniSenders.index(sender)]+=1
    
            print (numArr)   
    #Finding the max        
    for i in range(len(numArr)):
        if numArr[i] >maxs:
            maxs = numArr[i]
            inde = i
    #Final calculations
    mostSender= uniSenders[inde]
    numEmails = maxs
    numUni = len(numArr)

    print("\n##############################################################") 
    print("There are "+str(numUni)+" unique senders.")
    print("The sender who sent the most emails was: "+str(mostSender)+" with "+str(numEmails)+ " emails")
    print("##############################################################\n")    
           
def isValidFile(my_path, usrIn):
    try: #checks if the file exists if it is able to open it 
        myfile= open(my_path)
        myfile.close()
        validFile=True 
    except:
        validFile = False
        return validFile
    
    #this is where it checks that averything is valid and returns true if it is and false if it isnt 
    if '.txt' in usrIn and validFile == True and os.path.getsize(my_path) != 0:
        return True
    else:
        return False
                
try:
    
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    usrIn = input("Please enter the name of the file you want to read through, please include the '.txt' at the end \n")
    my_path=Path("/Users/briannagarland/Desktop/FundOfSoftware/"+usrIn)
    #This allows for the user to keep trying to input file names until they enter one that the program can handle 
    while isValidFile(my_path, usrIn) == False:
        usrIn = input("Sorry you have entered a File that was either empty or does not exist please enter the file name again and be sure to include the '.txt' \n")
        my_path=Path("/Users/briannagarland/Desktop/FundOfSoftware/"+usrIn)
    #calling the average function 
    emails(my_path)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
except:
    print("Sorry there has been an error please run the program again")
