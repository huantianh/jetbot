from jetbot import Robot

robot = Robot()

try: 
	while True:
		mode = input("Enter mode: f forward, b backward, l left, r right, s stop ")
		
		if mode ==  'f':	
			robot.forward(0.5)
			print("Jetbot is moving foward!")	
			
		if mode ==  'b':	
			robot.backward(0.5)
			print("Jetbot is moving backward!")			

		if mode ==  'l':	
			robot.left(0.5)
			print("Jetbot is turning left!")			

		if mode ==  'r':	
			robot.right(0.5)
			print("Jetbot is turning right!")			
				
		if mode ==  's':	
			robot.stop()

## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	robot.stop()     
	print('\n		Stop!!! See you again!')
