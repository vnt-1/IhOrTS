import sys

# Importação dos módulos necessários do PyQt5 para criação da interface gráfica
from PyQt5.QtWidgets import QApplication, QWidget

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from views.cadastro_plantas import CadastroPlantas


# Definição da classe CadastroPlantas, que representa a interface gráfica do cadastro de plantas
class index(QWidget):
    def __init__(self):
        super().__init__()  # Inicializa a classe pai QWidget
        self.view = CadastroPlantas()
        # Instancia o controlador para manipular os dados das plantas
        self.imagem_path = ""  # Variável para armazenar o caminho da imagem selecionada
        self.initUI()  # Chama o método para inicializar a interface gráfica


# Bloco principal para rodar o programa
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa o aplicativo PyQt5
    janela = CadastroPlantas()  # Cria uma instância da janela de cadastro de plantas
    janela.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém o aplicativo em execução até que o usuário o feche
