from model.pedra import Pedra

def minimax(tabuleiro):
    pedrasInimigas = acharPedrasInimigas(tabuleiro)
    max = 0
    pedra_vez =Pedra(0,0,0)
    direcao = 'd'

    for z in pedrasInimigas:
        if(z.valor == -1):
            res = funcaoAvaliativa(tabuleiro,z)
        else:
            res = funcaoAvaliativaRainha(tabuleiro,z)
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
    res = []
    valorD = 0
    valorE = 0
    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -2):
                valorD = -1
            else:
                valorD = 1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna + 2] == 0):
            valorD = 1
    
    
    except:
        pass



    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -2):
                valorE = -1
            else:
                valorE =1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna - 2] == 0):
            valorE = 1
    
    except:
        pass


    
    if(valorE > valorD):
        res.append(valorE)
        res.append('e')
    else:
        res.append(valorD)
        res.append('d')

    return res


def funcaoAvaliativaRainha(tabuleiro,pedra):
    valorCD = 0
    valorCE = 0
    valorBD = 0
    valorBE = 0
    res = []
    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -2):
                valorCD = -1
            else:
                valorCD = 1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna + 2] == 0):
            valorCD = 1
    except:
        pass



    try:
        if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -2):
                valorCE = -1
            else:
                valorCE =1
        if(tabuleiro.matriz[pedra.linha - 2][pedra.coluna - 2] == 0):
            valorCE = 1

        if(pedra.linha == 0):
            valorCE = -1
    except:
        pass



    try:
        if(tabuleiro.matriz[pedra.linha + 1][pedra.coluna + 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna + 1].valor == -2):
                valorBD = -1
            else:
                valorBD = 1
        if(tabuleiro.matriz[pedra.linha + 2][pedra.coluna + 2] == 0):
            valorBD = 1
    except:
        pass

    
    try:
        if(tabuleiro.matriz[pedra.linha + 1][pedra.coluna - 1] != 0 ):
            if(tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -1 or tabuleiro.matriz[pedra.linha - 1][pedra.coluna - 1].valor == -2):
                valorBE = -1
            else:
                valorBE =1
        if(tabuleiro.matriz[pedra.linha + 2][pedra.coluna - 2] == 0):
            valorBE = 1
    except:
        pass

    aux = []
    if(valorBD > valorBE):
        res.append(valorBD)
        res.append('bd')
    else:
        res.append(valorBE)
        res.append('be')
        
    if(valorCD > valorCE):
        aux.append(valorCD)
        aux.append('cd')
    else:
        aux.append(valorCE)
        aux.append('ce')
    
    if(res[0] > aux[0]):
        pass
    else:
        res = aux

    
    
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