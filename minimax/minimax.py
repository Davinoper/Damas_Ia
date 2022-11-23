from model.tabuleiro import Tabuleiro
from model.pedra import Pedra

def minimax(tabuleiro):
    pedrasInimigas = acharPedrasInimigas(tabuleiro)
    max = 0
    pedra_vez =Pedra(0,0,0)
    direcao = 'd'

    for z in pedrasInimigas:
        res = melhorMovimento(tabuleiro,z)
        print(f'Linha:{z.linha} coluna:{z.coluna} para a direita =', res[0] )
        if(res[0] > max):
            max = res[0]
            pedra_vez = z
            direcao =res[1]

    print(" ")
    print(f'Pedra a ser movida: L:{pedra_vez.linha},C:{pedra_vez.coluna}')
    print(f'Pontuação movimento: {max}')
    print(f'Direção a ser seguida:{direcao}')


def acharPedrasInimigas(tabuleiro):
    lista_pedras = []
    for l in range(len(tabuleiro.matriz)):
        for c in range(len(tabuleiro.matriz[l])):
            if type(tabuleiro.matriz[l][c]) == type(Pedra(0,0,0)):
                if(tabuleiro.matriz[l][c].valor == -1 or tabuleiro.matriz[l][c].valor == -2):
                    lista_pedras.append(tabuleiro.matriz[l][c])
    return lista_pedras

def acharPedrasAmigas(tabuleiro):
    lista_pedras = []
    for l in range(len(tabuleiro.matriz)):
        for c in range(len(tabuleiro.matriz[l])):
            if type(tabuleiro.matriz[l][c]) == type(Pedra(0,0,0)):
                if(tabuleiro.matriz[l][c].valor == 1 or tabuleiro.matriz[l][c].valor == 2):
                    lista_pedras.append(tabuleiro.matriz[l][c])
    return lista_pedras


def melhorMovimento(tabuleiro, pedra ):
    valoresD = 0
    valoresE = 0
    res = []
    try:
        #verifica se tem uma peça inimiga caso o movimento seja executado a direita
        if(tabuleiro.matriz[pedra.linha + 2][pedra.coluna + 2].valor == 1 ):
            valoresD = -1
        else:
          if(tabuleiro.matriz[pedra.linha + 1][pedra.coluna + 1].valor == 1 ):
            valoresD = 1
          elif (tabuleiro.matriz[pedra.linha + 1][pedra.coluna + 1].valor == -1 ):
            valoresD = -5
          else:
            valoresD = 0
             
        #verifica se tem uma peça inimiga caso o movimento seja executado a esquerda
        if(tabuleiro.matriz[pedra.linha + 2][pedra.coluna - 2].valor == 1 ):
            valoresE -= 1
        else:
          if(tabuleiro.matriz[pedra.linha + 1][pedra.coluna - 1].valor == 1 ):
            valoresE += 1
          elif (tabuleiro.matriz[pedra.linha + 1][pedra.coluna - 1].valor == -1 ):
            valoresE = -5
          else:
            valoresE = 0
    except:
        pass

    if(valoresE > valoresD):
        res.append(valoresE)
        res.append('e')
    else:
        res.append(valoresD)
        res.append('d')
    
    return res

    

    # 1 - para peças Pretas
    # -1 - para peças Brancas
    # 2 - Dama Preta
    # -2 - Dama Branca
    # d - segue a direita
    # e - segue a esquerda
    # bd - baixo e direita
    # be - baixo e esquerda
    # cd - cima e direita
    # ce - cima e esquerda