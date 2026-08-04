from models.funcionario import funcionario

funcionario1 = funcionario("Douglas", "123.456.789-00", "Engenheiro", 5000.00)
funcionario2 = funcionario("Richard", "123.426.779-00", "Técnico", 4000.00)
funcionario3 = funcionario("Ryan", "223.456.789-10", "ADM", 5000.00)
funcionario4 = funcionario("Wesley", "123.426.709-00", "Engenheiro Elétrico", 10000.00)




print(f"Nome: {funcionario1.nome}")
print(f"CPF: {funcionario1.cpf}")
print(f"Cargo: {funcionario1.cargo}")
print(f"Salário: {funcionario1.salario}")

print(f"Nome: {funcionario2.nome}")
print(f"CPF: {funcionario2.cpf}")
print(f"Cargo: {funcionario2.cargo}")
print(f"Salário: {funcionario2.salario}")

print(f"Nome: {funcionario3.nome}")
print(f"CPF: {funcionario3.cpf}")
print(f"Cargo: {funcionario3.cargo}")
print(f"Salário: {funcionario3.salario}")

print(f"Nome: {funcionario4.nome}")
print(f"CPF: {funcionario4.cpf}")
print(f"Cargo: {funcionario4.cargo}")
print(f"Salário: {funcionario4.salario}")