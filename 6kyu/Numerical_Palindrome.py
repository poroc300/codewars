#Problem "Numerical Palindrome #4"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/numerical-palindrome-number-4/python
####################################################### INSTRUCTIONS ######################################################################
#A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of 
#numerical palindromes are:
#
#2332
#110011
#54322345
#
#For a given number num, return its closest numerical palindrome which can either be smaller or larger than num. If there are 
#2 possible values, the larger value should be returned. If num is a numerical palindrome itself, return it.
#
#For this kata, single digit numbers will NOT be considered numerical palindromes.
#
#Also, you know the drill - be sure to return "Not valid" if the input is not an integer or is less than 0.
#
#palindrome(8) => 11
#palindrome(281) => 282 
#palindrome(1029) => 1001
#palindrome(1221) => 1221
#palindrome("1221") => "Not valid"
####################################################### SOLUTION ######################################################################
from math import log10
def palindrome(num):
    #if negative or not integer
    if not isinstance(num, int) or num < 0:
        return "Not valid"    
    
    #if num has only one digit, return 11
    elif int(log10(num))+1 == 1:
        return 11
    
    #if num itself is a palidrome
    elif str(num) == str(num)[::-1]:
        return num
        
    num1, num2 = num, num
  
    while True:
        num1 += 1
        num2 -= 1  
        
        if (str(num1) == str(num1)[::-1] and str(num2) == str(num2)[::-1]) or (str(num1) == str(num1)[::-1]):
            return num1
          
        elif str(num2) == str(num2)[::-1]:
            return num2          
