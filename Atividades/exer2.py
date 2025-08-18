def caixa_eletronico():
    
    valor = int(input("Digite o valor do saque (mínimo R$10 e máximo R$600): "))

    if valor < 10 or valor > 600:
        print("Valor inválido. O saque deve estar entre R$10 e R$600.")
        return


    notas = [100, 50, 10, 5, 1]
    resultado = {}


    resto = valor
    for nota in notas:
        quantidade = resto // nota
        if quantidade > 0:
            resultado[nota] = quantidade
            resto = resto % nota


    print(f"\nPara sacar R${valor}, o caixa fornecerá:")
    for nota, qtd in resultado.items():
        print(f"{qtd} nota(s) de R${nota}")



caixa_eletronico()
