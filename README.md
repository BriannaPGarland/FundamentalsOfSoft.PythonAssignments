# FundamentalsOfSoft.PythonAssignments
Masters class, Fundamentals of Software Engineering Python Assignments

### Homework 1
Create and submit a Python script that uses at least one variable along with the input() and print() functions described in 
section 2.10 to read the user's first name and last name, and then print a string of the format "Hello firstName lastName

### Homework 2
Write a script that asks the user for a quiz score and converts that numeric score to a letter grade as follows:
score greater that 92: A
score from 90 - 92: A-
score from 87 - 89: B+
score from 83 - 86: B
score from 80 - 82: B-
score from 70 - 79: C
score less than 70: F
Since legal scores generally fall between 0 and 100, your script should reject numbers above 100 or below 0. 

### Homework 3
This week's reading (Severance, Chapter 4) discusses built in and user defined functions.  This week's assignment is to define a function called 'maxOfThree' that takes three values and returns the maximum value of the three.  Please DO NOT use the built-in Python function max() in your "Max_of_three" function for this week's Python assignment.  Write your own! 

### Homework 4
Your assignment is to write a script (a program) that implements a “Guess the Number” game. Your script must generate a random number between 1 and 20 and ask the user to guess the number, telling them what numbers the random number falls within. Give the user 6 tries.

### Homework 5
English is a really silly language with many different rules for converting singular to plural.    Your assignment this week will use a simplified set of rules for 
converting singular to plural.

Read a line of text from the user with input() and convert each word in the line from singular form to plural form using the following heuristics:

if the word ends in a 'y' preceded by a vowel (a,e,i,o,u), add 's'; e.g. monkey -> monkeys
if the word ends in 'y' not preceded by a vowel, remove the 'y' and add 'ies', e.g. fly -> flies
if the word ends in 'o','ch', 's', 'sh', 'x', or 'z' then add 'es'
otherwise, just add 's'
For example, if the user enters: 'monkey elephant potato porch fly button fish fox buzz', then the output should be 'monkeys elephants potatoes porches flies 
buttons fishes foxes buzzes'

Organize your program with a function 'plural(s)' which given a string, returns the plural form of the string using the rules above. 
Read the line of input and call plural() on each token in the string and create a new string, appending each token to the new string.   
write your final output with a single print, don't print each word separately.
 
### Homework 6
Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475

“When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating
 point number on the line. Count these lines and compute the total of the spam confidence values from these lines. 
 When you reach the end of the file, print out the average spam confidence” rounded to four decimal places.      

 Enter the file name: mbox.txt

 Average spam confidence: 0.8941....

       Enter the file name: mbox-short.txt

       Average spam confidence: 0.7507....

 “Test your file on the mbox.txt and mbox-short.txt files.”
 
### Homework 7
sing the mbox.txt file, find the lines that start with From: and determine how many unique sender email addresses are included in this file, e.g. 

        From: cwen@iupui.edu

Also count the total number of email messages sent by each unique user.  Only print the number of unique senders and the email address and number of 
emails sent by the address that sent the most email messages.

### Homework 8
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

### Homework 9 
Write a script that finds all of the capitalized words (not words in all caps except individual letters) in a text file and
presents them in alphabetical order.

For example, if the text file used is:

    But soft what light through yonder window breaks. "It is I, Romeo."
    There is but one of you and one more of me. It is the east and Juliet is the sun.
    Arise fair sun and kill the envious moon Who is already sick and pale with grief.

Your script would return:

    ['Arise', 'But', 'I', 'It', 'Juliet', 'Romeo', 'There', 'Who']
   
### Homework 10 
You wrote code In assignment P7 to count the number of emails sent by each distinct user.   That code may be helpful for this 
assignment.

Ask the user for the name of an email file, e.g. mbox.txt.  Read the contents of the file and calculate how many emails are 
sent each day of the week, Sunday through Saturday.  The datetime module is one way to convert an arbitrary date to a day of 
the week but you may use any method you prefer.  

Once you've collected the summary data, plot the data in a bar chart using any library you choose.   There's an overview of 
doing bar charts in MatPlotLib which is a very popular data visualization tool for Python and other languages.
