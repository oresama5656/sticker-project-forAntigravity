import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def get_themes_from_csv(csv_path):
    """
    CSVファイルを読み込み、テーマ名のリストを返す関数。
    'theme' 列がある場合はその列の重複しない値を取得し、
    無い場合はファイル名（_prompts.csv等を除外したもの）をテーマとする。
    """
    themes = set()
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            
            if not header:
                return []

            # BOMを取り除くなどのクリーンアップ
            header = [h.lstrip('\ufeff').strip() for h in header]

            if 'theme' in header:
                theme_idx = header.index('theme')
                for row in reader:
                    # 行が短すぎる場合や空の場合はスキップ
                    if len(row) > theme_idx and row[theme_idx].strip():
                        themes.add(row[theme_idx].strip())
            else:
                # 'theme' 列がない場合はファイル名をテーマ名として利用
                filename = os.path.basename(csv_path)
                filename_without_ext = os.path.splitext(filename)[0]
                # '_prompts' などのサフィックスがあれば除去
                theme_name = filename_without_ext.replace('_prompts', '')
                themes.add(theme_name)
    except Exception as e:
        print(f"Error reading CSV {csv_path}: {e}")
        
    return list(themes)

def create_folders(themes, base_dir):
    """
    指定されたディレクトリ配下に、テーマ名のフォルダを一括作成する関数。
    """
    created_count = 0
    for theme in themes:
        # フォルダ名として使用できない文字を削除・置換 (Windowsの制限考慮)
        safe_theme = "".join([c for c in theme if c not in r'\/:*?"<>|'])
        folder_path = os.path.join(base_dir, safe_theme)
        
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
                print(f"作成成功: {folder_path}")
                created_count += 1
            except Exception as e:
                print(f"作成失敗 ({folder_path}): {e}")
        else:
            print(f"既存フォルダのためスキップ: {folder_path}")
            
    return created_count

def main(parent=None):
    """
    GUIを使用してCSVファイルを選択し、フォルダ作成を実行する。
    parent: 呼び出し元のTkinterウィンドウ（指定がない場合は自身で非表示の一時ウィンドウを生成）
    """
    make_root = False
    if parent is None:
        parent = tk.Tk()
        parent.withdraw()
        make_root = True

    messagebox.showinfo("案内", "テーマを読み取るCSVファイルを選択してください。\n（例: all_prompts.csv や 〇〇_prompts.csv）", parent=parent)
    
    csv_file_path = filedialog.askopenfilename(
        parent=parent,
        title="CSVファイルを選択",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )

    if not csv_file_path:
        print("ファイル選択がキャンセルされました。")
        if make_root:
            parent.destroy()
        return

    # 今回のプロジェクト構成上、'outputs/images' などを保存先にする設定例
    # 必要に応じて保存先を変更可能
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "outputs", "images")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"対象CSV: {csv_file_path}")
    
    # テーマ名の抽出
    themes = get_themes_from_csv(csv_file_path)
    
    if not themes:
        messagebox.showwarning("警告", "CSVからテーマを取得できませんでした。", parent=parent)
        if make_root:
            parent.destroy()
        return

    # フォルダの作成
    created = create_folders(themes, output_dir)
    
    # 結果表示
    result_msg = (f"{len(themes)} 個のテーマを検出しました。\n\n"
                  f"新規作成したフォルダ数: {created} 個\n"
                  f"保存先:\n{output_dir}")
    messagebox.showinfo("作成完了", result_msg, parent=parent)

    if make_root:
        parent.destroy()

if __name__ == "__main__":
    main()
