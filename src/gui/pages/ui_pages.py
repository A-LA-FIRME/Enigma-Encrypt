# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'pagesjIYEdm.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# //////////////////////////////////////////////////////////////////////////////////////////
#
# BY: Jhonathan Vargas y Jose Martinez
# PROJECT: EnigmaScrypt
# V: 1.0.0
#
# Este projecto se hizo con la finalidad de ser presentado como Projecto semestral
# para la materia de Analsis y diseno de algoritmo impartida por Sharon Saldana
#
# EnigmaEncrypt es un programa enfocado a la codificacion y decodificacion de texto
# con la peculiaridad de que lo hara de una forma diferente dependiendo del dia,
# asemejando el funcionamiento de la 'Maquina Enigma', de ahi el nombre.
#
# //////////////////////////////////////////////////////////////////////////////////////////

# IMPORTANDO DEPENDENCIAS DE ARCHIVOS
from qt_core import *


class Ui_app_pages(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1223, 650)
        StackedWidget.setStyleSheet('font: 700 9pt "Segoe UI"')


        #PAGINA DECRIPTAR
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(1200, 650))
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1200, 650))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(600, 500))
        self.lineEdit_3.setMaximumSize(QSize(550, 16777215))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
                                    "background-color: rgb(68,71,90);\n"
                                    "padding: 8px;\n"
                                    "border: 2px solid #c3ccdf;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.lineEdit_3.setAlignment(
                    Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label")
        self.label_2.setMinimumSize(QSize(1200, 20))
        self.label_2.setMaximumSize(QSize(600, 20))
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(600, 500))
        self.lineEdit_4.setMaximumSize(QSize(550, 16777215))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
                                      "background-color: rgb(68,71,90);\n"
                                      "padding: 8px;\n"
                                      "border: 2px solid #c3ccdf;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.lineEdit_4.setAlignment(
                    Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(600, 0))
        self.pushButton_2.setMaximumSize(QSize(600, 16777215))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                      "background-color: #44475a;\n"
                                      "border: 2px solid #c3ccdf;\n"
                                      "color: rgb(255,255,255);\n"
                                      "padding: 8px;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #4f5368;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #282a36;\n"
                                      "}")

        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_2)

        StackedWidget.addWidget(self.page_2)

        #PAGINA ENCRIPTAR
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(1200, 650))
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1200, 650))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(600, 500))
        self.lineEdit.setMaximumSize(QSize(550, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
                                    "background-color: rgb(68,71,90);\n"
                                    "padding: 8px;\n"
                                    "border: 2px solid #c3ccdf;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.lineEdit.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(1200, 20))
        self.label.setMaximumSize(QSize(600, 20))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(600, 500))
        self.lineEdit_2.setMaximumSize(QSize(550, 16777215))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
                                      "background-color: rgb(68,71,90);\n"
                                      "padding: 8px;\n"
                                      "border: 2px solid #c3ccdf;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.lineEdit_2.setAlignment(
                    Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(600, 0))
        self.pushButton.setMaximumSize(QSize(600, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "background-color: #44475a;\n"
                                      "border: 2px solid #c3ccdf;\n"
                                      "color: rgb(255,255,255);\n"
                                      "padding: 8px;\n"
                                      "border-radius: 10px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #4f5368;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #282a36;\n"
                                      "}")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.verticalLayout.addWidget(self.frame)

        StackedWidget.addWidget(self.page_1)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex()

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate(
            "StackedWidget", u"StackedWidget", None))
        self.label_2.setText(QCoreApplication.translate(
            "StackedWidget", u"DECRIPTAR", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate(
            "StackedWidget", u"INGRESE EL TEXTO PARA ENCRIPTAR...", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate(
            "StackedWidget", u"INGRESE EL TEXTO PARA DECRIPTAR...", None))
        self.label.setText(QCoreApplication.translate(
            "StackedWidget", u"ENCRIPTAR", None))
        self.pushButton.setText(QCoreApplication.translate(
            "StackedWidget", u"ENCRIPTAR", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "StackedWidget", u"DECRIPTAR", None))
    # retranslateUi
