import itertools

class Medicamento:
    id_iter = itertools.count()

    def __init__(self, nome, principal_composto, laboratorio, descricao, preco):
        self._nome : str = nome
        self._principal_composto : str = principal_composto
        self._laboratorio : str = laboratorio
        self._descricao : str = descricao
        self._preco : float = preco
        self._id = next(self.id_iter)
    
    def __str__(self):
        return f"{self._nome} - {self._principal_composto} - {self._laboratorio} - {self._descricao} - {self._preco} - {self._id}"
    
    @property
    def dados_medicamento(self):
        return {
            "id": self.id,
            "nome": self._nome,
            "principal_composto": self._principal_composto,
            "laboratorio": self._laboratorio,
            "descricao": self._descricao,
            "preco": self._preco
        }
    
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
    
    @property
    def id(self):
        return self._id
    
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
        
    # Outras funções
    def to_string(self):
        print(f"Nome: {self._nome}")
        print(f"Principal composto: {self._principal_composto}")
        print(f"Laboratório: {self._laboratorio}")
        print(f"Descrição: {self._descricao}")
        print(f"Preço: {self._preco}")
        print(f"ID: {self._id}")