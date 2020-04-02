from Hardware import Hardware
from time import sleep

hardware = Hardware()
for i in range(10):
    hardware.valveOpen()
    sleep(1)
    hardware.valveClose()
    sleep(1)
hardware.terminate()
quit()
