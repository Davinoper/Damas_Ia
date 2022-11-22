import numpy as np
from model.pedra import Pedra
import rotate_matrix as rtm

class Tabuleiro:
    def __init__(self):
        self.matriz = []
        self.pedras_amigas = 12
        self.pedras_inimigas =12
        self.rainhas_amigas = 0
        self.rainhas_inimigas = 0
        self.vez = True
        self.turnos = 0

    def getJogador(self):
        if(self.vez):
            print("")
            print("++++++++++++")
            print('Sua vez')
            print("++++++++++++")
            print("")
        else:
            print("")
            print("++++++++++++")
            print('Vez do inimigo')
            print("++++++++++++")
            print("")

    def imprimirTabuleiro(self):
        self.getJogador()
        count = 0
        for i in self.matriz:
            print(f'linha {count} {i}')
            count += 1
        print(" ")
        print('coluna   0, 1, 2, 3, 4, 5, 6, 7')
        print(" ")
        print("=========================================================================")
        print(f'Pedras: {self.pedras_amigas} | Pedras Inimigas: {self.pedras_inimigas}')
        print(f'Rainhas: {self.rainhas_amigas} | Rainhas Inimigas: {self.rainhas_inimigas}')
        print(f'Turnos: {self.turnos}')
        print("=========================================================================")
        print(" ")

        

    def gerarTabuleiro(self):
         for linha in range(8):
            self.matriz.append([])
            for coluna in range(8):
                if coluna % 2 == ((linha +  1) % 2):
                    if linha < 3:
                        self.matriz[linha].append(Pedra(linha, coluna, 1))
                    elif linha > 4:
                        self.matriz[linha].append(Pedra(linha, coluna, -1))
                    else:
                        self.matriz[linha].append(0)
                else:
                    self.matriz[linha].append(0)
                 
    





    def moverPedra(self, linha, coluna, direcao):
        pedra = self.matriz[linha][coluna]

        if self.vez and pedra.valor == 1:
            aux = self.moverAmigo(linha,coluna,direcao,pedra)
            if(aux.linha == 7):
                self.matriz[aux.linha][aux.coluna].transformarRainha()
                self.rainhas_amigas +=1
        elif self.vez and pedra.valor == 2:
            self.moverRainhaAmiga(linha,coluna,direcao,pedra)
        elif not self.vez and pedra.valor == -1:
            aux = self.moverInimigo(linha,coluna,direcao,pedra)
            if(aux.linha == 0):
                self.matriz[aux.linha][aux.coluna].transformarRainha()
                self.rainhas_inimigas +=1
        elif not self.vez and pedra.valor == -2:
            self.moverRainhaInimiga(linha,coluna,direcao,pedra)


        

    def moverRainhaAmiga(self,linha,coluna,direcao,pedra):
        if direcao == 'be':
            if self.matriz[linha + 1][coluna -1] == 0:
                pedra.linha = linha + 1
                pedra.coluna = coluna - 1
                self.matriz[linha + 1][coluna - 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha +1][coluna -1]  == 0) and (self.matriz[linha+1][coluna-1].valor == -1 or self.matriz[linha+1][coluna-1].valor == -2):
                pedra.linha = linha + 2
                pedra.coluna = coluna - 2
                self.matriz[linha + 1][coluna - 1] = 0
                self.matriz[linha + 2][coluna - 2]  = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_inimigas -= 1

        elif direcao == 'bd':
            if self.matriz[linha +1][coluna+1] == 0:
                pedra.linha = linha + 1
                pedra.coluna = coluna + 1
                self.matriz[linha + 1][coluna + 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha+1][coluna+1] == 0) and (self.matriz[linha+1][coluna+1].valor == -1 or self.matriz[linha+1][coluna+1].valor == -2):
                pedra.linha = linha + 2
                pedra.coluna = coluna + 2
                self.matriz[linha + 1][coluna + 1] = 0
                self.matriz[linha + 2][coluna + 2]  = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_inimigas -= 1

        if direcao == 'ce':
            if self.matriz[linha - 1][coluna -1] == 0:
                pedra.linha = linha - 1
                pedra.coluna = coluna - 1
                self.matriz[linha - 1][coluna - 1] = pedra
                self.matriz[linha][coluna] = 0
            
            elif not(self.matriz[linha - 1][coluna -1] == 0) and (self.matriz[linha - 1][coluna -1].valor == -1 or self.matriz[linha-1][coluna-1].valor == -2):
                pedra.linha = linha - 2
                pedra.coluna = coluna - 2
                self.matriz[linha - 1][coluna - 1] = 0
                self.matriz[linha - 2][coluna - 2] = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_inimigas -= 1

        elif direcao == 'cd':
            if self.matriz[linha - 1][coluna +1] == 0:
                pedra.linha = linha - 1
                pedra.coluna = coluna + 1
                self.matriz[linha - 1][coluna + 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha - 1][coluna +1] == 0) and (self.matriz[linha - 1][coluna +1].valor == -1 or self.matriz[linha-1][coluna+1].valor == -2):
                pedra.linha = linha - 2
                pedra.coluna = coluna + 2
                self.matriz[linha - 1][coluna + 1] = 0
                self.matriz[linha - 2][coluna + 2] = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_inimigas -= 1
        else:
           pass

        self.turnos += 1
        self.vez = False


    def moverRainhaInimiga(self,linha,coluna,direcao,pedra):
        if direcao == 'be':
            if self.matriz[linha + 1][coluna -1] == 0:
                pedra.linha = linha + 1
                pedra.coluna = coluna - 1
                self.matriz[linha + 1][coluna - 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha +1][coluna -1]  == 0) and (self.matriz[linha+1][coluna-1].valor == 1 or self.matriz[linha+1][coluna-1].valor == 2):
                pedra.linha = linha + 2
                pedra.coluna = coluna - 2
                self.matriz[linha + 1][coluna - 1] = 0
                self.matriz[linha + 2][coluna - 2]  = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_amigas -= 1


        elif direcao == 'bd':
            if self.matriz[linha +1][coluna+1] == 0:
                pedra.linha = linha + 1
                pedra.coluna = coluna + 1
                self.matriz[linha + 1][coluna + 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha+1][coluna+1] == 0) and (self.matriz[linha+1][coluna+1].valor == 1 or self.matriz[linha+1][coluna+1].valor == 2):
                pedra.linha = linha + 2
                pedra.coluna = coluna + 2
                self.matriz[linha + 1][coluna + 1] = 0
                self.matriz[linha + 2][coluna + 2]  = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_amigas -= 1

        if direcao == 'ce':
            if self.matriz[linha - 1][coluna -1] == 0:
                pedra.linha = linha - 1
                pedra.coluna = coluna - 1
                self.matriz[linha - 1][coluna - 1] = pedra
                self.matriz[linha][coluna] = 0
            
            elif not(self.matriz[linha - 1][coluna -1] == 0) and (self.matriz[linha - 1][coluna -1].valor == 1 or self.matriz[linha-1][coluna-1].valor == 2):
                pedra.linha = linha - 2
                pedra.coluna = coluna - 2
                self.matriz[linha - 1][coluna - 1] = 0
                self.matriz[linha - 2][coluna - 2] = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_amigas -= 1

        elif direcao == 'cd':
            if self.matriz[linha - 1][coluna +1] == 0:
                pedra.linha = linha - 1
                pedra.coluna = coluna + 1
                self.matriz[linha - 1][coluna + 1] = pedra
                self.matriz[linha][coluna] = 0

            elif not(self.matriz[linha - 1][coluna +1] == 0) and (self.matriz[linha - 1][coluna +1].valor == 1 or self.matriz[linha-1][coluna+1].valor == 2):
                pedra.linha = linha - 2
                pedra.coluna = coluna + 2
                self.matriz[linha - 1][coluna + 1] = 0
                self.matriz[linha - 2][coluna + 2] = pedra
                self.matriz[linha][coluna] = 0
                self.pedras_amigas -= 1
        else:
           pass

        self.turnos += 1
        self.vez = True

    def moverAmigo(self, linha, coluna, direcao, pedra):
        if pedra.valor == 1:
            if direcao == 'e':
                if self.matriz[linha + 1][coluna -1] == 0:
                    pedra.linha = linha + 1
                    pedra.coluna = coluna - 1
                    self.matriz[linha + 1][coluna - 1] = pedra
                    self.matriz[linha][coluna] = 0

                elif not(self.matriz[linha +1][coluna -1]  == 0) and (self.matriz[linha+1][coluna-1].valor == -1 or self.matriz[linha+1][coluna-1].valor == -2):
                    pedra.linha = linha + 2
                    pedra.coluna = coluna - 2
                    self.matriz[linha + 1][coluna - 1] = 0
                    self.matriz[linha + 2][coluna - 2]  = pedra
                    self.matriz[linha][coluna] = 0
                    self.pedras_inimigas -= 1


            elif direcao == 'd':
                if self.matriz[linha +1][coluna+1] == 0:
                    pedra.linha = linha + 1
                    pedra.coluna = coluna + 1
                    self.matriz[linha + 1][coluna + 1] = pedra
                    self.matriz[linha][coluna] = 0

                elif not(self.matriz[linha+1][coluna+1] == 0) and (self.matriz[linha+1][coluna+1].valor == -1 or self.matriz[linha+1][coluna+1].valor == -2):
                    pedra.linha = linha + 2
                    pedra.coluna = coluna + 2
                    self.matriz[linha + 1][coluna + 1] = 0
                    self.matriz[linha + 2][coluna + 2]  = pedra
                    self.matriz[linha][coluna] = 0
                    self.pedras_inimigas -= 1
        else:
            pass

        self.turnos += 1
        self.vez = False
        return pedra


    
        

    def moverInimigo(self,linha,coluna,direcao,pedra):
        if pedra.valor == -1:
                if direcao == 'e':
                    if self.matriz[linha - 1][coluna -1] == 0:
                        pedra.linha = linha - 1
                        pedra.coluna = coluna - 1
                        self.matriz[linha - 1][coluna - 1] = pedra
                        self.matriz[linha][coluna] = 0
                    
                    elif not(self.matriz[linha - 1][coluna -1] == 0) and (self.matriz[linha - 1][coluna -1].valor == 1 or self.matriz[linha - 1][coluna -1].valor == 2):
                        pedra.linha = linha - 2
                        pedra.coluna = coluna - 2
                        self.matriz[linha - 1][coluna - 1] = 0
                        self.matriz[linha - 2][coluna - 2] = pedra
                        self.matriz[linha][coluna] = 0
                        self.pedras_amigas -= 1

                elif direcao == 'd':
                    if self.matriz[linha - 1][coluna +1] == 0:
                        pedra.linha = linha - 1
                        pedra.coluna = coluna + 1
                        self.matriz[linha - 1][coluna + 1] = pedra
                        self.matriz[linha][coluna] = 0

                    elif not(self.matriz[linha - 1][coluna +1] == 0) and (self.matriz[linha - 1][coluna +1].valor == 1 or self.matriz[linha - 1][coluna +1].valor == 2):
                        pedra.linha = linha - 2
                        pedra.coluna = coluna + 2
                        self.matriz[linha - 1][coluna + 1] = 0
                        self.matriz[linha - 2][coluna + 2] = pedra
                        self.matriz[linha][coluna] = 0
                        self.pedras_amigas -= 1
        else:
           pass

        self.turnos += 1
        self.vez = True
        return pedra
        
