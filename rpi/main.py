import header *

## Initializing module objects: ##
arm = Arm()
cameras = Cameras()
#hardware = Hardware()
#webUI = WebUI()

running = True
frameRate = 30 # fps

## Main loop: ##
while(running):
#    pattern = network.recievePattern()
    arm.drawPattern()
    running = False
#    resultFrame = cameras.captureResult()
#    result = rd.determineResult(resultFrame)
#    webui.sendResult(result)
#    hardware.flipBottles()
#    hardware.pumpTrough()
terminate((arm,cameras))

## Frame callback: ##
def receiveAlarm(signum,stack):
    if(running):
        ts = time.time()
        frames = cameras.grabFramesEach()
        cameras.showFramesEach(frames)
#        network.sendFrames(feed1,feed2,feed3)
        timeElapsed = time.time()-ts
        signal.alarm(1/frameRate-timeElapsed)
        print("frame callback"+str(timeElapsed))
    #also possible to ignore flags during critical operations
