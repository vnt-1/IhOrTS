
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
)
from PyQt6.QtCore import Qt

from controller.dados_controller import DadosController


class CadastroDados(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = DadosController()
        self.initUI()

    def enviar_dados(self):
        umidade = self.input_umidade.text().strip()
        temperatura = self.input_temperatura.text().strip()
        luminosidade = self.input_luminosidade.text().strip()

        if not umidade or not temperatura or not luminosidade:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")
            return

        dados_id = self.controller.salvar_dados(umidade, temperatura, luminosidade)

        if dados_id:
            QMessageBox.information(self, "Sucesso", "Dados cadastrado com sucesso!")

            self.input_umidade.clear()
            self.input_temperatura.clear()
            self.input_luminosidade.clear()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar dados.")

    def initUI(self):
        self.setWindowTitle("Receber e enviar dados")
        self.setGeometry(100, 100, 300, 400)
        # self.setStyleSheet("background-color: antiquewhite;")

        layout = QVBoxLayout()
        titulo = QLabel("Receber e enviar Dados")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo_umidade = QLabel("Umidade")
        self.input_umidade = QLineEdit()
        self.input_umidade.setPlaceholderText("Umidade")

        titulo_temperatura = QLabel("Temperatura")
        self.input_temperatura = QLineEdit()
        self.input_temperatura.setPlaceholderText("Temperatura")

        titulo_luminosidade = QLabel("Luminosidade")
        self.input_luminosidade = QLineEdit()
        self.input_luminosidade.setPlaceholderText("Luminosidade")

        botao_enviar = QPushButton("Enviar Dados")
        botao_enviar.clicked.connect(self.enviar_dados)

        layout.addWidget(titulo)
        layout.addWidget(titulo_umidade)
        layout.addWidget(self.input_umidade)
        layout.addWidget(titulo_temperatura)
        layout.addWidget(self.input_temperatura)
        layout.addWidget(titulo_luminosidade)
        layout.addWidget(self.input_luminosidade)
        layout.addWidget(botao_enviar)

        self.setLayout(layout)
