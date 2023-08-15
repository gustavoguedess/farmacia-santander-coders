import json

class Cliente:
    def __init__(self, cpf: str, nome: str, sobrenome: str, data_nascimento: str):
        self.cpf: str = cpf #PK      
        self._nome: str = nome
        self._sobrenome: str = sobrenome
        self._data_nascimento: str = data_nascimento
        self.add_cliente()

    @property
    def dados_cliente(self):
        return {
            "cpf": self.cpf,
            "nome": self._nome,
            "sobrenome": self._sobrenome,
            "data de nascimento": self._data_nascimento
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
    
    def read_cliente(self):
        cliente = {}
        try:
            with open("clientes.json", "r") as file:
                clientes = json.load(file)
            return clientes
        except FileNotFoundError:
            raise "Arquivo clientes.json não encontrado."

    def add_cliente(self):
        if self.cpf.isnumeric():
            clientes = self.read_cliente()
            clientes[self.cpf] = {
                "nome": self._nome,
                "sobrenome": self._sobrenome,
                "data de nascimento": self._data_nascimento
            }

            with open("clientes.json", "w") as file:
                json.dump(clientes, file, indent=4)
        else:
            raise 'Digite um número de CPF com 11 digitos!'

    def busca_cliente_por_cpf(self, cpf: str):
        if cpf.isnumeric():
            clientes = self.read_cliente()
            if clientes[cpf] is not None:
                cliente = clientes[cpf]
                return cliente
            else:
                raise 'O CPF digitado não existe!'        
        else:
            raise 'Digite um número de CPF com 11 digitos!'        

    def clientes_ordem_alfabetica(self):
        clientes = self.read_cliente()
        sorted_clientes = dict(sorted(clientes.items(), key=lambda item: item[1]['nome']))
        return sorted_clientes

pedro = Cliente("123456789", "Pedro", "Ferrari", "10/10/1998")
thiago = Cliente("987654321", "Thiago", "Anamastor", "21/12/1976")

print(thiago.clientes_ordem_alfabetica())
print(thiago.busca_cliente_por_cpf("123456789"))