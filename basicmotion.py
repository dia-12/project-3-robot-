from buildhat import Motor
from basehat import Button

frontRightMotor = Motor('C')
frontLeftMotor = Motor('A')
backMotor = Motor('B')

button = Button(22)

try:
    while True:
        value = button.value()
        if value:
            speed = 100
        else:
            speed = 0
    
    frontRightMotor.start(speed)
    frontLeftMotor.start(speed)
    backMotor.start(speed)

except KeyboardInterrupt:
        frontRightMotor.stop()
        frontLeftMotor.stop()
        backMotor.stop()
   
    



