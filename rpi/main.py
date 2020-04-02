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

#### Functions: ####

## Frame callback: ##
def receiveAlarm(signum,stack):
    global running
    global cameras
    if(running):
#        ts = time.time()
        key = cv2.waitKey(1) & 0xFF #strange but necessary
        frames = cameras.grabFramesEach()
        cameras.showFramesEach(frames)
#        network.sendFrames(feed1,freed2,feed3)
#        timeElapsed = time.time()-ts
#        signal.alarm(1/frameRate-timeElapsed) #timeElapsed must be less than framerate
#        print("frame callback: "+str(timeElapsed))
    #also possible to ignore alarm during critical operations

def terminate(objs):
    for obj in objs:
        obj.terminate()

def startIntervalTimer(interval):
# generates a signal every 1/frameRate seconds
# intercepted w/ the callback recieveAlarm
    signal.signal(signal.SIGALRM, receiveAlarm)
    signal.setitimer(signal.ITIMER_REAL,interval,interval)

#### Main: ####

## Initializing module objects: ##
arm = Arm()
cameras = Cameras()
#hardware = Hardware()
#webUI = WebUI()

running = True
frameRate = 30 # fps
startIntervalTimer(1/frameRate)

## Main loop: ##
try:
    while True:
    #    pattern = network.recievePattern()
        arm.drawPatternSVG("arm/border.svg")
        break
    #    resultFrame = cameras.captureResult()
    #    result = rd.determineResult(resultFrame)
    #    webui.sendResult(result)
    #    hardware.flipBottles()
    #    hardware.pumpTrough()
except KeyboardInterrupt:
    print("Ctrl C pressed, terminating...")
finally:
    terminate((arm,cameras))

