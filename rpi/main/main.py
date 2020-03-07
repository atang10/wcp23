import signal
import time
import arm
import cameras
import hardware
import webUI
import resultDiscrimination as rd


frameRate = 30 # fps

def receiveAlarm(signum,stack):
	if(running):
	        ts = time.time()
        	(feed1,feed2,feed3) = cameras.captureFrames()
		network.sendFrames(feed1,feed2,feed3)
        	timeElapsed = time.time()-ts
        	signal.alarm(1/frameRate-timeElapsed)
	#also possible to ignore flags during critical operations

## Highest Level Psuedocode ##

arm.init()
cameras.init()
hardware.init()
webui.connect()

while(running):
	pattern = network.recievePattern()
	arm.drawPattern()
	time.sleep(time)
	resultFrame = cameras.captureResult()
	result = rd.determineResult(resultFrame)
	webui.sendResult(result)
	hardware.flipBottles()
	hardware.pumpTrough()
terminate()

## OLD ##
	#Checking for process statuses
#	if !(arm.drawing):
#		(patternArrived, pattern) = webUI.getPattern()
#		if patternArrived: # to avoid drawing when no pattern in queue
#			patternArrived = False
#			activePattern.pass(pattern)
#	elif(arm.finishedDrawing)
#		arm.finishedDrawing = False # fix: i dont like main reaching into arm.py
#		cameras.captureResult() # (3)
#		result = rd.determineResult() # location of result photo should be set
#		webui.sendResult(result) # (4)
#		hardware.flipBottles() #activates timer
#		hardware.pumpTrough() #timer
#	else
#		activePattern = arm.draw(activePattern) # sloppy
	
#shutdown()

## Notes ##
# pseudocode for other parts will be written in separate files, imported at top
# 1: using sleep(), the camera recording time will likely conflict with the pattern drawing. Need a good solution (*)
#	* ideally the arm's controls can all be sent at once, i.e. the arm has its own command buffer	
# 2: not sure how best to give the website access to the video feed;
#	does this require waiting to send?
# 3: need to wait until result is computed
# 4: web ui should be waiting for result in this stage, or the result history is one big array that can be appended and read at any time

# Potentially good solution:
# import time
# class TimedItem:
# 	def __init__(...):
#		active #indicates whether timer for item has started
#		tActivated #records time at which timer starts
#		tStop #holds amount of time the item should be active for
#		deactivate #function pointer pointing at the protocol which deactivates the ongoing process
#	def timeIsUp(self):
#		return (time.time()-self.tActivated)=> self.tStop
#	def stopWhenDone(self):
#		if self.timeIsUp():
#			self.deactivate()
#
# cameraTimer = TimedItem( ... , camera.stopRecording)
# ...
# timedItems = [cameraTimer, ... ]
#
# for item in timedItems:
#	item.stopWhenDone()

# ** checking if the arm has executed a sent instruction
# activePattern: for each command to be sent to the arm, indicates whether:
#	-command has been sent and executed
#	-command not sent
#	-command sent but not executed

## /OLD ##
