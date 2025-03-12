from model.dados_model import DadosModel


class DadosController:
    def __init__(self):
        self.model = DadosModel()

    def salvar_dados(self, umidade, temperatura, luminosidade):
        if umidade and temperatura and luminosidade:
            return self.model.inserir_dados(umidade, temperatura, luminosidade)
        return None

    def mostrar_dados(self):
        return self.model.buscar_dados()
