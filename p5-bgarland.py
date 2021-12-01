'''
Brianna Garland 
Fundamentals of Software Engineering 
I pledge my honor that I have abided by the Stevens Honor System 
Homework 5
----------------------------------------------------------------------------------------------------------------

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
 Write your final output with a single print, don't print each word separately.

'''
#This function takes in a word and converts it to the plural veriosn of its self 
def plurals(wordStr):
   
    #chedk if the word ends with y 
        #check if word ends in ay, ey, iy, oy, uy, and just add an s 
        #else take :-1 and join ies 
    #else check if word ends with o, ch, s, sg, x, z and just join es to the end 
    #else just add s 

    if wordStr.endswith('y'):
       if wordStr.endswith('ay') or wordStr.endswith('ey') or wordStr.endswith('iy') or wordStr.endswith('oy') or wordStr.endswith('uy'):
           wordStr=wordStr+'s'
       else:
           wordStr = wordStr[:-1]
           wordStr=wordStr+'ies'
    elif wordStr.endswith('o') or wordStr.endswith('ch') or wordStr.endswith('s') or wordStr.endswith('sh') or wordStr.endswith('x') or wordStr.endswith('z'):
        wordStr=wordStr+'es'
    else:
        wordStr=wordStr+'s'
    return wordStr

    
try:
    print("------------------------------------------------------------")
    
    inputString = input("Welcome to Plurals, please enter a string of words and the program will convert \nall of the words in the string to its plurals and print out the resutls \n\n")
    wordArr=inputString.split()
    
    for i in range(len(wordArr)):
        wordArr[i]=plurals(wordArr[i])
    finalStr = ' '.join(wordArr)
    print("\nYour Final Result after converting into plurals is: ", finalStr)
    
    print("------------------------------------------------------------")

except:
    print("Sorry there has been an error please run the program again")



