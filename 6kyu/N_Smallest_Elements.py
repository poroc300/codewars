#Problem "N smallest elements in original order"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/5aec1ed7de4c7f3517000079
####################################################### INSTRUCTIONS ######################################################################
#Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you 
#are not getting out of it just throwing a lame bas sorting method there) with an array/list/vector of integers and 
#the expected number n of smallest elements to return.
#
#Also:
#
#the number of elements to be returned cannot be higher than the array/list/vector length;
#elements can be duplicated;
#in case of duplicates, just return them according to the original order (see third example for more clarity).
#Same examples and more in the test cases:
#
#first_n_smallest([1,2,3,4,5],3) == [1,2,3]
#first_n_smallest([5,4,3,2,1],3) == [3,2,1]
#first_n_smallest([1,2,3,4,1],3) == [1,2,1]
#first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
#first_n_smallest([1,2,3,4,5],0) == []
####################################################### SOLUTION ######################################################################
def first_n_smallest(arr, n):
    arr_copy = arr[:]
    index_ls = () #create tuple to store indexes
    for x in range(n):
        idx = arr_copy.index(min(arr_copy)) #get index of minimum
        index_ls += (idx,)
        arr_copy[idx] = max(arr_copy)+1 #replace min value per max + 1 (guarantee it will not be selected)
        
    return [arr[i] for i in sorted(index_ls)]
