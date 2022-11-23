from model.pedra import Pedra

def minimax(tabuleiro):
    pedrasAmigas = acharPedrasInimigas(tabuleiro)
    max = 0
    pedra_vez =Pedra(0,0,0)
    direcao = 'd'

    for z in pedrasAmigas:
        res = funcaoAvaliativa(tabuleiro,z)
        print(f'Linha:{z.linha} coluna:{z.coluna} para a direita =', res[0] )
        if(res[0] > max):
            max = res[0]
            pedra_vez = z
            direcao =res[1]

    return [pedra_vez, direcao]


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
    valorD = 0
    valorE = 0
    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -2):
                valorD = 1
            else:
                valorD =1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna + 2] == 0):
            valorD = 1
    
        if(tabuleiro.pedras_inimigas < aux.pedras_inimigas):
            valorD =1

        if(tabuleiro.pedras_amigas < aux.pedras_amigas):
            valorD = 1

        
    except:
        print(f'Linha:{pedra.linha} coluna:{pedra.coluna} -> não pode ir para a direita')

    tabuleiro = aux

    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -2):
                valorE = 1
            else:
                valorE =1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna - 2] == 0):
            valorE = 1
    
        if(tabuleiro.pedras_inimigas < aux.pedras_inimigas):
            valorE =1

        if(tabuleiro.pedras_amigas < aux.pedras_amigas):
            valorE = 1
    except:
        print(f'Linha:{pedra.linha} coluna:{pedra.coluna} -> não pode ir para a esquerda')

    tabuleiro = aux
    res = []
    if(valorE > valorD):
        res.append(valorE)
        res.append('e')
    else:
        res.append(valorD)
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