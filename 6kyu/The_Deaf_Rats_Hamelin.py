#Problem "The Deaf Rats of Hamelin"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/598106cb34e205e074000031
####################################################### INSTRUCTIONS ######################################################################
#Story
#The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
#
#But some of the rats are deaf and are going the wrong way!
#
#Kata Task
#How many deaf rats are there?
#
#Legend
#P = The Pied Piper
#O~ = Rat going left
#~O = Rat going right
#Example
#ex1 ~O~O~O~O P has 0 deaf rats
#ex2 P O~ O~ ~O O~ has 1 deaf rat
#ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

####################################################### SOLUTION ######################################################################
def count_deaf_rats(town): 
    #remove white spaces
    town = town.replace(" ","")
    
    #get index of Pied Piper
    idx = town.index("P")
    
    #get strings of rats to left and right of Piper
    left, right = town[:idx], town[idx+1:]
    
    #rats to left are going to Piper if "tails" are in even index
    #rats to right are going to Piper if "tails" are in odd index
    idx_left = [i for i, char in enumerate(left) if i%2 != 0 and char=="~"]
    idx_right = [i for i, char in enumerate(right) if i%2 == 0 and char=="~"]
    
    #return no. deaf rats
    return len(idx_left) + len(idx_right)
