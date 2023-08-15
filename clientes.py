class Cliente:
    def __init__(self, cpf: str, nome: str, sobrenome: str, data_nascimento: str):
        self.cpf: str = cpf       
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.data_nascimento: str = data_nascimento
        self.add_cliente()

    @property
    def dados_cliente(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "data de nascimento": self.data_nascimento
        }
    
    def read_cliente(self):
        dic_cliente = {}
        try:
            with open("dic_clientes.txt", "r") as file:
                dic_cliente = eval(file.read())
            return dic_cliente
        except FileNotFoundError:
            raise "Arquivo dic_clientes.txt não encontrado."

    def add_cliente(self):
        if self.cpf.isnumeric():
            dic_cliente = self.read_cliente()
            dic_cliente[self.cpf] = {
                "nome": self.nome,
                "sobrenome": self.sobrenome,
                "data de nascimento": self.data_nascimento
            }

            with open("dic_clientes.txt", "w") as file:
                file.write(str(dic_cliente))
        else:
            raise 'Digite um número de CPF com 11 digitos!'

    def busca_cliente_por_cpf(self, cpf: str):
        if cpf.isnumeric():
            dic_cliente = self.read_cliente()
            if dic_cliente[cpf] is not None:
                cliente = dic_cliente[cpf]
                dados_cliente =  f"Dados do cliente:\nCPF: {cpf}\nNome: {cliente['nome']}\nSobrenome: {cliente['sobrenome']}\nData de Nascimento: {cliente['data de nascimento']}"
                return dados_cliente
            else:
                raise 'O CPF digitado não existe!'        
        else:
            raise 'Digite um número de CPF com 11 digitos!'        

    def clientes_ordem_alfabetica(self):
        dic_cliente = self.read_cliente()
        sorted_clientes = dict(sorted(dic_cliente.items(), key=lambda item: item[1]['nome']))
        index = 1
        for cpf, dados in sorted_clientes.items():
            info = f"Dados do Cliente {index}:\n"
            info += f"CPF: {cpf}\n"
            info += f"Nome: {dados['nome']}\n"
            info += f"Sobrenome: {dados['sobrenome']}\n"
            info += f"Data de Nascimento: {dados['data de nascimento']}\n"
            index += 1
            print(info)

pedro = Cliente("123456789", "Pedro", "Ferrari", "10/10/1998")

thiago = Cliente("987654321", "Thiago", "Anamastor", "21/12/1976")

thiago.clientes_ordem_alfabetica()