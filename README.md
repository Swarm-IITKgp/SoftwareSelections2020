# Swarm Robotics Software Team Selections

## Pre-requisites
* Please install Ubuntu 16.04 or above on your laptop (Cannot verify the sanity of the codes for Windows machine)
* Ensure you have Python3 (no guarantees for Python2, should work though) and pip installed
* Ensure you have basic understanding of Python
* Please download/clone the latest version of this repository. If any bug is discovered, please mail to spandankumarsahu@gmail.com, with the bug details. For the most updated codes, use `git pull swarm master`, once you have cloned the repository.

## Resources
* [Git and Github tutorial](https://in.udacity.com/course/how-to-use-git-and-github--ud775-india)
* [A* path planning algorithm](https://www.hackerearth.com/practice/notes/a-search-algorithm/)
* [Dijkstra path planning](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
* [Obstacle Avoidance and Path Retracing](https://2019.robotix.in/tutorial/pathplanning/obstacleavoidance/)
* [RRT Path Planning](https://2019.robotix.in/tutorial/pathplanning/rrtplanner/)

## Submission Guidelines

We have already added you to a Google Group. You should receive further notifications on that group itself.

The contest is live till 4th March, 2020. You need to submit only `code.py` file over email to the following email address: spandankumarsahu@gmail.com, with the subject as `[Software Selections 2020]<RollNumber>`

There will be meetings held for doubts and help, on a per need basis, the exact date and time will be notified through email. Having said that, please feel free to mail at: spandankumarsahu@gmail.com, if you've any questions regarding either the Problem statement or help regarding the codes.

For any queries, doubts or help, please email at: spandankumarsahu@gmail.com or give a call to Shreyase(9167887737) or Spandan(7477858944).

## How to Run
Clone this repository (either download it, or use this command on a terminal: `git clone https://github.com/Swarm-IITKgp/SoftwareSelections2020`)


FIRST RUN:

In one terminal, enter the following:

  `python controller.py`

The program would prompt you to enter a level. Start with 1 and work your way upto level 6.


Your task is to complete up as many functions/levels as possible in `code.py` and submit your codes to spandankumarsahu@gmail.com. You need not attempt all the levels, but sure, the more the better your chances are to get into the team. Your functions may not be optimal (in some cases, optimality cannot even be guaranteed!). We would solely judge on how you approach the problem and how much effort you've put in! :)

This problem statement will be updated with a sample (path planning algorithm) submission for level 1 problem before midsems. We shall be providing samples (pretty pretty unintelligent algorithms) for higher levels too. But we expect you to do better than the dumb algorithms we provide.

We will also try to provide C++ APIs, if the need arises. However, we would strongly suggest you to use Python in this case. We will also keep on updating the codes and information regarding this would be sent on the Google group.

## Code Structure
There is really not much to play with. There is only one file named `code.py`, which you must edit and fill out the functions. You're encouraged to use solutions from the lower levels to solve problems of higher level. You can refer to the documentations in `api.py`, in case you are unsure about what a command does.

## Working Procedure
(PS: Please go through the problem description to understand the working procedure)

There is an instance of a server which is responsible for maintaining the grid, the position of the bots, handling multiple command requests and so on. The `controller.py` is responsible for simulating multiple bots, using threads. The `code.py` file uses functions from `api.py` to send commands to the server which then replicates what would happen in the zooids' world.

To attempt a different level, just close the terminal processes (like using Ctrl+c), and follow the run instructions again.

You can also use the APIs to view different metrics. Just `from api import *` in your Python code.

## Problem Description
The problem is based on the world of zooids, where you are their master. The world of zooid is a grid of dimension 200 x 200. As in any real world, there are obstacles occupying some portions of the grid. The obstacles are strictly rectangular in shape.

Each zooid is capable of some basic locomotion. If the zooid is at a location X in a grid, then a movement of type 1, would take it to the grid marked as 1, a movement of type 2 would take it to the grid marked 2 and so on.

1 2 3

8 X 4

7 6 5

As such, zooids are pretty unintelligent beings. Your mission, should you choose to accept, is to make them intelligent and intelligent as a whole. You would learn what is an agent, what is an objective, what is environment, what is a more constrained environment, what is intelligence and how swarm intelligence works.

The obstacles (you cannot move through obstacles) are marked in the map in black, the moving blue colored objects are your zooids, the green colored regions are the ones you must visit, and the red colored regions are the ones you should avoid (you can go through them, but you will end up paying twice as much in any other traversable cell). At each level, the goal is to visit all the green colored regions in as minimum number of steps as possible.

### Level 1
The first level, is to make zooid Zoozoo aware of his capabilities, and show him that he can walk efficiently. Zoozoo's initial and final position will be known to you, and you have to guide Zoozoo through the grid to his destination. Once you reach the destination, you will be awarded a score. Your goal is to reach the destination with as little score as possible. This is an example of a single agent, single objective system.

### Level 2
The second level, is to make Zoozoo intelligent enough to go through all the green regions at least once. This is an example of a single agent, but multiple objective system.

### Level 3
They say, third's the charm! Zoozoo finally has a friend. They have many green regions to go through, and they should co-operate among themselves to achieve this goal with minimum steps. This is an example of multi-agent, multi-objective system.

### Level 4
Zoozoo and his friend have now wondered into a swarm. There are many more zooids, each equally capable as Zoozoo. And there are still more than one green regions to go through. Can they cooperate as a group? This should teach them something about swarm systems!

### Level 5
Zoozoo and his friend have now been landed into a harsher territory. It's only two of them and they are still to go through the green regions, but now, there are patches of red regions that they should ideally avoid, because each step through the red region is counted as 2 steps. But then, sometimes, it might be necessary to go through the red regions in order to avoid a longer way through the green one. Hmmmm.. they need some intelligence!

### Level 6
Now a swarm of zooids has joined in to help Zoozoo and his friend. This is the beginning of swarm intelligence. Now, do you feel like a God who programmed his creations to intelligence?

## Problems?
Please understand that this game was developed to give a feel of Swarm. There might be bugs, or instances of server being down or upgrades happening and many such issues which we couldn't have possibly accounted for.

In case anything about the code seems off to you, please drop an email at spandankumarsahu@gmail.com
