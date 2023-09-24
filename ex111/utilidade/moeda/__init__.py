def metade(n, formato=False):
    x = n / 2
    return x if not formato else moeda(x)


def dobro(n, formato=False):
    x = 2 * n
    return x if not formato else moeda(x)


def aumentar(n, p, formato=False):
    x = n + n * (p / 100)
    return x if not formato else moeda(x)


def diminuir(n, p, formato=False):
    x = n - n * (p / 100)
    return x if not formato else moeda(x)


def moeda(v):
    din = f'R${v:.2f}'
    return din


def resumo(preco, mais=10, menos=5):
    print('=' * 30)
    print(f'{"ANALISANDO VALOR":^30}')
    print('=' * 30)
    print(f'Preço analizado: \t{moeda(preco)}')
    print(f'A Metade do preço: \t{metade(preco, True)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'{mais}% de aumento: \t{aumentar(preco, mais,True)}')
    print(f'{menos:0>2}% de redução: \t{diminuir(preco, menos, True)}')
