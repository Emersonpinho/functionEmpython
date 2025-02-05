def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print('Sua primeira nota foi:', nota1)
    print('Sua segunda nota foi:', nota2)
    print('Sua terceira nota foi:', nota3)
    print(f'A media entre esssas é: {media:.2f}')
   

print(calcularMedia(7, 8, 7))