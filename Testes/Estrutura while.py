## utilizando palavra reservada break

num_digitados = 0
soma = 0

## enquanto for verdadeiro

while True:
    n = float(input("Digite um número (Ou zero para encerrar): "))
    if n == 0:
        break
    num_digitados = num_digitados + 1
    soma = soma + n

print("Números digitados = %d" % num_digitados)
print("Soma = %d" % soma)

if num_digitados != 0:
    media_aritmetica = soma/num_digitados
    print("Média aritmética = %f" % media_aritmetica)
