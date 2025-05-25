import socket

def main():
    host = '172.16.16.101'  
    port = 45000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Terhubung ke server. Ketik 'TIME' atau 'QUIT'")

        while True:
            pesan = input("Kirim: ").strip().upper()

            if pesan not in ['TIME', 'QUIT']:
                print("Pesan hanya boleh 'TIME' atau 'QUIT'")
                continue

            s.sendall((pesan + "\r\n").encode('utf-8'))
            data = s.recv(1024)
            print("Respon:", data.decode('utf-8').strip())

            if pesan == 'QUIT':
                print("Menutup koneksi...")
                break

if __name__ == "__main__":
    main()
