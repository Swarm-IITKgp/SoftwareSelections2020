from api import *
import threading, os, sys

class myThread (threading.Thread):
   def __init__(self, botId):
      threading.Thread.__init__(self)
      self.botId = botId

   def run(self):
      os.system("python3 code.py "+str(self.botId))

level = 0
while level == 0:
    if sys.version_info[0] == 2:
        level = int(raw_input("Please enter the level you're attempting(1-6): "))
    else:
        level = int(input("Please enter the level you're attempting(1-6): "))
    if 1 <= level <= 6:
        restart_mission(level)
        break
    else:
        level = 0

if level == 1:
    os.system("python3 code.py 0")
    print("The final score is: " + str(get_score()))
elif level == 2:
    os.system("python3 code.py 0")
    print("The final score is: " + str(get_score()))
elif level == 3:
    threads = []
    for i in range(2):
        thread = myThread(i)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 4:
    threads = []
    for i in range(get_numbots()):
        thread = myThread(i)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 5:
    threads = []
    for i in range(2):
        thread = myThread(i)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
elif level == 6:
    threads = []
    for i in range(get_numbots()):
        thread = myThread(i)
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    print("The final score is: "+str(get_score()))
