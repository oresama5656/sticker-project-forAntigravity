import os
import csv
from data1 import themes as t1
from data2 import themes as t2
from data3 import themes as t3
from data4 import themes as t4

os.makedirs('outputs/prompts', exist_ok=True)

all_themes = t1 + t2 + t3 + t4

def generate_theme_csv(theme_name, data_rows):
    """テーマごとにCSVファイルを生成する関数"""
    filename = f'outputs/prompts/{theme_name}_prompts.csv'
    with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prompt'])
        for row in data_rows:
            writer.writerow([row])

for name, rows in all_themes:
    generate_theme_csv(name, rows)
