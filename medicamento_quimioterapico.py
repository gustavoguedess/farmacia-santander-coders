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
        print(f"Nome: {self._nome}")
        print(f"Principal composto: {self._principal_composto}")
        print(f"Laboratório: {self._laboratorio.nome}")
        print(f"Descrição: {self._descricao}")
        print(f"Preço: {self._preco}")
        print(f"Preço: {'Sim' if self._controlado else 'Não'}")
        print(f"ID: {self._id}")