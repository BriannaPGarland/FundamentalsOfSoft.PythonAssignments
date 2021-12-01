'''

Your assignment is to write a script (a program) that implements a “Guess the Number” game. Your script must generate a random number between 1 and 20 and ask the user to guess the number, telling them what numbers the random number falls within. Give the user 6 tries. Running my script, it looks like this:

Hello! What is your name? Jim

Well, Jim, I am thinking of a number between 1 and 20.

Take a guess. 5

Your guess is too low.

Take a guess. 10

Your guess is too high.

Take a guess. 7

Your guess is too low.

Take a guess. 8

Your guess is too low.

 

Take a guess. 9

Good job, Jim! You guessed my number in 5 guesses!

If Jim hadn’t found the number in 6 tries, the script would say “The number I was thinking of was __”

Your solution should include a function that takes two parameters, the number to be guessed and the number that was guessed and returns:

0 if the two numbers match 
-1 if the number to be guessed is smaller than the number that was guessed
1 if the number to be guessed is larger than the number that was guessed
Your program should generate the target random number and then loop until either the user guesses the target or exceeds 6 tries. Each iteration through 
the loop should collect the user's guess, and then call your function to compare the guess to the target.  Be sure to use a try/except block to insure 
that your program handles invalid inputs in a user friendly manner.

Be sure to test your program under a variety of conditions, including:

- the user guesses the number in < 6 tries

- the user doesn't guess the number in 6 tries

- the user enters invalid input, e.g. twenty

- the user enters a value < 1 or > 20[]
'''

import random 
def numCompare(guess,answer):
    if guess == answer:
        return 0
    elif guess < answer:
        return 1
    else:
        return -1
def inputControl(i):
    if i>20 or i<1:
        raise TypeError("Out of Range")

def gameControl():
    tries=0
    name = input("Hello and Welcome to the Number Guessing Game!!! To start, what is your name?\n")
    print("Well "+name+"... I am thinking of a number between 1 and 20 you have 6 chances to guess\n")
    answer = random.randint(1,20)

    #First Guess
    try:
        guess = int(input("Take your first guess\n"))
        inputControl(guess)
        guessStat=numCompare(guess, answer)

        while guessStat!=0 and tries <6:
            if guessStat>0:
                guess=int(input("Your guess is too low try again\n"))
                inputControl(guess)
            else:
                guess=int(input("Your guess is too hightry again\n"))
                inputControl(guess)
            guessStat=numCompare(guess, answer)
            tries=tries+1

        if tries < 6:
            print("Congrats "+name+"!! You guessed the correct number and it only took you "+str(tries)+" tries!! Game Over")
        else:
            print("Sorry "+name+" you ran out of tries, the number I was thinking of was "+str(answer))
    
    except(TypeError): 
        print("************************************************************")
        print("\nSorry you have entered input outside of the number range. \nPlease re-run the program and try again.")
        print("************************************************************")
    except:
        print("\n************************************************************")
        print("Sorry you have entered input that is not a number or you typed the word rather than using the number. \nPlease re-run the program and try again.")
        print("************************************************************")

gameControl()