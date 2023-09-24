def leiaint(msg='', quer = False):
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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[0;31m\nUsuario preferiu não esolher um número. \033[m')
            n = 0
            break
        except:
            print('\033[0;31mErro! Tente digitar um número válido.\033[m')
        else:
            break
    return n
