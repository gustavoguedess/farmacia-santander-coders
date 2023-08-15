from medicamento import Medicamento

class MedicamentoQuimioterapico(Medicamento):
    def __init__(self, nome, principal_composto, laboratorio, descricao, preco, controlado=True):
        super().__init__(nome, principal_composto, laboratorio, descricao, preco)
        self._controlado : bool = controlado
    
    @property
    def controlado(self):
        return self._controlado
    
    @controlado.setter
    def controlado(self, controlado):
        self._controlado = controlado