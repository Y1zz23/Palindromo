frase = str(input("Digite uma frase: ")).strip().upper()
frase_sem_espacos = "".join(frase.split())
frase_reverso = frase[::-1]
frase_reversoo = "".join(frase_reverso.split())
if frase_sem_espacos == frase_reversoo:
    print("A frase {} é palíndromo".format(frase))
else:
    print("A frase {} não é um palíndromo".format(frase))
print("O inverso de {} é {}".format(frase_sem_espacos,frase_reversoo))