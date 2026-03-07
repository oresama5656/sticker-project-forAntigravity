import tkinter as tk
from tkinter import messagebox
import os
import sys

# scriptsフォルダにパスを通す（他モジュールインポートのため）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

# 各機能モジュールのインポート
try:
    import create_theme_folders
    import merge_prompts
except ImportError as e:
    # 起動前にメッセージボックスを出せるように一時的なrootを作る
    temp_root = tk.Tk()
    temp_root.withdraw()
    messagebox.showerror("インポートエラー", f"モジュールの読み込みに失敗しました:\n{e}", parent=temp_root)
    sys.exit(1)

class StickerToolsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LINE Sticker 生成サポートツール統合GUI")
        self.root.geometry("600x450")
        
        # 全体のフォント設定
        title_font = ("Helvetica", 16, "bold")
        
        # ヘッダー
        header_frame = tk.Frame(root, bg="#f0f0f0", pady=15)
        header_frame.pack(fill=tk.X)
        title_label = tk.Label(header_frame, text="ステッカー制作サポートツール", font=title_font, bg="#f0f0f0")
        title_label.pack()
        
        # 案内テキスト
        info_label = tk.Label(root, text="実行したいツールのボタンをクリックしてください。今後の拡張を見据えた構成です。", pady=10)
        info_label.pack()

        # ボタンリスト用フレーム
        self.buttons_frame = tk.Frame(root, pady=10)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # --- ツールの登録 ---
        self.add_tool_button(
            title="テーマフォルダ自動作成", 
            description="CSVファイルからテーマを読み取り、空のフォルダを一括作成します",
            command=self.run_create_folders
        )
        
        self.add_tool_button(
            title="プロンプトCSVの統合", 
            description="outputs/prompts 内の未統合の *_prompts.csv を all_prompts.csv にまとめます",
            command=self.run_merge_prompts
        )

    def add_tool_button(self, title, description, command):
        """
        GUIにツール起動ボタンを追加する
        """
        frame = tk.Frame(self.buttons_frame, bd=1, relief=tk.RAISED, pady=5)
        frame.pack(fill=tk.X, pady=5)
        
        # 実行ボタン
        btn = tk.Button(
            frame, 
            text=title, 
            font=("Helvetica", 11, "bold"), 
            width=25, 
            bg="#e0e0e0",
            command=command
        )
        btn.pack(side=tk.LEFT, padx=15, pady=10)
        
        # 説明ラベル
        desc = tk.Label(frame, text=description, font=("Helvetica", 9), anchor="w", justify=tk.LEFT)
        desc.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

    # --- 各ツールの呼び出しメソッド ---
    def run_create_folders(self):
        try:
            # create_theme_folders の main 関数を現在のrootを渡して呼ぶ
            create_theme_folders.main(parent=self.root)
        except Exception as e:
            messagebox.showerror("エラー", f"テーマフォルダ作成中にエラーが発生しました:\n{e}", parent=self.root)

    def run_merge_prompts(self):
        try:
            # merge_prompts の run_merge 関数を呼ぶ
            success, msg = merge_prompts.run_merge()
            if success:
                messagebox.showinfo("成功", msg, parent=self.root)
            else:
                messagebox.showwarning("警告", msg, parent=self.root)
        except Exception as e:
            messagebox.showerror("エラー", f"CSV統合中にエラーが発生しました:\n{e}", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = StickerToolsApp(root)
    root.mainloop()
