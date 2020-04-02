import RPi.GPIO as GPIO   # Import the GPIO library.
from time import sleep               # Import time library

class Hardware:

    def __init__(self, pins=[12,16,20]):
        GPIO.setmode(GPIO.BCM) #bcm pin names, use `pinout` in terminal
        self.servoPin = pins[0]
        self.pumpPin = pins[1]
        self.valvePin = pins[2]

        #Servo initialization:
        GPIO.setup(self.servoPin,GPIO.OUT)
        self.servo = GPIO.PWM(self.servoPin,50) #pwm on pins[0] and 50Hz freq
        self.servo.start(5) # 5% pwm duty cycle = 1ms = 0 degrees 

        #Pump initialization:
        GPIO.setup(self.pumpPin,GPIO.OUT, initial=0)

        #Valve initialization:
        GPIO.setup(self.valvePin,GPIO.OUT, initial=0) 

    def terminate(self):
        self.servo.stop()      # stop PWM
        GPIO.cleanup()  # resets GPIO ports used back

    def flipBottles(self):
        self.servo.ChangeDutyCycle(10) # 10% pwm = 2ms = 180 degrees
        sleep(5)
        self.servo.ChangeDutyCycle(5) # 5% pwm

    def pumpOn(self):
        GPIO.output(self.pumpPin,GPIO.HIGH)

    def pumpOff(self):
        GPIO.output(self.pumpPin,GPIO.LOW)

    def valveOpen(self):
        GPIO.output(self.valvePin,GPIO.HIGH)

    def valveClose(self):
        GPIO.output(self.valvePin,GPIO.LOW)
