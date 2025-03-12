import sys

# Importação dos módulos necessários do PyQt6 para criação da interface gráfica
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from controller.planta_controller import PlantaController


# Definição da classe CadastroPlantas, que representa a interface gráfica do cadastro de plantas
class CadastroPlantas(QWidget):
    def __init__(self):
        super().__init__()  # Inicializa a classe pai QWidget
        self.controller = PlantaController()
        # Instancia o controlador para manipular os dados das plantas
        self.imagem_path = ""  # Variável para armazenar o caminho da imagem selecionada
        self.initUI()  # Chama o método para inicializar a interface gráfica

    # Método acionado ao clicar no botão "Cadastrar"
    def botao_clicado(self):
        # Obtém os valores dos campos de entrada e remove espaços extras
        nome_popular = self.input_nome_popular.text().strip()
        nome_cientifico = self.input_nome_cientifico.text().strip()

        # Verifica se os campos estão preenchidos
        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(
                self, "Erro", "Preencha todos os campos!"
            )  # Exibe um alerta caso algum campo esteja vazio
            return  # Retorna sem continuar o cadastro

        # Chama o método do controlador para salvar a planta no banco de dados
        planta_id = self.controller.salvar_planta(
            nome_popular, nome_cientifico, self.imagem_path
        )

        # Verifica se o cadastro foi bem-sucedido
        if planta_id:
            QMessageBox.information(
                self, "Sucesso", "Planta cadastrada com sucesso!"
            )  # Exibe mensagem de sucesso
            # Limpa os campos de entrada e a área da imagem
            self.input_nome_popular.clear()
            self.input_nome_cientifico.clear()
            self.area_imagem.clear()
            self.imagem_path = ""  # Reseta o caminho da imagem
        else:
            QMessageBox.critical(
                self, "Erro", "Erro ao cadastrar a planta."
            )  # Exibe mensagem de erro

    # Método responsável por configurar os elementos da interface gráfica
    def initUI(self):
        self.setWindowTitle("Cadastro de Plantas")  # Define o título da janela
        self.setGeometry(100, 100, 300, 400)  # Define a posição e o tamanho da janela
        self.setStyleSheet(
            "background-color: antiquewhite;"
        )  # Define a cor de fundo da janela

        layout = QVBoxLayout()  # Cria um layout vertical para organizar os elementos

        # Criação do título da tela
        titulo = QLabel("Faça o CADASTRO")
        titulo.setFont(
            QFont("Arial", 14, QFont.Weight.Bold)
        )  # Define a fonte e o tamanho do texto
        titulo.setStyleSheet("color: black;")  # Define a cor do texto
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Campo de entrada para o nome popular da planta
        self.input_nome_popular = QLineEdit()
        self.input_nome_popular.setPlaceholderText(
            "Nome Popular"
        )  # Texto de dica no campo
        self.input_nome_popular.setStyleSheet(
            "background-color: white;"
        )  # Define a cor de fundo

        # Campo de entrada para o nome científico da planta
        self.input_nome_cientifico = QLineEdit()
        self.input_nome_cientifico.setPlaceholderText("Nome Científico")
        self.input_nome_cientifico.setStyleSheet("background-color: white;")

        # Botão para selecionar uma imagem da planta
        self.botao_imagem = QPushButton("Insira uma Imagem")
        self.botao_imagem.setStyleSheet(
            "background-color: white; color: black;"
        )  # Define o estilo do botão
        self.botao_imagem.clicked.connect(
            self.abrir_arquivo
        )  # Conecta o clique do botão ao método abrir_arquivo

        # Área onde a imagem selecionada será exibida
        self.area_imagem = QLabel()
        self.area_imagem.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )  # Centraliza a imagem
        self.area_imagem.setStyleSheet(
            "border: 1px solid black; min-height: 100px; background-color: antiquewhite;"
        )  # Define estilo da borda e fundo

        # Botão de cancelar
        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setStyleSheet(
            "background-color: white; color: black;"
        )  # Define o estilo do botão

        # Botão para cadastrar a planta
        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.setStyleSheet(
            "background-color: white; color: black;"
        )  # Define o estilo do botão
        botao_cadastrar.clicked.connect(
            self.botao_clicado
        )  # Conecta o clique do botão ao método botao_clicado

        # Adiciona os elementos ao layout
        layout.addWidget(titulo)
        layout.addWidget(self.input_nome_popular)
        layout.addWidget(self.input_nome_cientifico)
        layout.addWidget(self.botao_imagem)
        layout.addWidget(self.area_imagem)
        layout.addWidget(botao_cancelar)
        layout.addWidget(botao_cadastrar)

        self.setLayout(layout)  # Define o layout da janela

    # Método para abrir um seletor de arquivos para escolher uma imagem
    def abrir_arquivo(self):
        options = QFileDialog.Options()  # Configurações do seletor de arquivos
        # Abre a janela para selecionar a imagem, permitindo vários formatos
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Abrir Arquivo",
            "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.gif);;Todos os Arquivos (*)",
            options=options,
        )
        if file_name:  # Se um arquivo for selecionado
            self.imagem_path = file_name  # Armazena o caminho da imagem escolhida
            pixmap = QPixmap(file_name)  # Carrega a imagem
            self.area_imagem.setPixmap(
                pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            )  # Exibe a imagem redimensionada


# Bloco principal para rodar o programa
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa o aplicativo PyQt6
    janela = CadastroPlantas()  # Cria uma instância da janela de cadastro de plantas
    janela.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém o aplicativo em execução até que o usuário o feche
