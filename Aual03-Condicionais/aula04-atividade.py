def verificar_nota(nota):
    while nota < 0 or notaA > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
        return nota
    
notaA = float(input("Digite a 1ª nota: "))
verificar_nota(notaA)

notaB = float(input("Digite a 2ª nota: "))
while notaB < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite a nota novamente: "))

media = (notaA + notaB) / 2
print(media)
