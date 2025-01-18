# web

## Easy

### Scavenger Hunt

https://play.picoctf.org/practice/challenge/161

- 成功したファイル
  - robots.txt: クローリングの許可/禁止設定を記載したファイル
  - .htaccess: apache のディレクトリアクセス設定を上書きするファイル
  - .DS_Store: MacOS のディレクトリメタデータファイル
- 失敗したファイル
  - .htpasswd: apache の Basic 認証パスワードファイル
  - /etc/passwd: linux システムのユーザーアカウント情報
  - /proc/self/environ: 現在実行中のプロセスの環境変数

### Get aHEAD

https://play.picoctf.org/practice/challenge/132

- HEAD メソッドのレスポンスにフラグあり
- HEAD メソッドは指定したリソースのメタデータのみを返却(ボディなしのため軽量)

## Medium

### Trickstar

https://play.picoctf.org/practice/challenge/445

- robots.txt を見ると`instruction.txt`と`upload/`がある
- instruction.txt によると、ファイルの最初の数バイトに`PNG`があれば png ファイルという判定
