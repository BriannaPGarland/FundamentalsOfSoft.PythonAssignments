'''
Brianna Garland 
Fundamentals of Software Engineering 
Homework 9
______________________________________________________________________________________________________________________________
Write a script that finds all of the capitalized words (not words in all caps except individual letters) in a text file and
presents them in alphabetical order.

For example, if the text file used is:

    But soft what light through yonder window breaks. "It is I, Romeo."
    There is but one of you and one more of me. It is the east and Juliet is the sun.
    Arise fair sun and kill the envious moon Who is already sick and pale with grief.

Your script would return:

    ['Arise', 'But', 'I', 'It', 'Juliet', 'Romeo', 'There', 'Who']

If you offered up a bad filename, your script might return:

    The file name entered is invalid or does not exist.

And if your file had no capitalized words, your script might return:

    Sorry. No capitalized words were found in this file.
'''
from string import punctuation
from pathlib import Path
import re
import os

def capitals(fileName):
    inputFile=[]
    filer = open(fileName)
    capList=[]
    count =0
    pattern = '(^[A-Z])+[a-z]+$'
    #reads in each line of the txt file as an element in a list 
    with filer as f:
        inputFile = list(f)
    #Looping through the list 
    for i in range(len(inputFile)):
        punc_translator = str.maketrans({key: None for key in punctuation})
        inputFile[i]  = inputFile[i].translate(punc_translator)
        temp=inputFile[i].split()
        for j in temp:
            if len(j)<2:
                if j.isupper():
                    capList.append(j)
                    print(j)
            else:
                if re.search(pattern, j):
                    capList.append(j)
                    print(j)
    if len(capList)>0:
        capList.sort()
    else:
        print("Sorry. No capitalized words were found in this file.")
    
    print("\n##############################################################") 
    print(capList)
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
    capitals(my_path)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
except:
    print("Sorry there has been an error please run the program again")
