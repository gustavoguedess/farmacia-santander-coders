from medicamento_fitoterapico import MedicamentoFitoterapico

class MedicamentoQuimioterapico(MedicamentoFitoterapico):
    def __init__(self, nome, principal_composto, laboratorio, descricao, preco, controlado=True):
        super().__init__(nome, principal_composto, laboratorio, descricao, preco)
        self._controlado : bool = controlado
    
    @property
    def controlado(self):
        return self._controlado
    
    @controlado.setter
    def controlado(self, controlado):
        self._controlado = controlado