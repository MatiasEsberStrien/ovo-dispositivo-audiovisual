import http.server, os

class SinCache(http.server.SimpleHTTPRequestHandler):
    # que el navegador vuelva a pedir la página: si no, muestra versiones viejas
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

http.server.ThreadingHTTPServer(("0.0.0.0", int(os.environ.get("PORT", 8080))), SinCache).serve_forever()
