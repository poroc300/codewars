#Problem "Simple Fun #258: Is Divisible By 6"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/5911385598dcd432ae000004
####################################################### INSTRUCTIONS ######################################################################
#Task
#A masked number is a string that consists of digits and one asterisk (*) that should be replaced by exactly one digit. Given a 
#masked number s, find all the possible options to replace the asterisk with a digit to produce an integer divisible by 6.
#
#Input/Output
#[input] string s
#
#A masked number.
#
#1 ≤ inputString.length ≤ 10000.
#
#[output] a string array
#
#Sorted array of strings representing all non-negative integers that correspond to the given mask and are divisible by 6.
#
#Example
#For s = "1*0", the output should be ["120", "150", "180"].
#
#For s = "*1", the output should be [].
#
#For s = "1234567890123456789012345678*0",
#
#the output should be
#
#[
#"123456789012345678901234567800",
#"123456789012345678901234567830",
#"123456789012345678901234567860",
#"123456789012345678901234567890"]```
#As you can see, the masked number may be very large ;-)

####################################################### SOLUTION ######################################################################
def is_divisible_by_6(s):    
    #if number is odd then it is not divisible by 6
    if s[-1] != "*" and int(s[-1])%2 != 0:
        return []
     
    #s is only one digit
    elif s=="*": 
        return ["0", "6"]
    
    #even numbers
    else:
        output=[]
        #last digit is masked; only even numbers can be divisible by 6
        if s[-1] == "*":
            numbers = (0,2,4,6,8)
        else:
            numbers = range(10)
                  
        for num in numbers:
            string = s #make copy
            string = string.replace("*",str(num))
            if int(string)%6 == 0:
                output.append(string.lstrip("0")) #remove leading zeros
    return output
