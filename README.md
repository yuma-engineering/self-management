# self-management
自己管理用のアプリです。todolistの応用として作りました。まだreactが学習中で途中です。申し訳ありません。

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
       └──Login.tsx


#機能
1.ユーザーのログイン、登録機能（数字、特殊文字含めないと登録できない）
2.ユーザーの今日の目標時間の設定
3.ユーザーが今日行ったタスクと時間の記録
4.2と3の比較でコメントを出す

