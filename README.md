# LINEスタンプ制作ワークフロー管理

LINEクリエイターズマーケット向けスタンプの、プロンプト生成からパッケージ情報管理までを一元管理するプロジェクトです。

## ディレクトリ構成

```
sticker-project/
├── prompts/                        # AIエージェント用プロンプト（指示書）
│   ├── agent_a_csv.md              # 画像生成プロンプトCSVを作成する指示書
│   └── agent_b_title.md            # パッケージ情報CSVを作成する指示書
├── scripts/                        # Python スクリプト群
│   ├── gen_csv.py                  # 単一テーマのプロンプトCSV生成
│   ├── gen_csv_5_themes.py         # 5テーマ分のプロンプトCSV一括生成
│   ├── gen_package_csv.py          # パッケージ情報CSV生成
│   └── merge_prompts.py            # プロンプトCSV統合スクリプト
├── outputs/                        # 出力ファイル
│   ├── package_info.csv            # パッケージ情報（タイトル・説明文）
│   ├── all_prompts.csv             # 統合プロンプト（merge_prompts.py で生成）
│   └── prompts/                    # テーマ別プロンプトCSV
│       ├── 和服美人ｘ猫ｘスタンダードあいさつ_prompts.csv
│       ├── 和服美人ｘ猫ｘ気遣いあいさつ_prompts.csv
│       ├── 和服美人ｘ猫ｘ敬語_prompts.csv
│       ├── 和服美人ｘ猫ｘ猫好き_prompts.csv
│       └── 和服美人ｘ猫ｘいつでも使える_prompts.csv
└── README.md
```

## 使い方

### 1. 画像生成用プロンプトCSVの作成

`prompts/agent_a_csv.md` の指示書をAIエージェントに渡し、テーマごとのプロンプトCSVを生成します。  
CSVは `outputs/prompts/` に保存されます。

### 2. パッケージ情報CSVの作成

`prompts/agent_b_title.md` の指示書をAIエージェントに渡し、各テーマのタイトル・説明文を生成します。  
CSVは `outputs/package_info.csv` に保存されます。

### 3. プロンプトCSVの統合（任意）

すべてのテーマのプロンプトを1ファイルにまとめたい時だけ実行します。

```bash
python scripts/merge_prompts.py
```

統合ファイルは `outputs/all_prompts.csv` に出力されます。  
元のテーマ別CSVには一切変更を加えません。

## 出力ファイルの分離ルール

| ファイル | 保存先 | 用途 |
|---|---|---|
| テーマ別プロンプトCSV | `outputs/prompts/` | 画像生成AIへの入力 |
| 統合プロンプトCSV | `outputs/all_prompts.csv` | 全テーマ一括処理用 |
| パッケージ情報CSV | `outputs/package_info.csv` | LINE登録用メタデータ |

> **Note:** `outputs/prompts/` と `outputs/` 直下を分離することで、プロンプトCSVの一括処理時に `package_info.csv` が巻き込まれることを防いでいます。
