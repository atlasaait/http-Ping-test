import http.server
import socketserver
import pandas as pd

port = 80
address = ("", server)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"Server démarré sur le PORT {port}")
httpd.serve_forever()