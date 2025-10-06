# test_client_verbose.py
import socket
import time

HOST = "127.0.0.1"
PORT = 2222
MSG = b"hello_from_test_client\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5.0)
try:
    print(f"Connecting to {HOST}:{PORT}...")
    s.connect((HOST, PORT))
    print("Connected. Sending data...")
    s.sendall(MSG)
    time.sleep(0.2)
    s.settimeout(3.0)
    parts = []
    try:
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            parts.append(chunk)
    except socket.timeout:
        # expected when no more data
        pass
    if parts:
        print("Reply from server:", b"".join(parts).decode(errors="ignore").strip())
    else:
        print("No reply received from server.")
except ConnectionRefusedError:
    print("Connection failed: Connection refused (is the honeypot running?)")
except Exception as e:
    print("Connection failed:", repr(e))
finally:
    s.close()
    print("Client socket closed.")
