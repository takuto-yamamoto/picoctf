import socket

HOST = "titan.picoctf.net"
PORT = 52781


def recv_until(sock, target: bytes, buffer_size: int = 1024) -> bytes:
    """
    ソケットから特定の文字列が現れるまでデータを受信する。
    """
    data = b""
    while target not in data:
        part = sock.recv(buffer_size)
        if not part:
            raise ConnectionError("Connection closed by the server.")
        data += part
    return data


with open("password.enc") as file:
    c = int(file.read())

with socket.create_connection((HOST, PORT)) as s:
    data = recv_until(s, b"decrypt.")
    print(data.decode())

    s.sendall(b"E\n")
    data = recv_until(s, b"keysize): ")
    print(data.decode())

    s.sendall(b"\x02\n")
    data = recv_until(s, b"mod n) ")
    c_a = int(data.decode().strip())
    print(f"Encrypted 2 (c_a): {c_a}")

    s.sendall(b"D\n")
    data = recv_until(s, b"decrypt: ")
    print(data.decode())

    s.sendall(str(c_a * c).encode() + b"\n")
    data = recv_until(s, b"mod n): ")
    password_num = int(data.decode().strip(), 16) // 2
    print(f"Decrypted password (num): {password_num}")

    password = password_num.to_bytes(len(str(password_num))).decode("utf-8")
    print("Password:", password)
