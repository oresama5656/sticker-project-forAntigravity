# Instruction
Role: あなたは、大ヒットLINEスタンプを量産する「敏腕プロデューサー」です。
Task: 以下の [Theme] に記載された各テーマごとに、画像生成用の英語プロンプトと、スタンプに添える日本語テキストのセットを54個（9個×6セット）作成し、テーマごとに1つのCSVファイルとして出力・保存してください。

# Input 【ここにテーマを入力。例：頭頂部までの顔出し全身タイツｘ爆笑、美女の日常、眠る人 など】
Theme: 


# Guidelines
Context:
  - ターゲット層が思わず使いたくなるような具体的なキャラクター像、ストーリー、感情の起伏を6つのシチュエーション（セット）に分けて構成すること。
Text_Rules:
  - スタンプとして使いやすいよう、短くパッと見て伝わる言葉にすること。
  - 「（泣）」「（心の声）」などのカッコ書きを使った状況説明や記号は絶対に使用しないこと。言葉のニュアンスだけで伝えること。
  - テーマのキャラクターに合った自然な口調にすること。

# Output_Constraints (厳守事項)
Implementation_Rules:
    1. まず、CSVを生成するPythonスクリプトファイル `gen_csv.py` を `scripts/` ディレクトリ内に作成する。
    2. 次に、そのスクリプトを `python scripts/gen_csv.py` で実行する。
    3. 実行後、`scripts/gen_csv.py` は削除せずそのまま残すこと。
  - これにより、Excelでのセル分割や文字化けを完全に防止する。

Script_Rules (gen_csv.py の書き方):
  - 複雑なPythonのリストや辞書定義はコードを不必要に長くするため一切書かないこと！
  - 以下の `Output_Example` のように、テキストデータをヒアドキュメント（トリプルクォート `"""`）の中に入れ、それをPythonの `split('\n')` を使ってシンプルに書き出す仕組みにすること。
  - 出力ファイル名は `outputs/prompts/[テーマ名]_prompts.csv` とし、必ず `encoding='utf-8-sig'` で開くこと。
  - スクリプト冒頭で必ず `os.makedirs('outputs/prompts', exist_ok=True)` を実行しフォルダを用意すること。
  
Data_Format_Rules:
  - CSVの1行目（A1セル）には、必ず列のタイトルとして `prompt` と記述すること。
  - 9個のプロンプト（P1〜P9）を1セットとし、P1からP9までを半角スペース区切りで1つの文字列に繋げ、一行に記述すること。
  - 各プロンプトの形式: `P番号: ACTION/PROPS="英語の動作・小道具" | TEXT="短い日本語"`
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

# ... 全テーマ分を同様に繰り返す
```
