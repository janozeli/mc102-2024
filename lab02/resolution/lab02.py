###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Em Busca de um Chuveiro
# Nome:
# RA:
###################################################

# Leitura da entrada
resistencia = int(input()) 
voltagem = int(input()) 
horas_ligado = int(input()) 
custo_kwh = float(input()) 
limite = int(input())

# Cálculo do consumo e impressão da saída
pontencia = voltagem**2 / resistencia
consumo_kwh = (pontencia * horas_ligado) / 1000
consumo_rs = consumo_kwh * custo_kwh

if consumo_rs <= limite:
    print(True)
else:
    print(False)
    