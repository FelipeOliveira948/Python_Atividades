gabarito = ["a", "d", "a", "d", "b", "c", "c", "b", "b", "a"]
resposta = 0
alunos = 0
geral = 0
lista = []


print("Bem vindo ao nosso sistema de provas, o teste possui 10 questões, lembre-se de escolher entre (a, b, c, d):" )

while(resposta == 0):
    acertos = 0
    for i in range(0, 10):
        questao = input(f' Digite a resposta da questão {i + 1}: ')

        while questao not in ("a", "b", "c", "d"):
            print("Opção inválida, tente novamente.")
            questao = input(f' Digite a resposta da questão {i + 1}: ')

        if (questao == gabarito[i]):
            acertos += 1
    
    geral += acertos

    sistema = input("Mais algum aluno gostaria de fazer a prova?(sim / não): ")

    while sistema not in ('sim', 'não'):
        print("Opção inválida, tente novamente.")
        sistema = input("Mais algum aluno gostaria de fazer a prova?(sim / não): ")

    lista.append(acertos)
    alunos += 1

    if(sistema == "sim"):
        continue
    else:
        if(alunos == 0):
            alunos += 1
        media = geral / alunos
        resposta += 1

print(f'O maior acerto foi {max(lista)} o menor foi {min(lista)}, com {alunos} aluno(s) realizaram a prova, tendo a média de {media:.2f}')
