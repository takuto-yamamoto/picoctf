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

## Medium

- Blast from the past
  - exiftool で書き換えていく
  - samsun の timestamp は writable=no なのでバイナリエディタで書き換える
    - https://exiftool.org/TagNames/Samsung.html
  - バイナリエディタで末尾のデータを 000000000001 に書き換える
- MobPsycho
  - apk ファイルを unzip して`find . -type f | grep flag`で flag.txt を発見
  - unzip するだけだとほとんどのファイルはバイナリのまま
  - `find . -type f -exec strings {} + | grep picoCTF`とかもありかも
- Endianness
  - 先頭のバイトを見ると`e0 ff d8 ff`であるが、JPEG のマジックナンバーである`ff d8 ff e0`の反転っぽい
  - 4 バイトごとに反転させれば OK
- Dear Diary
  - 激ムズ...
  - fls を駆使して`innocuous-file.txt`と`its-all-in-the-name`というファイルを発見
  - ディスクイメージをバイナリで開き`innocuous-file.txt`を検索すると近くにフラグの断片
- pcap poisoning
  - 検索 -> packet bytes + string -> `pico`
- MSB
  - MSB=Most Significant Bit のこと
  - ステガノグラフィは、人間の目からは変化に気づきにくい LSB(Least Significant Bit)に情報を埋め込むのが一般的
  - 今回のケースは MSB に埋め込まれているため画像のノイズが実際に気づくレベルになっている
  - 青空白猫 or GPT に Python スクリプト書いてもらって MSB を抽出してテキスト化 -> `grep -oE 'pico\{.*\}'`
- hideme
  - strings したら`secret/flag.png`の文字列 -> ファイル構造が含まれている？
  - binwalk したら zip ファイルが隠れてた
  - 抽出したらフラグが書かれた png
- FindAndOpen
  - キャプチャ調べてたら怪しげなデータを発見 -> base64 デコードしてパスワードゲット
  - zip をパスワードで開いたらフラグ平文
