# 使えそうなツール/アプリ

## Web

- burp suite
  - http プロキシ
- netcat
  - `nc [hostname] [port]`
    - 指定したホストとポートとの TCP 接続を開く
    - ヒアドキュメントやファイルを入力(`<<`や`<`)すれば HTTP リクエストやファイルの受け渡しが可能
  - `nc -l [port]`
    - 指定したポートでリッスン
- nmap
  - ポートスキャナ
- python
  - サーバ側の実装やスクリプトの作成に多用される
- curl
  - url リクエストツール
- SQLi チートシート類
  - [PortSwigger](https://portswigger.net/web-security/sql-injection/cheat-sheet)
  - [invicti](https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/)
  - HackTricks
- jwt 系
  - https://jwt.io
    - jwt のエンコード/デコード
  - https://github.com/ticarpi/jwt_tool
    - jwt の改ざんや既知の攻撃
- php
  - サーバサイドレンダリングを実現する言語
  - サーバ側で system コマンド実行 -> html 内に結果を埋め込んで表示
- robots.txt
  - サーバのファイル構成がわかる場合もある
  - instructions.txt とかある場合も

## Crypto

- quipquip
  - 単一換字暗号の自動解析(間違えることあり)
- https://gchq.github.io/CyberChef/
  - 暗号解読からハッシュ、バイナリ操作まで何でもできる
  - QR や Exif にも対応
- 難解プログラミング言語(esolang)
  - brainfuck
    - 難解プログラミング言語(esolang)
    - `<>+-.,[]`の 8 文字でポインタを操作しながら実装する
  - whitespace
    - ` `, `\t`, `\n`のみで構成される言語
    - https://vii5ard.github.io/whitespace/で実行可能
  - piet
    - ドットでコーディングする(抽象画みたいになる)
  - lazy k
    - S, K と()だけで実装される関数型言語(ショートカットとして I も登場する)
  - JSFuck
    - `!+()[]`のみで動く難読化 JS
  - jjendoce/decode
    - js の難読化とそのデコード
  - 意味不明なコードは実行 or`console.log`する
- bkcrack/pkcrack
  - zip ファイルの既知平文攻撃
  - bkcrack でうまくいかない場合に pkcrack する
  - `bkcrack -L encrypted.zip`で zip の中身メタデータチェック
- SageMath
  - Python 各種数学ライブラリを一括で扱える+一部独自機能
  - CTF 当日使えないかも
- hashcat
  - hash の総当たり
  - https://github.com/hashcat/hashcat
- python 組み込み関数
  - pow
    - pow(a, -1, n) で ax mod n = 1 となる x(モジュラ逆元)を計算する
    - pow(a, e, n)で a^e mod n の解を計算数 r
  - hashlib(ハッシュ関数)
  - Crypto.Cipher(暗号化)
- RSA 暗号系
  - http://www.factordb.com/index.php で素因数分解

## Reversing

- dnSpy
  - .NET デバッガ
- OllyDbg
  - C/C++デバッガ
- IDA
  - 汎用デバッガ

## pwnable

- pwntools
  - python の tcp 通信ライブラリ
  - 標準の socket でも同じことができるがちょっと面倒

## Forensics

- wireshark
  - パケットキャプチャ解析ツール
  - HTTP や TCP などでフィルタできる
- file
  - ファイルのメタデータやバイナリ情報確認
- strings
  - バイナリ中の文字列を調べるコメント
- sleuth kit
  - img ファイルの中身を操作するツール
  - `fls example.img`で構造確認
  - `icat example.img XX`で指定した inode 番号(エントリ番号)のファイルの内容を出力する
    - `icat drive.img 36-128-1 > extracted.jpg`

## チェックしておくツール

- John The Ripper
- bz
- stirling
- process monitor
- process explorer
- process hacker
- autoruns
- regshot
- steghide
- sonic visualizer
- image-exiftool
- ghidra
- Aperi'Solve
