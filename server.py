#!/usr/bin/env python3
"""弈律独立静态服务，提供 WASM 多线程需要的响应头。"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent

class ChessHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8011
    with ThreadingHTTPServer(('127.0.0.1', port), partial(ChessHandler, directory=str(ROOT))) as server:
        print(f'弈律：http://localhost:{port}/', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
