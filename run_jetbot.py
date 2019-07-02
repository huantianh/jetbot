from jetbot import Robot
import time
import ipywidgets.widgets as widgets
from IPython.display import display
import traitlets

robot = Robot()

def stop():
    robot.stop()
    
def forward():
    robot.forward(0.4)

def backward():
    robot.backward(0.4)

def left():
    robot.left(0.3)

def right():
    robot.right(0.3)

try: 
	while True:
		forward()
				
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()     
	print('\n		Stop!!! See you again!')


