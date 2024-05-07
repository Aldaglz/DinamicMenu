# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazDMcsmI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1212, 684)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameSuperior = QFrame(self.centralwidget)
        self.frameSuperior.setObjectName(u"frameSuperior")
        self.frameSuperior.setMinimumSize(QSize(0, 40))
        self.frameSuperior.setMaximumSize(QSize(16777215, 40))
        self.frameSuperior.setStyleSheet(u"background-color: rgb(19, 136, 168);")
        self.frameSuperior.setFrameShape(QFrame.StyledPanel)
        self.frameSuperior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameSuperior)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_Menu = QPushButton(self.frameSuperior)
        self.btn_Menu.setObjectName(u"btn_Menu")
        self.btn_Menu.setMinimumSize(QSize(200, 35))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.btn_Menu.setFont(font)
        self.btn_Menu.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(19, 136, 168);\n"
"font :87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font :87 12pt \"Arial Black\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Menu.setIcon(icon)
        self.btn_Menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_Menu)

        self.horizontalSpacer = QSpacerItem(644, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_Minimizar = QPushButton(self.frameSuperior)
        self.btn_Minimizar.setObjectName(u"btn_Minimizar")
        self.btn_Minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Minimizar.setIcon(icon1)
        self.btn_Minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_Minimizar)

        self.btn_Restaurar = QPushButton(self.frameSuperior)
        self.btn_Restaurar.setObjectName(u"btn_Restaurar")
        self.btn_Restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Restaurar.setIcon(icon2)
        self.btn_Restaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_Restaurar)

        self.btn_Maximizar = QPushButton(self.frameSuperior)
        self.btn_Maximizar.setObjectName(u"btn_Maximizar")
        self.btn_Maximizar.setMaximumSize(QSize(16777215, 35))
        self.btn_Maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Maximizar.setIcon(icon3)
        self.btn_Maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_Maximizar)

        self.btn_Cerrar = QPushButton(self.frameSuperior)
        self.btn_Cerrar.setObjectName(u"btn_Cerrar")
        self.btn_Cerrar.setMaximumSize(QSize(16777215, 35))
        self.btn_Cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Cerrar.setIcon(icon4)
        self.btn_Cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_Cerrar)


        self.gridLayout_2.addWidget(self.frameSuperior, 0, 0, 1, 1)

        self.frameInferior = QFrame(self.centralwidget)
        self.frameInferior.setObjectName(u"frameInferior")
        self.frameInferior.setFrameShape(QFrame.StyledPanel)
        self.frameInferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameInferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameLateral = QFrame(self.frameInferior)
        self.frameLateral.setObjectName(u"frameLateral")
        self.frameLateral.setMinimumSize(QSize(0, 0))
        self.frameLateral.setMaximumSize(QSize(0, 16777215))
        self.frameLateral.setStyleSheet(u"QFrame{\n"
"background-color: rgb(19, 136, 168);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(19, 136, 168);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font:75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font:75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"")
        self.frameLateral.setFrameShape(QFrame.StyledPanel)
        self.frameLateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameLateral)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_Inicio = QPushButton(self.frameLateral)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setMinimumSize(QSize(0, 40))
        self.btn_Inicio.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Inicio.setIcon(icon5)
        self.btn_Inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_Inicio)

        self.btn_Pacientes = QPushButton(self.frameLateral)
        self.btn_Pacientes.setObjectName(u"btn_Pacientes")
        self.btn_Pacientes.setMinimumSize(QSize(0, 40))
        self.btn_Pacientes.setMaximumSize(QSize(16777215, 40))
        icon6 = QIcon()
        icon6.addFile(u"icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Pacientes.setIcon(icon6)
        self.btn_Pacientes.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_Pacientes)

        self.btn_Terapias = QPushButton(self.frameLateral)
        self.btn_Terapias.setObjectName(u"btn_Terapias")
        self.btn_Terapias.setMinimumSize(QSize(0, 40))
        self.btn_Terapias.setMaximumSize(QSize(16777215, 40))
        icon7 = QIcon()
        icon7.addFile(u"icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Terapias.setIcon(icon7)
        self.btn_Terapias.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.btn_Terapias)

        self.verticalSpacer = QSpacerItem(20, 425, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frameLateral)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Cascadia Mono")
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frameLateral)

        self.frameContenedor = QFrame(self.frameInferior)
        self.frameContenedor.setObjectName(u"frameContenedor")
        self.frameContenedor.setStyleSheet(u"\n"
"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frameContenedor.setFrameShape(QFrame.StyledPanel)
        self.frameContenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameContenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_Pacientes_no_usable = QWidget()
        self.page_Pacientes_no_usable.setObjectName(u"page_Pacientes_no_usable")
        self.verticalLayout_4 = QVBoxLayout(self.page_Pacientes_no_usable)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 188, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.btn_CrearPaciente = QPushButton(self.page_Pacientes_no_usable)
        self.btn_CrearPaciente.setObjectName(u"btn_CrearPaciente")
        font2 = QFont()
        font2.setPointSize(16)
        self.btn_CrearPaciente.setFont(font2)
        self.btn_CrearPaciente.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente)

        self.btn_CrearPaciente_4 = QPushButton(self.page_Pacientes_no_usable)
        self.btn_CrearPaciente_4.setObjectName(u"btn_CrearPaciente_4")
        self.btn_CrearPaciente_4.setFont(font2)
        self.btn_CrearPaciente_4.setStyleSheet(u"\n"
"background-color: rgb(98, 198, 80);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_4)

        self.btn_CrearPaciente_2 = QPushButton(self.page_Pacientes_no_usable)
        self.btn_CrearPaciente_2.setObjectName(u"btn_CrearPaciente_2")
        self.btn_CrearPaciente_2.setFont(font2)
        self.btn_CrearPaciente_2.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_2)

        self.btn_CrearPaciente_3 = QPushButton(self.page_Pacientes_no_usable)
        self.btn_CrearPaciente_3.setObjectName(u"btn_CrearPaciente_3")
        self.btn_CrearPaciente_3.setFont(font2)
        self.btn_CrearPaciente_3.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_3)

        self.verticalSpacer_2 = QSpacerItem(20, 187, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_Pacientes_no_usable)
        self.page_Inicio = QWidget()
        self.page_Inicio.setObjectName(u"page_Inicio")
        self.page_Inicio.setAutoFillBackground(False)
        self.page_Inicio.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.page_Inicio)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.page_Inicio)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")
        self.label_5.setPixmap(QPixmap(u"bg_MainBody.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.page_Inicio)
        self.page_Pacientes = QWidget()
        self.page_Pacientes.setObjectName(u"page_Pacientes")
        self.page_Pacientes.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.page_Pacientes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_RegistroUsuario = QGroupBox(self.page_Pacientes)
        self.gb_RegistroUsuario.setObjectName(u"gb_RegistroUsuario")
        font3 = QFont()
        font3.setFamily(u"MS Sans Serif")
        font3.setPointSize(15)
        font3.setItalic(True)
        self.gb_RegistroUsuario.setFont(font3)
        self.gb_RegistroUsuario.setStyleSheet(u"background-color: rgb(70, 157, 214);")
        self.gridLayout_6 = QGridLayout(self.gb_RegistroUsuario)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lb_Contacto = QLabel(self.gb_RegistroUsuario)
        self.lb_Contacto.setObjectName(u"lb_Contacto")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.lb_Contacto.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_Contacto, 5, 0, 1, 1)

        self.txt_Apellido_Materno = QLineEdit(self.gb_RegistroUsuario)
        self.txt_Apellido_Materno.setObjectName(u"txt_Apellido_Materno")
        self.txt_Apellido_Materno.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.txt_Apellido_Materno, 2, 3, 1, 3)

        self.lb_LastNameMother = QLabel(self.gb_RegistroUsuario)
        self.lb_LastNameMother.setObjectName(u"lb_LastNameMother")
        self.lb_LastNameMother.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_LastNameMother, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(80, 23, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.txt_Tutor = QLineEdit(self.gb_RegistroUsuario)
        self.txt_Tutor.setObjectName(u"txt_Tutor")
        self.txt_Tutor.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.txt_Tutor, 4, 3, 1, 3)

        self.lb_Tutor = QLabel(self.gb_RegistroUsuario)
        self.lb_Tutor.setObjectName(u"lb_Tutor")
        self.lb_Tutor.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_Tutor, 4, 0, 1, 1)

        self.lb_Edad = QLabel(self.gb_RegistroUsuario)
        self.lb_Edad.setObjectName(u"lb_Edad")
        self.lb_Edad.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_Edad, 3, 0, 1, 1)

        self.txt_Telefono = QLineEdit(self.gb_RegistroUsuario)
        self.txt_Telefono.setObjectName(u"txt_Telefono")
        self.txt_Telefono.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.txt_Telefono, 5, 3, 1, 3)

        self.lb_Grade_Of_TEA = QLabel(self.gb_RegistroUsuario)
        self.lb_Grade_Of_TEA.setObjectName(u"lb_Grade_Of_TEA")
        self.lb_Grade_Of_TEA.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_Grade_Of_TEA, 3, 4, 1, 1)

        self.txt_Apellido_Paterno = QLineEdit(self.gb_RegistroUsuario)
        self.txt_Apellido_Paterno.setObjectName(u"txt_Apellido_Paterno")
        self.txt_Apellido_Paterno.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.txt_Apellido_Paterno, 1, 4, 1, 2)

        self.lb_LastNameFater = QLabel(self.gb_RegistroUsuario)
        self.lb_LastNameFater.setObjectName(u"lb_LastNameFater")
        self.lb_LastNameFater.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_LastNameFater, 1, 0, 1, 1)

        self.lb_Name = QLabel(self.gb_RegistroUsuario)
        self.lb_Name.setObjectName(u"lb_Name")
        self.lb_Name.setFont(font4)

        self.gridLayout_6.addWidget(self.lb_Name, 0, 0, 1, 1)

        self.txt_Nombre = QLineEdit(self.gb_RegistroUsuario)
        self.txt_Nombre.setObjectName(u"txt_Nombre")
        self.txt_Nombre.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.txt_Nombre, 0, 3, 1, 3)

        self.cb_Grado_TEA = QComboBox(self.gb_RegistroUsuario)
        self.cb_Grado_TEA.setObjectName(u"cb_Grado_TEA")
        self.cb_Grado_TEA.setMaximumSize(QSize(121, 21))
        self.cb_Grado_TEA.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.cb_Grado_TEA, 3, 5, 1, 1)

        self.cb_Edad = QComboBox(self.gb_RegistroUsuario)
        self.cb_Edad.setObjectName(u"cb_Edad")
        self.cb_Edad.setMaximumSize(QSize(121, 21))
        self.cb_Edad.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.cb_Edad, 3, 2, 1, 1)

        self.btn_SaveDataOfUser = QPushButton(self.gb_RegistroUsuario)
        self.btn_SaveDataOfUser.setObjectName(u"btn_SaveDataOfUser")
        self.btn_SaveDataOfUser.setMinimumSize(QSize(131, 81))
        self.btn_SaveDataOfUser.setMaximumSize(QSize(131, 81))
        font5 = QFont()
        font5.setPointSize(12)
        self.btn_SaveDataOfUser.setFont(font5)
        self.btn_SaveDataOfUser.setStyleSheet(u"background-color:rgb(255, 163, 35)")
        icon8 = QIcon()
        icon8.addFile(u"icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_SaveDataOfUser.setIcon(icon8)

        self.gridLayout_6.addWidget(self.btn_SaveDataOfUser, 6, 4, 1, 1)


        self.gridLayout.addWidget(self.gb_RegistroUsuario, 0, 0, 1, 1)

        self.gb_SeleccionTerapias = QGroupBox(self.page_Pacientes)
        self.gb_SeleccionTerapias.setObjectName(u"gb_SeleccionTerapias")
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(16)
        font6.setItalic(True)
        self.gb_SeleccionTerapias.setFont(font6)
        self.gb_SeleccionTerapias.setStyleSheet(u"background-color: rgb(55, 177, 116);")
        self.gridLayout_7 = QGridLayout(self.gb_SeleccionTerapias)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lb_Ejercicio_3 = QLabel(self.gb_SeleccionTerapias)
        self.lb_Ejercicio_3.setObjectName(u"lb_Ejercicio_3")
        font7 = QFont()
        font7.setFamily(u"Cascadia Mono")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.lb_Ejercicio_3.setFont(font7)

        self.gridLayout_7.addWidget(self.lb_Ejercicio_3, 7, 0, 1, 1)

        self.btn_SaveDataOfTerhapy = QPushButton(self.gb_SeleccionTerapias)
        self.btn_SaveDataOfTerhapy.setObjectName(u"btn_SaveDataOfTerhapy")
        self.btn_SaveDataOfTerhapy.setMinimumSize(QSize(131, 81))
        self.btn_SaveDataOfTerhapy.setMaximumSize(QSize(131, 81))
        self.btn_SaveDataOfTerhapy.setFont(font5)
        self.btn_SaveDataOfTerhapy.setStyleSheet(u"background-color:rgb(255, 163, 35)")
        self.btn_SaveDataOfTerhapy.setIcon(icon8)

        self.gridLayout_7.addWidget(self.btn_SaveDataOfTerhapy, 10, 0, 1, 1)

        self.lb_Ejercicio_2 = QLabel(self.gb_SeleccionTerapias)
        self.lb_Ejercicio_2.setObjectName(u"lb_Ejercicio_2")
        self.lb_Ejercicio_2.setFont(font7)

        self.gridLayout_7.addWidget(self.lb_Ejercicio_2, 5, 0, 1, 1)

        self.cb_Ejercicio_1 = QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_1.setObjectName(u"cb_Ejercicio_1")
        self.cb_Ejercicio_1.setMinimumSize(QSize(421, 18))
        self.cb_Ejercicio_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.cb_Ejercicio_1, 4, 0, 1, 1)

        self.cb_Ejercicio_3 = QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_3.setObjectName(u"cb_Ejercicio_3")
        self.cb_Ejercicio_3.setMinimumSize(QSize(421, 20))
        self.cb_Ejercicio_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.cb_Ejercicio_3, 8, 0, 1, 1)

        self.lb_Ejercicio_1 = QLabel(self.gb_SeleccionTerapias)
        self.lb_Ejercicio_1.setObjectName(u"lb_Ejercicio_1")
        self.lb_Ejercicio_1.setFont(font7)

        self.gridLayout_7.addWidget(self.lb_Ejercicio_1, 3, 0, 1, 1)

        self.cb_Ejercicio_2 = QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_2.setObjectName(u"cb_Ejercicio_2")
        self.cb_Ejercicio_2.setMinimumSize(QSize(421, 20))
        self.cb_Ejercicio_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.cb_Ejercicio_2, 6, 0, 1, 1)

        self.l_PacienteInSelection = QLabel(self.gb_SeleccionTerapias)
        self.l_PacienteInSelection.setObjectName(u"l_PacienteInSelection")
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.l_PacienteInSelection.setFont(font8)

        self.gridLayout_7.addWidget(self.l_PacienteInSelection, 0, 0, 1, 1)

        self.lb_contador = QLabel(self.gb_SeleccionTerapias)
        self.lb_contador.setObjectName(u"lb_contador")
        self.lb_contador.setFont(font8)

        self.gridLayout_7.addWidget(self.lb_contador, 2, 0, 1, 1)

        self.cb_SeleccionPaciente = QComboBox(self.gb_SeleccionTerapias)
        self.cb_SeleccionPaciente.setObjectName(u"cb_SeleccionPaciente")
        self.cb_SeleccionPaciente.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.cb_SeleccionPaciente, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 9, 0, 1, 1)


        self.gridLayout.addWidget(self.gb_SeleccionTerapias, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_Pacientes)
        self.page_Interfaz_de_Terapia = QWidget()
        self.page_Interfaz_de_Terapia.setObjectName(u"page_Interfaz_de_Terapia")
        self.horizontalLayout_3 = QHBoxLayout(self.page_Interfaz_de_Terapia)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.page_Interfaz_de_Terapia)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_ConectionWithHead = QGroupBox(self.groupBox)
        self.gb_ConectionWithHead.setObjectName(u"gb_ConectionWithHead")
        self.gb_ConectionWithHead.setMaximumSize(QSize(16777215, 138))
        self.gridLayout_3 = QGridLayout(self.gb_ConectionWithHead)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cb_Puertos = QComboBox(self.gb_ConectionWithHead)
        self.cb_Puertos.setObjectName(u"cb_Puertos")

        self.gridLayout_3.addWidget(self.cb_Puertos, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gb_ConectionWithHead)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gb_ConectionWithHead)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)

        self.cb_Baudios = QComboBox(self.gb_ConectionWithHead)
        self.cb_Baudios.setObjectName(u"cb_Baudios")

        self.gridLayout_3.addWidget(self.cb_Baudios, 2, 2, 1, 1)

        self.btn_Conectar = QPushButton(self.gb_ConectionWithHead)
        self.btn_Conectar.setObjectName(u"btn_Conectar")

        self.gridLayout_3.addWidget(self.btn_Conectar, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.gb_ConectionWithHead)

        self.gb_Vision = QGroupBox(self.groupBox)
        self.gb_Vision.setObjectName(u"gb_Vision")
        self.horizontalLayout_4 = QHBoxLayout(self.gb_Vision)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_VideoSkeleto = QLabel(self.gb_Vision)
        self.lb_VideoSkeleto.setObjectName(u"lb_VideoSkeleto")
        self.lb_VideoSkeleto.setStyleSheet(u"background-color: rgb(176, 195, 255);")
        self.lb_VideoSkeleto.setScaledContents(True)
        self.lb_VideoSkeleto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.lb_VideoSkeleto)

        self.lb_Video = QLabel(self.gb_Vision)
        self.lb_Video.setObjectName(u"lb_Video")
        self.lb_Video.setEnabled(True)
        self.lb_Video.setStyleSheet(u"background-color: rgb(255, 195, 255);")
        self.lb_Video.setScaledContents(True)
        self.lb_Video.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.lb_Video)


        self.verticalLayout.addWidget(self.gb_Vision)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 138))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rb_both = QRadioButton(self.groupBox_2)
        self.rb_both.setObjectName(u"rb_both")

        self.gridLayout_4.addWidget(self.rb_both, 1, 2, 1, 1)

        self.btn_Encender = QPushButton(self.groupBox_2)
        self.btn_Encender.setObjectName(u"btn_Encender")
        font9 = QFont()
        font9.setBold(True)
        font9.setWeight(75)
        self.btn_Encender.setFont(font9)
        self.btn_Encender.setStyleSheet(u"background-color: rgb(56, 206, 22);")

        self.gridLayout_4.addWidget(self.btn_Encender, 0, 0, 1, 1)

        self.rb_Emociones = QRadioButton(self.groupBox_2)
        self.rb_Emociones.setObjectName(u"rb_Emociones")

        self.gridLayout_4.addWidget(self.rb_Emociones, 1, 0, 1, 1)

        self.rb_Skeleto = QRadioButton(self.groupBox_2)
        self.rb_Skeleto.setObjectName(u"rb_Skeleto")

        self.gridLayout_4.addWidget(self.rb_Skeleto, 1, 1, 1, 1)

        self.btn_Apagar = QPushButton(self.groupBox_2)
        self.btn_Apagar.setObjectName(u"btn_Apagar")
        self.btn_Apagar.setFont(font9)
        self.btn_Apagar.setStyleSheet(u"background-color: rgb(220, 74, 38);")

        self.gridLayout_4.addWidget(self.btn_Apagar, 0, 2, 1, 1)

        self.lb_StateVideo = QLabel(self.groupBox_2)
        self.lb_StateVideo.setObjectName(u"lb_StateVideo")
        self.lb_StateVideo.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_StateVideo, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.gb_Workout = QGroupBox(self.page_Interfaz_de_Terapia)
        self.gb_Workout.setObjectName(u"gb_Workout")
        self.gb_Workout.setMaximumSize(QSize(400, 16777215))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.gb_Workout.setFont(font10)
        self.verticalLayout_5 = QVBoxLayout(self.gb_Workout)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_3 = QGroupBox(self.gb_Workout)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font11 = QFont()
        font11.setFamily(u"Georgia")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setItalic(True)
        font11.setWeight(75)
        self.groupBox_3.setFont(font11)
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lisWid_WorkOut = QListWidget(self.groupBox_3)
        self.lisWid_WorkOut.setObjectName(u"lisWid_WorkOut")
        self.lisWid_WorkOut.setFont(font10)

        self.gridLayout_5.addWidget(self.lisWid_WorkOut, 1, 0, 1, 3)

        self.cb_Paciente = QComboBox(self.groupBox_3)
        self.cb_Paciente.setObjectName(u"cb_Paciente")

        self.gridLayout_5.addWidget(self.cb_Paciente, 0, 1, 1, 2)

        self.lb_NamePaciente = QLabel(self.groupBox_3)
        self.lb_NamePaciente.setObjectName(u"lb_NamePaciente")
        self.lb_NamePaciente.setFont(font8)

        self.gridLayout_5.addWidget(self.lb_NamePaciente, 0, 0, 1, 1)

        self.btn_StopWorkout = QPushButton(self.groupBox_3)
        self.btn_StopWorkout.setObjectName(u"btn_StopWorkout")
        icon9 = QIcon()
        icon9.addFile(u"icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_StopWorkout.setIcon(icon9)

        self.gridLayout_5.addWidget(self.btn_StopWorkout, 3, 2, 1, 1)

        self.btn_PlayWorkout = QPushButton(self.groupBox_3)
        self.btn_PlayWorkout.setObjectName(u"btn_PlayWorkout")
        icon10 = QIcon()
        icon10.addFile(u"icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_PlayWorkout.setIcon(icon10)
        self.btn_PlayWorkout.setIconSize(QSize(16, 16))

        self.gridLayout_5.addWidget(self.btn_PlayWorkout, 3, 1, 1, 1)

        self.btn_BuscarEjercicios = QPushButton(self.groupBox_3)
        self.btn_BuscarEjercicios.setObjectName(u"btn_BuscarEjercicios")
        icon11 = QIcon()
        icon11.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_BuscarEjercicios.setIcon(icon11)

        self.gridLayout_5.addWidget(self.btn_BuscarEjercicios, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.gb_Workout)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(380, 358))
        self.groupBox_4.setMaximumSize(QSize(380, 358))
        self.groupBox_4.setFont(font11)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(226, 199, 90);")

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.groupBox_4)


        self.horizontalLayout_3.addWidget(self.gb_Workout)

        self.stackedWidget.addWidget(self.page_Interfaz_de_Terapia)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frameContenedor)


        self.gridLayout_2.addWidget(self.frameInferior, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Menu.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.btn_Minimizar.setText("")
        self.btn_Restaurar.setText("")
        self.btn_Maximizar.setText("")
        self.btn_Cerrar.setText("")
        self.btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"  Inicio", None))
        self.btn_Pacientes.setText(QCoreApplication.translate("MainWindow", u"  Pacientes", None))
        self.btn_Terapias.setText(QCoreApplication.translate("MainWindow", u"  Terapias", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NEUROROBOTICS </p><p align=\"center\">S.A de C.V</p></body></html>", None))
        self.btn_CrearPaciente.setText(QCoreApplication.translate("MainWindow", u"Crear Paciente", None))
        self.btn_CrearPaciente_4.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Paciente", None))
        self.btn_CrearPaciente_2.setText(QCoreApplication.translate("MainWindow", u"Modificar Paciente", None))
        self.btn_CrearPaciente_3.setText(QCoreApplication.translate("MainWindow", u"Eliminar Paciente", None))
        self.label_5.setText("")
        self.gb_RegistroUsuario.setTitle(QCoreApplication.translate("MainWindow", u"Registro de Usuarios", None))
        self.lb_Contacto.setText(QCoreApplication.translate("MainWindow", u"Contacto:", None))
        self.lb_LastNameMother.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.lb_Tutor.setText(QCoreApplication.translate("MainWindow", u"Tutor Responsable:", None))
        self.lb_Edad.setText(QCoreApplication.translate("MainWindow", u"Edad:", None))
        self.lb_Grade_Of_TEA.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Grado de TEA:</p></body></html>", None))
        self.lb_LastNameFater.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.lb_Name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.btn_SaveDataOfUser.setText(QCoreApplication.translate("MainWindow", u"Guardar Datos", None))
        self.gb_SeleccionTerapias.setTitle(QCoreApplication.translate("MainWindow", u"Selecci\u00f3n de Terapias", None))
        self.lb_Ejercicio_3.setText(QCoreApplication.translate("MainWindow", u"Ejercicio #3:", None))
        self.btn_SaveDataOfTerhapy.setText(QCoreApplication.translate("MainWindow", u"Guardar \n"
"Terapias", None))
        self.lb_Ejercicio_2.setText(QCoreApplication.translate("MainWindow", u"Ejercicio #2:", None))
        self.lb_Ejercicio_1.setText(QCoreApplication.translate("MainWindow", u"Ejercicio #1:", None))
        self.l_PacienteInSelection.setText(QCoreApplication.translate("MainWindow", u"Paciente:", None))
        self.lb_contador.setText(QCoreApplication.translate("MainWindow", u"Elige tres ejercicios que mejor se adapten a tu terapia", None))
        self.groupBox.setTitle("")
        self.gb_ConectionWithHead.setTitle(QCoreApplication.translate("MainWindow", u"CONNECTION WITH NEUROBOT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Puerto", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Baudios", None))
        self.btn_Conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.gb_Vision.setTitle(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.lb_VideoSkeleto.setText("")
        self.lb_Video.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Controles de Video", None))
        self.rb_both.setText(QCoreApplication.translate("MainWindow", u"Video Normal", None))
        self.btn_Encender.setText(QCoreApplication.translate("MainWindow", u"Turn On", None))
        self.rb_Emociones.setText(QCoreApplication.translate("MainWindow", u"Activar Reconocimientos\n"
"de Emociones", None))
        self.rb_Skeleto.setText(QCoreApplication.translate("MainWindow", u"Activar Esqueleto", None))
        self.btn_Apagar.setText(QCoreApplication.translate("MainWindow", u"Turn Off", None))
        self.lb_StateVideo.setText(QCoreApplication.translate("MainWindow", u"State of Video", None))
        self.gb_Workout.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"WorkOut List", None))
        self.lb_NamePaciente.setText(QCoreApplication.translate("MainWindow", u"Paciente: ", None))
        self.btn_StopWorkout.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_PlayWorkout.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.btn_BuscarEjercicios.setText(QCoreApplication.translate("MainWindow", u"Buscar Ejercicios", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Emocion Detectada", None))
        self.label_4.setText("")
    # retranslateUi

