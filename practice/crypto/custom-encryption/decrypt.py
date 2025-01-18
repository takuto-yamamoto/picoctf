def decrypt(cipher_list):
    KEY = "trudeau"
    semi_cipher = []

    for num in cipher_list:
        semi_cipher_code = num // 14617
        semi_cipher.append(chr(semi_cipher_code))

    reversed_plain = ""
    for i, ch in enumerate(semi_cipher):
        key_char = KEY[i % 7]
        reversed_plain += chr(ord(ch) ^ ord(key_char))

    plain_text = reversed_plain[::-1]

    return plain_text


cipher = [
    131553,
    993956,
    964722,
    1359381,
    43851,
    1169360,
    950105,
    321574,
    1081658,
    613914,
    0,
    1213211,
    306957,
    73085,
    993956,
    0,
    321574,
    1257062,
    14617,
    906254,
    350808,
    394659,
    87702,
    87702,
    248489,
    87702,
    380042,
    745467,
    467744,
    716233,
    380042,
    102319,
    175404,
    248489,
]
plain_text = decrypt(cipher)
print("Decrypted text:", plain_text)
