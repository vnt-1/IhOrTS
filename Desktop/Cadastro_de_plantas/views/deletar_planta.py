from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
)
from PyQt6.QtCore import Qt

from controller.planta_controller import PlantaController


class DeletarPlanta(QWidget):
    def __init__(self, planta_id):
        super().__init__()
        self.controller = PlantaController()
        self.planta_id = planta_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Deletar Planta")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Deletar Planta")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_deletar = QPushButton("Deletar")
        botao_deletar.clicked.connect(self.deletar_registro)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.clicked.connect(self.close)

        layout.addWidget(botao_deletar)
        layout.addWidget(botao_cancelar)

        self.setLayout(layout)

    def deletar_registro(self):
        if self.planta_id:
            self.controller.deleta_registro(self.planta_id)
            self.close()
