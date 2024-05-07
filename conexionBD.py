import mysql.connector

class Registro_datos():

	def __init__(self):
		self.conexion = mysql.connector.connect(host = 'localhost',
												database = 'neurobot',
												user='root',
												password='LuzRoja21_')
		self.terapias=['Levanta Brazo Derecho Hasta Arriba','Levanta Brazo Izquierdo Hasta Arriba', 'Levanta Brazos Hacia Enfrente', 'Mueve la cabeza hacia la Izquierda','Mueve la cabeza hacia la derecha','T-Pose','Sonrie']

	def inserta_usuario (self, nombre, apPat, apMat, Edad, Grado, Tutor, Contacto):
		cur=self.conexion.cursor()
		sql = '''INSERT INTO pacientes(nombre, apellido_paterno, apellido_materno, edad, grado_de_TEA, tutor_responsable, contacto) 
		VALUES ('{}','{}','{}','{}','{}', '{}','{}')'''. format(nombre, apPat, apMat, Edad, Grado, Tutor, Contacto)
		cur.execute(sql)
		print("DATOS ENVIADOS CORRECTAMENTE")
		self.conexion.commit()
		cur.close()

	def inserta_terapias (self, nombre,ejercicio_1, ejercicio_2, ejercicio_3):
		cur=self.conexion.cursor()
		sql = '''INSERT INTO terapias(nombre,ejercicio_1, ejercicio_2, ejercicio_3 ) 
		VALUES ('{}','{}', '{}','{}')'''.format(nombre, ejercicio_1, ejercicio_2, ejercicio_3)
		cur.execute(sql)
		self.conexion.commit()
		cur.close()

	def buscar_terapias (self, nombresito):
		cur = self.conexion.cursor()
		sql = "SELECT ejercicio_1, ejercicio_2, ejercicio_3 FROM terapias WHERE nombre = {}".format(nombresito)
		cur.execute(sql)
		nombreX = cur.fetchall()
		cur.close()
		return nombreX

	def buscar_nombre(self):
		cur = self.conexion.cursor()
		sql = "SELECT nombre FROM pacientes"
		cur.execute(sql)
		nombreX = cur.fetchall()
		print ("UAUAUAUUAUAAUAU")
		cur.close()
		return nombreX

