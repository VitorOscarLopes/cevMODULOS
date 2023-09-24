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
