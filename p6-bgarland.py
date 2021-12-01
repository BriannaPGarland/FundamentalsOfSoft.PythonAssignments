'''
“Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

“When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating
 point number on the line. Count these lines and compute the total of the spam confidence values from these lines. 
 When you reach the end of the file, print out the average spam confidence” rounded to four decimal places.      

 Enter the file name: mbox.txt

 Average spam confidence: 0.8941....

       Enter the file name: mbox-short.txt

       Average spam confidence: 0.7507....

 “Test your file on the mbox.txt and mbox-short.txt files.”

 

Be sure to use try and except when querying the user for file names.  

Your code should handle bad data values, e.g. what happens if the input file is corrupted, e.g. 

X-DSPAM-Result: Innocent
X-DSPAM-Processed: Sat Jan 5 09:14:16 2008
X-DSPAM-Confidence: BAD value
X-DSPAM-Probability: BAD value
X-DSPAM-Confidence: BAD
X-DSPAM-Probability: BAD

Also, be sure that you test your program to be sure that it works properly with empty files or non-existent files, e.g. the user types in the wrong file name.
Beware evil professors who might run test cases that might cause a divide by zero error.
'''
from pathlib import Path
import os

def emails(fileName):
    print("in in emails function")
    count=0.0
    sum =0.0
  # take in each line in the file as apart of an array 
  #loop through that array
    # look fot the index of  ('X-DSPAM-Confidence:') in each line if it returns a -1 its not in the line if it doesnt then grab the next 4 letters after the thing (index of returns the first)
    #have a count for how many of them it runs into and then have a sum to add them all together
  #compute the average and print out the average at the end to 4 decimals 
    inputFile= open(fileName).readlines()
    for i in range(len(inputFile)):
        if inputFile[i].includes('X-DSPAM-Confidence:'):
            temp = inputFile[i].split()
            num = temp[1]
            if num.type==int:
                count = float(count +1)
                sum = float(sum + num)
            else:
                print("---- The confidence at line "+(i+1)+ " has a bad data value and was not counted towards the average ----")
    average = float(sum/count)
    average = round(average,4)
    print("\n##############################################################")    
    print("The X-DSPAM-Confidence average is: ",average) 
    print("##############################################################\n")    
           
    
try:
    validFile = False
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    usrIn = input("Please enter the name of the file you want to read through, please include the '.txt' at the end \n")
    print("got here")
    my_path=Path("/Users/briannagarland/Desktop/Fund.\ of\ Software/")
    print(my_path)
    print("got here")
    print(usrIn.index('.txt')>0)    
    try: 
        myfile= open(my_path)
        myfile.close()
        validFile=True 
        print ("exists")
    except:
        validFile = False
        print("no")
    # if usrIn.index('.txt')>0 and path.exists(my_path):
    #     print("in valid file if ")
    #     validFile = True
    # else:
    #     print("in valid file else")
    #     while validFile == False:
    #         print("in valid file while")
    #         if not usrIn.includes('.txt'): #incorrect File format
    #             usrIn = input("Sorry you have entered a file name without '.txt'. Please enter the name of the file you want to read through, please include the '.txt' at the end\n")
    #             if usrIn.includes('.txt') and path.exists(my_path):
    #                  validFile = True
    #         if not path.exists(my_path): #non-existant file
    #                 usrIn = input("Sorry you have entered a file name that does not exist in the working Directory. Please try again and  enter the name of the file you want to read through, please include the '.txt' at the end \n")
    #                 if usrIn.includes('.txt') and path.exists(my_path):
    #                     validFile = True
    #         if not Path(path).is_file(): #empty file 
    #             usrIn = input("Sorry you have entered an empty file. Please try again and  enter the name of the file you want to read through, please include the '.txt' at the end\n")
    #             if usrIn.includes('.txt') and path.exists(my_path):
    #                 validFile = True
    emails(usrIn)
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
except:
    print("Sorry there has been an error please run the program again")
