from cliente import Cliente
from medicamento_fitoterapico import MedicamentoFitoterapico
from medicamento_quimioterapico import MedicamentoQuimioterapico
from laboratorio import Laboratorio
from farmacia import Farmacia

def main():
    farmacia = Farmacia("dados/")
    print(farmacia)

    # farmacia.add_laboratorio(Laboratorio("Laboratório 1", "Rua das Flores", "41 99999999", "Curitiba", "SC"))
    # farmacia.add_laboratorio(Laboratorio("Laboratório 2", "Rua dos lindos", "92 88888888 ", "Manaus", "AM"))

    

if __name__ == '__main__':
    main()
