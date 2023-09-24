from ex115.mods.interface import *
from ex115.mods.arquivo import *

arq = 'cursoemvideo.txt'
if not arqex(arq):
    criarq(arq)
while True:
    menu('MENU PRINCIPAL', ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    resp = opcao()
    if resp == 1:
        lerarq(arq)
    if resp == 2:
        cabecalho(f'NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    if resp >= 4 or resp < 1:
        while True:
            print('\033[31mErro! Digite uma opção válida.\033[m')
            resp = opcao()
            if resp == 1 or resp == 2 or resp == 3:
                break
    if resp == 3:
        cabecalho('SAINDO DO SITEMA... ATÉ LOGO!')
        break
