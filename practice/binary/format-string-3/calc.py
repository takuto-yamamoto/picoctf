setvbuf_address = 0x730D3EE7D3F0
setvbuf_offset = 0x7A3F0
system_offset = 0x4F760


libc_base = setvbuf_address - setvbuf_offset
system_address = libc_base + system_offset

print(f"system address: {hex(system_address)}")
