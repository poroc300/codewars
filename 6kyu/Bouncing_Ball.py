#Problem "Bouncing Balls"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
####################################################### INSTRUCTIONS ######################################################################
#A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

#He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

#His mother looks out of a window 1.5 meters from the ground.

#How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

#Three conditions must be met for a valid experiment:
  #Float parameter "h" in meters must be greater than 0
  #Float parameter "bounce" must be greater than 0 and less than 1
  #Float parameter "window" must be less than h.
  
#If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

#Note:
#The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

####################################################### SOLUTION ######################################################################
def bouncingBall(h, bounce, wind):
    bounce = float(bounce)
    
    #check if requirements are met
    if not ((h > 0) and (0 < bounce < 1) and (wind < h)):
        return -1
    
    count = 1 #the ball should pass at least one time when it falls the first time
    while h > wind:
        h *= bounce        
        count += 2 if h > wind else 0 #bounce and falls, but when lower than window, is not seen by the mother
    return count
