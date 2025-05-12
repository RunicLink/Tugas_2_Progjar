import socket
import threading
from datetime import datetime

def handle_client(conn, addr):
    print(f"Koneksi dari {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode('utf-8')
            print(f"Dari {addr}: {repr(message)}")

            # Cek QUIT
            if message.strip() == "QUIT":
                break

            # Cek format TIME
            if message.startswith("TIME") and message.endswith("\r\n"):
                now = datetime.now()
                waktu = now.strftime("%H:%M:%S")
                response = f"JAM {waktu}\r\n"
                conn.sendall(response.encode('utf-8'))
            else:
                conn.sendall(b"Format salah\r\n")

    print(f"Koneksi ditutup: {addr}")

def main():
    host = '0.0.0.0'
    port = 45000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Time server aktif di port {port}...")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    main()
