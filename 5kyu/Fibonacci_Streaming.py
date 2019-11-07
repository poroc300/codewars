#Problem "Fibonacci Streaming"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/55695bc4f75bbaea5100016b
####################################################### INSTRUCTIONS ######################################################################
#You're going to provide a needy programmer a utility method that generates an infinite sized, sequential IntStream 
#(in TypeScript Iterator<number>, in Python generator) which contains all the numbers in a fibonacci sequence.
#A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements. See:
#1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...
####################################################### SOLUTION #######################################################################
def all_fibonacci_numbers():
    x,y = 0,1
    while True:
        yield y
        x,y = y, x+y
