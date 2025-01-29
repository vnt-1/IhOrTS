import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFormLayout, QLineEdit

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Cadastro de plantas")
    window.setGeometry(50, 200, 350, 150)

    header_label = QLabel("Faça o Cadastro", window)
    header_label.move(100, 30)

    cadastro_label = QLabel("Cadastrar Nova Planta", window)

    nome_popular_edit = QLineEdit()
    nome_cientifico_edit = QLineEdit()

    nome_popular_edit.setPlaceholderText("Nome Popular")
    nome_cientifico_edit.setPlaceholderText("Nome Científico")
    inserir_imagem_label = QLabel("Inserir Imagem", window)
    inserir_imagem_button = QPushButton("Upload", window)
    cancelar_button = QPushButton("Cancelar")
    cadastrar_button = QPushButton("Cadastrar")


    layout = QVBoxLayout(window)
    layout.addWidget(header_label)
    layout.addWidget(cadastro_label)
    layout.addWidget(nome_popular_edit)
    layout.addWidget(nome_cientifico_edit)


    # cadastro_layout = QFormLayout(window)
    # cadastro_layout.addRow(QLabel("Nome Popular"), nome_popular_edit)
    # cadastro_layout.addRow(QLabel("Nome Científico"), nome_cientifico_edit)
    


    # layout = QVBoxLayout(window)
    # layout.addWidget(label_text)

    window.show()
    sys.exit(app.exec_())