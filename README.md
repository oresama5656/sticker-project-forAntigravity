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
│       ├── *.csv                   # 未統合のプロンプトCSV
│       └── merged/                 # 統合済みCSV（自動移動先）
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

- `outputs/prompts/` にある未統合CSVを `outputs/all_prompts.csv` に**追記**
- 各行に **theme列**（元のファイル名）が付与される
- 統合済みCSVは `outputs/prompts/merged/` に自動移動
- 既存の `all_prompts.csv` のデータ（done列含む）はそのまま保持

## 出力ファイルの分離ルール

| ファイル | 保存先 | 用途 |
|---|---|---|
| テーマ別プロンプトCSV（未統合） | `outputs/prompts/` | 画像生成AIへの入力 |
| テーマ別プロンプトCSV（統合済） | `outputs/prompts/merged/` | バックアップ |
| 統合プロンプトCSV | `outputs/all_prompts.csv` | 全テーマ一括処理用 |
| パッケージ情報CSV | `outputs/package_info.csv` | LINE登録用メタデータ |

## 統合の仕組み

```
outputs/prompts/
  ├── 新テーマA_prompts.csv    ← 未統合（次回 merge で取り込まれる）
  └── merged/
        ├── テーマ1_prompts.csv  ← 統合済み（もう取り込まれない）
        └── テーマ2_prompts.csv

outputs/all_prompts.csv
  theme          | prompt              | done
  テーマ1        | P1: ACTION/PROPS... |  1    ← 処理済み（保持される）
  テーマ2        | P1: ACTION/PROPS... |       ← 未処理
  新テーマA      | P1: ACTION/PROPS... |       ← 次回統合時に追加
```
