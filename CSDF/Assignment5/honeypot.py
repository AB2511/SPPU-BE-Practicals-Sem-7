# honeypot.py
import socket
import datetime
import sys

HOST = "0.0.0.0"   # or "127.0.0.1" for local-only testing
PORT = 2222
LOG_FILE = "honeypot_log.txt"


def log_event(message):
    """Log connection attempts to a file with timestamp and print to console."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    # append and flush
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(line + "\n")
    print(line)


def start_honeypot():
    """Start a simple honeypot TCP server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        log_event(f"Honeypot started on port {PORT} (bind={HOST})")
        try:
            while True:
                client_socket, client_addr = server_socket.accept()
                ip, port = client_addr
                log_event(f"Connection attempt from {ip}:{port}")
                try:
                    data = client_socket.recv(4096).decode(errors="ignore")
                    if data:
                        log_event(f"Data from {ip}: {data.strip()}")
                    # respond with a polite denial
                    client_socket.sendall(b"Access Denied. This activity is logged.\n")
                except Exception as e:
                    log_event(f"Error communicating with {ip}: {e}")
                finally:
                    client_socket.close()
        except KeyboardInterrupt:
            log_event("Honeypot stopped by KeyboardInterrupt")
            print("\n[!] Honeypot stopped by user.")
        except Exception as e:
            log_event(f"Honeypot fatal error: {e}")
            raise


if __name__ == "__main__":
    start_honeypot()
