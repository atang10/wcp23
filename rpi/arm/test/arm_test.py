from pyaxidraw import axidraw   # import module
import signal
import time

def receiveAlarm(signum,stack):
    #ts = time.time()
    print("paused")
    time.sleep(.1)
    #timeElapsed = time.time()-ts
   # signal.setitimer(signal.ITIMER_REAL,.1)
    print("drawing")

signal.signal(signal.SIGALRM, receiveAlarm)
signal.setitimer(signal.ITIMER_REAL,.2,.2)

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
