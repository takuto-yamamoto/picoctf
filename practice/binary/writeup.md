# binary

## Easy

- heap 0
  - でかい値を入れてオーバーフローさせる
- format string 0
  - フォーマット演算子でフラグのメモリにアクセスする

## Medium

- format string 3
  - フォーマット演算子を使用して不正にメモリを漏洩させる
  - フォーマット演算子
    - `%s`は文字列, `%d`は 10 進数、`%x`は 16 進数, ...
    - `%p`はポインタアドレス、`%n`はポインタアドレスの書き換え
      - 今回は`printf(buf)`という箇所があるので、buf に`%n`を入れればアドレスを書き換えられる
  - setvbuf のアドレスがわかっているので、libc 内のオフセットから system 関数のアドレスを特定する
    - 相対位置が分かれば OK なので ASLR によるランダム化は無視できる
    - objdump すると setvbuf は`000000000007a3f0`、system は`000000000004f760`にあることがわかる
    - system の絶対アドレスは`0x730d3ee52760`（calc.py）
    - puts@GOT のアドレスは`0x404018`
  - ここまで分かればあとは書き換えるだけだがこれが難しい...(solve.py)
    - ペイロードがスタックのどこに配置されるかを特定する
    - ペイロードのスタックオフセットをもとに、ペイロードを構築する
  - シェルを取得し`cat flag.txt`
- format string 2
  - フォーマット演算子を使用して不正にメモリを書き換える問題
  - sus が特定の値になれば OK
  - sus はグローバル変数、、かつ返却値的には ASLR や PIE は無効化されていそうなので、コンパイル時点で sus のアドレスは決まる
  - objdump で実行ファイルから sus のアドレスを特定し、fmtstr_payload と FmtStr で書き換えてフラグゲット
- format string 1
  - フォーマット演算子を使用して不正にメモリを書き換える問題
  - スタック内に読み込まれた flag を取得すれば OK
  - %x 連打で picoCTF 取得可能
- heap1
  - 単純なヒープオーバーフローの問題
- heap2
  - `void check_win() { ((void (*)())*(int*)x)(); }`をみる限り x のアドレスを `win()`のアドレスにすればいい
  - objdump で win のアドレスを取得できたので、引き続きヒープオーバーフローで x を書き換える
    - pwntools の p64 でペイロードを構築
- heap3
  - free(x)があるが x=NULL のように再利用防止がなされていない -> UseAfterFree 攻撃
  - 構造体 x を解放し、x と同じサイズのメモリ(35)を割り当てると、x があった場所に割り当てられる可能性が高い
  - 30 の内訳が a~c10 ずつ、flag5 であることはコードからわかるので、メモリ割り当て時のデータ書き込みで`A*30+pico`を書き込めば x->flag に`pico`が入る
