import sys


def decrypt(cipher):
    lookup1 = '\n "#()*+/1:=[]abcdefghijklmnopqrstuvwxyz'  # length 40
    lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"  # length 40

    out = ""

    cur_sum = 0
    for char in cipher:
        cur = lookup2.index(char)
        cur_sum += cur
        out += lookup1[cur_sum % 40]

    print(out)


if __name__ == "__main__":
    cipher = sys.argv[1]

    decrypt(cipher)
