#!/usr/bin/env python3

import subprocess
import os

enconding = "utf-8"
all_executables = "/home/maycon/files"
path = "/sbin/"

# subprocess.run(["ls", "-l"])
# lista todos executaveis
out = subprocess.check_output(["find", path, "-executable"])
executables = out.decode(enconding).split("\n")

if(os.path.exists(all_executables)):

    linhas = open(all_executables, "r").readlines()

    if(len(linhas) == len(executables)):
        print("A LISTA CONTINUA A MESMA")
    else:
        print("UM NOVO EXECUTAVEL FOI ENCONTRADO")
        for i in range(len(executables)):
            try:
                # \n pequena gambiarra pra funfar direitin
                exec_index = linhas.index(executables[i]+"\n")
            except ValueError:
                file = open(all_executables, "a")
                print(executables[i])
                file.write(executables[i] + "\n")
                file.close()
                print("NOVO EXECUTAVEL REGISTRADO")

else:
    file = open(all_executables, "w")
    for exec in executables:
        if(executables.index(exec) == len(executables)-1):
            file.write(exec)
        file.write(exec + "\n")
    file.close()
    print("ARQUIVO FILES CRIADO " + all_executables)
