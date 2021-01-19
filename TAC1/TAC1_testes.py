seq = input('Digite a sequência: ')
codon_lista = []
for i in range(0, len(seq), 3):
    codon_lista.append(seq[i:i+3])

print(codon_lista)