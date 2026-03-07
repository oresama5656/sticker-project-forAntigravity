import csv
import os

rows = [
    # ヘッダー行
    ['No', 'theme', 'title_en', 'desc_en', 'title_ja', 'desc_ja', 'copy_right', 'ai_flag', 'taste_category', 'character_category', 'zip_path'],
    
    # 考案したデータ（5個）
    ['1', '着物美人_敬語', 'Kimono Beauty: Polite Daily', 'Elegant kimono woman speaking politely for your everyday conversations and greetings.', '着物美人で好印象！毎日使える大人の気遣いや丁寧な敬語ご挨拶', '上品な和服の女性が、気遣いあふれる言葉であなたの気持ちを代弁。「了解」「お疲れ様」など毎日使いやすい汎用的な語句を網羅し、職場や目上の方への日常会話・連絡に最適。', '©ryo', 'TRUE', '敬語・丁寧', '女性キャラ', ''],
    ['2', '着物美人_癒し', 'Kimono Beauty: Healing Words', 'Healing your busy days with kind words and gentle smiles from a beautiful kimono woman.', '着物美人の癒やし♪毎日の会話で大活躍する優しい挨拶と思いやり', '柔らかな笑顔の着物美人が、忙しい毎日にちょっとした癒やしをお届け。「了解です」「ありがとう」など日常会話でヘビロテ必至！相手への労いや思いやりを優しく伝えられるセット。', '©ryo', 'TRUE', 'ほんわか・癒し', '女性キャラ', ''],
    ['3', '着物美人_シュール', 'Kimono Beauty: Surreal Truths', 'A surreal kimono beauty expressing your true feelings and making awkward moments funny.', '着物美人の本音爆弾！建前と裏腹なシュールな日常や気まずい場面', '凛とした着物姿の女性が、言いにくい本音や感情を堂々と代弁！気まずい状況を笑いに変えるネタ要素に加えて、「了解（真顔）」など普段使いしやすい表現もバッチリ収録されて便利。', '©ryo', 'TRUE', 'シュール', '女性キャラ', ''],
    ['4', '着物美人_方言', 'Kimono Beauty: Cute Dialect', 'Express your feelings warmly using elegant Japanese regional dialects and cute phrases.', '着物美人の京言葉！はんなり可愛い方言で伝える毎日のほんね挨拶', '艶やかな着物美人が「おおきに」「かんにんな」と可愛い京風の方言であなたの感情をご案内！毎日の「了解」「お疲れ様」の代わりに使えて、日常トークがパッと華やぐこと間違いなし。', '©ryo', 'TRUE', '方言・スラング', '女性キャラ', ''],
    ['5', '着物美人_クール', 'Kimono Beauty: Cool & Work', 'Cool Japanese kimono lady supporting your busy working days with quick and stylish replies.', '着物美人の仕事術！働く大人女子が毎日使えるクールな返信セット', 'デキる大人の着物美人が、あなたの忙しい毎日をサポート。「承知いたしました」「お疲れ様です」など、仕事仲間や友人への日々の連絡に何度も使える汎用性の高いスタイリッシュな内容。', '©ryo', 'TRUE', 'カッコいい', '女性キャラ', '']
]

os.makedirs('outputs', exist_ok=True)
with open('outputs/package_info_kimono.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
