"""
outputs/prompts/ 内の未統合 *_prompts.csv を all_prompts.csv に追記し、
統合済みCSVを outputs/prompts/merged/ に移動するスクリプト。

- theme列にファイル名由来のテーマ名を付与
- 既存の all_prompts.csv のデータ（done列含む）はそのまま保持
- 統合済みCSVは merged/ に移動するため、次回実行時に重複しない
"""
import csv
import os
import glob
import shutil

# --- 0. パスの設定 (スクリプトの場所を基準にする) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# scripts の親がプロジェクトルート
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

PROMPTS_DIR = os.path.join(PROJECT_ROOT, 'outputs', 'prompts')
MERGED_DIR = os.path.join(PROJECT_ROOT, 'outputs', 'prompts', 'merged')
OUTPUT_FILE = os.path.join(PROJECT_ROOT, 'outputs', 'all_prompts.csv')
HEADER = ['theme', 'prompt', 'done']

def run_merge():
    """
    CSV結合処理を実行し、結果メッセージを返す関数。
    """

    # --- 1. 未統合CSVを探す ---
    csv_files = sorted(glob.glob(os.path.join(PROMPTS_DIR, '*_prompts.csv')))

    if not csv_files:
        msg = '統合対象のCSVファイルが見つかりませんでした。\n（outputs/prompts/ に *_prompts.csv がありません）'
        print(msg)
        return False, msg

    # --- 2. 既存の all_prompts.csv を読み込む ---
    existing_rows = []
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if row and len(row) >= 2:
                    existing_rows.append(row)
        print(f'既存データ: {len(existing_rows)}行（保持）')

    # --- 3. 新規CSVを読み込み ---
    new_rows = []
    for filepath in csv_files:
        theme = os.path.basename(filepath).replace('_prompts.csv', '')
        with open(filepath, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # ヘッダーをスキップ
            count = 0
            for row in reader:
                if row:
                    new_rows.append([theme, row[0], ''])
                    count += 1
        print(f'  ★ {theme} → {count}行追加')

    # --- 4. all_prompts.csv に書き出す ---
    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)
        for row in existing_rows:
            writer.writerow(row)
        for row in new_rows:
            writer.writerow(row)

    # --- 5. 統合済みCSVを merged/ に移動 ---
    os.makedirs(MERGED_DIR, exist_ok=True)
    for filepath in csv_files:
        dest = os.path.join(MERGED_DIR, os.path.basename(filepath))
        shutil.move(filepath, dest)

    success_msg = (f'統合完了: {OUTPUT_FILE}\n'
                   f'既存 {len(existing_rows)}行 + 新規 {len(new_rows)}行 = 計 {len(existing_rows) + len(new_rows)}行\n'
                   f'統合済みCSVは {MERGED_DIR}/ に移動しました')
    
    print(success_msg)
    return True, success_msg

if __name__ == '__main__':
    run_merge()
