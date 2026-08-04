from METALSUL.models.funcionario import Funcionario
from datetime import date

def main():
    funcionario = Funcionario(
        nome = "Douglas",
        cpf = "123.456.789-00",
        cargo = "Desenvolvedor",
        departamento = "TI",
        salario = 5000,
        data_admissao = date.today()
    )

    print(funcionario)

if __name__ == "__main__":
    main()