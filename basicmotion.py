from buildhat import Motor
from basehat import Button
from basehat import LightSensor
from basehat import LineFinder

frontRightMotor = Motor('C')
frontLeftMotor = Motor('A')
backMotor = Motor('B')
lightSensor = LightSensor(2)
lineFinder = LineFinder(12)
button = Button(22)

try:
    while True:
        buttonValue = button.value()
        lightValue = lightSensor.value()
        lineValue = lineFinder.value()
        if buttonValue:
            if lineValue == 1 and lightValue <= 100:
                frontRightSpeed = 50
                frontLeftSpeed = -50
                backSpeed = 50
            elif lineValue == 1:
                frontRightSpeed = 100
                frontLeftSpeed = -50
                backSpeed = 5
            elif lightValue <= 100:
                frontRightSpeed = -50
                frontLeftSpeed = 100
                backSpeed = 5
            else:
                frontRightSpeed = 0
                frontLeftSpeed = 0
                backSpeed = 0
                print("No lines detected")
            frontRightSpeed = 100
            frontLeftSpeed = 50
            backSpeed = 50
        
        frontRightMotor.start(frontRightSpeed)
        frontLeftMotor.start(frontLeftSpeed)
        backMotor.start(backSpeed)

except KeyboardInterrupt:
        frontRightMotor.stop()
        frontLeftMotor.stop()
        backMotor.stop()
   
    



