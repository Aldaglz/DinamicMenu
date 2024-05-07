#cód1go principal 
#Nyaaaa

import sys
from diseño import * 

from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore , QtGui , QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, QThread, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import mediapipe as mp
import numpy as np
import os
import math
import time
import threading


import serial

from Comunicacion_Serial import Comunicacion
from conexionBD import Registro_datos

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

degrees=math.degrees
acos=math.acos




mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)



class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		#Mover ventana
		self.ui.frameSuperior.mouseMoveEvent = self.mover_ventana

		#Acceder a las paginas
		self.ui.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_Inicio))
		self.ui.btn_Pacientes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_Pacientes))
		self.ui.btn_Terapias.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_Interfaz_de_Terapia))

		#control barra de titulos
		self.ui.btn_Maximizar.clicked.connect(self.control_btn_Maximizar)
		self.ui.btn_Minimizar.clicked.connect(self.control_btn_Minimizar)
		self.ui.btn_Restaurar.clicked.connect(self.control_btn_Restaurar)
		self.ui.btn_Cerrar.clicked.connect(lambda: self.close())

		self.ui.btn_Restaurar.hide()

		#menu lateral
		self.ui.btn_Menu.clicked.connect(self.mover_menu)

		#Conexion con Arduino 
		self.serial =Comunicacion()
		self.puertos_disponibles()
		self.ui.cb_Baudios.addItems(self.serial.baudrates)
		self.ui.btn_Conectar.clicked.connect(self.conectar)
		
		#Video
		self.ui.btn_Encender.clicked.connect(self.start_video)
		self.ui.btn_Apagar.clicked.connect(self.cancel)
		
		#Combobox de Edad
		for i in range (100):
			self.ui.cb_Edad.addItem(str(i))

		#Combobox de Grado de TEA
		for i in range (3):
			self.ui.cb_Grado_TEA.addItem(str(i+1))

		#WorkOut List
		self.WorkOut = Registro_datos()
		
		#Boton para insertar datos del usuario en la base de datos
		self.ui.btn_SaveDataOfUser.clicked.connect(self.insertar_datos)
		

		#Boton para insertar terapias del usuario en la base de datos
		self.ui.btn_SaveDataOfTerhapy.clicked.connect(self.insertar_terapias)


		#Boton para ver los ejercicios del paciente
		self.ui.btn_BuscarEjercicios.clicked.connect(self.buscar_ejercicios)

		#Boton para inicia la terapia
		self.ui.btn_PlayWorkout.clicked.connect(self.Inicio)


		#------------------Variables de los angulos del cuerpo------------------------------------
		self.Var_Shoulder_Right=0
		self.Var_Shoulder_Left=0
		
		self.Var_Elbow_Right=0
		self.Var_Elbow_Left=0

		self.Var_Wrist_Right=0
		self.Var_Wrist_Left=0

		self.Var_Cuello=0
		self.Var_Cabeza=0

		self.Var_Expresion=0

		#Lista de Terapias insertadas en el combobox de ejercicio 1,2 y 3
		self.ui.cb_Ejercicio_1.addItems(self.WorkOut.terapias)
		self.ui.cb_Ejercicio_2.addItems(self.WorkOut.terapias)
		self.ui.cb_Ejercicio_3.addItems(self.WorkOut.terapias)

		self.buscar_pacientes();

	def Inicio(self,):
		
		
		mg_box = QMessageBox()
		mg_box.setWindowTitle("INICIO DE TERAPIA")
		mg_box.setText('MUCHO EXITO CON LA TERAPIA')
		mg_box.setIcon(QMessageBox.Information)
		mg_box.exec_()	
				




		
			

	

	def buscar_pacientes(self):
		self.ui.cb_SeleccionPaciente.clear()
		self.ui.cb_Paciente.clear()
		datoNombre=self.WorkOut.buscar_nombre()
		
		iter=0

		
		for row in datoNombre:
			self.ui.cb_Paciente.addItems(datoNombre[iter])
			self.ui.cb_SeleccionPaciente.addItems(datoNombre[iter])
			iter=iter+1
		

	def buscar_ejercicios(self):
		self.ui.lisWid_WorkOut.clear()
		nombrePaciente=self.ui.cb_Paciente.currentText()
		nombrePaciente=str("'"+nombrePaciente+"'")
		datoEjercicios = self.WorkOut.buscar_terapias(nombrePaciente)
		
		iter=0
		for row in datoEjercicios:
			self.ui.lisWid_WorkOut.addItems(datoEjercicios[iter])
			iter=iter+1
		
	def insertar_datos(self):
		Nombre=self.ui.txt_Nombre.text()
		ApePat=self.ui.txt_Apellido_Paterno.text()
		ApeMat=self.ui.txt_Apellido_Materno.text()
		Edad=self.ui.cb_Edad.currentText()
		Grado=self.ui.cb_Grado_TEA.currentText()
		Tutor=self.ui.txt_Tutor.text()
		Contacto=self.ui.txt_Telefono.text()

		self.WorkOut.inserta_usuario(Nombre,ApePat,ApeMat,Edad,Grado,Tutor,Contacto)
		self.ui.txt_Nombre.clear()
		self.ui.txt_Apellido_Paterno.clear()
		self.ui.txt_Apellido_Materno.clear()
		self.ui.cb_Edad.setCurrentText('0')
		self.ui.cb_Grado_TEA.setCurrentText('0')
		self.ui.txt_Tutor.clear()
		self.ui.txt_Telefono.clear()
		self.buscar_pacientes()

		mg_box = QMessageBox()
		mg_box.setWindowTitle("REGISTRO EXITOSO")
		mg_box.setText('REGISTRO DE DATOS DEL PACIENTE REALIZADO CON EXITO')
		mg_box.setIcon(QMessageBox.Information)
		mg_box.exec_()



	def insertar_terapias(self):
		Nombre=self.ui.cb_SeleccionPaciente.currentText()
		Ejercicio_1=self.ui.cb_Ejercicio_1.currentText()
		Ejercicio_2=self.ui.cb_Ejercicio_2.currentText()
		Ejercicio_3=self.ui.cb_Ejercicio_3.currentText()

		self.WorkOut.inserta_terapias (Nombre, Ejercicio_1, Ejercicio_2, Ejercicio_3)


		mg_box = QMessageBox()
		mg_box.setWindowTitle("REGISTRO EXITOSO")
		mg_box.setText('REGISTRO DE TERAPIAS DEL PACIENTE REALIZADO CON EXITO')
		mg_box.setIcon(QMessageBox.Information)
		mg_box.exec_()


	def start_video(self):
		bd=0

		if self.ui.rb_Skeleto.isChecked()==True:
			self.Streaming = Skeleton()
			bd=3
		elif self.ui.rb_both.isChecked()==True:
			self.Streaming = Streaming()
			bd=2
		elif self.ui.rb_Emociones.isChecked()==True:
			self.Streaming = Emotion()
			bd=1

	

		if bd==1:
			self.ui.lb_StateVideo.setText("Encendiendo...")
			
			#Se conectan con las imagenes generadas
			self.Streaming.ImageEmotion.connect(self.Imageupd_slot_Emotions)
			self.Streaming.ImageSkeleton.connect(self.Imageupd_slot_Skeleton)
			self.Streaming.PNG_Emoji.connect(self. Imageupd_slot_emoji)
			
			#Se conectan con los angulos tomados
			self.Streaming.Shoulder_Right.connect(self.Angulo_Shoulder_Derecho)
			self.Streaming.Shoulder_Left.connect(self.Angulo_Shoulder_izquierdo)
			self.Streaming.Elbow_Right.connect(self.Angulo_Elbow_Derecho)
			self.Streaming.Elbow_Left.connect(self.Angulo_Elbow_izquierdo)
			self.Streaming.Wrist_Right.connect(self.Angulo_Wrist_Derecho)
			self.Streaming.Wrist_Left.connect(self.Angulo_Wrist_izquierdo)
			self.Streaming.Cuello.connect(self.Angulo_Cuello)			
			self.Streaming.Cabeza.connect(self.Angulo_Cabeza)
			
			#Pantalla LCD
			self.Streaming.Expresion.connect(self.Expresion)
			self.Streaming.start()

		elif bd==2:
			self.ui.lb_StateVideo.setText("Encendiendo...")
			self.Streaming.Imageupd.connect(self.Imageupd_slot_video)
			self.Streaming.start()

		elif bd==3:
			self.ui.lb_StateVideo.setText("Encendiendo...")
			self.Streaming.Imageupd.connect(self.Imageupd_slot_videoSkele)
			self.Streaming.start()
	


		else:
			mg_box = QMessageBox()
			mg_box.setWindowTitle("ERROR")
			mg_box.setText('Seleccione una opcion de abajo')
			mg_box.setIcon(QMessageBox.Information)
			mg_box.exec_()

	#Funciones para enviar los datos a cada articulacion del cuerpo 

	def Angulo_Shoulder_Derecho(self,Shoulder_Right):#LISTO
		self.Shoulder_Right=Shoulder_Right
		trama=bytes(('S'+str((int(Shoulder_Right)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Shoulder_izquierdo(self,Shoulder_Left):
		self.Shoulder_Left=Shoulder_Left
		print (Shoulder_Left)
		trama=bytes(('s'+str((int(Shoulder_Left)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Elbow_Derecho(self,Elbow_Right): #LISTO
		self.Elbow_Right=Elbow_Right
		trama=bytes(('E'+str((int(abs(Elbow_Right-180))))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Elbow_izquierdo(self,Elbow_Left): #LISTO
		self.Elbow_Left=Elbow_Left
		trama=bytes(('e'+str((int(abs(Elbow_Left-180))))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Wrist_Derecho(self,Wrist_Right): #LISTO
		self.Wrist_Right=Wrist_Right
		trama=bytes(('W'+str(abs(int(Wrist_Right-90)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Wrist_izquierdo(self,Wrist_Left):#LISTO
		self.Wrist_Left=Wrist_Left
		trama=bytes(('w'+str(abs(int(Wrist_Left-90)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Cuello(self,Cuello):
		self.Cuello=Cuello
		trama=bytes(('N'+str((int(Cuello)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	def Angulo_Cabeza(self,Cabeza):
		self.Cabeza=Cabeza
		trama=bytes(('H'+str((int(Cabeza)))+"\n"), "utf-8")
		self.serial.enviar_datos(trama)

	#Funcion q manda la cara al LCD

	def Expresion(self,Expresion):
		trama=bytes('G'+(str(Expresion)+"\n"), "utf-8")
		self.serial.enviar_datos(trama)



	#Funciones que colocan las imagenes generadas en el hilo
	def Imageupd_slot_Emotions(self, ImageEmotion):
		self.ui.lb_Video.setPixmap(QPixmap.fromImage(ImageEmotion))
		self.ui.lb_StateVideo.setText("Captura de emociones activado") 


	def Imageupd_slot_Skeleton(self, ImageSkeleton):
		self.ui.lb_VideoSkeleto.setPixmap(QPixmap.fromImage(ImageSkeleton))
		self.ui.lb_StateVideo.setText("Captura del cuerpo activado") 

	def Imageupd_slot_emoji(self, PNG_Emoji):
		self.ui.label_4.setPixmap(PNG_Emoji)



	def Imageupd_slot_video(self,Imageupd):
		self.ui.lb_Video.setPixmap(QPixmap.fromImage(Imageupd))
	
	def Imageupd_slot_videoSkele(self,Imageupd):
		self.ui.lb_VideoSkeleto.setPixmap(QPixmap.fromImage(Imageupd))


	

	
	def cancel(self, Image):
		self.ui.lb_VideoSkeleto.clear()
		self.ui.lb_Video.clear()
		self.ui.label_4.clear()
		self.Streaming.stop()
		self.ui.lb_StateVideo.setText("Apagado")


	def control_btn_Minimizar(self):
		self.showMinimized()

	def control_btn_Restaurar(self):
		self.showNormal()
		self.ui.btn_Restaurar.hide()
		self.ui.btn_Maximizar.show()
		
	def control_btn_Maximizar(self):
		self.showMaximized()		
		self.ui.btn_Maximizar.hide()
		self.ui.btn_Restaurar.show()
		

	
	def mover_menu(self):
		if True:
			width = self.ui.frameLateral.width()
			normal = 0
			if width==0:
				extender = 200
			else: 
				extender= normal
			self.animacion=QPropertyAnimation(self.ui.frameLateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

			
 	##SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)


	##Mover ventana
	def mousePressEvent(self, event):
		self.clickPosition=event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized()==False:
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos()+event.globalPos()-self.clickPosition)
				self.clickPosition =event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()
			

	#Funciones para conectar la comunication serial del arduino
	def conectar(self):
		if (self.ui.btn_Conectar.text()=="Conectar"):		
			port = self.ui.cb_Puertos.currentText()
			baud = self.ui.cb_Baudios.currentText()
			self.serial.arduino.port= port
			self.serial.arduino.baudrate = baud
			self.serial.conexion_serial()
			self.ui.btn_Conectar.setText("Desconectar")
		elif (self.ui.btn_Conectar.text()=="Desconectar"):
			self.serial.desconectar()
			self.ui.btn_Conectar.setText("Conectar")
	
	def puertos_disponibles(self):
		self.serial.puertos_disponibles()
		self.ui.cb_Puertos.clear()
		self.ui.cb_Puertos.addItems(self.serial.puertos)
			




class Skeleton(QThread):
    Imageupd = Signal(QImage)
    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(1)
        with mp_pose.Pose(static_image_mode=False) as pose:
            while self.hilo_corriendo:
                ret, frame = cap.read() 
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flip = cv2.flip(Image, 1)

                    results=pose.process(flip)
                    if results.pose_landmarks is not None:
                        mp_drawing.draw_landmarks(flip,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(128,0,250),thickness=5,circle_radius=3),mp_drawing.DrawingSpec(color=(255,255,0),thickness=10))   
                        convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                        if self.hilo_corriendo:
                            pic = convertir_QT.scaled(600, 621, Qt.KeepAspectRatio)

                            self.Imageupd.emit(pic)
    def stop(self):
        self.hilo_corriendo = False
        self.quit()



class Streaming(QThread):
	Imageupd = Signal(QImage)
	def run(self):
		self.hilo_corriendo  = True
		cap = cv2.VideoCapture(1)
		while self.hilo_corriendo:
			ret, frame = cap.read() 
			if ret:
				Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				flip = cv2.flip(Image, 1)
				convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
				if self.hilo_corriendo:
					pic = convertir_QT.scaled(471, 321, Qt.KeepAspectRatio)
					self.Imageupd.emit(pic)
		
	def stop(self):
		self.hilo_corriendo = False
		self.quit()


def emotionsImage(emotion):
			resul=""
			if emotion=='angry': 
				resul="ta enojao"

			if emotion=='happy': 
				resul = "ta feli"
			return resul


class Emotion(QThread):
	#Señales Visuales
	ImageEmotion = Signal(QImage)
	ImageSkeleton = Signal(QImage)
	PNG_Emoji = Signal(QPixmap)

	#Angulos Pa' Mandar al Arduino
	Shoulder_Right= Signal(int)
	Shoulder_Left= Signal(int)
	Elbow_Right= Signal(int)
	Elbow_Left= Signal(int)
	Wrist_Right= Signal(int)
	Wrist_Left= Signal(int)
	Cuello= Signal(int)
	Cabeza= Signal(int)

	#Emociones
	Expresion= Signal(int)
	
	def run(self):
		dataPath=r'C:/Users/USUARIO LENOVO/Desktop/DinamicMenu/Emotions/Data'
		imagePaths = os.listdir(dataPath)
		print('imagePaths=',imagePaths)

		method='LBPH'
		if method=='LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

		emotion_recognizer.read("Emotions/modelitoLBPH.xml")
 
		self.hilo_corriendo = True
		cap=cv2.VideoCapture(1,cv2.CAP_DSHOW)
		faceClassif =cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
		with mp_pose.Pose(static_image_mode=False) as pose:
			while self.hilo_corriendo:
				bd =[0,0,0]

				ret,frame = cap.read()
				if ret:
					gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
					auxFrame=gray.copy() #Una copia del frame

					Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					flip = cv2.flip(Image, 1)

					#----------------------------------------------------PARTE DE RECONOCIMIENTO DE EMOCIONES----------------------------------------

					faces = faceClassif.detectMultiScale(gray,1.3,5)

					for (x,y,w,h) in faces:
						rostro=auxFrame[y:y+h,x:x+w]
						rostro = cv2.resize(rostro,(48,48),interpolation=cv2.INTER_CUBIC)	
						result = emotion_recognizer.predict(rostro)
						
						cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
								
						if method == 'LBPH':
							#LBPH
							if result[1] < 170:
								cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,0,255),5,cv2.LINE_AA)
								cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)								
								if imagePaths[result[0]]=='happy':
									bd[2]=1
								elif imagePaths[result[0]]=='angry':
									bd[2]=2
							else:
								cv2.putText(frame,"Desconocido",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
								cv2.rectangle(frame,(x,y),(x+w,y +h),(0,255,0),2)
			
					frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					convertir_QTEmo = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
					bd[0]=1
					
					#--------------------------------------------------PARTE DE DIAGRAMADO DE ESQUELETO--------------------------------------------
					results=pose.process(flip)
					if results.pose_world_landmarks is not None:

						#--------------------------------------PUNTOS DEL CUERPO:

						#Nota:Estos valores son tomados del tamañno de la ventana al full size (EJECUTAR VIDEO EN FULL SIZE)
						#width=723
						#height=631
						
						#Nota:Estos valores son tomados del tamañno de la ventana al promedio de reproduccion (EJECUTAR VIDEO ASI COMO ESTA; NO AGRADAR PANTALLA)
						width=640
						height=480

						#Nota: La nt da igual Xdddd


						#1___Nariz:
						nariz_x = int(results.pose_world_landmarks.landmark[0].x * width)
						nariz_y = int(results.pose_world_landmarks.landmark[0].y * height)
						
						#2___Oido Derecho:
						R_ear_x = int(results.pose_world_landmarks.landmark[7].x * width)
						R_ear_y = int(results.pose_world_landmarks.landmark[7].y * height)

						#3___Oido Izquierdo:
						L_ear_x = int(results.pose_world_landmarks.landmark[8].x * width)
						L_ear_y = int(results.pose_world_landmarks.landmark[8].y * height)

						#4___Hombro derecho:
						R_Shou_x = int(results.pose_world_landmarks.landmark[12].x * width)
						R_Sho_y = int(results.pose_world_landmarks.landmark[12].y * height)
						
						#5___Hombro Izquierdo:
						L_Shou_x = int(results.pose_world_landmarks.landmark[11].x * width)
						L_Sho_y = int(results.pose_world_landmarks.landmark[11].y * height)
							
						#6___Codo Derecho:
						R_Elb_x = int(results.pose_world_landmarks.landmark[14].x * width)
						R_Elb_y = int(results.pose_world_landmarks.landmark[14].y * height)
						

						#7___Codo Izquierdo:
						L_Elb_x = int(results.pose_world_landmarks.landmark[13].x * width)
						L_Elb_y = int(results.pose_world_landmarks.landmark[13].y * height)
						

						#8___Muñeca Derecha:
						R_Wri_x = int(results.pose_world_landmarks.landmark[16].x * width)
						R_Wri_y = int(results.pose_world_landmarks.landmark[16].y * height)
						
						
						#9___Muñeca Izquierda:
						L_Wri_x = int(results.pose_world_landmarks.landmark[15].x * width)
						L_Wri_y = int(results.pose_world_landmarks.landmark[15].y * height)

						#10__Cadera Derecha:
						R_Hip_x = int(results.pose_world_landmarks.landmark[24].x * width)
						R_Hip_y = int(results.pose_world_landmarks.landmark[24].y * height)

						#11__Cadera Izquierda:
						L_Hip_x = int(results.pose_world_landmarks.landmark[23].x * width)
						L_Hip_y = int(results.pose_world_landmarks.landmark[23].y * height)
						

						
						try:
						
							#----------------------PENDIENTES DEL
							def calculoPendientes(y2, y1, x2, x1):
								return ((y2 - y1) / (x2 - x1))

							def calculo_codos(m1,m2):
								return math.atan(((m2 - m1) / ((1) + (m1 * m2)))) * 180 / (math.pi)


							m1=calculoPendientes(R_Wri_y, R_Elb_y, R_Wri_x, R_Elb_x)
							m2=calculoPendientes(R_Elb_y, R_Sho_y, R_Elb_x, R_Shou_x)			
							
							m3=calculoPendientes(L_Wri_y, L_Elb_y, L_Wri_x, L_Elb_x)
							m4=calculoPendientes(L_Elb_y, L_Sho_y, L_Elb_x, L_Shou_x)
							
							
							#------------------------ANGULOS CAPTURADOS DEL LADO DERECHO

							angHombroIzq = abs(((math.atan((L_Sho_y - L_Elb_y) / ( L_Shou_x - L_Elb_x ))) * 180 / (math.pi)) + 90)
							angleBrazoIzq= calculo_codos(m1,m2)
							

							angHombroDer = abs(((math.atan((R_Sho_y - R_Elb_y) / ( R_Shou_x - R_Elb_x ))) * 180 / (math.pi)) + 90)
							angleBrazoDer=calculo_codos(m3,m4)

							

						except ZeroDivisionError:
							pass
						
						
						#CALCULO PARA SIMULACION DE PROFUNDIDAD EN BASE CODO-HOMBRO:

						R_Codos_Dath_Deep=results.pose_world_landmarks.landmark[14] #Capturamos todos los puntos (en este caso del codo derecho)					
						obtepcion_R=(str(R_Codos_Dath_Deep)).split('\n')#quitamos el salto de linea y los convertimos en una list 
						R_Elb_punto_Z=obtepcion_R[2]# para obtener el punto X, ubicamos la lista la posicion 0 (correspondiente a la coordenada x)
						DeteccionDeFrentizida =abs((float(R_Elb_punto_Z[3:]))*100)
						
						if (DeteccionDeFrentizida >22):
							Profundidad_Left=(90)
							angHombroDer=0
							angleBrazoIzq=0				
							
						elif (DeteccionDeFrentizida <=22  ):
							Profundidad_Left=(0)
							

						L_Codos_Dath_Deep=results.pose_world_landmarks.landmark[13] #Capturamos todos los puntos (en este caso del codo derecho)					
						obtepcion_L=(str(L_Codos_Dath_Deep)).split('\n')#quitamos el salto de linea y los convertimos en una list 
						L_Elb_punto_Z=obtepcion_L[2]# para obtener el punto X, ubicamos la lista la posicion 0 (correspondiente a la coordenada x)
						DeteccionDeFrentizida2 =abs((float(L_Elb_punto_Z[3:]))*100)
						
						if (DeteccionDeFrentizida2 >22 ):
							Profundidad_Right=(90)
							angHombroIzq=180
							angleBrazoDer=0				
							
						elif (DeteccionDeFrentizida2 <=22  ):
							Profundidad_Right=(180)
							
						
						
						#--------------------------------------------IMAGEN DE SALIDA------------------------------------------------------------
						mp_drawing.draw_landmarks(flip,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(128,0,250),thickness=5,circle_radius=3),mp_drawing.DrawingSpec(color=(255,255,0),thickness=10))   
						convertir_QTSke = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
						bd[1]=1
						

							
					

					if self.hilo_corriendo and bd[0]==1 and bd[1]==1: #Las banderas son para detectar una persona y q no crashee el programa
							self.ImageEmotion.emit(convertir_QTEmo)					
							self.ImageSkeleton.emit(convertir_QTSke)								

							#-------------------PUNTOS DEL CUERPO
							self.Elbow_Left.emit(angHombroIzq)
							self.Elbow_Right.emit(angHombroDer)

							self.Wrist_Right.emit(angleBrazoIzq)
							self.Wrist_Left.emit(angleBrazoDer)
							
							#self.Shoulder_Right.emit(Profundidad_Left)
							#self.Shoulder_Left.emit(Profundidad_Right)
							

							
							
							
							if bd[2]==1: #Aqui, las banderas son usadas para determinar la emocion justo al finalizar el proceso
								self.PNG_Emoji.emit(QPixmap("C:/Users/USUARIO LENOVO/Desktop/DinamicMenu/Emotions/emojis/feli.png"))
								self.Expresion.emit(3)
							elif bd[2]==2:
								self.PNG_Emoji.emit(QPixmap("C:/Users/USUARIO LENOVO/Desktop/DinamicMenu/Emotions/emojis/enojao.png"))						
								self.Expresion.emit(6)
		time.sleep(0.5)
						
	def stop(self):
		self.hilo_corriendo = False
		self.quit()






if __name__ == "__main__":
	app = QApplication(sys.argv) 
	mi_app = MiApp()
	mi_app.show()
	sys.exit(app.exec_())

















