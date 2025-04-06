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


class EditarDado(QWidget):
    def __init__(
        self, dado_id, umidade, temperatura, luminosidade, visualizacao
    ) -> None:
        super().__init__()
        self.controller = DadosController()
        self.dado_id = dado_id
        self.initUI(umidade, temperatura, luminosidade)

    def initUI(self, umidade, temperatura, luminosidade) -> None:
        self.setWindowTitle("Editar dado")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Editar dado")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo_temperatura = QLabel("Temperatura")
        self.input_temperatura = QLineEdit(temperatura)

        titulo_luminosidade = QLabel("Luminosidade")
        self.input_luminosidade = QLineEdit(luminosidade)

        titulo_umidade = QLabel("Umidade")
        self.input_umidade = QLineEdit(umidade)

        botao_enviar = QPushButton("Salvar alterações")
        botao_enviar.clicked.connect(self.salvar_edicao)

        layout.addWidget(titulo)

        layout.addWidget(titulo_temperatura)
        layout.addWidget(self.input_temperatura)

        layout.addWidget(titulo_luminosidade)
        layout.addWidget(self.input_luminosidade)

        layout.addWidget(titulo_umidade)
        layout.addWidget(self.input_umidade)

        layout.addWidget(botao_enviar)

        self.setLayout(layout)

    def salvar_edicao(self) -> None:
        umidade = self.input_umidade.text().strip()
        temperatura = self.input_temperatura.text().strip()
        luminosidade = self.input_luminosidade.text().strip()

        if not umidade or not temperatura or not luminosidade:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")
            return

        self.controller.atualizar_dado(self.dado_id, umidade, temperatura, luminosidade)
        self.close()
