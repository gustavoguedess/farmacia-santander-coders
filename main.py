from cliente import Cliente
from medicamento_fitoterapico import MedicamentoFitoterapico
from medicamento_quimioterapico import MedicamentoQuimioterapico
from laboratorio import Laboratorio
from farmacia import Farmacia

BANCO_DE_DADOS = "dados/"

def menu():
    print("1 - Cadastrar Laboratório")
    print("2 - Cadastrar Cliente")
    print("3 - Cadastrar Medicamento")
    print("4 - Cadastrar Venda")
    print("5 - Listar clientes")
    print("6 - Listar medicamentos")
    print("7 - Listar medicamentos Quimioterapicos")
    print("8 - Listar medicamentos Fitoterapicos")
    print("9 - Listar estatisticas")
    print("10 - Listar Informações")
    print("11 - Sair")

    op = int(input("Digite a opção desejada: "))
    
    return op

def cadastrar_laboratorio(farmacia: Farmacia):
    nome = input("Digite o nome do laboratório: ")
    endereco = input("Digite o endereço do laboratório: ")
    telefone = input("Digite o telefone do laboratório: ")
    cidade = input("Digite a cidade do laboratório: ")
    estado = input("Digite o estado do laboratório: ")

    laboratorio = Laboratorio(nome, endereco, telefone, cidade, estado)
    farmacia.add_laboratorio(laboratorio)

def cadastrar_cliente(farmacia: Farmacia):
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente: ")

    cliente = Cliente(cpf, nome, sobrenome, data_nascimento)
    farmacia.add_cliente(cliente)

def cadastrar_medicamento(farmacia: Farmacia):
    nome = input("Digite o nome do medicamento: ")
    principal_composto = input("Digite o principal composto do medicamento: ")
    laboratorio = input("Digite o laboratório do medicamento: ")
    descricao = input("Digite a descrição do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))

    tipo = None
    while tipo != "F" and tipo != "Q":
        tipo = input("O medicamento é fitoterápico (F) ou quimioterápico (Q): ")
        tipo = tipo.upper()
    
    if tipo == "F":
        medicamento = MedicamentoFitoterapico(nome, principal_composto, laboratorio, descricao, preco)
    elif tipo == "Q":
        controlado = input("O medicamento é controlado (S/N): ")
        controlado = controlado.upper()
        if controlado == "S":
            controlado = True
        elif controlado == "N":
            controlado = False
        medicamento = MedicamentoQuimioterapico(nome, principal_composto, laboratorio, descricao, preco, controlado)

    farmacia.add_medicamento(medicamento)

def cadastrar_venda(farmacia: Farmacia):
    cpf = input("Digite o CPF do cliente: ")
    nome_medicamentos = []
    while True:
        nome_medicamento = (input("Digite o Nome do medicamento: "))
        nome_medicamentos.append(nome_medicamento)
        op = input("Deseja adicionar mais um medicamento (S/N): ")
        op = op.upper()
        if op == "N":
            break

    farmacia.vender(cpf, nome_medicamentos)

def listar_informacoes(farmacia: Farmacia):
    print(farmacia)

def main():
    farmacia = Farmacia(BANCO_DE_DADOS)

    while True:
        op = menu()

        if op == 1: # Cadastrar Laboratório
            cadastrar_laboratorio(farmacia)
        elif op == 2: # Cadastrar Cliente
            cadastrar_cliente(farmacia)
        elif op == 3: # Cadastrar Medicamento
            cadastrar_medicamento(farmacia)
        elif op == 4: # Cadastrar Venda
            cadastrar_venda(farmacia)
        elif op == 5: # Listar clientes
            print("\n\nClientes:")
            print(farmacia.clientes)
        elif op == 6: # Listar medicamentos
            print("\n\nMedicamentos:")
            print(farmacia.medicamentos)
        elif op == 7: # Listar medicamentos Quimioterapicos
            print("\n\nMedicamentos Quimioterapicos:")
            print(farmacia.medicamentos_quimioterapicos)
        elif op == 8: # Listar medicamentos Fitoterapicos
            print("\n\nMedicamentos Fitoterapicos:")
            print(farmacia.medicamentos_fitoterapicos)
        elif op == 9: # Listar estatisticas
            print("\n\nEstatisticas do dia:")
            print(farmacia.estatisticas)
        elif op == 10: # Listar Informações
            listar_informacoes(farmacia)
        elif op == 11: # Sair
            break
    
    print("Estatisitcas do dia:")
    print(farmacia.estatisticas)
    farmacia.salvar_dados(BANCO_DE_DADOS)
    

if __name__ == '__main__':
    main()
