from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from controller.dados_controller import DadosController
from views.editar_dado import EditarDado
from views.deletar_dado import DeletarDado


class VisualizarDados(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Dados cadastrados")
        self.setGeometry(800, 800, 600, 600)
        layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Temperatura", "Luminosidade", "Umidade"]
        )

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar")
        botao_atualizar.clicked.connect(self.carregar_dados)
        layout.addWidget(botao_atualizar)

        botao_editar = QPushButton("Editar")
        botao_editar.clicked.connect(self.abrir_tela_edicao)
        layout.addWidget(botao_editar)

        botao_deletar = QPushButton("Deletar")
        botao_deletar.clicked.connect(self.abrir_tela_delete)
        layout.addWidget(botao_deletar)

        self.setLayout(layout)

    def carregar_dados(self):
        self.controller = DadosController()
        dados = self.controller.mostrar_dados()
        self.tabela.setRowCount(len(dados))

        for row, dado in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(dado[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(dado[1])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(dado[2])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(dado[3])))

    def abrir_tela_edicao(self):
        linha_selecionada = self.tabela.currentRow()

        if linha_selecionada != -1:
            dado_id = int(self.tabela.item(linha_selecionada, 0).text())
            temperatura = self.tabela.item(linha_selecionada, 1).text()
            luminosidade = self.tabela.item(linha_selecionada, 2).text()
            umidade = self.tabela.item(linha_selecionada, 3).text()

            self.tela_edicao = EditarDado(
                dado_id, umidade, temperatura, luminosidade, self
            )
            self.tela_edicao.show()
            self.close()

    def abrir_tela_delete(self):
        linha_selecionada = self.tabela.currentRow()

        if linha_selecionada != -1:
            dado_id = int(self.tabela.item(linha_selecionada, 0).text())

            self.tela_delete = DeletarDado(dado_id)
            self.tela_delete.show()
            self.close()
