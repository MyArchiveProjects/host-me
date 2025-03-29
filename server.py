import http.server
import socketserver
import webbrowser
import os

try:
    from config import port
except ImportError:
    print("Config file missing or malformed.")
    exit(1)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"\033[92m[+] Server started on http://localhost:{port}\033[0m")
    try:
        webbrowser.open(f"http://localhost:{port}")
    except:
        print("[!] Could not open browser.")
    httpd.serve_forever()
