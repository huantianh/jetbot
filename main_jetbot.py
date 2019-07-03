from jetbot import Robot
import xbox
import motor
import time

move = Robot()

try: 
	while True:
		mode = input("Enter mode: f forward, b backward, l left, r right, s stop, c controller ")
		
		if mode ==  'f':	
			move.forward(0.5)
			print("Jetbot is moving foward!")	
			
		elif mode ==  'b':	
			move.backward(0.5)
			print("Jetbot is moving backward!")			

		elif mode ==  'l':	
			move.left(0.5)
			print("Jetbot is turning left!")			

		elif mode ==  'r':	
			move.right(0.5)
			print("Jetbot is turning right!")			
				
		elif mode ==  's':	
			move.stop()
	
		elif mode ==  'c':	
			joy = xbox.Joystick()
			while True:
				if (joy.Y()):
					move.forward(0.5)
					print("Jetbot is moving foward!")	
				elif (joy.A()):
					move.backward(0.5)	
					print("Jetbot is moving backward!")	
				elif (joy.X()):
					move.left(1)
					move.stop()
					move.forward(0.5)	
					print("Jetbot is turning left!")
				elif (joy.B()):
					move.right(1)
					move.stop()
					move.forward(0.5)
					print("Jetbot is turning right!")
				elif (joy.Start()):
					move.stop()
		


## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	move.stop()     
	print('\n		Stop!!! See you again!')
