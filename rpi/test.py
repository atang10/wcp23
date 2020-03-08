from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import cv2

import signal
import time
from Arm import Arm
from Cameras import Cameras
#from Hardware import Hardware
#from WebUI import WebUI
#from ResultDiscrimination import ResultDiscrimination

## Initializing module objects: ##
#arm = Arm()
#cameras = Cameras()
#hardware = Hardware()
#webUI = WebUI()

def receiveAlarmCams(signum,stack):
    global cameras
    global running
    if(running):
#        ts = time.time()
        frames = cameras.grabFramesEach()
        cameras.showFramesEach(frames)
#        network.sendFrames(feed1,freed2,feed3)
#        timeElapsed = time.time()-ts
#        signal.alarm(1/frameRate-timeElapsed) #timeElapsed must$
#        print("frame callback: "+str(timeElapsed))
    #also possible to ignore alarm during critical operations

def terminate(objs):
    for obj in objs:
        obj.terminate()

def startIntervalTimer(interval):
# generates a signal every 1/frameRate seconds
# intercepted w/ the callback recieveAlarm
    signal.signal(signal.SIGALRM, receiveAlarmCams)
    signal.setitimer(signal.ITIMER_REAL,interval,interval)


running = True
frameRate = 30 # fps
cameras = Cameras()

startIntervalTimer(1/frameRate)

#frames = cameras.grabFramesEach()
#cameras.showFramesEach(frames)

while True:
    # check to see if a key was pressed
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cameras.terminate()
