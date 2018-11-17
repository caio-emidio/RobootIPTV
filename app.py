import os
aprovados = [".mp4"]
ip = "http://192.168.0.9:8001/"
def lista(nPath, aprovados, ip):
    listaSaida = []
    for path, f, arquivo in os.walk(nPath):
        folder = path.split("\\")[-1]
        for a in arquivo:
            nome = a[0:-4]
            #print("{}\{} - {} - {}".format(path,a,nome,folder))
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
        #print(L['caminho'])
        t = open(arquivo, "a")
        t.write('#EXTINF:-1 tvg-id="" tvg-logo="" group-title="{}",{}\n'.format(L['pasta'],L['nome']))
        t.write(L['caminho'])
        t.write('\n\n')

if __name__ == "__main__":
    arquivo="RobootTV.m3u"
    Lista = lista('D:\\RobootTV', aprovados, ip)
    inicializa(arquivo)
    preenche_locais(arquivo,Lista)
