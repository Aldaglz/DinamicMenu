import cv2
import mediapipe as mp
import numpy as np
import math
import serial
import time
ser = serial.Serial('COM6',9600,timeout=1)
time.sleep(1)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
degrees=math.degrees
acos=math.acos

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

def calculoPendientes(y2, y1, x2, x1):
	return ((y2 - y1) / (x2 - x1))
	


with mp_pose.Pose(
	static_image_mode=False) as pose:

	while True:
		ret, frame = cap.read()
		if ret == False:
			break
		frame = cv2.flip(frame,1)
		height, width, _ = frame.shape
		frame_rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		results=pose.process(frame_rgb)

		if results.pose_landmarks is not None:

	#-------------------------PUNTOS DEL CUERPO--------------------------------------------
			xRW = int(results.pose_landmarks.landmark[16].x * width)
			yRW = int(results.pose_landmarks.landmark[16].y * height)

			xRE = int(results.pose_landmarks.landmark[14].x * width)
			yRE = int(results.pose_landmarks.landmark[14].y * height)

			xRS = int(results.pose_landmarks.landmark[12].x * width)
			yRS = int(results.pose_landmarks.landmark[12].y * height)
			
			xLW = int(results.pose_landmarks.landmark[15].x * width)
			yLW = int(results.pose_landmarks.landmark[15].y * height)

			xLE = int(results.pose_landmarks.landmark[13].x * width)
			yLE = int(results.pose_landmarks.landmark[13].y * height)

			xLS = int(results.pose_landmarks.landmark[11].x * width)
			yLS = int(results.pose_landmarks.landmark[11].y * height)

			



			muñecaRight = np.array([xRW,yRW])
			codoRight = np.array([xRE,yRE])
			hombroRight = np.array([xRS,yRS])

			muñecaLeft = np.array([xLW,yLW])
			codoLeft = np.array([xLE,yLE])
			hombroLeft = np.array([xLS,yLS])

			try:
				m1=calculoPendientes(yRW,yRE,xRW,xRE)
				m2=calculoPendientes(yRE,yRS,xRE,xRS)			
				
				m3=calculoPendientes(yLW,yLE,xLW,xLE)
				m4=calculoPendientes(yLE,yLS,xLE,xLS)


				angHombroIzq = abs(((math.atan((yRS - yRE) / (xRS-xRE))) * 180 / (math.pi)) + 90)
				angCodoIzq= math.atan(((m2 - m1) / ((1) + (m1 * m2)))) * 180 / (math.pi)

				angHombroDer = abs(((math.atan((yLS - yLE) / (xLS-xLE))) * 180 / (math.pi)) + 90)
				angCodoDer= math.atan(((m4 - m3) / ((1) + (m3 * m4)))) * 180 / (math.pi)

				mp_drawing.draw_landmarks(
					frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
					mp_drawing.DrawingSpec(color=(128,0,250), thickness=10, circle_radius=3),
					mp_drawing.DrawingSpec(color=(255,255,0), thickness=20))
				
				print (yRE-yRS)
				#<>
	
				if ((yRE-yRS) >0):
					Ang="P0\n"
					print (Ang)

					angle=(int(angHombroIzq))
					Ang='s'+str(angle)+"\n"
					print (Ang)

					angle=(int(angCodoIzq)+90)
					Ang='e'+str(angle)+"\n"
					print (Ang)

						
					
				if ((yRE-yRS)<0):
					Ang="P180\n"
					print (Ang)

					angle=(180-int(angHombroIzq))
					Ang='s'+str(angle)+"\n"
					print (Ang)

					angle=(90-int(angCodoIzq))
					Ang='e'+str(angle)+"\n"
					print (Ang)

		
				if ((yLE-yLS) >0):
					angle=(int(angHombroDer))
					Ang='S'+str(angle)+"\n"
					print (Ang)

					angle=(int(angCodoDer)+90)
					Ang='E'+str(angle)+"\n"
					print (Ang)


				if ((yLE-yLS)<0):
					angle=(int(angHombroDer))
					Ang='S'+str(angle)+"\n"
					print (Ang)

					angle=(int(angCodoDer)+90)
					Ang='E'+str(angle)+"\n"
					print (Ang)
				
				

			except ZeroDivisionError:
				print("\U0001F917")
				

		cv2.imshow("Frame",frame)
		if cv2.waitKey(1) & 0xFF==27:
			break
cap.release()
cv2.destroyAllWindows()

