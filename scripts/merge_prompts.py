"""
outputs/prompts/ 内のすべての *_prompts.csv を1つに統合するスクリプト。
統合ファイルは outputs/all_prompts.csv に出力される。
元のCSVファイルには一切変更を加えない。
"""
import csv
import os
import glob

PROMPTS_DIR = 'outputs/prompts'
OUTPUT_FILE = 'outputs/all_prompts.csv'

csv_files = sorted(glob.glob(os.path.join(PROMPTS_DIR, '*_prompts.csv')))

if not csv_files:
    print('統合対象のCSVファイルが見つかりませんでした。')
    exit()

all_rows = []

for filepath in csv_files:
    theme = os.path.basename(filepath).replace('_prompts.csv', '')
    with open(filepath, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None)  # ヘッダー行をスキップ
        for row in reader:
            if row:
                all_rows.append(row)
    print(f'  ✔ {theme} ({len(all_rows)}行)')

with open(OUTPUT_FILE, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['prompt'])
    for row in all_rows:
        writer.writerow(row)

print(f'\n統合完了: {OUTPUT_FILE} ({len(all_rows)}行)')
