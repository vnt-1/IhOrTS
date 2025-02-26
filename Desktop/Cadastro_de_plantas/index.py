import sys

# Importação dos módulos necessários do PyQt5 para criação da interface gráfica
from PyQt5.QtWidgets import QApplication

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
)
from PyQt5.QtCore import Qt
from views.cadastro_plantas import CadastroPlantas
from views.dados_plantas import DadosPlantas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.window_cadastro_planta = CadastroPlantas()
        self.window_cadastro_dados = DadosPlantas()

    def show_cadastrar_planta(self):
        self.window_cadastro_planta.show()

    def show_dados_plantas(self):
        self.window_cadastro_dados.show()

    def initUI(self):
        self.setWindowTitle("Janela principal")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Selecione uma ação")
        titulo.setAlignment(Qt.AlignCenter)

        botao_cadastro_planta = QPushButton("Cadastrar Planta")
        botao_cadastro_planta.clicked.connect(self.show_cadastrar_planta)

        botao_cadastro_dados = QPushButton("Cadastrar dados")
        botao_cadastro_dados.clicked.connect(self.show_dados_plantas)

        layout.addWidget(titulo)
        layout.addWidget(botao_cadastro_planta)
        layout.addWidget(botao_cadastro_dados)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())
