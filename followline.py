from buildhat import Motor
from basehat import Button
from basehat import grovepi

frontRightMotor = Motor('C')
frontLeftMotor = Motor('A')
backMotor = Motor('B')

lineFinder = 12
lightSensor = 2

button = Button(22)

try:
    while True:
        value = button.value()
        line = grovepi.digitalread(lineFinder)
        light = grovepi.digitalread(lightSensor)
        if value:
            
            if line and light:
                frontRightMotor.start(100)
                frontLeftMotor.start(100)
                backMotor.start(100)
            else if line:
                frontRightMotor.start(50)  #one front motor has different speed to make it turn one direction
                frontLeftMotor.start(100)
                backMotor.start(100)
            else if light:
                frontRightMotor.start(100)
                frontLeftMotor.start(50)
                backMotor.start(100)
        else:
            speed = 0
    
    frontRightMotor.start(speed)
    frontLeftMotor.start(speed)
    backMotor.start(speed)

except KeyboardInterrupt:
        frontRightMotor.stop()
        frontLeftMotor.stop()
        backMotor.stop()
