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
    
    # Outras funções
    def to_string(self):
        return f"{super().to_string()} - {self._controlado}"
    
    @property
    def dados_medicamento(self):
        dados_medicamento = super().dados_medicamento
        dados_medicamento["controlado"] = self._controlado
        return dados_medicamento