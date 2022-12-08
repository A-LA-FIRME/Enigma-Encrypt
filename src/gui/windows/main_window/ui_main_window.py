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
from gui.pages.ui_pages import Ui_app_pages
from gui.widgets.push_btn import PushBtn

# VENTANA PRINCIPAL


class UI_MainWindow():
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')

        # CONFIGURANDO PARAMETROS INICIALES
        parent.resize(1280, 720)
        parent.setMinimumSize(1280, 720)
        parent.setMaximumSize(1280, 720)
        parent.setStyleSheet('font: 700 9pt "Segoe UI"')

        # CREANDO EL FONDO
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet('background-color: black;')
        # CONFIGURANDO FONDO
        parent.setCentralWidget(self.central_frame)

        # CREANDO EL PANEL PRINCIPAL
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # CREANDO EL PANEL LATERAL
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet('background-color: #44475a;')
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # FRAME DEL PANEL LATERAL
        self.left_menu_frame = QVBoxLayout(self.left_menu)
        self.left_menu_frame.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame.setSpacing(0)

        # FRAME DEL PANEL LATERAL - PARTE SUPERIOR
        self.left_menu_frame_top = QFrame()
        self.left_menu_frame_top.setMinimumHeight(40)
        self.left_menu_frame_top.setObjectName('left_menu_frame_top')

        # FRAME LATERAL - PARTE SUPERIOR - BOTONES - LAYOUT
        self.left_menu_layout_top = QVBoxLayout(self.left_menu_frame_top)
        self.left_menu_layout_top.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout_top.setSpacing(0)

        # FRAME LATERAL - PARTE SUPERIOR - BOTONES
        self.left_menu_toggle_btn = PushBtn(
            text='MENU', icon_path='icon_menu.svg')
        self.left_menu_btn_1 = PushBtn(
            text='ENCRIPTAR', is_active=True, icon_path='icon_encriptar.svg')
        self.left_menu_btn_2 = PushBtn(
            text='DECRIPTAR', icon_path='icon_decriptar.svg')

        # ANADIENDO BTN SUPERIOR A LOS LAYOUTS
        self.left_menu_layout_top.addWidget(self.left_menu_toggle_btn)
        self.left_menu_layout_top.addWidget(self.left_menu_btn_1)
        self.left_menu_layout_top.addWidget(self.left_menu_btn_2)

        # FRAME DEL PANEL LATERAL - ESPACEADOR
        self.left_menu_frame_spacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # FRAME DEL PANEL LATERAL - VERSION TEXT
        self.left_menu_frame_version = QLabel('v1.0.0')
        self.left_menu_frame_version.setAlignment(Qt.AlignCenter)
        self.left_menu_frame_version.setMinimumHeight(30)
        self.left_menu_frame_version.setMaximumHeight(30)
        self.left_menu_frame_version.setStyleSheet('color: #c3ccdf')

        # ANADIENDO AL FRAME PANEL LATERAL
        self.left_menu_frame.addWidget(self.left_menu_frame_top)
        self.left_menu_frame.addItem(self.left_menu_frame_spacer)
        self.left_menu_frame.addWidget(self.left_menu_frame_version)

        # CONTENIDO
        self.content = QFrame()
        self.content.setStyleSheet('background-color: #282a36;')

        # LAYOUT DEL CONTENIDO
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # BARRA SUPERIOR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet(
            'background-color: #21232d; color: #6272a4;')
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # TEXTO DE LA IZQUIERDA - BARRA SUPERIOR
        self.top_bar_label_left = QLabel('ENIGMA ENCRYPT')

        # ESPACEADOR - BARRA SUPERIOR
        self.top_bar_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TEXTO DE LA DERECHA - BARRA SUPERIOR
        self.top_bar_label_right = QLabel('|')

        # ANADIENDO A LA BARRA SUPERIOR
        self.top_bar_layout.addWidget(self.top_bar_label_left)
        self.top_bar_layout.addItem(self.top_bar_spacer)
        self.top_bar_layout.addWidget(self.top_bar_label_right)

        # BARRA INFERIOR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet(
            'background-color: #21232d; color: #6272a4;')
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # TEXTO DE LA IZQUIERDA - BARRA INFERIOR
        self.bottom_bar_label_left = QLabel(
            'CREATED BY: Jhonathan Vargas & Jose Martinez')

        # ESPACEADOR - BARRA INFERIOR
        self.bottom_bar_spacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TEXTO DE LA DERECHA - BARRA INFERIOR
        self.bottom_bar_label_right = QLabel('© 2022')

        # ANADIENDO A LA BARRA INFERIOR
        self.bottom_bar_layout.addWidget(self.bottom_bar_label_left)
        self.bottom_bar_layout.addItem(self.bottom_bar_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_bar_label_right)

        # PAGINAS DE LA APP
        self.pages = QStackedWidget()
        self.pages.setStyleSheet('font-size: 12px; color: #f8f8f2;')
        self.ui_pages = Ui_app_pages()
        self.ui_pages.setupUi(self.pages)

        # ANADIENDO EL CONTENIDO
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # ANADIENDO LAYOUT DEL CONTENIDO
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
