# FundamentalsOfSoft.PythonAssignments
Masters class, Fundamentals of Software Engineering Python Assignments

### Homework 1
Create and submit a Python script that uses at least one variable along with the input() and print() functions described in 
section 2.10 to read the user's first name and last name, and then print a string of the format "Hello <firstName> <lastName>

## Homework 2
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
