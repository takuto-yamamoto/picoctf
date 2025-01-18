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

### NoSQL Injection

https://play.picoctf.org/practice/challenge/443

```js
const user = await User.findOne({
  email:
    email.startsWith('{') && email.endsWith('}') ? JSON.parse(email) : email,
  password:
    password.startsWith('{') && password.endsWith('}')
      ? JSON.parse(password)
      : password,
});
```

- 上記コードで email/password がサニタイズされないことが確認できる
- MongoDB において`"{ \"$ne\": null }"`とすることで、null でなければ OK 条件を作成できる
- 返却値の token を base64 デコードして flag を取得

### SOAP

https://play.picoctf.org/practice/challenge/376

- `/etc/passwd`をなんとか確認する問題
- 一般的な XXE 攻撃

### More SQLi

https://play.picoctf.org/practice/challenge/358

- SQL インジェクション問題
- ご丁寧にも構文を返してくれる
  - `SELECT id FROM users WHERE password = 'password' AND username = 'username'`
- password に`' OR '1'='1' LIMIT 1--`を入れれば OK

### Match The Regex

https://play.picoctf.org/practice/challenge/356

- easy 過ぎたため特になし

### Java Code Analysis!?!

https://play.picoctf.org/practice/challenge/355

- https://jwt.io/ で jwt トークンを確認する
- payload と秘密鍵があれば良さそう
  - payload
    - role を Admin にするだけだとだめ
    - email を admin, userId を 2 に変更 (初期ユーザーコード参照)
  - 秘密鍵
    - SecretGenerator.java を見ると`return "1234";`してるだけの箇所あり
    - ソースコードのコメントアウト検索するのアリかも
- `base/books/pdf/5`に作成した jwt ででアクセスして flag ゲット
