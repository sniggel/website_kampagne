"""
Lokaler Entwicklungsserver fuer den Website-Draft von Yvone Janssen.
Startet einen Live-Reload-Server unter Nutzung des virtuellen Environments (.venv).
Aenderungen an HTML, CSS oder JS werden sofort automatisch im Browser aktualisiert.
"""

import os
import sys
import webbrowser
from pathlib import Path

# UTF-8 fuer Windows Konsole sicherstellen
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Sicherstellen, dass im Skript-Verzeichnis gearbeitet wird
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

PORT = 8000

try:
    from livereload import Server
    server = Server()
    
    # Dateien und Ordner zur automatischen Ueberwachung hinzufuegen
    server.watch(str(BASE_DIR / "*.html"))
    server.watch(str(BASE_DIR / "assets" / "css" / "*.css"))
    server.watch(str(BASE_DIR / "assets" / "js" / "*.js"))
    server.watch(str(BASE_DIR / "assets" / "images" / "*.*"))

    url = f"http://127.0.0.1:{PORT}"
    print("=" * 65)
    print(">> Lokaler Entwicklungsserver aktiv!")
    print(f">> Adresse: {url}")
    print(">> Live-Reload ist aktiviert (Aenderungen aktualisieren sofort)")
    print(">> Zum Beenden: Druecke Strg + C im Terminal")
    print("=" * 65)

    # Browser automatisch oeffnen
    try:
        webbrowser.open(url)
    except Exception:
        pass

    # Server starten
    server.serve(port=PORT, host="127.0.0.1")

except ImportError:
    import http.server
    import socketserver
    
    print("=" * 65)
    print(">> Standard Python HTTP-Server gestartet.")
    print(f">> Adresse: http://127.0.0.1:{PORT}")
    print("=" * 65)

    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        try:
            webbrowser.open(f"http://127.0.0.1:{PORT}")
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer beendet.")
