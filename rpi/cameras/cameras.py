from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

class Cameras:

    def __init__(self):
        self.frameRate = 30
#try:
        print("Starting cameras...")
        self.webcam1 = VideoStream(src=0).start()
        #self.webcam2 = VideoStream(src=1).start()
        self.picam = VideoStream(usePiCamera=True).start()
        time.sleep(2.0)

    def grabFramesEach(self):
        frames = []
        for stream in [self.webcam1,self.picam]: #self.webcam2
                frame = stream.read()
                frame = imutils.resize(frame, width=400)
                frames.append(frame)
        return frames

    def showFramesEach(self,frames):
        timestamp = datetime.datetime.now()
        ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        # loop over the frames a second time
        for (frame, name) in zip(frames, ("Webcam1", "Picamera")):
            # draw the timestamp on the frame and display it
            cv2.putText(frame, ts, (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.imshow(name, frame)

    def terminate(self):
        cv2.destroyAllWindows()
        self.webcam1.stop()
        self.picam.stop()

cams = Cameras()
while True:
    frames = cams.grabFramesEach()
    cams.showFramesEach(frames)

    # check to see if a key was pressed
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cams.terminate()
