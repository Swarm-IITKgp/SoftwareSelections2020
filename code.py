import sys
from api import *
from time import sleep
import numpy as np

#######    YOUR CODE FROM HERE #######################
grid =[]

class Node:
    def __init__(self,value,point):
        self.value = value  #0 for blocked,1 for unblocked
        self.point = point
        self.parent = None
        self.move=None
        self.H = 0
        self.G = 0
        
neigh=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

def isValid(pt):
    return pt[0]>=0 and pt[1]>=0 and pt[0]<200 and pt[1]<200

def neighbours(point):  #returns valid neighbours
    global grid,neigh
    x,y = point.point
    links=[]
    for i in range(len(neigh)):
        newX=x+neigh[i][0]
        newY=y+neigh[i][1]
        if not isValid((newX,newY)):
            continue
        links.append((i+1,grid[newX][newY]))
    return links
        
def diagonal(point,point2):
    return max(abs(point.point[0] - point2.point[0]),abs(point.point[1]-point2.point[1]))

def aStar(start, goal):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
                if(current.point==start.point):
                    path.append(current)
                    return path[::-1]
        #Loop through the node's children/siblings which are valid and not blocked
        for move,node in neighbours(current):
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #if cell is blocked
            if node.value==0:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + 1 #onl
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
                    node.move=move
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + 1
                node.H = diagonal(node, goal)
                #Set the parent to our current item
                node.parent = current
                node.move=move
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')

'''
PS: You need not write codes for all levels. You must
at least complete the function corresponding to the level
you're attempting at the moment.
'''
    
def level1(botId):
    global grid
    moveType = 5
    botsPose = get_botPose_list()
    obstaclePose = get_obstacles_list()
    greenZone = get_greenZone_list()
    redZone = get_redZone_list()
    originalGreenZone = get_original_greenZone_list()
    for i in range(200):
        grid.append([])
        for j in range(200):
            grid[i].append(Node(1,(i,j)))
    for pt in obstaclePose:
        for i in range(pt[0][0],pt[2][0]+1):
            for j in range(pt[0][1],pt[2][1]+1):
                grid[i][j]=Node(0,(i,j))
    start=grid[botsPose[0][0]][botsPose[0][1]]
    goal=grid[greenZone[0][0][0]][greenZone[0][0][1]]
    path=aStar(start, goal)
    print(len(path))
    print("final pos:",greenZone[0][0])
    pos=get_botPose_list()
    print("initial pos:",pos[0])
    sleep(5)
    for i in range(1,len(path)):
        successful_move, mission_complete = send_command(botId,path[i].move)
        pos=get_botPose_list()
        if successful_move:
            print("YES")
        else:
            print("NO")
        if mission_complete:
            print("MISSION COMPLETE")
        pos=get_botPose_list()
        print(pos[0])

def level2(botId):
    pass

def level3(botId):
    pass

def level4(botId):
    pass

def level5(botId):
    pass

def level6(botId):
    pass


#######    DON'T EDIT ANYTHING BELOW  #######################

if  __name__=="__main__":
    botId = int(sys.argv[1])
    level = get_level()
    if level == 1:
        level1(botId)
    elif level == 2:
        level2(botId)
    elif level == 3:
        level3(botId)
    elif level == 4:
        level4(botId)
    elif level == 5:
        level5(botId)
    elif level == 6:
        level6(botId)
    else:
        print("Wrong level! Please restart and select correct level")
