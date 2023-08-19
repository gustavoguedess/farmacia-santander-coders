from datetime import datetime 

class Cliente:
    def __init__(self, cpf: str, nome: str, sobrenome: str, data_nascimento: str):
        self.cpf: str = cpf #PK      
        self._nome: str = nome
        self._sobrenome: str = sobrenome
        self._data_nascimento: str = data_nascimento

    def __str__(self):
        return f"{self.cpf} - {self._nome} {self._sobrenome} - {self._data_nascimento} - {self.idade} anos"

    @property
    def dados_cliente(self):
        return {
            "cpf": self.cpf,
            "nome": self._nome,
            "sobrenome": self._sobrenome,
            "data_nascimento": self._data_nascimento
        }
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, valor):
        self._data_nascimento = valor
    
    @property
    def idade(self):
        # diff datetime
        return (datetime.now() - datetime.strptime(self._data_nascimento, "%d/%m/%Y")).days // 365

    