from medicamento import Medicamento

class MedicamentoFitoterapico(Medicamento):
    def __init__(self, nome, principal_composto, laboratorio, descricao, preco, controlado=True):
        super().__init__(nome, principal_composto, laboratorio, descricao, preco)