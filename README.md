# Discord bot for floc

某コンテストの某プロジェクトで稼働しているDiscord botです。

## 機能・コマンド

### 自動ピン留め機能

- 指定されたチャンネルに投稿があったときに自動でメッセージをピン留め
  - ユーザごとにピン留め, 前のピン留めは解除され、常に最新の内容がピン留めされる
- 使い方
  - メッセージを送信すると、そのユーザの最新の投稿のみが自動でピン留めされる
  - `[タグ名]`からメッセージを始めると、タグをつけることができる
    - タグ付きメッセージでは、同じタグがつけられたメッセージがまとめられる

### リマインド機能

- 指定した日時に自動で通知
- 使い方
  - `(prefix)remind (日付) (時間) (対象) (通知内容)`
    - 例: `!remind 2019-5-16 16:20 everyone 進捗報告会`
  - 日付: %Y-%m-%d
  - 時間: %H:%M or %H:%M:%S
  - 対象: everyone / here / 役割名 / name#discriminator(例: oyakodon#6149)
    - 注意: @はつけないこと

### dicedice-dice

- サイコロを振る
- 使い方
  - `dicedice-dice`
  - ある数列になるとリアクションで祝ってくれる

### README

- `(prefix)help`でconfig['readme']の内容が表示される
  - デフォルトはこのMarkdownへのリンク

## 使用方法

1. このリポジトリをclone
2. `pip install -r requirements.txt`を実行
3. `config.json.example`を`config.json`としてコピー
4. `config.json`に必要事項を記入
5. `python bot.py`でBotを起動

## 環境

- Python 3.6.6
  - 追加ライブラリ的な
    - discord.py
- さくらのVPSで稼働
