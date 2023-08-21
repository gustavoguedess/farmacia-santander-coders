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
    def medicamentos_fitoterapicos(self):
        medicamentos_fitoterapicos = []
        for medicamento in self._medicamentos.values():
            if isinstance(medicamento, MedicamentoFitoterapico):
                medicamentos_fitoterapicos.append(medicamento.nome)
        
        medicamentos_fitoterapicos.sort()

        medicamentos_str = ""
        for medicameont in medicamentos_fitoterapicos:
            medicamentos_str += str(self._medicamentos[medicamento]) + "\n"
        
        return medicamentos_str

    @property
    def medicamentos_quimioterapicos(self):
        medicamentos_quimioterapicos = []
        for medicamento in self._medicamentos.values():
            if isinstance(medicamento, MedicamentoQuimioterapico):
                medicamentos_quimioterapicos.append(medicamento.nome)
        
        medicamentos_quimioterapicos.sort()

        medicamentos_str = ""
        for medicamento in medicamentos_quimioterapicos:
            medicamentos_str += str(self._medicamentos[medicamento]) + "\n"
        
        return medicamentos_str

    @property
    def remedio_mais_vendido(self):
        remedios_vendidos = {}

        for venda in self._vendas.values():
            if venda.novo:
                for medicamento in venda.medicamentos:
                    if medicamento.nome in remedios_vendidos:
                        remedios_vendidos[medicamento.nome] += 1
                    else:
                        remedios_vendidos[medicamento.nome] = 1
        
        mais_vendido = ""
        quantidade = 0
        for remedio, quantidade_vendida in remedios_vendidos.items():
            if quantidade_vendida > quantidade:
                mais_vendido = remedio
                quantidade = quantidade_vendida

        if mais_vendido == "":
            return "Nenhum remédio foi vendido!"

        total = quantidade * self._medicamentos[mais_vendido].preco
        str_remedios_vendidos = f"O remédio mais vendido foi {mais_vendido} com {quantidade} vendas. R$ {total}"
        return str_remedios_vendidos
    
    @property
    def quantidade_pessoas_atendidas(self):
        pessoas_atendidas = set()
        for venda in self._vendas.values():
            if venda.novo:
                pessoas_atendidas.add(venda.cliente.cpf)
        return len(pessoas_atendidas)
    
    @property
    def numero_fitoterapicos_vendidos(self):
        fitoterapicos_vendidos = []
        for venda in self._vendas.values():
            if venda.novo:
                for medicamento in venda.medicamentos:
                    if isinstance(medicamento, MedicamentoFitoterapico):
                        fitoterapicos_vendidos.append(medicamento.nome)
        return len(fitoterapicos_vendidos)
    
    @property
    def valor_total_venda_fitoterapicos(self):
        valor_total = 0
        for venda in self._vendas.values():
            if venda.novo:
                for medicamento in venda.medicamentos:
                    if isinstance(medicamento, MedicamentoFitoterapico):
                        valor_total += medicamento.preco
        return valor_total
    
    @property
    def numero_quimioterapicos_vendidos(self):
        quimioterapicos_vendidos = []
        for venda in self._vendas.values():
            if venda.novo:
                for medicamento in venda.medicamentos:
                    if isinstance(medicamento, MedicamentoQuimioterapico):
                        quimioterapicos_vendidos.append(medicamento.nome)
        return len(quimioterapicos_vendidos)

    @property
    def valor_total_venda_quimioterapicos(self):
        valor_total = 0
        for venda in self._vendas.values():
            if venda.novo:
                for medicamento in venda.medicamentos:
                    if isinstance(medicamento, MedicamentoQuimioterapico):
                        valor_total += medicamento.preco
        return valor_total
    
    @property
    def estatisticas(self):
        str_estatisticas = ""
        str_estatisticas += f"{self.remedio_mais_vendido}\n"
        str_estatisticas += f"Quantidade de pessoas atendidas: {self.quantidade_pessoas_atendidas}\n"
        str_estatisticas += f"Numero de fitoterapicos vendidos: {self.numero_fitoterapicos_vendidos}\n"
        str_estatisticas += f"Valor total de venda de fitoterapicos: {self.valor_total_venda_fitoterapicos}\n"
        str_estatisticas += f"Numero de quimioterapicos vendidos: {self.numero_quimioterapicos_vendidos}\n"
        str_estatisticas += f"Valor total de venda de quimioterapicos: {self.valor_total_venda_quimioterapicos}\n"
        
        return str_estatisticas


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
        self._medicamentos[medicamento.nome] = medicamento

    def vender(self, id_cliente: int, id_medicamentos: list[int]):
        cliente = self._clientes[id_cliente]
        medicamentos = []
        for id_medicamento in id_medicamentos:
            medicamentos.append(self._medicamentos[id_medicamento])
        venda = Venda(cliente, medicamentos)

        print('\n=-=-=-=-=-=-=-=-=-=-=-=- COMPRA -=-=-=-=-=-=-=-=-=-=-=-=-=\n')
        print(venda)

        if venda.possui_controlado:
            receita_apresentada = input("O cliente apresentou a receita médica (S/N): ")
            receita_apresentada = receita_apresentada.upper()
            if receita_apresentada == "S":
                venda.efetuar_compra()
                self._vendas[venda.id] = venda
            else:
                print("Compra não efetuada!")
        else:
            venda.efetuar_compra()
            self._vendas[venda.id] = venda

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
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
                cliente = self._clientes[venda["cpf_cliente"]]
                medicamentos = []
                for id_medicamento in venda["medicamentos"]:
                    medicamentos.append(self._medicamentos[id_medicamento])
                _venda = Venda(cliente, medicamentos, novo=False)
                _venda.datatime = venda['data_hora']

                self._vendas[venda["id"]] = _venda


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
            vendas = [venda.dados_venda for venda in self._vendas.values()]
            json.dump(vendas, file, indent=4)