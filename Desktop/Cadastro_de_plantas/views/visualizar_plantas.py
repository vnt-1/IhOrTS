from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from controller.planta_controller import PlantaController


class VisualizarPlantas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Plantas cadastradas")
        self.setGeometry(500, 100, 400, 300)
        layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["ID", "Nome Popular", "Nome Científico"])

        layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar")
        botao_atualizar.clicked.connect(self.carregar_dados)

        layout.addWidget(botao_atualizar)
        self.setLayout(layout)
        self.carregar_dados()

    def carregar_dados(self):
        self.controller = PlantaController()
        plantas = self.controller.mostrar_plantas()
        self.tabela.setRowCount(len(plantas))

        for row, planta in enumerate(plantas):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(planta[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(planta[1]))
            self.tabela.setItem(row, 2, QTableWidgetItem(planta[2]))
