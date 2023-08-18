import json
class Laboratorios:
    ultimo_id = 0

    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.id = Laboratorios.ultimo_id #PK
        Laboratorios.ultimo_id += 1
        self._nome: str = nome
        self._endereco: str = endereco
        self._telefone: str = telefone
        self._cidade: str = cidade
        self._estado: str = estado
        self.add_laboratorio()
    
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
    
    def read_laboratorios(self):
        laboratorios = {}
        try:
            with open("laboratorios.json", "r") as file:
                laboratorios = json.load(file)
            return laboratorios
        except FileExistsError:
            raise "Arquivo laboratorios.json não encontrado."

    def add_laboratorio(self):
        laboratorio = self.read_laboratorios()
        laboratorio[self.id] = {
            "nome": self._nome,
            "endereco": self._endereco,
            "telefone": self._telefone,
            "cidade": self._cidade,
            "estado": self._estado
        } 

        with open("laboratorios.json", "w") as file:
            json.dump(laboratorio, file, indent=4)

    def lista_laboratorios(self):
        dic_laboratorio = self.read_laboratorios()
        for nome, dados in dic_laboratorio.items():
            info = f"Dados do Laboratório:\n"
            info += f"ID: {dados[id]}\n"
            info += f"Nome: {nome}\n"
            info += f"Endereço: {dados['endereço']}\n"
            info += f"Telefone: {dados['telefone']}\n"
            info += f"Cidade: {dados['cidade']}\n"
            info += f"Estado: {dados['estado']}\n"
            print(info)        

lab01 = Laboratorios("ARM", "Rua Remedio", "47 99999999", "Joinville", "SC")
lab02 = Laboratorios("URI", "Rua Remedio", "47 99999999", "Joinville", "SC")
lab01.nome = "ASD"

print(lab01.dados_laboratorio)
print(lab02.dados_laboratorio)