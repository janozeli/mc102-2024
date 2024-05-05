# -*- coding: utf-8 -*-

# Script para testar tarefas de laboratório de MC102 em ambiente GNU/Linux.

# Uso: python3 testador.py

# O programa lab<x>.py será testado com todos os arquivos arq<i>.in
# encontrados no diretório corrente. Os testes serão iniciados com i
# igual a 01 e serão interrompidos quando arq<i>.in não for encontrado.

# As saídas serão comparadas com os arquivos arquivos arq<i>.out. 

# Durante o processamento serão criados e posteriormente removidos
# arquivos arq<i>.res e arq<i>.diff. 

import os
import sys
import re

# Imprime as saídas do programa e do gabarito
output = True

path = ''
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    exit(0)

os.chdir(path + '/resolution')

r = re.compile(r'lab\d\d.py')
for file in os.listdir():
    if r.match(file):
        labfile = file
        break
else:
    print("Código do laboratório não encontrado.")
    exit(0)

i = 1
testfile = path + "/tests/arq" + "{:02d}".format(i) + ".in"

while (os.path.exists(testfile)):
    resfile = path + "/tests/arq" + "{:02d}".format(i) + ".out"
    if not os.path.exists(resfile):
        print("Arquivo", resfile, "não encontrado.")
        sys.exit()

    outfile = path + "/tests/arq" + "{:02d}".format(i) + ".res"
    difffile = path + "/tests/arq" + "{:02d}".format(i) + ".diff"

    try:
        os.system("python3 " + labfile + " < " + testfile + " > " + outfile)
        if os.system("diff " + outfile + " " + resfile + " > " + difffile) == 0:
            print("Teste ", "{:02d}".format(i), ": resultado correto")
        else:
            print("Teste ", "{:02d}".format(i), ": resultado incorreto")
            if output:
                # os.system("cat " + difffile)
                print(">>> Sua resposta:")
                os.system("cat " + outfile)
                print(">>> Resposta correta:")
                os.system("cat " + resfile)
                break
    finally:
        if os.path.exists(outfile):
            os.remove(outfile)
        if os.path.exists(difffile):    
            os.remove(difffile)

    i += 1
    testfile = path + "/tests/arq" + "{:02d}".format(i) + ".in"
