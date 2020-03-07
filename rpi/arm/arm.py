#scaling wrong: {12"} = 9+5/8"
# {fake inches} = real inches
#max distance is {14.6"} = 11+3/4"
# changing speed requires disconnecting
# program frozen until finished moving



#from pyaxidraw import axidraw
#ad = axidraw.AxiDraw()
#ad.plot_setup("AxiDraw_API_v256/test/assets/AxiDraw_trivial.svg")
#print('bals')
#ad.plot_run()
#print("bals2")

from pyaxidraw import axidraw   # import module
import signal
import time

def receiveAlarm(signum,stack):
	#ts = time.time()
	print("paused")
	time.sleep(1)
	#timeElapsed = time.time()-ts
	signal.alarm(2)
	print("drawing")

signal.signal(signal.SIGALRM, receiveAlarm)
signal.alarm(2)

ad = axidraw.AxiDraw()          # Initialize class
ad.interactive()                # Enter interactive context
ad.connect()                    # Open serial port to AxiDraw 
                                # Absolute moves follow:
ad.moveto(0,0)                  # Pen-up move to (1 inch, 1 inch)
print("drawing")
ad.lineto(8,0)                  # Pen-down move, to (2 inch, 1 inch)
ad.lineto(8,8)
ad.lineto(0,8)
ad.lineto(0,0)
ad.move(0,0)                  # Pen-up move, back to origin.
ad.disconnect()                 # Close serial port to AxiDraw

### Project code ###

#from pyaxidraw import axidraw

#class Arm
#	def __init__(self):
#		self.axidraw = axidraw.AxiDraw() 
	
#	def drawPattern
