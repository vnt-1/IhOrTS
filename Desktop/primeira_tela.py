import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


def botaoClicado():
    print("Você clicou no botão")


def click():
    num.setText("Click!")


# Criando a aplicação
app = QApplication(sys.argv)

with open("estilo.qss", "r") as arquivo_qss:
    estilo = arquivo_qss.read()
    app.setStyleSheet(estilo)

# Criando a janela principal
janelinha = QWidget()
janelinha.setWindowTitle("Wonderful window name")
janelinha.setGeometry(50, 200, 350, 150)

# Criando um rótulo
textoRotulo = QLabel("Clique aqui nesse botão abaixo", janelinha)
textoRotulo.move(105, 30)

# num label
num = QLabel("Não clicado", janelinha)
num.setObjectName("num")
num.move(140, 75)

# Criando um botão
botao = QPushButton("Botão", janelinha)
botao.move(130, 50)
botao.clicked.connect(click)

# layout
layout = QVBoxLayout(janelinha)
layout.addWidget(textoRotulo)
layout.addWidget(num)
layout.addWidget(botao)

# Exibindo a janela
janelinha.show()

# Iniciando o loop de eventos
sys.exit(app.exec_())
