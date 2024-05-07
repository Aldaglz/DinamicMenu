# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfazmrFcwe.ui'
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

import bg_MainBody_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout.addWidget(self.frameSuperior)

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
        self.page_Pacientes = QWidget()
        self.page_Pacientes.setObjectName(u"page_Pacientes")
        self.verticalLayout_4 = QVBoxLayout(self.page_Pacientes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 188, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.btn_CrearPaciente = QPushButton(self.page_Pacientes)
        self.btn_CrearPaciente.setObjectName(u"btn_CrearPaciente")
        font2 = QFont()
        font2.setPointSize(16)
        self.btn_CrearPaciente.setFont(font2)
        self.btn_CrearPaciente.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente)

        self.btn_CrearPaciente_4 = QPushButton(self.page_Pacientes)
        self.btn_CrearPaciente_4.setObjectName(u"btn_CrearPaciente_4")
        self.btn_CrearPaciente_4.setFont(font2)
        self.btn_CrearPaciente_4.setStyleSheet(u"\n"
"background-color: rgb(98, 198, 80);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_4)

        self.btn_CrearPaciente_2 = QPushButton(self.page_Pacientes)
        self.btn_CrearPaciente_2.setObjectName(u"btn_CrearPaciente_2")
        self.btn_CrearPaciente_2.setFont(font2)
        self.btn_CrearPaciente_2.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_2)

        self.btn_CrearPaciente_3 = QPushButton(self.page_Pacientes)
        self.btn_CrearPaciente_3.setObjectName(u"btn_CrearPaciente_3")
        self.btn_CrearPaciente_3.setFont(font2)
        self.btn_CrearPaciente_3.setStyleSheet(u"background-color: rgb(221, 117, 255);")

        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_3)

        self.verticalSpacer_2 = QSpacerItem(20, 187, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_Pacientes)
        self.page_Inicio = QWidget()
        self.page_Inicio.setObjectName(u"page_Inicio")
        self.page_Inicio.setStyleSheet(u"image: url(:/prefijoNuevo/bg_MainBody.png);")
        self.stackedWidget.addWidget(self.page_Inicio)
        self.page_Terapias = QWidget()
        self.page_Terapias.setObjectName(u"page_Terapias")
        self.page_Terapias.setStyleSheet(u"")
        self.btn_CrearTerapias = QPushButton(self.page_Terapias)
        self.btn_CrearTerapias.setObjectName(u"btn_CrearTerapias")
        self.btn_CrearTerapias.setGeometry(QRect(70, 250, 151, 121))
        font3 = QFont()
        font3.setPointSize(14)
        self.btn_CrearTerapias.setFont(font3)
        self.btn_CrearTerapias.setStyleSheet(u"background-color: rgb(255, 153, 69);")
        self.btn_ModificarTerapias = QPushButton(self.page_Terapias)
        self.btn_ModificarTerapias.setObjectName(u"btn_ModificarTerapias")
        self.btn_ModificarTerapias.setGeometry(QRect(290, 250, 151, 121))
        self.btn_ModificarTerapias.setFont(font3)
        self.btn_ModificarTerapias.setStyleSheet(u"background-color: rgb(255, 153, 69);")
        self.btn_CrearTerapias_3 = QPushButton(self.page_Terapias)
        self.btn_CrearTerapias_3.setObjectName(u"btn_CrearTerapias_3")
        self.btn_CrearTerapias_3.setGeometry(QRect(520, 250, 141, 121))
        self.btn_CrearTerapias_3.setFont(font3)
        self.btn_CrearTerapias_3.setStyleSheet(u"background-color: rgb(255, 153, 69);")
        self.stackedWidget.addWidget(self.page_Terapias)
        self.page_EjerciciosPaciente = QWidget()
        self.page_EjerciciosPaciente.setObjectName(u"page_EjerciciosPaciente")
        self.gb_ConectionWithHead = QGroupBox(self.page_EjerciciosPaciente)
        self.gb_ConectionWithHead.setObjectName(u"gb_ConectionWithHead")
        self.gb_ConectionWithHead.setGeometry(QRect(10, 20, 231, 71))
        self.btn_Conectar = QPushButton(self.gb_ConectionWithHead)
        self.btn_Conectar.setObjectName(u"btn_Conectar")
        self.btn_Conectar.setGeometry(QRect(20, 30, 75, 23))
        self.comboBox = QComboBox(self.gb_ConectionWithHead)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 30, 111, 22))
        self.gb_ConectionWithSkeleton = QGroupBox(self.page_EjerciciosPaciente)
        self.gb_ConectionWithSkeleton.setObjectName(u"gb_ConectionWithSkeleton")
        self.gb_ConectionWithSkeleton.setGeometry(QRect(270, 20, 231, 71))
        self.btn_Conectar_2 = QPushButton(self.gb_ConectionWithSkeleton)
        self.btn_Conectar_2.setObjectName(u"btn_Conectar_2")
        self.btn_Conectar_2.setGeometry(QRect(20, 30, 75, 23))
        self.comboBox_2 = QComboBox(self.gb_ConectionWithSkeleton)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(110, 30, 111, 22))
        self.label_2 = QLabel(self.page_EjerciciosPaciente)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 461, 331))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tableView = QTableView(self.page_EjerciciosPaciente)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(550, 110, 221, 192))
        self.label_3 = QLabel(self.page_EjerciciosPaciente)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 75, 131, 21))
        self.label_3.setFont(font3)
        self.stackedWidget.addWidget(self.page_EjerciciosPaciente)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frameContenedor)


        self.verticalLayout.addWidget(self.frameInferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"INDUSTRIAS CHRIS", None))
        self.btn_CrearPaciente.setText(QCoreApplication.translate("MainWindow", u"Crear Paciente", None))
        self.btn_CrearPaciente_4.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Paciente", None))
        self.btn_CrearPaciente_2.setText(QCoreApplication.translate("MainWindow", u"Modificar Paciente", None))
        self.btn_CrearPaciente_3.setText(QCoreApplication.translate("MainWindow", u"Eliminar Paciente", None))
        self.btn_CrearTerapias.setText(QCoreApplication.translate("MainWindow", u"Crear \n"
"Terapias", None))
        self.btn_ModificarTerapias.setText(QCoreApplication.translate("MainWindow", u"Modificar \n"
"Terapias", None))
        self.btn_CrearTerapias_3.setText(QCoreApplication.translate("MainWindow", u"Eliminar\n"
"Terapias", None))
        self.gb_ConectionWithHead.setTitle(QCoreApplication.translate("MainWindow", u"CONNECTION WITH HEAD", None))
        self.btn_Conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.gb_ConectionWithSkeleton.setTitle(QCoreApplication.translate("MainWindow", u"CONNECTION WITH BODY", None))
        self.btn_Conectar_2.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Workout List", None))
    # retranslateUi

