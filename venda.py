from cliente import Cliente
from medicamento import Medicamento
from medicamento_quimioterapico import MedicamentoQuimioterapico
from datetime import datetime

class Venda:
    proximo_id = 0
    def __init__(self, cliente: Cliente, medicamentos: list[Medicamento]):
        self._id = Venda.proximo_id
        Venda.proximo_id += 1
        self.cliente = cliente
        self.medicamentos = medicamentos
        self._datetime = None

        self.calcular_total(desconto=0.0)
        self.efetuar_compra()

    def __str__(self):
        str_venda = ""
        str_venda += f"ID: {self.id}\n"
        str_venda += f"Cliente: {self.cliente}\n"
        str_venda += f"Medicamentos:\n"
        for medicamento in self.medicamentos:
            str_venda += f"\t{medicamento}\n"
        str_venda += f"Valor: {self.valor}\n"
        str_venda += f"Desconto: {self.desconto}\n"
        str_venda += f"Valor Total: {self.valor_total}\n"
        str_venda += f"Data e Hora: {self.datatime}\n"
        return str_venda
    
    @property
    def dados_venda(self):
        return {
            "id": self.id,
            "cpf_cliente": self.cliente.cpf,
            "medicamentos": [medicamento.nome for medicamento in self.medicamentos],
            "valor": self.valor,
            "desconto": self.desconto,
            "valor_total": self.valor_total,
            "data_hora": self.datatime
        }

    @property
    def id(self):
        return self._id
    
    @property
    def datatime(self):
        return self._datatime
    
    @datatime.setter
    def datatime(self, datatime):
        self._datatime = str(datatime)

    def verificar_produto(self, id_produto: int):
        verificado = False
        for produto in self.produtos:
            if produto.id == id_produto:
                produto.verificar()
                verificado = True
        return verificado

    def efetuar_compra(self):
        self.datatime = datetime.now()
        print("Compra efetuada com sucesso!")
    
    @property
    def possui_controlado(self):
        possui_controlados = False

        for medicamento in self.medicamentos:
            if isinstance(medicamento, MedicamentoQuimioterapico) and medicamento.controlado:
                print(f"O produto {produto.nome} é controlado!")
                possui_controlados = True

        return possui_controlados

    @property
    def desconto(self):
        return self._desconto
    
    @desconto.setter
    def desconto(self, desconto:float=0.0):
        self._desconto = desconto
        if self.cliente.idade > 65:
            self._desconto = max(self._desconto, 0.20)
        if self.valor > 150:
            self._desconto = max(self._desconto, 0.10)

    def calcular_valor_produtos(self):
        valor = 0
        for produto in self.medicamentos:
            valor += produto.preco
        return valor
    
    def calcular_total(self, desconto:float=0.0):
        self.valor = self.calcular_valor_produtos()

        self.desconto = desconto
        self.valor_total = self.valor*(1-self.desconto)

        return self.valor_total
