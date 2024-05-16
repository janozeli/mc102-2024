###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Montanha Russa
# Nome:
# RA:
###################################################

# Leitura de dados
dias = int(input())

precos = []
for _ in range(dias):
   precos.append(float(input()))

dinheiro_inicial = float(input())

# Cálculo dos dias de compra e venda
lucro_maximo = 0
melhores_dias = (0, 0, 0, 0)

for D1 in range(dias):
    for D2 in range(D1 + 1, dias):
        preco_acao_primeira_compra = precos[D1]
        preco_acao_primeira_venda = precos[D2]
        quantidade_acoes_primeira_compra = dinheiro_inicial // preco_acao_primeira_compra
        dinheiro_restante_primeira_compra = dinheiro_inicial % preco_acao_primeira_compra
        primeiro_lucro = quantidade_acoes_primeira_compra * (preco_acao_primeira_venda - preco_acao_primeira_compra)
        dinheiro_total_primeira_venda = quantidade_acoes_primeira_compra * preco_acao_primeira_venda + dinheiro_restante_primeira_compra

        for D3 in range(D2 + 1, dias):
            for D4 in range(D3 + 1, dias):
                preco_acao_segunda_compra = precos[D3]
                preco_acao_segunda_venda = precos[D4]
                quantidade_acoes_segunda_compra = dinheiro_total_primeira_venda // preco_acao_segunda_compra
                dinheiro_restante_segunda_compra = dinheiro_total_primeira_venda % preco_acao_segunda_compra
                segundo_lucro = quantidade_acoes_segunda_compra * (preco_acao_segunda_venda - preco_acao_segunda_compra)
                dinheiro_total_segunda_venda = primeiro_lucro + segundo_lucro

                if dinheiro_total_segunda_venda > lucro_maximo or D4 == 3:
                    lucro_maximo = dinheiro_total_segunda_venda
                    melhores_dias = (D1 + 1, D2 + 1, D3 + 1, D4 + 1)

# Impressão da saída
print(f"Dia da primeira compra: {melhores_dias[0]}")
print(f"Valor de compra: R$ {precos[melhores_dias[0] - 1]:.2f}".replace('.', ','))
print(f"Dia da primeira venda: {melhores_dias[1]}")
print(f"Valor de venda: R$ {precos[melhores_dias[1] - 1]:.2f}".replace('.', ','))
print(f"Dia da segunda compra: {melhores_dias[2]}")
print(f"Valor de compra: R$ {precos[melhores_dias[2] - 1]:.2f}".replace('.', ','))
print(f"Dia da segunda venda: {melhores_dias[3]}")
print(f"Valor de venda: R$ {precos[melhores_dias[3] - 1]:.2f}".replace('.', ','))
print(f"Valor final: R$ {lucro_maximo + dinheiro_inicial:.2f}".replace('.', ','))
