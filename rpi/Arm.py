#scaling wrong: {12"} = 9+5/8"
# {fake inches} = real inches
#max distance is {14.6"} = 11+3/4"
# changing speed requires disconnecting
# program frozen until finished moving

from pyaxidraw import axidraw   # import module
import signal
import time

### Project code ###

#from pyaxidraw import axidraw

class Arm:
    def __init__(self):
        self.axidraw = axidraw.AxiDraw() 

    def drawPatternSVG(self,pattern):
        self.axidraw.plot_setup(pattern)
        self.axidraw.plot_run()

#    def drawPatternCoord(self,pattern)
#        self.axidraw.disconnect()

    def terminate(self):
        pass
