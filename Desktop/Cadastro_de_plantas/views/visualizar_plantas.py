from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from controller.planta_controller import PlantaController
from views.editar_planta import EditarPlanta


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

        botao_editar = QPushButton("Editar")
        botao_editar.clicked.connect(self.abrir_tela_edicao)
        layout.addWidget(botao_editar)

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

    def abrir_tela_edicao(self):
        linha_selecionada = self.tabela.currentRow()

        if linha_selecionada != -1:
            planta_id = int(self.tabela.item(linha_selecionada, 0).text())
            nome_popular = self.tabela.item(linha_selecionada, 1).text()
            nome_cientifico = self.tabela.item(linha_selecionada, 2).text()

            self.tela_edicao = EditarPlanta(
                planta_id, nome_popular, nome_cientifico, self
            )
            self.tela_edicao.show()
            self.close()
