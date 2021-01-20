'''''''''
seq = input('Digite a sequência: ')
codon_lista = []
for i in range(0, len(seq), 3):
    codon_lista.append(seq[i:i+3])

print(codon_lista)
'''''

seq = input('Digite a sequência:')
contador = 1
lista = []
seq = seq.upper()

for x in range(0, len(seq)):
    if seq[x] == seq[x - 1]:
        contador = contador + 1
        if contador == 3:
            posicao = x - 1
    elif seq[x] != seq[x - 1]:
        if contador >= 3:
            lista.append((seq[x - 1], contador, posicao))
            contador = 1
        else:
            contador = 1
print(lista)
