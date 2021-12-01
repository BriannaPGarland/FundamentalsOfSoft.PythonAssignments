'''
Brianna Garland 
Fundamentals of Software Engineering 
Homework 10
______________________________________________________________________________________________________________________________
You wrote code In assignment P7 to count the number of emails sent by each distinct user.   That code may be helpful for this 
assignment.

Ask the user for the name of an email file, e.g. mbox.txt.  Read the contents of the file and calculate how many emails are 
sent each day of the week, Sunday through Saturday.  The datetime module is one way to convert an arbitrary date to a day of 
the week but you may use any method you prefer.  

Once you've collected the summary data, plot the data in a bar chart using any library you choose.   There's an overview of 
doing bar charts in MatPlotLib which is a very popular data visualization tool for Python and other languages.

'''
from pathlib import Path
import os
import matplotlib.pyplot as plt

def emails(fileName):
    days = {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 0,
        "Fri": 0,
        "Sat": 0,
        "Sun": 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    }
    inputFile=[]
    filer = open(fileName)

    #reads in each line of the txt file as an element in a list 
    with filer as f:
        inputFile = list(f)
    #Looping through the list 
    for i in range(len(inputFile)):
        if 'Date:' in inputFile[i]:
            temp = inputFile[i].split()
            day = temp[1]
            #Logic to see which day of the week the email was being sent 
            if "Mon," in day:
                days["Mon"]+=1
            elif "Tue," in day:
                days["Tue"]+=1
            elif "Wed," in day:
                days["Wed"]+=1
            elif "Thu," in day:
                days["Thu"]+=1
            elif "Fri," in day:
                days["Fri"]+=1
            elif "Sat," in day:
                days["Sat"]+=1
            elif "Sun," in day:
                days["Sun"]+=1

    print("\n##############################################################") 
    print("A chart should be displayed on a seperate screen now but here is the raw data being graphed:\n",days)
    print("##############################################################\n")    
    
    # Logic to create the graph
    dayList = list(days.keys())
    numOfEmails = list(days.values())       

    #setting the chart type, the data sets, and the color  
    plt.bar(range(len(days)), numOfEmails, tick_label=dayList, color= "pink")
    #Axis Labels
    plt.xlabel('Days of the Week')
    plt.ylabel('Num of Emails Recieved')
 
    # displaying the title
    plt.title("Number of Emails Sent Each Day of the Week")
    plt.show()
    

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
