from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt

from controller.dados_controller import DadosController


class DeletarDado(QWidget):
    def __init__(self, dado_id):
        super().__init__()
        self.controller = DadosController()
        self.dado_id = dado_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Deletar Dado")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Deletar Dado")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_deletar = QPushButton("Deletar")
        botao_deletar.clicked.connect(self.deletar_registro)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.clicked.connect(self.close)

        layout.addWidget(botao_deletar)
        layout.addWidget(botao_cancelar)

        self.setLayout(layout)

    def deletar_registro(self):
        if self.dado_id:
            self.controller.deletar_registro(self.dado_id)
            self.close()
