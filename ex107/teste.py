from ex107 import moeda
p = int(input('Digite um número: '))
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'Aumentando 10% de {p} temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13% de {p} temos {moeda.diminuir(p, 13)}')
