#!/usr/bin/python3

import hashlib, os;

def verificarAlteracoes():
    relatorio = open('/home/usuario/relatorio.txt', 'w')
    linhasArquivos = open('arquivo.txt', 'r').readlines()
    linhasSaida = open('saida.txt', 'r').readlines()

    quantidade = len(linhasArquivos)

    for i in range(quantidade):
        linhaSaida = linhasSaida[i].__str__().split(":")
        hashsaida = linhaSaida[1].strip()
        linha = linhasArquivos[i].strip()

        if(os.path.exists(linha)):
            arquivo = open(linha, 'rb')
            key = hashlib.md5(arquivo.read()).hexdigest().rstrip()
            if(hashsaida != key):
                relatorio.write("Modificações no arquivo: " + linha + "\n")
                print("ALGUM ARQUIVO FOI MODIFICADO")

def gravarSaida():
    saida = open('saida.txt', 'w')
    linhas = open('arquivo.txt', 'r').readlines()

    for linha in linhas:
        linha = linha.rstrip();
        if(os.path.exists(linha)):
            arquivo = open(linha, 'rb')
            key = hashlib.md5(arquivo.read()).hexdigest()
            saida.write(linha + ': ' + key + '\n')



if(os.path.getsize('saida.txt') == 0):
    gravarSaida()
else:
    verificarAlteracoes()











