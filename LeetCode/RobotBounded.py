def moved(instructions):
        # pos=[x-axis of robot position,y-axis of robot position]
        # direction: N=0, E=1, S=2, W=3
        pos,direction=[0,0],0
        for d in instructions:
            if d=='G' and direction==0:
                pos[0] += 1    # move to North (x+1,y)
            elif (d,direction)==('G',2) :
                pos[0] -= 1    # move to South (x-1,y)
            elif (d,direction)==('G',1) :
                pos[1] += 1    # move to East (x,y+1)
            elif (d,direction)==('G',3) :
                pos[1] -= 1    # move to West (x,y-1)
            elif d=='L':
                direction = (direction-1)%4
            else:
                direction = (direction+1)%4
        if pos==[0,0]:
            return False      # Robot is not moved after following the set of instructions
        else:
            return True       # Robot has moved from the starting position
    
def isRobotBounded(instructions):
        rcount=instructions.count('R')%4  # count number of right turns. Mod 4 as 4 times right means coming back to 
        lcount=instructions.count('L')%4
        gcount=instructions.count('G')

        if gcount==0:        # if the Robot is not moving, then it will stay at the same place
            return True
        if rcount==lcount:   # direction of robot remains same as before
            if moved(instructions)=='True': 
                return False # if the robot's position has changed, then robot can not be confined in a circle indefinitely
            else:
                return True  # if robot didn't change position after following the set of instruction, then it will repeat same movements indefinitely
        else:
            return True      # if direction is changed after the set of instruction, then robot will either make a rhombus (if facing L or R) and come back to start position after 4 sets, or (if facing opposite direction) will come back to start pos after 2nd set

if __name__=='__main__':
    print(isRobotBounded('GLRLLGLL'))
        
