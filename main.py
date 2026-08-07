from datetime import date

from models.funcionario import Funcionario
from repositories.funcionario_repository import FuncionarioRepository


def main():
    funcionario = Funcionario(
        nome="Robertão",
        cpf="01362397220",
        rg="88.999.555-A",
        data_nascimento=date(1996, 5, 5),
        sexo="M",
        estado_civil="CASADO",
        email="robertocarlos99@gmail.com",
        telefone="68999250388",
        celular="68999250368",
        cargo="Técnico",
        departamento="Engenharia",
        salario=10000.00,
        data_admissao=date.today(),
        data_demissao=date(2026, 9, 21),
        turno="Terceiro Turno",
        status="ATIVO",
        observacoes="Tem 8 filhos com a Sthefany"
    )

    repository = FuncionarioRepository()
    repository.salvar(funcionario)

    print(funcionario)


if __name__ == "__main__":
    main()