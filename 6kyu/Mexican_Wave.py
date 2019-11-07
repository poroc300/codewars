#Problem "Mexican Wave"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/mexican-wave/python
####################################################### INSTRUCTIONS ######################################################################
#In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and 
#you must return that string in an array where an uppercase letter is a person standing up.
#Rules
#1.  The input string will always be lower case but maybe empty.
#2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
#Example
#wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
####################################################### SOLUTION ##########################################################################
def wave(s):
    output=[]
    for i in range(len(s)):
        if s[i].isalnum():
            output.append(s[:i] + s[i].upper() + s[i+1:])
    return output
    # using list comprehension
    # return [s[:i] + s[i].upper() + s[i+1:] for i in in range(len(s)) if s[i].isalnum()]
        
