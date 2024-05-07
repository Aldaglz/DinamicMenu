import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('C:\\Users\\USUARIO LENOVO\\Desktop\\Archivos VIDEO INNNOVATEC\\pito.wav') as source:
	audio=r.listen(source)

	try: 
		print("Reading audio file. Please, wait a moment...")
		text = r.recognize_google(audio, language='es-ES')
		time.sleep(1.5)
		print(text)

	except:
		print("I am sorry!, I can not understand!")