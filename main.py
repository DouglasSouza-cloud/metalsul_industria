from METALSUL.models.funcionario import Funcionario
from datetime import date
from METALSUL.repositories.funcionario_repository import Funcionario

def main():
    funcionario = Funcionario(
                nome = "Robertão",
                cpf = "013.623.972-20",
                rg = "88.999.555-A"
                data_nascimento = date(1996,5,5)
                sexo = "MASCULINO"
                estado_civil = "CASADO"
                email = "robertocarlos99@gmail.com"
                telefone = "68999250388"
                celular = "68999250368"
                cargo = "Técnico"
                departamento = Engenharia
                salario = 10000 
                data_admissao = date.today()
                data_demissao = date(2026,9,21)
                turno = "Terceiro Turno"
                status = "ATIVO"
                observacoes = "Tem 8 filhos com a Sthefany"
    )

    repository = FuncionarioRepository
    repository.salvar(funcionario)
    funcionario.__str__()

if __name__ == "__main__":
    main()