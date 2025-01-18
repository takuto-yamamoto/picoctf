# asciiorder
# fortychars
# selfinput
# pythontwo
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
cipher_path = os.path.join(current_dir, "ciphertext2")

with open(cipher_path) as f:
    ciphertext = f.read()

b = 1

for i in range(len(ciphertext)):
    if i == b * b * b:
        print(ciphertext[i])
        b += 1
