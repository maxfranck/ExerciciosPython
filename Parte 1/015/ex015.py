n1 = int(input('Quantos dias alugados? '))
n2 = int(input('Quantos Km rodados? '))

x = 60 * n1
y = 0.15 * n2
total = x + y

print(f'O total a pagar é de R${total:.2f}')