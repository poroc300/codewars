#Problem "Blackjack Scorer"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/534ffb35edb1241eda0015fe
####################################################### INSTRUCTIONS ######################################################################
#Complete the function that determines the score of a hand in the card game Blackjack (aka 21).
#
#The function receives an array of strings that represent each card in the hand ("2", "3", ..., "10", "J", "Q", "K" or "A") and 
#should return the score of the hand (integer).
#
#Scoring rules:
#Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.
#
#Return the highest score of the cards that is less than or equal to 21. If there is no score less than or equal to 21 return the 
#smallest score more than 21.
#
#Examples
#["A"]                           ==>  11
#["A", "J"]                      ==>  21
#["A", "10", "A"]                ==>  12
#["5", "3", "7"]                 ==>  15
#["5", "4", "3", "2", "A", "K"]  ==>  25
####################################################### SOLUTION ##########################################################################

def score_hand(cards):
    #replace face cards by "10" to sort the list and put Aces in the end
    #to better control their value
    cards = sorted( ["10" if c in "JQK" else c for c in cards] )
    score = 0
    n_aces = cards.count("A")    
    for card in cards:
        #score numbers
        if card in "2345678910":
            score += int(card)
        #score aces
        else:
            #deal with multiple aces
            if (score + 11 + (n_aces-1)) > 21:
                score += n_aces
            else:
                score += 11 + (n_aces-1)
            break
    return score  
    
###more efficient solution
#def score_hand(cards):
#    score = sum(11 if c == "A" else 10 if c in "JQK" else int(c) for c in cards)
#    for _ in range(cards.count("A")):
#        if score > 21:
#            score -= 10
#    return score
