#Problem "Integers: Recreation One"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/integers-recreation-one/python
####################################################### INSTRUCTIONS ######################################################################
#Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared 
#divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 
#42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the 
#number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

#list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
#list_squared(42, 250) --> [[42, 2500], [246, 84100]]

####################################################### SOLUTION ##########################################################################
from functools import reduce
import numpy as np
def divisors_sum(n):
    '''
    returns the sum of the squares of all possible divisors of a integer
    '''
    if n%2 == 0:
        step = 1
    else:
        step = 2
    #calculate divisors
    temp = [[m, n//m] for m in range(1,int(n**0.5)+1, step) if n%m==0] 
    divs = list(set(reduce(list.__add__, temp)))
    return np.sum(np.array(divs)**2)
 

def list_squared(start, end):
    output = []
    for n in range(start, end+1):
        sum_val = divisors_sum(n)
        #check if perfect square
        if sum_val**0.5 % 1 == 0:
            output.append([n, sum_val])
    return output

