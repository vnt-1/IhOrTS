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


class EditarPlanta(QWidget):
    def __init__(self, planta_id, nome_popular, nome_cientifico, visualizacao):
        super().__init__()
        self.controller = PlantaController()
        self.planta_id = planta_id
        self.visualizacao = visualizacao
        self.initUI(nome_popular, nome_cientifico)

    def salvar_edicao(self):
        nome_popular = self.input_nome_popular.text().strip()
        nome_cientifico = self.input_nome_cientifico.text().strip()

        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")
            return

        self.controller.atualizar_planta(self.planta_id, nome_popular, nome_cientifico)
        self.close()

    def initUI(self, nome_popular, nome_cientifico):
        self.setWindowTitle("Editar planta")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        titulo = QLabel("Editar planta")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo_nome_popular = QLabel("Nome Popular")
        self.input_nome_popular = QLineEdit(nome_popular)

        titulo_nome_cientifico = QLabel("Nome Científico")
        self.input_nome_cientifico = QLineEdit(nome_cientifico)

        botao_enviar = QPushButton("Salvar alterações")
        botao_enviar.clicked.connect(self.salvar_edicao)

        layout.addWidget(titulo)

        layout.addWidget(titulo_nome_popular)
        layout.addWidget(self.input_nome_popular)

        layout.addWidget(titulo_nome_cientifico)
        layout.addWidget(self.input_nome_cientifico)

        layout.addWidget(botao_enviar)

        self.setLayout(layout)
