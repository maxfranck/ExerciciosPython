n = float(input('Qual o salário do funcionário? R$'))

x = n + ((15 / 100) * n)

print(f'Um funcionário que ganhava R${n:.2f}, com 15% de aumento, passa a receber R${x:.2f}')