# Instruction
Role: あなたは、LINEクリエイターズマーケットの「スタンプ販売戦略のプロ」です。
Task: プロジェクトの `outputs/prompts/` フォルダ内に保存されているすべてのCSVファイル（スタンプ画像用プロンプトデータ）を読み込み、それぞれのテーマに合わせた「パッケージ用タイトルと説明文」を作成し、CSVファイルとして出力・保存してください。

# Mission Start
- 作業を開始する前に、まずワークスペース内の `outputs/prompts/` フォルダを調べ、どのようなCSVファイルが存在するか（ファイル名や中身）を確認してください。
- 確認したCSVファイルの数と同じ行数（ヘッダー行を除く）のパッケージ情報を作成してください。例えば10個のCSVがあれば、10個の独立したテーマとしてタイトルと説明文を考案します。

# Guidelines
Context:
  - そのテーマのスタンプセット全体を代表するような、キャッチーな内容にすること。

Text_Rules:
  - 言語: 日本語と英語の両方を作成すること。
  - 文字数制限（LINE公式仕様）:
    * タイトル: 40文字以内
    * 説明文: 160文字以内
  - カテゴリ選択: 各テーマに最も適したカテゴリを、以下の選択肢から **必ず1つだけ** 選ぶこと。選択肢にない値は絶対に使わないこと。
    * taste_category（以下から1つ）: 未設定, カワイイ・キュート, ラブリー, カッコいい, ほんわか・癒し, 方言・スラング, シュール, 面白い・ネタ, 挨拶, 敬語・丁寧, 季節・行事, 吹き出し
    * character_category（以下から1つ）: 未設定, 男性キャラ, 女性キャラ, 家族・カップル, ネコ, ウサギ, イヌ, クマ, トリ, パンダ, アザラシ, 食べ物, 名前・名字, その他

# Output_Constraints (厳守事項)
Implementation_Rules:
    1. まず、パッケージ情報を生成するPythonスクリプトファイル `gen_package_csv.py` を `scripts/` ディレクトリ内に作成する。
    2. 考案したタイトルや説明文などのテキストデータは、すべてPythonスクリプト内のリスト（配列）にハードコードし、それをスクリプトが書き出す形式にすること。
    3. 次に、そのスクリプトを `python scripts/gen_package_csv.py` で実行する。
    4. 実行後、`scripts/gen_package_csv.py` は削除せずそのまま残すこと。

Script_Rules (gen_package_csv.py の書き方):
  - 出力ファイル名は `outputs/package_info.csv` とし、必ず `outputs/` フォルダに出力すること。
  - ファイルは必ず `encoding='utf-8-sig'`（BOM付きUTF-8）で開くこと。これによりExcelでの日本語文字化けを防ぐ。
  - 書き込みには必ず Python 標準ライブラリの `csv.writer` を使用すること。カンマ区切り（デフォルト）で書き出すこと（TSVやタブ区切りは禁止）。

Data_Format_Rules:
  - 必ずヘッダー行を含めて出力すること。
  - 列の順序（厳守）: No, theme, title_en, desc_en, title_ja, desc_ja, copy_right, ai_flag, taste_category, character_category, zip_path
  - 各テーマにつき1行ずつのみ出力すること。
  - 固定値の列:
    * copy_right: ©ryo
    * ai_flag: TRUE
  - zip_path列: 空欄（空文字）のまま出力すること。
  - No列: 1からの連番を入れること。
  - theme列: 読み込んだCSVファイルごとのテーマ名を記入すること。
  - ユーザーへの前後の挨拶や解説は一切不要。速やかにスクリプト作成と実行のみを行うこと。

# Output_Example (gen_package_csv.py のコード構造例)
```python
import csv

rows = [
    # ヘッダー行
    ['No', 'theme', 'title_en', 'desc_en', 'title_ja', 'desc_ja', 'copy_right', 'ai_flag', 'taste_category', 'character_category', 'zip_path'],
    
    # 考案したデータ（CSVの個数分作成する）
    ['1', '和服美人の日常', 'English Title...', 'English Desc...', '日本語タイトル...', '日本語説明文...', '©ryo', 'TRUE', 'ほんわか・癒し', '女性キャラ', ''],
    # ... CSVの数だけ行を追加
]

with open('outputs/package_info.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
```
