class Laboratorio:
    ultimo_id = 0

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.id = Laboratorio.ultimo_id #PK
        Laboratorio.ultimo_id += 1
        self._nome: str = nome
        self._endereco: str = endereco
        self._telefone: str = telefone
        self._cidade: str = cidade
        self._estado: str = estado
    
    def __str__(self):
        return f"{self._nome} - {self._endereco} - {self._telefone} - {self._cidade} - {self._estado}"

    @property
    def dados_laboratorio(self):
        return {
            "id": self.id,
            "nome": self._nome,
            "endereco": self._endereco,
            "telefone": self._telefone,
            "cidade": self._cidade,
            "estado": self._estado
        }
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def endereco(self):
        return self._endereco
    
    @nome.setter
    def endereco(self, valor):
        self._endereco = valor
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor
    
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, valor):
        self._cidade = valor
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        self._estado = valor
    