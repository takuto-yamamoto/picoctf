# crypto

## easy

- interencdec
  - シーザー暗号と base64 の組み合わせ
- mod26
  - シーザー暗号(ROT13)
- the numbers
  - A1Z26 暗号(A=1, ..., Z=26)
- 13
  - シーザー暗号(ROT13)

## medium

### rsa oracle

https://play.picoctf.org/practice/challenge/422

- RSA 暗号の乗法準同型性を利用(ここら辺あまりよくわかってない)
- 2(バイト列なので CLI から直接入力できないことに注意)を暗号化し、パスワードとの積をとる
- パスワードとの積を復号する

### Custom encryption

https://play.picoctf.org/practice/challenge/412

- 値 a, b に基づいて暗号化アルゴリズムを埋めていく
- 逆順にアルゴリズムを書いていけば OK(xor は 2 回繰り返せば元通りになることに注意)

### C3

https://play.picoctf.org/practice/challenge/407

- アルゴリズムに則って複合アルゴリズムを書く
- 複合した結果が暗号文であり複合アルゴリズムの python ファイルにもなるので自分自身を複合
