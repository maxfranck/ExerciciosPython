from math import sqrt, pow

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

n = pow(co,2) + pow(ca,2)
hip = sqrt(n)

print(f'A hipotenusa vai medir {hip:.2f}')