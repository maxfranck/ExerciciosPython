n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))

a = n1 * n2
x = a / 2

print(f'Sua parede tem a dimensão de {n1}x{n2} e sua área é de {a}m².')
print(f'Para pintar essa parede, você precisará de {x:.3f}l de tinta.')