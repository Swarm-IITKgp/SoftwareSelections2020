import requests, time, pickle, sys
from io import BytesIO
from PIL import Image
import numpy as np

'''
You can view using browser also!
Contact any team member, if you want a demo
'''

BASE_URL = 'http://10.72.22.92:5000/'
add_usr_url = BASE_URL+'add'
restart_mission_url = BASE_URL+'restart'
cmd_url = BASE_URL+'move'
score_url = BASE_URL+'score'
botPose_url = BASE_URL+'botPose'
obstacle_url = BASE_URL+'obstaclesPose'
greenZone_url =  BASE_URL+'greenZone'
original_greenZone_url = BASE_URL+'originalGreenZone'
redZone_url = BASE_URL+'redZone'
level_url = BASE_URL+'level'
numbots_url = BASE_URL+'numbots'
map_url = BASE_URL+'map'

def authenticate():
    try:
        f = open('credentials.p', 'rb')
    except IOError:
        if sys.version_info[0] == 2:
            roll = raw_input("Enter your roll: ")
        else:
            roll = input("Enter your roll: ")
        pswd = roll + str(int(time.time()))
        args = {
            'roll': roll,
            'pswd': pswd
        }
        r=requests.get(add_usr_url, params=args)
        if r.json()['success']:
            with open('credentials.p', 'wb') as f:
                pickle.dump({'pswd': pswd}, f, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            print("Please contact someone in the team!")
            exit(0)
        f = open('credentials.p', 'rb')
    finally:
        credentials = pickle.load(f)
        f.close()
        return credentials

def restart_mission(level):
    '''
    Inputs:
        level       int     the level of the game you're attempting
    Returns:
        success             bool    True, if the move being tried happened, False otherwise
        message             bool    (optional)

    Work:
    You won't be needing this command, unless you decide to tweak something in
    the APIs. This API does exactly what it says, it resets and restarts a mission
    based on the "level" you mention.
    '''
    args = authenticate()
    args['level'] = level
    r=requests.get(restart_mission_url, params=args)
    time.sleep(0.05)
    return r.json()['success']

def send_command(botId, moveType):
    '''
    Inputs:
        botId       int     The ID of the bot
        moveType    int     movement type, as descriped in the README
    Returns:
        success             bool    True, if the move being tried happened, False otherwise
        mission_complete    bool    True, if all the goals have been completed

    Work:
        Use this command to instruct the zooid to move. If the zooid cannot move,
        because of obstacle, or another zooid already occupying the grid or all
        green regions have already been collected, then it will return False.
        Otherwise, it will update the position of the zooid with ID as botId to
        the required location and return True. Now, if all the green regions
        have been collected, the mission_complete value will be set to True
    '''
    args = authenticate()
    args['botId'], args['moveType'] = botId, moveType
    r=requests.get(cmd_url, params=args)
    time.sleep(0.05)
    return r.json()['success'], r.json()['mission_complete']

def get_level():
    '''
    Inputs:

    Returns:
        level   int     The level which you're attempting
    '''
    args = authenticate()
    r = requests.get(level_url, params=args)
    time.sleep(0.05)
    return r.json()['level']

def get_numbots():
    '''
    Inputs:

    Returns:
        numbots   int     Total number of zooids on the grid
    '''
    args = authenticate()
    r = requests.get(numbots_url, params=args)
    time.sleep(0.05)
    return r.json()['numbots']

def get_score():
    '''
    Inputs:

    Returns:
        score   int     Total number of steps, the less the better
    '''
    args = authenticate()
    r = requests.get(score_url, params=args)
    time.sleep(0.05)
    return r.json()['score']

def get_obstacles_list():
    '''
    Inputs:

    Returns:
        obs_list   list     Each element of the returned list is a list containing
                            4 vertices of the rectangular obstacle, in a
                            clockwise manner,starting from the left top corner
    Work:
    This represents the list of rectangular obstacles. You cannot move a zooid
    through an obstacle.
    '''
    args = authenticate()
    r = requests.get(obstacle_url, params=args)
    time.sleep(0.05)
    return r.json()

def get_redZone_list():
    '''
    Inputs:

    Returns:
        red_list   list     Each element of the returned list is a list containing
                            4 vertices of the rectangular obstacle, in a
                            clockwise manner,starting from the left top corner
    Work:
    This represents the list of rectangular red regions. You can move a zooid
    through a red region, but you have to pay twice the number of steps. So try
    and avoid this region, unless the other viable path is really long.
    '''
    args = authenticate()
    r = requests.get(redZone_url, params=args)
    time.sleep(0.05)
    return r.json()

def get_greenZone_list():
    '''
    Inputs:

    Returns:
        green_list   list   Each element of the returned list is a list containing
                            4 vertices of the rectangular obstacle, in a
                            clockwise manner,starting from the left top corner
    Work:
    This represents the list of rectangular green regions. Each green region must
    be visited by at least one zooid, and a green region is said to be visited,
    if any zooid passes through at least one of its grid.

    Please keep in mind, that this is a dynamic list. That is, once a green region
    is visited, it is moved out of this list. So the mission is to get this list empty.
    '''
    args = authenticate()
    r = requests.get(greenZone_url, params=args)
    time.sleep(0.05)
    return r.json()

def get_original_greenZone_list():
    '''
    Inputs:

    Returns:
        green_list   list   Each element of the returned list is a list containing
                            4 vertices of the rectangular obstacle, in a
                            clockwise manner,starting from the left top corner
    Work:
    Same as the list of green regions, except that, this list is not changed. So,
    it would contain all the green regions that were there in the beginning
    '''
    args = authenticate()
    r = requests.get(original_greenZone_url, params=args)
    time.sleep(0.05)
    return r.json()

def get_botPose_list():
    '''
    Inputs:

    Returns:
        botPose     list    Each element of the returned list is a list containing
                            2 elements (x, y) denoting the position of the zooids
                            on the grid.
    Work:
    Contains the updated list of position of the zooids on the grid. This is the
    most important function, in terms of feedback.
    '''
    args = authenticate()
    r = requests.get(botPose_url, params=args)
    time.sleep(0.05)
    return r.json()

def get_Map():
    '''
    Inputs:

    Returns:
        numpy array of map image
    Work:
    '''
    args = authenticate()
    r = requests.get(map_url, params=args)
    img = np.array(Image.open(BytesIO(r.content)))
    return img
