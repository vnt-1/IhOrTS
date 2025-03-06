import sys

# Importação dos módulos necessários do PyQt6 para criação da interface gráfica
from PyQt6.QtWidgets import QApplication

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
)
from PyQt6.QtCore import Qt
from views.cadastro_plantas import CadastroPlantas
from views.cadastro_dados import CadastroDados
from views.visualizar_plantas import VisualizarPlantas
from views.visualizar_dados import VisualizarDados


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.window_cadastro_planta = CadastroPlantas()
        self.window_cadastro_dado = CadastroDados()
        self.window_visualizar_plantas = VisualizarPlantas()
        self.window_visualizar_dados = VisualizarDados()

    def show_cadastrar_planta(self):
        self.window_cadastro_planta.show()

    def show_cadastrar_dado(self):
        self.window_cadastro_dado.show()

    def show_visualizar_plantas(self):
        self.window_visualizar_plantas.show()

    def show_visualizar_dados(self):
        self.window_visualizar_dados.show()

    def initUI(self):
        self.setWindowTitle("Janela principal")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Selecione uma ação")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_cadastro_planta = QPushButton("Cadastrar Planta")
        botao_cadastro_planta.clicked.connect(self.show_cadastrar_planta)

        botao_cadastro_dados = QPushButton("Cadastrar dados")
        botao_cadastro_dados.clicked.connect(self.show_cadastrar_dado)

        botao_mostrar_plantas = QPushButton("Mostrar plantas")
        botao_mostrar_plantas.clicked.connect(self.show_visualizar_plantas)

        botao_mostrar_dados = QPushButton("Mostrar dados")
        botao_mostrar_dados.clicked.connect(self.show_visualizar_dados)

        layout.addWidget(titulo)
        layout.addWidget(botao_cadastro_planta)
        layout.addWidget(botao_cadastro_dados)
        layout.addWidget(botao_mostrar_plantas)
        layout.addWidget(botao_mostrar_dados)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
