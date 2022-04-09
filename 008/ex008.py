n = float(input('Digite uma distância em metros: '))

km = n / 1000
hm = n / 100
dam = n / 10
dm = int(n * 10)
cm = int(n * 100)
mm = int(n * 1000)

print(f'A medida de {n}m corresponde a: ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')