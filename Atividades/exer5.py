cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total_pedido = 0
itens_pedidos = {}

while True:
    codigo = int(input("Digite o código do pedido (1 para encerrar): "))

    if codigo == 1:
        break

    if codigo in cardapio:
        quantidade = int(input("Quantidade: "))

        nome, preco = cardapio[codigo]
        valor_total_item = preco * quantidade
        total_pedido += valor_total_item

        if nome in itens_pedidos:
            itens_pedidos[nome][0] += quantidade
            itens_pedidos[nome][1] += valor_total_item
        else:
            itens_pedidos[nome] = [quantidade, valor_total_item]

        print(f"{nome}: {quantidade} = R$ {valor_total_item:.2f}")
    else:
        print("Código inválido! Tente novamente.")


print("========= Pedidos =========")
for nome, (quantidade, valor) in itens_pedidos.items():
    print(f"{quantidade}x {nome}: R$ {valor:.2f}")

print(f"\nTotal: R$ {total_pedido:.2f}")
