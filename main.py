"""Serve the portfolio locally: `uv run main.py` (opens your browser automatically)."""
import functools
import http.server
import webbrowser
from pathlib import Path


def main():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=Path(__file__).parent)
    # Try 8000, then the next few ports if one is already in use
    for port in range(8000, 8011):
        try:
            httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
            break
        except OSError:
            continue
    else:
        raise SystemExit("Ports 8000-8010 are all busy; close another server and retry.")

    url = f"http://localhost:{port}"
    print(f"Portfolio running at {url}  (Ctrl+C to stop)")
    webbrowser.open(url)
    with httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()
