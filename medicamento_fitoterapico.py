class MedicamentoFitoterapico:
    def __init__(self, nome, principal_composto, laboratorio, descricao, preco):
        self._nome : str = nome
        self._principal_composto : str = principal_composto
        self._laboratorio : str = laboratorio
        self._descricao : str = descricao
        self._preco : float = preco
    
    # Getters
    @property
    def nome(self):
        return self._nome
    
    @property
    def principal_composto(self):
        return self._principal_composto
    
    @property
    def laboratorio(self):
        return self._laboratorio
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def preco(self):
        return self._preco
    
    # Setters
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @principal_composto.setter
    def principal_composto(self, principal_composto):
        self._principal_composto = principal_composto
    
    @laboratorio.setter
    def laboratorio(self, laboratorio):
        self._laboratorio = laboratorio
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
        
    @preco.setter
    def preco(self, descricao):
        self._preco = preco