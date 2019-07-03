import xbox,time,cv2
import camera_jetbot as video


try: 
	while True:
		video.show_camera()
		
## Ctrl + c to stop robot
except KeyboardInterrupt:
        # Close serial connection
	move.stop()     
	print('\n		Stop!!! See you again!')
