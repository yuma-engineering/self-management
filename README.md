# self-management
自己管理用のアプリです。todolistの応用として作りました。まだreactが学習中のため途中です。申し訳ありません。もともとはhtmlで表示していましたが、これからreactに置き換えて行きたいと思ってます。

#使用技術
Python
HTML
CSS
JavaScript
React

#ファイル構成（重要な部分のみ）
self-management/
├──backend/
│    └──__init__.py
│    └──forms.py
│    └──home.py
│    └──login.py
│    └──models.py
│    └──result.py
     ├──templates/
     └──各種.html
     
├──frontend/
│      └──App.tsx
       └──Login.tsx（reactは追加予定）


#機能
1.ユーザーのログイン、登録機能（数字、特殊文字含めないと登録できない）
2.ユーザーの今日の目標時間の設定
3.ユーザーが今日行ったタスクと時間の記録
4.2と3の比較でコメントを出す

#工夫した点
ユーザーのログイン機能で数字や特殊文字を使うサイトなどがあったので真似してみました。
目標を設定し自分の現在の合計時間と比較することで、習慣化しやすいだろうと思って作りました。
コードでわからない部分はgoogleやchatgptなどから情報を集めました。そしてそのコードの意味をchatgptに聞くなどして少しでも学習効果を上げようとしました。
