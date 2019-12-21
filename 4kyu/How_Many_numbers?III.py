#Problem "How many numbers?III"
#level: 4kyu
#language: Python
#link: https://www.codewars.com/kata/5877e7d568909e5ff90017e6
####################################################### INSTRUCTIONS ######################################################################
#We want to generate all the numbers of three digits where:
#
#the sum of their digits is equal to 10.
#
#their digits are in increasing order (the numbers may have two or more equal contiguous digits)
#
#The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334
#
#Make a function that receives two arguments:
#
#the sum of digits value
#
#the desired number of digits for the numbers
#
#The function should output an array with three values: [1,2,3]
#
#1 - the total number of possible numbers
#
#2 - the minimum number
#
#3 - the maximum number
#
#The example given above should be:
#
#find_all(10, 3) == [8, 118, 334]
#If we have only one possible number as a solution, it should output a result like the one below:
#
#find_all(27, 3) == [1, 999, 999]
#If there are no possible numbers, the function should output the empty array.
#
#find_all(84, 4) == []
#The number of solutions climbs up when the number of digits increases.
#
#find_all(35, 6) == [123, 116999, 566666]
#Features of the random tests:
#
#Number of tests: 112
#Sum of digits value between 20 and 65
#Amount of digits between 2 and 17

####################################################### SOLUTION ##########################################################################
###this solution is not fast enough to pass all random tests in 12 seconds (the last 4-5 random tests are not completed on time)
import numpy as np
def sum_digits(n):
   '''
   sums the digits of n (a integer)
   '''
   sum_dig = 0 
   while n: #will break when n=0
       sum_dig += n % 10 ##add rightmost digit
       n = n//10 #remove rightmost digit
   return sum_dig 

def generate_nums(digs, start, end):
    '''
    generate array of numbers with digits in ascending order in a given interval [start, end]
    '''
    ###base case
    if digs == 1:
        return np.arange(1,10)
    
    ###test cases
    arr = np.arange(start, end+1, start) 
    recur_arr = generate_nums(digs-1, start//10, end//10) #recursive array
    output = np.array([], dtype="int32") #output array to store results
    
    #generate numbers in ascending order
    for i,x in enumerate(arr,1):
        limit = int(str(i) * digs) #set lower bound to subset arrays
        temp = x + recur_arr
        temp = temp[limit <= temp] #subset temp
        output = np.concatenate((output, temp))
    return output

def find_all(sum_dig, digs):
    #define start and end points of the interval being evaluated
    start = int(10**(digs-1))
    end = start * 9
    
    #create array of nums with digits in ascending order and subset using sum_digits
    nums = generate_nums(digs, start, end)
    out = [n for n in nums if sum_digits(n) == sum_dig ]
    return [len(out),out[0], out[-1]] if out != [] else []

####################################################### MORE EFFICIENT SOLUTIONS ##########################################################################
###this solution developed by me passes all tests, although almost reaching the 12 seconds
def next_number(n, n_digits):
    '''
    given an input integer(n), returns the next number with
    the digits in ascending order 
    '''
    string = str(n)   
    if string[-1] != "9":
        return n+1
    else:
        idx = string.find("9")-1 #index of the first digit to be changed
        not_change, to_change = string[:idx], string[idx:]
        to_change = str(int(to_change[0])+1) * len(to_change) #changed numbers
        return int(not_change + to_change)

def sum_digits(n):
   '''
   sums the digits of n (a integer)
   '''
   sum_dig = 0 
   while n: #will break when n=0
       sum_dig += n % 10 ##add rightmost digit
       n = n//10 #remove rightmost digit
   return sum_dig 

def find_all(score, n_digits):
    max_val = int("9"*n_digits)
    if score > sum_digits(max_val):
        return []
    elif score == sum_digits(max_val):
        return [1, max_val, max_val]
    
    #set lower and upper limit of the interval to be evaluated
    start = int("1" * n_digits)
    final = int("9" * n_digits)
    
    #optimization step for the upper limit; numbers above a given threshold will always show a higher score
    perc = round(score/sum_digits(final),2) 
    final_adjust = int(final*perc) #last number to be evaluated
    
    #create list with numbers in ascending order and sum_digit(n)==score
    n=start-1
    nums = []
    while n < final_adjust:
        n = next_number(n, n_digits)
        if sum_digits(n) != score:
            continue
        nums += [n]
    return [len(nums),nums[0],nums[-1]] if nums != [] else []

####most efficient solution (adapted from the solution of other user)
from itertools import combinations_with_replacement
def find_all(score, n_digits):
    combs = combinations_with_replacement(range(1,10), n_digits)
    nums = ["".join(list(map(str,x))) for x in combs if sum(x) == score]
    return [len(nums),int(nums[0]), int(nums[-1])] if nums != [] else []




