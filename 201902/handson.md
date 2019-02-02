# Webスクレイピング入門 - PyLadies Tokyoハンズオン

## 環境構築

本ハンズオンで使用するPythonライブラリをインストールします．  
以下のコマンドを実行して下さい．

```
pip install requests beautifulsoup4
```

## Webスクレイピングとは

Webスクレイピング（Web scraping）とは，Webページから必要なデータを抽出することです．  
よく混同されがちな言葉にクローリング（crawling）がありますが，クローリングはリンクを辿ってWebページを収集することで，スクレイピングは収集したWebページから必要な情報を抜き出すことを指します．（両者を区別せず使うことも多いです）

このハンズオンでは，最終的に「[PyLadies Tokyo](https://pyladiestokyo.github.io/)」のページから特定の情報を抜き出すことにチャレンジします．

## Webスクレイピングを行う上での注意点

Webスクレイピングは大変便利な技術ですが，スクレイピングしたデータの使用目的やスクレイピング方法によっては，情報公開元に迷惑をかけたり，場合によっては法に触れることもあります．  
以下のページを読んで，誰にも迷惑をかけないWebスクレイピングを心がけましょう．  
[Webスクレイピングの注意事項一覧](http://qiita.com/nezuq/items/c5e827e1827e7cb29011)

- APIが提供されている場合はそちらを利用する
- サイトの利用規約を確認する
- robots.txtを確認する
  - [Facebook - robots.txt](https://www.facebook.com/robots.txt)
  - [Github - robots.txt](https://github.com/robots.txt)
- Webサイトに負荷をかけないようにアクセスする

## Webスクレイピングの基本

スクレイピングを行う際の大まかな手順は以下の通りです．

1. スクレイピングを行いたいページを取得する
2. ページのDOMツリーを確認する
3. 欲しいデータを抽出する

ここでは例として，PyLadies Tokyoのサイトのトップページからハイパーリンクを抽出してみます。

### 1. スクレイピングを行いたいページを取得する

Webページの取得には，Pythonの `requests` というモジュールを利用します．早速使ってみましょう．  
新しくPythonスクリプトを作成し，以下の内容を実行してみましょう．

```python
import requests  # ①

res = requests.get('https://pyladiestokyo.github.io/')  # ②
print(res.content)  # ③
```

上記のコードでは，①まず `requests` モジュールをインポートしてきて，②インポートした `requests` モジュールを利用して `https://pyladiestokyo.github.io/` のサイトの内容を取得し，③取得した内容を確認しています．  
正しく実行された場合には，PyLadies TokyoのHPのHTMLが表示されているはずです．

さて，そもそもPyLadies TokyoのHPのHTMLとは何を指しているのでしょうか？実際に確認してみましょう．以下のサイトに訪問し，右クリック ->「ページのソースを表示」を選択して下さい．  
[PyLadies Tokyo 公式サイト](https://pyladiestokyo.github.io/)

WebページはHTMLという専門の言語を利用して記載されています．  
`requests`モジュールを利用することで，対象のページのHTMLを取得しています．  
取得したページを保存しておきましょう．

```python
import requests

res = requests.get('https://pyladiestokyo.github.io/')
with open('pyladies-top.html', 'wb') as fout:
    fout.write(res.content)
```

### 2. ページのDOMツリーを確認する

先ほど保存したHTMLファイルをGoogle Chromeで開いて，右上の三本線のメニューから「その他のツール」-->「デベロッパーツール」を選択して下さい．

![](chrome.png)

欲しい情報がどこにあるのか見ていきましょう．  
タグはどうなっているでしょうか？

### 3. 欲しいデータを抽出する

スクレイピング対象のHTMLの内容を確認したところで，実際に欲しいデータをスクレイピングする処理に移っていきます．HTMLを解釈して任意のデータを抽出するのには，Pythonの `bs4 (BeautifulSoup4)` というモジュールを利用します．  
新しくPythonスクリプトを作成し，以下の内容を実行してみましょう．

```python
from bs4 import BeautifulSoup  # ①

html = open('pyladies-top.html').read()  # ②
soup = BeautifulSoup(html, 'html.parser')  # ③
```

上記のコードでは，①まず `BeautifulSoup` クラスをインポートしてきて，②スクレイピング対象のHTMLを読み込み，③インポートした `BeautifulSoup` クラスを利用してHTMLの内容を解釈しています．

実際に欲しいデータ（＝ハイパーリンク）を取り出してみましょう．ページのDOMツリーを確認してみた感じでは，`a` タグで囲まれている部分を抽出すると良さそうです．特定のタグが含まれている部分を抽出するには，`find_all()`を利用します．  
以下の内容を追記して実行してみて下さい．

```python
records = soup.find_all('a')
for record in records:
    print(record)
```

`a`タグを全て抽出すると，画像まで出力されてしまうようです．画像を用いたハイパーリンクを無視したい場合にはどうしたら良いでしょうか？  
両者を見比べてみましょう．

```html
<a class="navbar-brand" href="/">
<img alt="" class="d-inline-block align-top mr-1" height="30" src="/image/pyladies-tokyo.png" width="30"/> PyLadies Tokyo
                </a>
<a class="nav-link" href="/index.html">Top <span class="sr-only">(current)</span></a>
...
<img alt="" class="d-inline-block align-top mr-1" height="30" src="image/connpass.png" width="30"/>connpass
            </a>
<a href="https://www.facebook.com/PyLadiesTokyo" target="_blank">
<img alt="" class="d-inline-block align-top mr-1" height="30" src="image/facebook.png" width="30"/>Facebook
            </a>
...
```

`a` タグ中には　`img` タグが含まれているようです。 `img` タグが含まれている場合は無視するといった処理を追記しましょう．

```python
records = soup.select('a')
for record in records:
    if record.img:
        continue
    print(record)
```

欲しい情報を取得することができました！  
`record`を`record.string`と書き換えることでタグの内容を除いたテキスト情報のみを取得出来ます。
`record[属性]` とすると、属性に指定された値を取得出来ます。
`文字列: URL` となるように表示してみましょう。

Python3.6以上
```python
print(f'{record.string}: {record["href"]}')
```

Python3.5以下
```python
print('{title}: {url}'.format(title=record.string, url=record["href"]))
```

取得した情報を保存したい場合には，例えば以下のように書き換えます．

```python
records = soup.select('a')
with open('pyladies-staff.csv', 'w') as fout:
    for record in records:
        if record.img:
            continue
        fout.write(f'{record.string},{record["href"]}\n')
```

## 課題

[PyLadies Locations](https://www.pyladies.com/locations/)のページを取得して、加盟PyLadiesの都市名、URL、TwitterIDを表示してみましょう。

特定のclassを持つタグを取得する場合は、以下のようにします。

```python
records = soup.find_all('div', class_="属性値")
```

※任意のサイトでも問題ありません．

## もっと詳しく知りたい人へ

いくつか書籍を紹介しておきます．

- [Pythonクローリング＆スクレイピング―データ収集・解析のための実践開発ガイド―](https://gihyo.jp/book/2017/978-4-7741-8367-1)
  - 加藤耕太　著
  - 2016年12月16日発売 B5変形判／400ページ
- [PythonによるWebスクレイピング](https://www.oreilly.co.jp/books/9784873117614/)
  - Ryan Mitchell　著，黒川 利明　訳，嶋田 健志　技術監修
  - 2016年03月 発行，272ページ
- [実践Webスクレイピング＆クローリング](https://book.mynavi.jp/ec/products/detail/id=41408)
  - nezuq　著，東京スクラッパー　監修
  - 2015年08月 発行，208ページ
- [Pythonエンジニア ファーストブック](https://gihyo.jp/book/2017/978-4-7741-9222-2)
  - 鈴木たかのり，清原弘貴，嶋田健志，池内孝啓，関根裕紀　著
  - 2017年9月9日発売 A5判／328ページ
