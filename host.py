import os
from http import server
import socketserver

class Server (server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, directory = os.path.dirname(__file__))

with socketserver.ThreadingTCPServer(("", 8000), Server) as siteServer:
    siteServer.serve_forever()