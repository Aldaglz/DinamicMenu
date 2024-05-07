from PySide2.QtCore import QObject 
import serial, serial.tools.list_ports

class Comunicacion(QObject):
    def __init__(self):
        super().__init__()
        self.arduino = serial.Serial()
        self.arduino.timeout =0.5


        self.baudrates=['1200','2400','4800','9600','19200','38400','115200']
        self.puertos = []


    def puertos_disponibles(self):
        self.puertos=[port.device for port in serial.tools.list_ports.comports()]

    def conexion_serial(self):
        try:
            self.arduino.open()
        except:
            print('Error al conectado')

    def enviar_datos(self,data):
        if (self.arduino.is_open):
            self.datos = (data)
            self.arduino.write(self.datos)
        else:
            print('No conectado')

    
    def desconectar(self):
        self.arduino.close()
        
    











        