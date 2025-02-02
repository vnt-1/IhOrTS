import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QSizePolicy,
    QGridLayout,
)


class CadastroPlantasWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de plantas")
        self.setGeometry(50, 200, 350, 200)
        self.setFixedSize(350, 200)

        self.inicializar_interface()

    def inicializar_interface(self):
        self.header_label = QLabel("Faça o Cadastro")
        self.header_label.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )

        self.cadastro_label = QLabel("Cadastrar Nova Planta")

        self.nome_popular_edit = QLineEdit()
        self.nome_cientifico_edit = QLineEdit()

        self.nome_popular_edit.setPlaceholderText("Nome Popular")
        self.nome_cientifico_edit.setPlaceholderText("Nome Científico")

        self.inserir_imagem_label = QLabel("Inserir Imagem")
        self.inserir_imagem_button = QPushButton("Upload")

        self.cancelar_button = QPushButton("Cancelar")
        self.cadastrar_button = QPushButton("Cadastrar")

        self.layout = QGridLayout(self)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.layout.addWidget(self.header_label, 0, 0, 1, 2)
        self.layout.addWidget(self.cadastro_label, 1, 0, 1, 2)
        self.layout.addWidget(self.nome_popular_edit, 2, 0, 1, 2)
        self.layout.addWidget(self.nome_cientifico_edit, 3, 0, 1, 2)
        self.layout.addWidget(self.inserir_imagem_label, 4, 0)
        self.layout.addWidget(self.inserir_imagem_button, 4, 1)
        self.layout.addWidget(self.cancelar_button, 5, 0)
        self.layout.addWidget(self.cadastrar_button, 5, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CadastroPlantasWindow()
    window.show()

    sys.exit(app.exec())
