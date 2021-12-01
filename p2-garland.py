'''
Brianna Garland 
Fundamentals of Software Engineering 
Homework 2
----------------------------------------------------------------------------------------------------------------
Write a script that asks the user for a quiz score and converts that numeric score to a letter grade as follows:
score greater that 92: A
score from 90 - 92: A-
score from 87 - 89: B+
score from 83 - 86: B
score from 80 - 82: B-
score from 70 - 79: C
score less than 70: F
Since legal scores generally fall between 0 and 100, your script should reject numbers above 100 or below 0. 

The input(), float() and print() functions will be used in this script as will the conditionals and try/except.   Note that input() returns a string (a set of characters) and not a number so you'll need to convert the value returned to a floating point number before comparing it to other numbers. Calling float('twenty') will fail and raise an exception which you can catch and respond appropriately using try/except.

We will test your program on at least the following test inputs (so you should too):

100, 93, 92.99, 90, 89.9, 87, 83, 80, 75, 69, eighty, -1, 101

Your script should provide a good user experience on invalid inputs by catching bad input values and warning the user.   
'''

def gradeConvert():
    print("------------------------------------------------------------")
    try:
         
        #This takes in an input and casts it to a float so that users are able to enter grades with decimals and still have them converted 
        score = float(input("Welcome to Grade Converter!!! Please enter a numeric grade to be converted \n"))
       
       #This is a catch that allows the user to be able to re-enter the grade if they enter a grade out of the range of the converter 
        while (score < 0 or score >100):
            score = float(input("Sorry this converter only accepts grades between 0 and 100, please try entering the grade again \n"))
        
        #This is the logic for the converter break down 
        if score >92:                   #92.01-100
            letterGrade = "A"
        if score <=92 and score >=90:   #90-92
            letterGrade ="A-"
        if score <90 and score >=87:    #87-89.99
            letterGrade ="B+"
        if score <87 and score >=83:    #83-86.99
            letterGrade ="B"
        if score <83 and score >=80:    #80-82.99
            letterGrade ="B-"
        if score <80 and score >=70:    #70-79.99
            letterGrade ="C"
        if score <70:                   #0-69.99
            letterGrade ="F"
        
        #Printing the result 
        print("The score you entered was: "+str(score)+" which results in a letter grade of: "+letterGrade)
        print("------------------------------------------------------------")
    except:
        print("************************************************************")
        print("\nSorry you have entered a grade that is not in the format that is accepted.\nGrades must be entered as a numeric value, for example: 99, 56, 75.\nPlease re-run the program and try again.")
        print("************************************************************")

#Calling the function to run the program 
gradeConvert()
