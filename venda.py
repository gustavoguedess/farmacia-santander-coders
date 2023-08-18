from cliente import Cliente
from medicamento import Medicamento
from datetime import datetime

class Venda:
    def __init__(self, cliente: Cliente, medicamentos: list[Medicamento]):
        self.cliente = cliente
        self.medicamentos = medicamentos
        self.compra_efeituada = False
        self.datetime = None

        self.calcular_total(desconto=0.0)
        self.efetuar_compra()

    def verificar_produto(self, id_produto: int):
        verificado = False
        for produto in self.produtos:
            if produto.id == id_produto:
                produto.verificar()
                verificado = True
        return verificado

    def efetuar_compra(self):
        if self.checar_medicamentos():
            self.compra_efeituada = True
            self.datatime = datetime.now()
            print("Compra efetuada com sucesso!")
        else:
            print("Não foi possível efetuar a compra, verifique os medicamentos necessários!")
    
    def checar_medicamentos(self):
        possui_controlados = False

        for produto in self.produtos:
            if produto.controlado:
                print(f"O produto {produto} é controlado!")
                possui_controlados = True

        if possui_controlados:
            print("É necessário apresentar receita médica para a compra de produtos controlados!")
            print("Por favor, confirme cada produto controlado com a receita médica.")

        return not possui_controlados

    @property
    def desconto(self):
        return self.desconto
    
    @desconto.setter
    def desconto(self, desconto:float=0.0):
        self.desconto = desconto
        if self.cliente.idoso:
            self.desconto = max(self.desconto, 0.20)
        if self.valor_total > 150:
            self.desconto = max(self.desconto, 0.10)

    def calcular_valor_produtos(self):
        valor = 0
        for produto in self.produtos:
            valor += produto.preco
        return valor
    
    def calcular_total(self, desconto:float=0.0):
        self.valor = self.calcular_valor_produtos()

        self.desconto = desconto
        self.valor_total = self.valor*(1-self.desconto)

        return self.valor_total
