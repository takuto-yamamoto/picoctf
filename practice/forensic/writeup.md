# forensic

## Easy

- verify
  - `find files -type f -print0 | xargs -0 -I {} sh -c './decrypt.sh "{}" || true' | grep 'picoCTF'` で一発
- Scan Surprise
  - QR 読み取り
- Secret of the Polyglot
  - pdf であり png
- Can You See
  - exiftool で base64 文字列取得しデコード
  - ステガノグラフィーもあるがダミー
- information
  - これも exiftool で base64 文字列取得しデコード
- Glory of the Garden
  - strings で取得
