import sys

# Importação dos módulos necessários do PyQt5 para criação da interface gráfica
from PyQt5.QtWidgets import QApplication

# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from views.cadastro_plantas import CadastroPlantas


# Bloco principal para rodar o programa
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa o aplicativo PyQt5
    janela = CadastroPlantas()  # Cria uma instância da janela de cadastro de plantas
    janela.show()  # Exibe a janela
    sys.exit(app.exec_())  # Mantém o aplicativo em execução até que o usuário o feche
