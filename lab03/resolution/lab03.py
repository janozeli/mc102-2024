###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cupons de Desconto
# Nome:
# RA:
###################################################

# leitura de dados
cupom1_reais = float(input())
cupom1_minimo = float(input())
cupom2_porcentagem = float(input())
cupom2_limite = float(input())
cupom3_porcentagem = float(input())
cupom3_minimo = float(input())
valor_compra = float(input())

# cálculo dos descontos
desconto_cupom1 = float(0)
desconto_cupom2 = float(0)
desconto_cupom3 = float(0)

if valor_compra >= cupom1_minimo:
    desconto_cupom1 = cupom1_reais

if valor_compra >= cupom2_limite:
    desconto_cupom2 = (cupom2_limite if (valor_compra * cupom2_porcentagem / 100 > cupom2_limite) else valor_compra * cupom2_porcentagem / 100)

if valor_compra >= cupom3_minimo:
    desconto_cupom3 = valor_compra * cupom3_porcentagem / 100

# Impressão da saída
maior_desconto = max(desconto_cupom1, desconto_cupom2, desconto_cupom3)

lista_cupons = []

if desconto_cupom1 == maior_desconto:
    lista_cupons.append('1')
if desconto_cupom2 == maior_desconto:
    lista_cupons.append('2')
if desconto_cupom3 == maior_desconto:
    lista_cupons.append('3')

# ...
string_cupom = 'Cupom' if len(lista_cupons) == 1 else 'Cupons'
cupons = ', '.join(lista_cupons)

print(f'Maior desconto: {string_cupom} {cupons}')
print('Valor do desconto: R$ {:.2f}'.format(maior_desconto).replace(".", ","))
