from jetbot import Robot
import time
import ipywidgets.widgets as widgets
from IPython.display import display
import traitlets

robot = Robot()

try: 
	while True:
		robot.forward(0.5)
				
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()     
	print('\n		Stop!!! See you again!')


