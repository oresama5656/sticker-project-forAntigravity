import csv

rows = [
    # ヘッダー行
    ['No', 'theme', 'title_en', 'desc_en', 'title_ja', 'desc_ja', 'copy_right', 'ai_flag', 'taste_category', 'character_category', 'zip_path'],
    
    # 和服美人の日常
    ['1', '和服美人の日常', 'Kimono Beauty Everyday Life', 'Beautiful women wearing traditional Japanese kimonos. Perfect for daily use and chats.', '和服美人の日常スタンプ', '毎日使える！美しい和服姿の女性のスタンプです。日々の連絡に華を添えましょう。', '©ryo', 'TRUE', 'ほんわか・癒し', '女性キャラ', ''],
    
    # 和服美人ｘ猫ｘいつでも使える
    ['2', '和服美人ｘ猫ｘいつでも使える', 'Kimono Beauty & Cat Cute Stickers', 'A wonderful collaboration of a kimono beauty and cute cats! Very useful for any chat.', '和服美人＆猫のゆるふわスタンプ', '和服美人と可愛い猫がコラボ！いつでも楽しく使える便利なスタンプセットです。', '©ryo', 'TRUE', 'ほんわか・癒し', 'ネコ', ''],
    
    # 和服美人ｘ猫ｘスタンダードあいさつ
    ['3', '和服美人ｘ猫ｘスタンダードあいさつ', 'Kimono Beauty & Cat: Greetings', 'Standard greeting stickers featuring a kimono beauty and a cute cat for your daily messages.', '和服美人＆猫★定番あいさつ', '和服美人と猫による使いやすい基本の挨拶スタンプ。「おはよう」から「おやすみ」まで。', '©ryo', 'TRUE', '挨拶', '女性キャラ', ''],
    
    # 和服美人ｘ猫ｘ敬語
    ['4', '和服美人ｘ猫ｘ敬語', 'Kimono Beauty & Cat: Polite', 'Polite Japanese stickers featuring a kimono beauty and a cat. Great for formal contacts.', '和服美人＆猫【丁寧な敬語】', '先輩や仕事仲間にも送りやすい、和服美人と猫の敬語スタンプです。丁寧なやり取りに。', '©ryo', 'TRUE', '敬語・丁寧', 'ネコ', ''],
    
    # 和服美人ｘ猫ｘ気遣いあいさつ
    ['5', '和服美人ｘ猫ｘ気遣いあいさつ', 'Kimono Beauty & Cat: Thoughtful', 'Send your warm regards with these thoughtful stickers featuring a kimono beauty and a cat.', '和服美人＆猫のおもいやりスタンプ', '相手を気遣う優しい言葉を集めました。和服美人と猫があなたの思いやりを届けます。', '©ryo', 'TRUE', 'ほんわか・癒し', '女性キャラ', ''],
    
    # 和服美人ｘ猫ｘ猫好き
    ['6', '和服美人ｘ猫ｘ猫好き', 'Kimono Beauty & Cat Lover', 'Packed with the cuteness of cats and elegance of Kimono. Dedicated to all cat lovers!', '和服美人×猫【猫好き専用】', '猫の可愛さがたっぷり詰まった和服美人のスタンプ！猫を愛するすべての人に。', '©ryo', 'TRUE', 'カワイイ・キュート', 'ネコ', '']
]

with open('outputs/package_info.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
