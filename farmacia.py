from cliente import Cliente
from laboratorio import Laboratorio
from medicamento import Medicamento
from medicamento_fitoterapico import MedicamentoFitoterapico
from medicamento_quimioterapico import MedicamentoQuimioterapico
from venda import Venda

import json


class Farmacia:
    def __init__(self, path: str):
        self._laboratorios: list[Laboratorio] = {}
        self._clientes: list[Cliente] = {}
        self._medicamentos: list[Medicamento] = {}
        self._vendas: list[Venda] = {}

        self.carregar_dados(path)

    def __str__(self):
        str_farmacia = ""
        str_farmacia += "Laboratórios:\n"
        str_farmacia += self.laboratorios
        str_farmacia += "\nClientes:\n"
        str_farmacia += self.clientes
        str_farmacia += "\nMedicamentos:\n"
        str_farmacia += self.medicamentos
        return str_farmacia
    
    @property
    def laboratorios(self):
        str_laboratorios = ""
        for laboratorio in self._laboratorios.values():
            str_laboratorios += str(laboratorio) + "\n"
        return str_laboratorios
    
    @property
    def clientes(self):
        str_clientes = ""
        for cliente in self._clientes.values():
            str_clientes += str(cliente) + "\n"
        return str_clientes
    
    @property
    def medicamentos(self):
        str_medicamentos = ""
        for medicamento in self._medicamentos.values():
            str_medicamentos += str(medicamento) + "\n"
        return str_medicamentos
    
    @property
    def vendas(self):
        str_vendas = ""
        for venda in self._vendas.values():
            str_vendas += str(venda) + "\n"
        return str_vendas

    def add_laboratorio(self, laboratorio: Laboratorio):
        self._laboratorios[laboratorio.id] = laboratorio
    
    def add_cliente(self, cliente: Cliente):
        self._clientes[cliente.cpf] = cliente
    
    def add_medicamento(self, medicamento: Medicamento):
        self._medicamentos[medicamento.id] = medicamento

    def vender(self, id_cliente: int, id_medicamentos: list[int]):
        cliente = self._clientes[id_cliente]
        medicamentos = []
        for id_medicamento in id_medicamentos:
            medicamentos.append(self._medicamentos[id_medicamento])
        venda = Venda(cliente, medicamentos)
        self._vendas[venda.id] = venda
        return venda
    
    def carregar_laboratorios(self, path: str):
        with open(path + "laboratorios.json", "r") as file:
            laboratorios = json.load(file)
            for laboratorio in laboratorios:
                self.add_laboratorio(Laboratorio(laboratorio["nome"], laboratorio["endereco"], laboratorio["telefone"], laboratorio["cidade"], laboratorio["estado"]))
    
    def carregar_clientes(self, path: str):
        with open(path + "clientes.json", "r") as file:
            clientes = json.load(file)
            for cliente in clientes:
                self.add_cliente(Cliente(cliente["cpf"], cliente["nome"], cliente["sobrenome"], cliente["data_nascimento"]))

    def carregar_medicamentos(self, path: str):
        with open(path + "fitoterapicos.json", "r") as file:
            medicamentos = json.load(file)
            for medicamento in medicamentos:
                self.add_medicamento(MedicamentoFitoterapico(medicamento["nome"], medicamento["principal_composto"], medicamento["laboratorio"], medicamento["descricao"], medicamento["preco"]))
        
        with open(path + "quimioterapicos.json", "r") as file:
            medicamentos = json.load(file)
            for medicamento in medicamentos:
                self.add_medicamento(MedicamentoQuimioterapico(medicamento["nome"], medicamento["principal_composto"], medicamento["laboratorio"], medicamento["descricao"], medicamento["preco"], medicamento["controlado"]))
            
    def carregar_vendas(self, path: str):
        with open(path + "vendas.json", "r") as file:
            vendas = json.load(file)
            for venda in vendas:
                self.vender(venda["cliente"], venda["medicamentos"])

    def carregar_dados(self, path: str):
        self.carregar_laboratorios(path)
        self.carregar_clientes(path)
        self.carregar_medicamentos(path)
        self.carregar_vendas(path)
        
    
    def salvar_dados(self, path: str):
        with open(path + "laboratorios.json", "w") as file:
            laboratorios = [laboratorio.dados_laboratorio for laboratorio in self._laboratorios.values()]
            json.dump(laboratorios, file, indent=4)

        with open(path + "clientes.json", "w") as file:
            clientes = [cliente.dados_cliente for cliente in self._clientes.values()]
            json.dump(clientes, file, indent=4)

        with open(path + "fitoterapicos.json", "w") as file:
            fitoterapicos = [medicamento.dados_medicamento for medicamento in self._medicamentos.values() if isinstance(medicamento, MedicamentoFitoterapico)]
            json.dump(fitoterapicos, file, indent=4)

        with open(path + "quimioterapicos.json", "w") as file:
            quimioterapicos = [medicamento.dados_medicamento for medicamento in self._medicamentos.values() if isinstance(medicamento, MedicamentoQuimioterapico)]
            json.dump(quimioterapicos, file, indent=4)

        with open(path + "vendas.json", "w") as file:
            json.dump(self._vendas, file, indent=4)