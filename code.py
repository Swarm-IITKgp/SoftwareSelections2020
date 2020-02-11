import sys
from api import *
from time import sleep
import numpy as np

#######    YOUR CODE FROM HERE #######################
'''
PS: You need not write codes for all levels. You must
at least complete the function corresponding to the level
you're attempting at the moment.
'''

def level1(botId):
    send_command(botId, 2)

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
