from model.planta_model import PlantaModel


class PlantaController:
    def __init__(self):
        # Cria uma instância do modelo de planta para interagir com o banco de dados
        self.model = PlantaModel()

    def salvar_planta(self, nome_popular, nome_cientifico, imagem_path):
        """
        Salva uma nova planta no banco de dados.

        Parâmetros:
        - nome_popular: Nome popular da planta
        - nome_cientifico: Nome científico da planta
        - imagem_path: Caminho da imagem associada à planta

        Retorna:
        - O ID da planta inserida no banco de dados, se os dados forem válidos
        - None se os campos obrigatórios não forem preenchidos
        """
        if nome_popular and nome_cientifico:
            return self.model.inserir_planta(nome_popular, nome_cientifico, imagem_path)
        return None

    def mostrar_plantas(self):
        return self.model.buscar_plantas()

    def atualizar_planta(self, planta_id, nome_popular, nome_cientifico):
        if nome_popular and nome_cientifico:
            return self.model.update_planta(nome_popular, nome_cientifico, planta_id)

    def deletar_registro(self, planta_id):
        return self.model.delete_planta(planta_id)
