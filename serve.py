"""Feza ve Işıltı – local server.

Run:  python3 serve.py
Then open the printed address on the Mac or on an iPad on the same Wi-Fi.
"""
import http.server
import os
import socket

PORT = 8765
ROOT = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_POST(self):
        # Dev helper: the game posts its list of spoken lines here so gen_voice.py can record them.
        if self.path != "/save-lines":
            return self.send_error(404)
        n = int(self.headers.get("Content-Length", 0))
        os.makedirs(os.path.join(ROOT, "voice"), exist_ok=True)
        with open(os.path.join(ROOT, "voice", "lines.json"), "wb") as f:
            f.write(self.rfile.read(n))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *a):
        pass


def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


if __name__ == "__main__":
    print(f"Mac'te:   http://localhost:{PORT}")
    print(f"iPad'de:  http://{local_ip()}:{PORT}   (aynı Wi-Fi ağında olmalı)")
    http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
