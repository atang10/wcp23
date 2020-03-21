import RPi.GPIO as GPIO   # Import the GPIO library.
from time import sleep               # Import time library

class Hardware:

    def __init__(self, pins=[12,16,20]):
        GPIO.setmode(GPIO.BCM) #bcm pin names, use `pinout` in terminal
        self.servoPin = pins[0]
        self.pumpPin = pins[1]
        self.valvePin = pins[2]

        #Servo initialization:
        GPIO.setup(self.pins[0],GPIO.OUT)
        self.servo = GPIO.PWM(self.pins[0],50) #pwm on pins[0] and 50Hz freq
        self.servo.start(5) # 5% pwm duty cycle = 1ms = 0 degrees 

        #Pump initialization:
        GPIO.setup(self.pins[1],GPIO.OUT, initial=0)

        #Valve initialization:
        GPIO.setup(self.pins[2],GPIO.OUT, initial=0) 

    def terminate(self):
        servo.stop()      # stop PWM
        GPIO.cleanup()  # resets GPIO ports used back

    def flip_bottles(self):
        self.servo.ChangeDutyCycle(10) # 10% pwm = 2ms = 180 degrees
        sleep(5)
        self.servo.ChangeDutyCycle(5) # 5% pwm

    def pump_on(self):
        GPIO.output(pumpPin,GPIO.HIGH)

    def pump_off(self):
        GPIO.output(pumpPin,GPIO.LOW)

    def valve_open(self):
        GPIO.output(led,GPIO.HIGH)

    def valve_close(self):
        GPIO.output(led,GPIO.LOW)
