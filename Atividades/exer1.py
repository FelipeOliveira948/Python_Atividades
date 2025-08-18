
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()


preco_alcool = 1.90
preco_gasolina = 2.50


if tipo == 'E':
    preco_litro = preco_alcool
    if litros <= 20:
        desconto_percentual = 0.03
    else:
        desconto_percentual = 0.05
elif tipo == 'G':
    preco_litro = preco_gasolina
    if litros <= 20:
        desconto_percentual = 0.04
    else:
        desconto_percentual = 0.06
else:
    print("Tipo de combustível inválido!")
    exit()


valor_bruto = litros * preco_litro
desconto = valor_bruto * desconto_percentual
valor_final = valor_bruto - desconto


print(f"Valor a ser pago: R$ {valor_final:.2f}")
