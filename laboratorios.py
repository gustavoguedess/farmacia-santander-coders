class Laboratorios:
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.cidade: str = cidade
        self.estado: str = estado
        self.add_laboratorio()
    
    @property
    def dados_laboratorio(self):
        return {
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "cidade": self.cidade,
            "estado": self.estado
        }
    
    def read_laboratorios(self):
        dic_laboratorios = {}
        try:
            with open("dic_laboratorios.txt", "r") as file:
                dic_laboratorios = eval(file.read())
            return dic_laboratorios
        except FileExistsError:
            raise "Arquivo dic_laboratorios.txt não encontrado."

    def add_laboratorio(self):
        dic_laboratorio = self.read_laboratorios()
        dic_laboratorio[self.nome] = {
            "endereço": self.endereco,
            "telefone": self.telefone,
            "cidade": self.cidade,
            "estado": self.estado
        } 

        with open("dic_laboratorios.txt", "w") as file:
            file.write(str(dic_laboratorio))

    def lista_laboratorios(self):
        dic_laboratorio = self.read_laboratorios()
        for nome, dados in dic_laboratorio.items():
            info = f"Dados do Laboratório:\n"
            info += f"Nome: {nome}\n"
            info += f"Endereço: {dados['endereço']}\n"
            info += f"Telefone: {dados['telefone']}\n"
            info += f"Cidade: {dados['cidade']}\n"
            info += f"Estado: {dados['estado']}\n"
            print(info)        

lab01 = Laboratorios("ARM", "Rua Remedio", "47 99999999", "Joinville", "SC")

lab01.lista_laboratorios()