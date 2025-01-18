# Misc/General

## Easy

- Binary Search
  - 二分探索すれば OK
  - 10 回以内に 1000 までの数字を当てる(2^10>1000 なので可能)
- Time Machine
  - git log にフラグ
- Super SSH
  - 与えられた情報で SSH すれば OK
- endiannes
  - 与えられた文字列を ascii に変換し入力すればビッグエンディアン
  - バイトごとに逆順に入力すればリトルエンディアン
- Commitment Issues
  - コミットログ遡ればフラグ
- Collaborative Development
  - ブランチを巡ってフラグ集める
- Blame Game
  - `git log | grep picoCTF{`
- binhexa
  - バイナリ演算(`<<`, `>>`, `&`, `|`, `+`, `*`)
  - `<<`は 8 桁から 9 桁、`+`と`*`は一旦 decimal に戻して計算
  - Cyberchef の Base 操作で 10 進数から他の進数に変換できる

## Medium

- dont you love banners
  - 提供された別のサーバに SSH パスワード
  - いくつか一般的な質問されるので回答(DEFCON -> JOHN)
  - サーバ接続時に banner というファイルを読み込んでいる
  - フラグは/root/flag.txt
  - script.py は書き換えられないので、banner から flag.txt にシンボリックリンク
  - script.py の実行権限は root なので flag.txt を閲覧可能
- SansAlpha
  - 激ムズ...
  - 現在のディレクトリで`./*`とすると`blarge`ディレクトリを発見できる
  - `./*/*`とすると`flag.txt`を発見できる
  - 実行権限はないので読み取りを目指す
  - リダイレクト`<./??????/????.???`は効かない
  - /bin や/sbin 配下のコマンドをなんとか指定できないか
  - `/???/??????`のように?を増やしていくと base32 に辿り着く
  - 一応 x86*84 と競合するので`[!*]`で回避
- useless
  - エラー時の`read the manual`から`man useless`
- Specialer
  - タブフル活用で使えるコマンドとファイルを特定
  - mapfile を使って`mapfile var < ./ala/kazam.txt`で OK
- Special
  - `./*/*` で`./blargh/flag.txt`を発見
  - 絶対パス NG だったので相対パスで`../../bin/???[!_]64`で base64 呼び出し(cat とかも普通に使えたかも)
- Permissions
  - 活用できそうなものはないので root 権限が必要そう
  - `sudo -l`で`/usr/bin/vi`が全てのファイルに対して sudo できることがわかる
- chrono
  - `How to automate tasks to run at intervals on linux servers?` -> cron
  - システム全体の cron の設定は`/etc/crontab`（現在のユーザーにおけるせっては`crontab -l`）
