import http.server
import socketserver
import re
import os

def server(PORT):
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Servidor Iniciado na porta: ", PORT)
        httpd.serve_forever()
      
def getIp(gateway):
    #Baseado em algoritmo: https://www.vivaolinux.com.br/script/Python-Localiza-todos-os-IPs-da-rede
	gateway = gateway.split(".")
	ip = ".".join(gateway[0:2])
	cmd = 'ipconfig'
	t = os.popen(cmd)
	for i in t.readlines():
		if re.search('IPv4',i):
			if re.search(ip, i):
				i = i.split(':')
				return(i[1].strip())        
