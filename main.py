from datetime import date
from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository


def main():

    repository = FuncionarioRepository()
    funcionario = repository.buscar_por_id(1)

    if funcionario:
        print(funcionario)
    else:
        print("FUNCIONÁRIO NÃO ENCONTRADO. :(")
    repository.fechar()

if __name__ == "__main__":
    main()