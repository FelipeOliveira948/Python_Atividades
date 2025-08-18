nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media <= 10 and media >= 9):
    print(f'Sua nota foi {media}, CONCEITO: A, Aprovado.')

elif(media >= 7.5):
    print(f'Sua nota foi {media}, CONCEITO: B, Aprovado.')

elif(media >= 6.0):
    print(f'Sua nota foi {media}, CONCEITO: C, Aprovado.')

elif(media >= 4.0):
    print(f'Sua nota foi {media}, CONCEITO: D, Reprovado.')

else:
    print(f'Sua nota foi {media}, CONCEITO: E, Reprovado.')