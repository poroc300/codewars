#Problem "Traffic Lights - one car"
#level: 6kyu
#language: Python
#link: https://www.codewars.com/kata/5d0ae91acac0a50232e8a547
####################################################### INSTRUCTIONS ######################################################################
#The description uses several images to depict the problem. Please check the link provided above to see the description of this problem.
####################################################### SOLUTION #######################################################################
def light_changes_iter(n, *args):
    '''
    n - no. iterations
    args is a pattern in a form of tuple
    returns a tuple withthe iterations in which lights change
    '''
    iteration, tup = 0, ()
    while True:
        for x in args:
            iteration += x
            tup += (iteration,) #append tuple
            if max(tup) > n:
                return tup[:-1] #pop out last element, it is above last iteration

def update_road(road_state, init_lights):
    '''
    road_state - current road_state
    init_lights - list with the indexes of the state of the lights at iteration 0
    returns a string with the road status (lights) changed
    '''
    temp = road_state.split(" ") #string to list
    
    #only updates the positions correspondent to the initial signal
    #change current_pos if the car is in the same position as a signal
    for index in init_lights: 
        if temp[0][index] == "O":
            temp[0] = temp[0][:index] + "R" + temp[0][index+1:]

        elif temp[0][index] == "G":
            temp[0] = temp[0][:index] + "O" + temp[0][index+1:]

        elif temp[0][index] == "R":
            temp[0] = temp[0][:index] + "G" + temp[0][index+1:]

    return "".join(temp)
 
def traffic_lights(road_state, n):
    '''
    road_state is a list with the initial road state
    '''
    road = [] + [road_state] #store road progress in a list
    road_simulated = "." + road_state[1:] #simulates road without car
    
    #iterations where light changes if position starts with green, orange, red
    green = light_changes_iter(n, 5,1,5)
    orange = light_changes_iter(n, 1,5,5) 
    red = light_changes_iter(n, 5,5,1)

    #store the positions(indexes) of initial states of the lights to keep track 
    #how they should change across iterations
    init_green = [i for i,char in enumerate(road_simulated) if char == "G"]
    init_orange = [i for i,char in enumerate(road_simulated) if char == "O"]
    init_red = [i for i,char in enumerate(road_simulated) if char == "R"]
    
    #start variables
    pos_index = 0 #current position of the car

    for ite in range(1,n+1):
        #update lights according to iteration
        if ite in green:
            road_simulated = update_road(road_simulated, init_green)
        if ite in orange:
            road_simulated = update_road(road_simulated, init_orange)
        if ite in red:
            road_simulated = update_road(road_simulated, init_red)
        
        try:
            #check if car should stop
            if road_simulated[pos_index + 1] in ("O", "R"):
                road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index+1:]
                road.append(road_state)
                continue
            
            #move the car
            pos_index += 1
            road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index+1:]
            road.append(road_state)
    
        except IndexError: #last iteration, car goes out of road
            road.append(road_simulated)  
        
    return road
