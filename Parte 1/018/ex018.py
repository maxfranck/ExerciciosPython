from math import radians, sin, cos, tan
n = float(input('Digite um ângulo: '))

seno = sin(radians(n))
cosseno = cos(radians(n))
tangente = tan(radians(n))

print(f'O ângulo {n} tem o SENO de {seno:.2f}')
print(f'O ângulo {n} tem o SENO de {cosseno:.2f}')
print(f'O ângulo {n} tem o SENO de {tangente:.2f}')