n = float(input('Qual o preço do produto? R$'))

x = n - ((5 / 100) * n)

print(f'O produto que custava R${n:.2f}, na promoção com desconto de 5% vai custar R${x:.2f}')