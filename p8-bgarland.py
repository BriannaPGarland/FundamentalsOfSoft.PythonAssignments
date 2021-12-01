'''
Brianna Garland 
Fundamentals of Software Engineering 
Homework 9
______________________________________________________________________________________________________________________________
Create a Python program that prompts the user for the name of a file with an arbitrary 
ASCII document, reads the file, 
and prints a summary of the words in the document.

The summary should include:

Total words
Total distinct words
The top 25 most frequent words and counts (You do NOT need to handle ties.  Just pick the 
top 25)
Character frequency sorted from most frequent to least frequent characters
Test your program on a small file that you can check manually and then download Mark 
Twain's Adventures of Tom Sawyer 
from http://www.gutenberg.org/ebooks/74 (Links to an external site.) and verify that 
your code works on a large input file.

Note: Python's collections module has a really convenient Counter object that is a
 perfect match for this task, but that would be too easy!  
 Instead, please use either a dictionary or check out DefaultDict.
'''

from pathlib import Path
import os
from string import punctuation
from collections import defaultdict
from operator import itemgetter



def wordSum(fileName):
    inputFile=[]
    filer = open(fileName)
    totalWord = 0
    line=[]
    disWordDict = defaultdict(int)   # the default value will be an int with value 0
    disCharsDict = defaultdict(int)
    top25= []

    #reads in each line of the txt file as an element in a list 
    with filer as f:
        inputFile = list(f)
    #Looping through the list 
    for i in range(len(inputFile)):
        #Lower casing everything
        inputFile[i] = inputFile[i].lower()
        #character Frequency
        for k in inputFile[i]:
            if k in disCharsDict:
                disCharsDict[k] +=1
            else:
                disCharsDict[k] =1
        #removing Punctuation 
        punc_translator = str.maketrans({key: None for key in punctuation})
        inputFile[i]  = inputFile[i].translate(punc_translator)
        #separating each line 
        line = inputFile[i].split()
        print(line)
        #Word Manipulation  
        totalWord += len(line)
        #Finding unique words and their frequency 
        for j in line:
            disWordDict[j]+=1
    distWords = len(disWordDict)

    #sort to find top 25
    s = sorted(disWordDict.items(),key=itemgetter(1), reverse=True)
    if len(s) < 25:
        top25=s
    else:
        top25=s[:25]  

    #character frequency sorting
    charFreq = sorted(disCharsDict.items(),key=itemgetter(1), reverse=True)
      

    #Outputting the summary       
    print("\n##############################################################################################") 
    print("###########################          DOCUMENT SUMMARY             ############################\n\n")
    print("------------------------------------------------------------------------------")
    print("There are "+str(totalWord)+" total words in this document\n")
    print("Of those words, "+str(distWords)+" of them were distinct and unique\n")  
    print ("The top 25 words that were the most frequent and their number of occurences: ")
    print("------------------------------------------------------------------------------")
    for i in range(len(top25)):
        print(str(i+1)+".",top25[i])
    print("\n\nThe number of times each character found in the text is: ")
    print("------------------------------------------------------------------------------")
    for i in range(len(charFreq)):
        print(str(i+1)+".",charFreq[i])
    print("################################################################################################\n")    
           
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
    wordSum(my_path)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
except:
    print("Sorry there has been an error please run the program again")

