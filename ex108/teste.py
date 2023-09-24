from ex108 import moeda
p = int(input('Digite um número: '))
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, 13))}')
