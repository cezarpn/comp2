""""""""""
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
if valor1 > valor2:
    print("%d \n%d" % (valor2, valor1))
elif valor1 < valor2:
    print("%d \n%d" % (valor1, valor2))
else:
    print(valor1)
    print(valor2)
"""""""
porcentagem = float(input('Digite a porcentagem de receita antigida: '))
if porcentagem < 80:
    print('Não entregue')
elif porcentagem >= 80 and porcentagem <= 100:
    print('Entregue')
else:
    print('Excede a meta')
"""""""
valores = [0, 0, 0, 0, 0]

soma = 0
x = 0

## primeiro vamos ler os valores
while x < len(valores):
    valores[x] = float(input("Digite o valor %d: " % (x+1)))
    if valores[x] == 0:
        break
    else:
        x = x + 1

print(valores)
"""""
