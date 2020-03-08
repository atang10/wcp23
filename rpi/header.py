import signal
import time
from Arm import Arm
from Cameras import Cameras

#from Hardware import Hardware
#from WebUI import WebUI
#from ResultDiscrimination import ResultDiscrimination

def terminate(objs):
    for obj in objs:
        obj.terminate()
