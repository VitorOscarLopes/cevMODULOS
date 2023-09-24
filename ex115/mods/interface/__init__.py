def lin(tam=42):
    print('-'*tam)


def cabecalho(tit):
    lin()
    print(f'{tit:^42}')
    lin()


def menu(tit, opc):
    cabecalho(tit)
    for pos, item in enumerate(opc):
        print(f'\033[33m{pos+1}\033[m - \033[34m{item}\033[m')


def leiaint(msg='', quer=False):
    if quer is False:
        while True:
            try:
                n = int(input(msg))
            except KeyboardInterrupt:
                print('\033[0;31m\nErro! O usuario decidiu não esolher um número. \033[m')
                n = 0
                break
            except:
                print('\033[0;31mErro! Tente digitar um número válido.\033[m')
            else:
                break
        return n


def opcao():
    lin()
    n = leiaint('\033[33mSua opção:\033[m ')
    return n
