from model.tabuleiro import Tabuleiro 

tabuleiro = Tabuleiro()

tabuleiro.gerarTabuleiro()

tabuleiro.imprimirTabuleiro()

condicao = True
ganhador = 1

while condicao:
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    direcao = input('direcao: ')
    tabuleiro.moverPedra(linha,coluna,direcao)
    tabuleiro.imprimirTabuleiro()
    if tabuleiro.pedras_inimigas == 0:
        ganhador = 1
        condicao = False
    elif tabuleiro.pedras_amigas == 0:
        ganhador = -1
        condicao = False

if(ganhador == 1):
    print('Parabéns você ganhou!')
else:
    print('Você perdeu.')