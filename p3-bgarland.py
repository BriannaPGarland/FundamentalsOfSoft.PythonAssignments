'''
Brianna Garland 
Fundamentals of Software Engineering 
I pledge my honor that I have abided by the Stevens Honor System 
Homework 3
----------------------------------------------------------------------------------------------------------------
This week's reading (Severance, Chapter 4) discusses built in and user defined functions.  This week's assignment is to define a function called 'maxOfThree' that takes three values and returns the maximum value of the three.  Please DO NOT use the built-in Python function max() in your "Max_of_three" function for this week's Python assignment.  Write your own! 

Demonstrate that your function works properly by writing a Python script that requests three values from the user and then prints the maximum of the three values by calling your maxOfThree() function.

For example, my implementation looks like this at runtime:

Enter first value: 1

Enter second value: 2

Enter third value: 1

The maximum of 1 2 1 is 2

 Be sure to test your program on different cases including:

1,2,3
3,2,1
2,1,3
1,1,3
a, b, c
And don't forget to check for exceptions that might arise due to invalid inputs.

'''

def maxOfThree():
    print("------------------------------------------------------------")
    try:
        arr=[]
        max=0
        print("\n\n\n\n\n                          ################################ Welcome to Max of Three ###############################\n")
        print("You will be prompted to enter 3 values and the program will print out the max of those values. Values must be either integers or individual characters\n")

        #This is taking in the 3 
        arr.append((input("Please Enter first value\n")))
        arr.append((input("Please Enter second value\n")))
        arr.append((input("Please Enter third value\n")))
        
        #Checking the type of variables inputed and raising an exception if the user enter's a string 
        
        for i in arr:
            print(isinstance(i, str))
            if isinstance(i, str) and len(i)>1:
                raise TypeError("String entered")
            
        
       #Algorithm to find the max of 3 values 
        if arr[0]>arr[1]:
            if arr[0]>arr[2]:
                max=arr[0]
            else:
                max=arr[2]
        else:
            if arr[1]>arr[2]:
                max=arr[1]
            else:
                max=arr[2]
        
        #printing the result 
        print("\nThe maximum value for the three values you enterd is: "+str(max))
        print("------------------------------------------------------------")

    #specifying which exception recieves what type of error to make for a more specififc and responsive error solving 
    except(TypeError): 
        print("************************************************************")
        print("\nSorry you have entered input that is not in the format that is accepted.\nValues must be entered as a numeric value, for example: 1, 23, 14.\nPlease re-run the program and try again.")
        print("************************************************************")
    except:
        print("************************************************************")
        print("\nSorry there has been an unknown error\nPlease re-run the program and try again.")
        print("************************************************************")
    

####################  Main Program #########################
#Calling the function to run the program 
maxOfThree()