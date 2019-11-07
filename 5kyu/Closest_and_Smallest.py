#Problem "Closest and Smallest"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
####################################################### INSTRUCTIONS ######################################################################
#Input
#
#a string strng of n positive numbers (n = 0 or n >= 2)
#Let us call weight of a number the sum of its digits. For example 99 will have "weight" 18, 100 will have "weight" 1.
#
#Two numbers are "close" if the difference of their weights is small.
#
#Task:
#For each number in strng calculate its "weight" and then find two numbers of strng that have:
  #the smallest difference of weights ie that are the closest
  #with the smallest weights
  #and with the smallest indices (or ranks, numbered from 0) in strng

#Output:
#
#an array of two arrays, each subarray in the following format:
#[number-weight, index in strng of the corresponding number, original corresponding number instrng]
#
#or a pair of two subarrays (Haskell, Clojure, FSharp) or an array of tuples (Elixir, C++)
#
#or a (char*) in C mimicking an array of two subarrays or a string
#
#or a matrix in R (2 rows, 3 columns, no columns names)
#
#The two subarrays are sorted in ascending order by their number weights if these weights are different, by their 
#indexes in the string if they have the same weights.
####################################################### SOLUTION ##########################################################################
def closest(s):
    #string is empty
    if s == "":
        return []
    
    #list of original numbers, ls_w will be a 
    #nested list with the 3 parameters for each number 
    nums, ls_w = s.split(), []
    
    #build ls_w
    for index,n in enumerate(nums):
        weight = sum(int(digit) for digit in n) #calculate weight
        ls_w += [[weight, index, int(n)]]
    
    #sort ls_w
    ls_w.sort()
    
    #set variables to identify the pair of closest numbers
    closest = max(ls_w, key=lambda x: x[0])[0]  
    smallest = max(ls_w, key=lambda x: x[0])[0]
    best_index = len(ls_w)
    
    #identify the pair of closest numbers
    for i in range(1, len(ls_w)):
        diff_w = ls_w[i][0] - ls_w[i - 1][0] #difference in weight 
        min_w = min(ls_w[i][0], ls_w[i-1][0]) #minimum weight of pair
        min_index = min(ls_w[i][1], ls_w[i-1][1]) #minimum index of pair

        #check if they have a smaller difference in weight
        if diff_w < closest:
            closest, smallest, best_index = diff_w, min_w, min_index
            output = [ls_w[i - 1], ls_w[i]]
        
        #check if weight or index is lower if difference in weight equal
        elif diff_w == closest:
            if (min_w < smallest) or (min_w == smallest and min_index < best_index):
                closest, smallest, best_index = diff_w, min_w, min_index
                output = [ls_w[i - 1], ls_w[i]]
            
    return output   
