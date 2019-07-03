from jetbot import Robot
# ~ from jetbot import Camera
# ~ from jetbot import bgr8_to_jpeg

import xbox,time,cv2
# ~ import ipywidgets.widgets as widgets
# ~ import traitlets
import camera_jetbot as video

move = Robot()
# ~ camera = Camera.instance()

try: 
	while True:	
		joy = xbox.Joystick()
		print('Jetbot is running!!!')
		while True:
			# ~ if (joy.Y()):
				# ~ move.forward(0.5)
				# ~ print("Jetbot is moving foward!")	
			# ~ elif (joy.A()):
				# ~ move.backward(0.5)	
				# ~ print("Jetbot is moving backward!")	
			# ~ elif (joy.X()):
				# ~ move.left(1)
				# ~ move.stop()
				# ~ move.forward(0.5)	
				# ~ print("Jetbot is turning left!")
			# ~ elif (joy.B()):
				# ~ move.right(1)
				# ~ move.stop()
				# ~ move.forward(0.5)
				# ~ print("Jetbot is turning right!")
			# ~ elif (joy.Start()):
				# ~ move.stop()
			if (joy.leftY()):
				move.forward(0.5)
				print("Jetbot is moving foward!")	
			elif (joy.rightY()):
				move.backward(0.5)	
				print("Jetbot is moving backward!")	
			elif (joy.leftX()):
				move.left(1)
				move.stop()
				move.forward(0.5)	
				print("Jetbot is turning left!")
			elif (joy.rightX()):
				move.right(1)
				move.stop()
				move.forward(0.5)
				print("Jetbot is turning right!")
			elif (joy.Start()):
				move.stop()
			elif (joy.Back()):
				video.show_camera()	
			
			# ~ image = widgets.Image(format = 'jpeg', width = 500, hight = 500)
			# ~ display(image)
			# ~ camera_link = trailets.dlink((camera, 'value'), (image, 'value'), transform = bgr8_to_jpeg)


## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	move.stop()     
	print('\n		Stop!!! See you again!')
