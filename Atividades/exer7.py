def programa():
    valores = []

    while True:
        n = int(input("Digite um número (ou -1 para encerrar): "))
        if n == -1:
            break
        valores.append(n)

    if not valores:
        print("Nenhum valor foi informado.")
        return


    qtd = len(valores)
    ordem_normal = valores
    ordem_inversa = valores[::-1]
    soma = sum(valores)
    media = soma / qtd
    acima_media = sum(1 for v in valores if v > media)

    print("\n===== RESULTADO =====")
    print(f"Quantidade de valores lidos: {qtd}")
    print("Valores na ordem informada:", *ordem_normal)
    print("Valores na ordem inversa: ", *ordem_inversa)
    print(f"Soma dos valores: {soma}")
    print(f"Média dos valores: {media:.2f}")
    print(f"Quantidade de valores acima da média: {acima_media}")

programa()