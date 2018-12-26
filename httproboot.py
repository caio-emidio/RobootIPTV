import http.server
import socketserver

def server(PORT):
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Servidor Iniciado na porta: ", PORT)
        httpd.serve_forever()
