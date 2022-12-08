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

# IMPORTANDO MODULOS
import sys
import os

# IMPORTANDO DEPENDENCIAS DE ARCHIVOS
from qt_core import *
from functionability.funct import *
from gui.windows.main_window.ui_main_window import UI_MainWindow

# VENTANA PRINCIPAL


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Enigma Encrypt')
        self.setWindowIcon(QIcon('gui/img/favicons/ico.png'))

        # CONFIGURANDO PARAMETROS INICIALES
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # BOTON DESPLEGABLE DEL MENU LATERAL
        self.ui.left_menu_toggle_btn.clicked.connect(self.toggle_btn)

        # BOTON PARA PANTALLA 'ENCRIPTAR'
        self.ui.left_menu_btn_1.clicked.connect(self.showPage1)
        # BOTON PARA PANTALLA 'DECRIPTAR'
        self.ui.left_menu_btn_2.clicked.connect(self.showPage2)

        # BOTON  'ENCRIPTAR'
        self.ui.ui_pages.pushButton.clicked.connect(self.encriptText)
        # BOTON  'DECRIPTAR'
        self.ui.ui_pages.pushButton_2.clicked.connect(self.decriptText)

        self.show()

    def resetSelectionBtn(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.setActive(False)
            except:
                pass

    def showPage1(self):
        self.resetSelectionBtn()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.left_menu_btn_1.setActive(True)

    def showPage2(self):
        self.resetSelectionBtn()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.left_menu_btn_2.setActive(True)
    
    def encriptText(self):
        text = self.ui.ui_pages.lineEdit.text()
        result = encriptar(text.lower())
        self.ui.ui_pages.lineEdit_2.setText(result)

    def decriptText(self):
        text = self.ui.ui_pages.lineEdit_3.text()
        result = desencriptar(text)
        self.ui.ui_pages.lineEdit_4.setText(result)

    def toggle_btn(self):
        # OBTENIENDO EL ANCHO DEL MENU LATERAL
        left_menu_width = self.ui.left_menu.width()

        # VERIFICANDO EL HANCHO
        width = 50
        if left_menu_width == 50:
            width = 180

        # ANIMACION DEL MENU LATERAL
        self.left_menu_animation = QPropertyAnimation(
            self.ui.left_menu, b'minimumWidth')
        self.left_menu_animation.setStartValue(left_menu_width)
        self.left_menu_animation.setEndValue(width)
        self.left_menu_animation.setDuration(500)
        self.left_menu_animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.left_menu_animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
