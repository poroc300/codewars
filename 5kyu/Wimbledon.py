#Problem "Wimbledon Scoreboard - Game"
#level: 5kyu
#language: Python
#link: https://www.codewars.com/kata/wimbledon-scoreboard-game/python
####################################################### INSTRUCTIONS ######################################################################
#The description uses several images to depict the problem. Please check the link provided above to see the description of this problem.
####################################################### SOLUTION #######################################################################
class Match(object):
    def __init__(self, balls):
        self.balls = balls
        
    # update no. balls 
    def updateBalls(self, index):
        self.balls = self.balls[index:]

    # check if match is over    
    def isOver(self):
        return self.balls == []
    
    # check if game is in deuce
    def isDeuce(self, plyr_S, plyr_O):
        '''
        plyr_S, plyr_O are two instances of Player
        '''
        return plyr_S.getPoints() in (40, "AD") and plyr_O.getPoints() in (40, "AD")

    
class Player(object):
    def __init__(self):
        self.points = {0:15, 15:30, 30:40, 40:"win"}
        self.deuce = {40:"AD", "AD":"win"} # scoring system for deuce
        self.score = [0,0] # player's score [games, points]

    # get scored points of a player    
    def getPoints(self): 
        return self.score[1]

    # check if game was won by a player
    def gameWin(self):
        return self.getPoints() == "win"  
    
    # update score
    def UpdateScore(self, other_plyr, match):
        '''
        self wons the point
        self and other_plyr are two instances of Player
        match is an instance of Match
        '''
        # game in deuce
        if match.isDeuce(self, other_plyr):
            if other_plyr.score[1] == "AD":
                self.score[1], other_plyr.score[1] = 40, 40
            elif other_plyr.score[1] == 40:
                self.score[1] = self.deuce[self.getPoints()]
        
        else:
            self.score[1] = self.points[self.getPoints()]   
        
        #check if self wins
        if self.gameWin(): 
            reset_score(self, other_plyr)
            return True #determines if game is finished to change service             


### helper functions
def reset_score(plyr1, plyr2):
    '''
    plyr1, plyr2are two instances of Player
    assumes plyr1 wins the game
    '''
    plyr1.score, plyr2.score = [plyr1.score[0] + 1, 0], [plyr2.score[0], 0] # winner, looser

def play_service(plyr1, plyr2, match):
    '''
    plyr1, plyr2 are two instances of Player
    match is instance of Match
    assumes plyr1 is serving
    '''
    # only 1 ball left to play    
    if len(match.balls) == 1:
        if match.balls[0]: # True
            match.balls = []
            return plyr1.UpdateScore(plyr2, match)
        
        match.balls = []
    
    # double fault
    elif match.balls[0:2] == [False, False]:
        match.updateBalls(2)
        return plyr2.UpdateScore(plyr1, match) 
      
    # single fault 
    elif not match.balls[0]:
        match.updateBalls(1)

             
def wimbledon(balls):
    match = Match(balls)
    plyr_S, plyr_O = Player(), Player() # opposite, serving player
    n_games = 0
    
    # play until match is over
    while not match.isOver():
        game_finished = False
        plyr_S, plyr_O = plyr_O, plyr_S # shift service
        n_games += 1 
        
        # play a game
        while not match.isOver() and not game_finished:
            
            # play service
            while True:
                game_finished = play_service(plyr_S, plyr_O, match)
                if game_finished or match.isOver() or match.balls[0]:
                    break
            
            # terminate game
            if match.isOver() or game_finished:
                break
            
            # next moves after service (try to find a False)
            try:
                # if index is odd, serving player wins point
                if match.balls.index(False)%2 != 0:
                    game_finished = plyr_S.UpdateScore(plyr_O, match)
                else:
                    game_finished = plyr_O.UpdateScore(plyr_S, match)
                
                match.updateBalls(match.balls.index(False) + 1)
            
            # if only Trues remaining
            except ValueError:
                if len(match.balls)%2 != 0:
                    game_finished = plyr_S.UpdateScore(plyr_O, match)
                else:
                    game_finished = plyr_O.UpdateScore(plyr_S, match)
                    
                match.balls = []
        
                    
    # use no. games to display score (player 1, player 2)
    if n_games%2 != 0:
        P1, P2 = plyr_S, plyr_O
    else:
        P2, P1 = plyr_S, plyr_O
                 
    return [[str(P1.score[0]), str(P1.score[1])], 
            [str(P2.score[0]), str(P2.score[1])]]    
