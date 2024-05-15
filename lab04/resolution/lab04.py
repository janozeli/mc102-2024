###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Pedra, Papel e Tesoura 2.0
# Nome:
# RA: 
###################################################

# Leitura dos valores de força de cada jogador
bonus_jogador_1 = int(input())
bonus_jogador_2 = int(input())
vitorias_jogador_1 = 0
vitorias_jogador_2 = 0
empate = 0


# Processamento dos dados
#...

entrada = input().split()
if entrada[0] == '0':
  break
else:
  jogada_jogador_1, forca_jogador_1, jogada_jogador_2, forca_jogador_2, fator_rodada = entrada
  forca_jogador_1 = int(forca_jogador_1)
  forca_jogador_2 = int(forca_jogador_2)
  fator_rodada = int(fator_rodada)





# Saída de dados
print('Vitórias do jogador 1:', vitorias_jogador_1)
print('Vitórias do jogador 2:', vitorias_jogador_2)
print('Empates:', empate)
