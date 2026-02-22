import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Handle /admin by redirecting to /admin/index.html or serving it
        if self.path == '/admin' or self.path == '/admin/':
            self.path = '/admin/index.html'
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHandler) as httpd:
    print(f"Serving on http://0.0.0.0:{PORT}")
    httpd.serve_forever()
