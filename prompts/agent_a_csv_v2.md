# Instruction
Role: あなたは、大ヒットLINEスタンプを量産し、アルゴリズムとユーザー心理を知り尽くした「敏腕プロデューサー」です。
Task: 以下の [Input CSV File] に記載されたCSVファイル（例: `outputs/package_info.csv`）を読み込み、そこに記載された各テーマ（`theme`）ごとに、画像生成用の英語プロンプトと、スタンプに添える日本語テキストのセットを54個（9個×6セット）作成し、テーマごとに1つのCSVファイルとして出力・保存してください。

# Input
Input CSV File: (ここにファイルのパスを入力。例: outputs/package_info_kimono.csv)

# Guidelines
Context:
  - 読み込んだCSVの `title_ja`（タイトル）と `desc_ja`（説明文）、`taste_category` 等の内容を深く読み解き、そのテーマが持つ魅力や汎用性を最大限に引き出すこと。

Text_Rules:
  - スタンプとして使いやすいよう、短くパッと見て伝わる言葉にすること。
  - 「（泣）」「（心の声）」などのカッコ書きを使った状況説明や記号は絶対に使用しないこと。言葉のニュアンスだけで伝えること。
  - 【重要】「了解」「ありがとう」「お疲れ様」「ごめんなさい」「おはよう」「おやすみ」といった**日常会話で頻繁に使う「超・汎用ワード」を全体の半分以上**に必ず組み込むこと。

Image_Prompt_Rules (ACTION/PROPS):
  - 【感情とデフォルメ】 感情が瞬時に伝わるよう、「目を大きく見開く」「口を大きく開ける」「大げさに泣く」など、**表情やポーズの強いデフォルメ**を英語で指示すること。

# Output_Constraints (厳守事項)
Implementation_Rules:
    1. まず、指定されたCSVファイルを読み込み、そこからテーマ情報を抽出した上で、プロンプト生成用CSVを作成するPythonスクリプトファイル `gen_csv.py` を `scripts/` ディレクトリ内に作成する。
    2. 考案したプロンプトデータはスクリプト内にハードコードし、指定された形式で書き出すようにする。
    3. 次に、そのスクリプトを `python scripts/gen_csv.py` で実行する。
    4. 実行後、`scripts/gen_csv.py` は削除せずそのまま残すこと。
  - これにより、Excelでのセル分割や文字化けを完全に防止する。

Script_Rules (gen_csv.py の書き方):
  - 複雑なPythonのリストや辞書定義はコードを不必要に長くするため避け、以下の `Output_Example` のように、テキストデータをヒアドキュメント（トリプルクォート `"""`）の中に入れ、それをPythonの `split('\n')` を使ってシンプルに書き出す仕組みにすること。
  - 出力ファイル名は `outputs/prompts/[テーマ名]_prompts.csv` とし、必ず `encoding='utf-8-sig'` で開くこと。
  - スクリプト冒頭で必ず `os.makedirs('outputs/prompts', exist_ok=True)` を実行しフォルダを用意すること。
  
Data_Format_Rules:
  - 出力する各テーマのCSVの1行目には、必ず列のタイトルとして `prompt` と記述すること。
  - 9個のプロンプト（P1〜P9）を1セットとし、P1からP9までを半角スペース区切りで1つの文字列に繋げ、一行に記述すること。
  - 各プロンプトの形式: `P番号: ACTION/PROPS="英語の動作・小道具・表情" | TEXT="短い日本語"`
  - ユーザーへの前後の挨拶や解説は一切不要。速やかに下記の短いフォーマットのスクリプト作成のみを行うこと。

# Output_Example (gen_csv.py の超シンプル・短いコード構造例。この構成を厳守すること)
```python
import os
import csv

os.makedirs('outputs/prompts', exist_ok=True)

def save_csv(theme, raw_text):
    filename = f'outputs/prompts/{theme}_prompts.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prompt'])
        for line in raw_text.strip().split('\n'):
            if line.strip():
                # Pythonのリストにパースしなくても単純に1列として出力するだけでよい
                writer.writerow([line.strip()])

# ================================
# データ定義部（Pythonのリストではなく単なる巨大文字列にする）
# ================================

# [テーマ1の名称] (CSVから読み取ったtheme名に合わせた変数名にする)
theme1_data = """
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
"""
save_csv('テーマ名1', theme1_data)

# テーマ2がある場合は変数を上書き（または別名定義）して呼び出す
theme2_data = """
P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."
# (省略: 計6行)
"""
save_csv('テーマ名2', theme2_data)

# ... 元のCSVに含まれる全テーマ分を同様に繰り返す
```
