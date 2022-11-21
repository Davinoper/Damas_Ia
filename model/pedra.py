class Pedra:
    def __init__(self, linha, coluna, valor):
        self.linha = linha
        self.coluna = coluna
        self.valor = valor

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def transformarRainha(self):
        if self.valor == 1:
            self.valor = 2
        elif self.valor == -1:
            self.valor = -2
    
    def __repr__(self):
        if(self.valor == 1):
            return 'P'
        else:
            return 'B'

