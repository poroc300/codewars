#Problem "Football - Yellow and Red Cards"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/5cde4e3f52910d00130dc92c
####################################################### INSTRUCTIONS ######################################################################
#Most football fans love it for the goals and excitement. Well, this Kata doesn't. You are to handle the referee's little 
#notebook and count the players who were sent off for fouls and misbehavior.

#The rules: Two teams, named "A" and "B" have 11 players each; players on each team are numbered from 1 to 11. 
#Any player may be sent off the field by being given a red card. A player can also receive a yellow warning card, 
#which is fine, but if he receives another yellow card, he is sent off immediately (no need for a red card in that case). 
#If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, and the team with less 
#than 7 players loses.

#A card is a string with the team's letter ('A' or 'B'), player's number, and card's color ('Y' or 'R') - all 
#concatenated and capitalized. e.g the card 'B7Y' means player #7 from team B received a yellow card.

#The task: Given a list of cards (could be empty), return the number of remaining players on each team at the 
#end of the game (as a tuple of 2 integers, team "A" first). If the game was terminated by the referee for 
#insufficient number of players, you are to stop the game immediately, and ignore any further possible cards.

#Note for the random tests: If a player that has already been sent off receives another card - ignore it.

####################################################### SOLUTION ######################################################################
def men_still_standing(cards):
    #create dictionaries 
    teamA = {"A"+str(i): 0 for i in range(1,12)}
    teamB = {"B"+str(i): 0 for i in range(1,12)}
    
    n_playersA, n_playersB = 11, 11
    
    for cd in cards:
        #check team
        if cd[0] == "A":
            team = teamA
        else:
            team = teamB
            
        #do not process players already sent off
        if team[cd[:-1]] >= 2:
            continue
        
        #set score for red card or yellow card
        score = 2 if cd[-1] == "R" else 1
        
        #update score
        team[cd[:-1]] += score
        
        #exclude players if they have a score >=2
        if team[cd[:-1]] >= 2 and cd[0] == "A":
            n_playersA -= 1
        elif team[cd[:-1]] >= 2 and cd[0] == "B":
            n_playersB -= 1
        
        #terminate game if a team has less than 7 players
        if n_playersA < 7 or n_playersB < 7:
            break
    
    return (n_playersA, n_playersB)
        
