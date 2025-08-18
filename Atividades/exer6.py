from datetime import datetime

salario = float(input("Digite o salário inicial do funcionário: "))
ano_inicio = 1995
percentual = 1.5 / 100

ano_atual = datetime.now().year

for ano in range(1996, ano_atual + 1):
    salario += salario * percentual
    percentual *= 2

print(f"Salário em {ano_atual}: R$ {salario:.2f}")