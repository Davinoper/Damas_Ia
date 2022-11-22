from model.tabuleiro import Tabuleiro
from model.pedra import Pedra

def minimax(tabuleiro):
    pedrasInimigas = acharPedrasInimigas(tabuleiro)
    pedrasAmigas = acharPedrasAmigas(tabuleiro)

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


def funcaoAvaliativa(tabuleiro,pedra):
    aux = tabuleiro
    pedraAmiga = aux.pedras_amigas
    max = 0
    if(pedra.valor == -1):
        aux.moverPedra(pedra.linha, pedra.coluna, 'e')
        if(aux.pedras_amigas < pedraAmiga):
            max +=1

        aux.moverPedra(pedra.linha, pedra.coluna, 'd')
        if(aux.pedras_amigas < pedraAmiga):
            max +=1
    
    if(pedra.valor == -2):
        aux.moverPedra(pedra.linha, pedra.coluna, 'be')
        if(aux.pedras_amigas < pedraAmiga):
            max +=1

        aux.moverPedra(pedra.linha, pedra.coluna, 'bd')
        if(aux.pedras_amigas < pedraAmiga):
            max +=1

        aux.moverPedra(pedra.linha, pedra.coluna, 'ce')
        if(aux.pedras_amigas < pedraAmiga):
            max +=1

        aux.moverPedra(pedra.linha, pedra.coluna, 'cd')
        if(aux.pedras_amigas < pedraAmiga):
            max += 1

