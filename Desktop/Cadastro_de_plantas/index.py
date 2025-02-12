import sys

# Importação dos módulos necessários do PyQt5 para criação da interface gráfica
from PyQt5.QtWidgets import QApplication

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from views.cadastro_plantas import CadastroPlantas
from views.dados_plantas import DadosPlantas


class Index(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def cadastrar_planta(self, event=None):
        janela = CadastroPlantas()
        janela.show()
        # self.hide()

    def cadastrar_dados(self, event=None):
        janela = DadosPlantas()
        janela.show()
        # self.hide()

    def initUI(self):
        self.setWindowTitle("Index")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Selecione uma ação")
        titulo.setAlignment(Qt.AlignCenter)

        botao_cadastro_planta = QPushButton("Cadastrar Planta")
        botao_cadastro_planta.clicked.connect(self.cadastrar_planta)

        botao_cadastro_dados = QPushButton("Cadastrar dados")
        botao_cadastro_dados.clicked.connect(self.cadastrar_dados)

        layout.addWidget(titulo)
        layout.addWidget(botao_cadastro_planta)
        layout.addWidget(botao_cadastro_dados)

        self.setLayout(layout)


# Bloco principal para rodar o programa
# if __name__ == "__main__":
#     app = QApplication(sys.argv)  # Inicializa o aplicativo PyQt5
#     janela = CadastroPlantas()  # Cria uma instância da janela de cadastro de plantas
#     janela.show()  # Exibe a janela
#     sys.exit(app.exec_())  # Mantém o aplicativo em execução até que o usuário o feche

# if __name__ == "__main__":
#     app = QApplication(sys.argv)  # Inicializa o aplicativo PyQt5
#     janela = DadosPlantas()  # Cria uma instância da janela de cadastro de plantas
#     janela.show()  # Exibe a janela
#     sys.exit(app.exec_())  # Mantém o aplicativo em execução até que o usuário o feche

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Index()
    janela.show()
    sys.exit(app.exec_())
