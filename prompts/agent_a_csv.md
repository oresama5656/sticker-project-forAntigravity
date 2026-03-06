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
  - テーマごとに個別のCSVファイルを生成すること。出力ファイル名は `outputs/prompts/[テーマ名]_prompts.csv` とし、必ず `outputs/prompts/` フォルダに出力すること。
  - スクリプト冒頭で `os.makedirs('outputs/prompts', exist_ok=True)` を実行し、ディレクトリが存在することを確認すること。
  - ファイルは必ず `encoding='utf-8-sig'`（BOM付きUTF-8）で開くこと。これによりExcelでの日本語文字化けを防ぐ。
  - 書き込みには必ず Python 標準ライブラリの `csv.writer` を使用すること。これによりダブルクォーテーションのエスケープやセル分割の問題を完全に回避する。
  - 各セット（P1〜P9）はPythonのリスト内の1つの文字列として定義し、`writer.writerow([row])` で1行ずつ書き出すこと。

Data_Format_Rules:
  - CSVの1行目（A1セル）には、必ず列のタイトルとして `prompt` とだけ記述して出力すること。
  - 9個のプロンプト（P1〜P9）を1セットとし、P1からP9までを半角スペース区切りで1つの文字列に繋げること。
  - 各プロンプトの形式: P番号: ACTION/PROPS="英語の動作・小道具" | TEXT="短い日本語"
  - セット内のダブルクォーテーションはPythonの文字列内でバックスラッシュエスケープ (\") を使い、csv.writerに正しいクォート処理を任せること。
  - 各CSVファイルは、タイトル行を含めファイル全体で合計7行（タイトル1行 ＋ データ6セット）になるようにすること。
  - ユーザーへの前後の挨拶や解説は一切不要。速やかにスクリプト作成と実行のみを行うこと。

# Output_Example (gen_csv.py のコード構造例)
```python
import os
import csv

os.makedirs('outputs/prompts', exist_ok=True)

def generate_theme_csv(theme_name, data_rows):
    """テーマごとにCSVファイルを生成する関数"""
    filename = f'outputs/prompts/{theme_name}_prompts.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prompt'])
        for row in data_rows:
            writer.writerow([row])

# --- テーマ1 ---
theme1_data = [
    'P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."',
    # ... 合計6つの文字列
]
generate_theme_csv('テーマ名1', theme1_data)

# --- テーマ2 ---
theme2_data = [
    'P1: ACTION/PROPS="..." | TEXT="..." ... P9: ACTION/PROPS="..." | TEXT="..."',
    # ... 合計6つの文字列
]
generate_theme_csv('テーマ名2', theme2_data)

# ... 全テーマ分を同様に繰り返す
```
