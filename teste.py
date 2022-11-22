from model.tabuleiro import Tabuleiro 
from minimax.minimax import minimax

tabuleiro = Tabuleiro()
tabuleiro.gerarTabuleiro()

minimax(tabuleiro)