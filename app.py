import sys
import os
import json
from httproboot import server

def lista(nPath, aprovados, ip):
    listaSaida = []
    for path, f, arquivo in os.walk(nPath):
        folder = path.split("\\")[-1]

        for a in arquivo:
            nome = a[0:-4]
            extensao = a[-4:]
            if extensao in aprovados:
                caminho = ip+folder+"/"+a
                aux = {
                    'caminho': caminho,
                    'nome': nome,
                    'pasta': folder
                    }
                listaSaida.append(aux)
    return(listaSaida)

def inicializa(arquivo):
    with open(arquivo, "w") as w:
        w.write("#EXTM3U\n\n")
        w.write('#PLAYLISTV: pltv-logo="{}" pltv-name="{}" pltv-description="{}" pltv-cover="{}" pltv-author="{}" pltv-email="{}"\n\n'.format("","Caio TV", "Caio TV", "", "Caio", "caio.emidio@gmail.com"))


def preenche_locais(arquivo, lista):
    for L in lista:
        t = open(arquivo, "a")
        t.write('#EXTINF:-1 tvg-id="" tvg-logo="" group-title="{}",{}\n'.format(L['pasta'],L['nome']))
        t.write(L['caminho'])
        t.write('\n\n')

def main(config):
    ip = config['address']['ip']
    port = config['address']['port']
    file = config['file']
    path = config['path']
    type = config['type']
    address = ip + ':' + str(port)
    ip = "http://" + address + "/"
    print(path,type,ip)
    Lista = lista(path, type, ip)
    inicializa(file)
    preenche_locais(file,Lista)


if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.loads(f.read())

    port = config['address']['port']
    main(config)
    server(port)
    input("...")
