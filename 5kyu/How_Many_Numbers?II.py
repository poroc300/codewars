#Problem "How Many Numbers? II"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/how-many-numbers-ii/python
####################################################### INSTRUCTIONS ######################################################################
#We want to find the numbers higher or equal than 1000 that the sum of every four consecutives digits cannot be higher than a 
#certain given value. If the number is num = d1d2d3d4d5d6, and the maximum sum of 4 contiguous digits is maxSum, then:
#
#d1 + d2 + d3 + d4 <= maxSum
#d2 + d3 + d4 + d5 <= maxSum
#d3 + d4 + d5 + d6 <= maxSum
#For that purpose, we need to create a function, max_sumDig(), that receives nMax, as the max value of the interval to study 
#(the range (1000, nMax) ), and a certain value, maxSum, the maximum sum that every four consecutive digits should be less or equal to. 
#The function should output the following list with the data detailed bellow:
#
#[(1), (2), (3)]
#
#(1) - the amount of numbers that satisfy the constraint presented above
#
#(2) - the closest number to the mean of the results, if there are more than one, the smallest number should be chosen.
#
#(3) - the total sum of all the found numbers
#
#Let's see a case with all the details:
#
#max_sumDig(2000, 3) -------> [11, 1110, 12555]
#
#(1) -There are 11 found numbers: 1000, 1001, 1002, 1010, 1011, 1020, 1100, 1101, 1110, 1200 and 2000
#
#(2) - The mean of all the found numbers is:
#      (1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000) /11 = 1141.36363,  
#      so 1110 is the number that is closest to that mean value.
#
#(3) - 12555 is the sum of all the found numbers
#      1000 + 1001 + 1002 + 1010 + 1011 + 1020 + 1100 + 1101 + 1110 + 1200 + 2000 = 12555
#
#Finally, let's see another cases
#max_sumDig(2000, 4) -----> [21, 1120, 23665]
#
#max_sumDig(2000, 7) -----> [85, 1200, 99986]
#
#max_sumDig(3000, 7) -----> [141, 1600, 220756] ```
####################################################### SOLUTION ##########################################################################
import numpy as np

def sum_digits(n):
   '''n is an int'''
   sum_dig = 0 
   #loop will break when n=0
   while n:
       sum_dig = sum_dig + n % 10 ##add rightmost digit
       n = n//10 #remove rightmost digit
   return sum_dig 

def valid_4digits(n, max_sum):
    '''check if sum of 4 consecutive digits <= max_sum'''
    str_n = str(n)
    for i in range(len(str_n)-3):
        digits4 = str_n[i:i+4] #4 consecutive digits being evaluated
        if sum_digits(int(digits4)) > max_sum:
            return False
    return True
        
def max_sumDig(n, max_sum):
    #find numbers in which valid_4digits is True
    nums, eval_n = [], 1000
    while eval_n <= n:
        if valid_4digits(eval_n, max_sum):
            nums.append(eval_n)
        eval_n += 1
    
    #convert to np.array and estimate mean
    nums = np.array(nums)
    mean = np.mean(nums)

    #check closest number to mean by subsetting array
    lower, upper = nums[nums <= mean], nums[nums > mean]
    if (mean - lower[-1]) <= (upper[0] - mean):
        closest = lower[-1]
    else:
        closest = upper[0]
        
    return [len(nums), closest, np.sum(nums)]
    
