#!/usr/bin/env python3
'''
3 - Registrar novas execuções de processo
3.1 A cada 5 minutos rodar um script Python3; (cron)
3.2 Neste script anote o horário de registro de todo novo processo localizado no sistema e salve
em um relatório em /home/usuario/ (marque, nome do processo, caminho do executável, PID, UID);
3.3 Esta lista não pode ser redundante, ou seja, só dos processo iniciados nos últimos 5 minutos;
'''
from datetime import datetime
import subprocess
import os

cmd = "ps -eo command,pid,uid"

enconding = "utf-8"
path = "/home/maycon/process"
path_aux = "/home/maycon/processAux"

process = subprocess.Popen(
    cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# peguei a saída
out, err = process.communicate()
new_process = out.decode(enconding).split("\n")

if os.path.exists(path):
    lines = open(path, "r").readlines()

    for i in range(len(new_process)):
        try:
            process_index = lines.index(new_process[i].strip() + "\n")

        except ValueError:
            file = open(path, "a")
            file.write(new_process[i] + "\n")
            print(new_process[i])
            file.close()
else:
    # gravar um arquivo com os processos
    file = open(path, "w")
    file_aux = open(path_aux, "w")
    for line in new_process:
        now = datetime.now()
        file.write(line + " " + str(now.hour) +
                   ":" + str(now.minute) + "\n")

    file.close()
    print("GEREI UM NOVO ARQUIVO")
