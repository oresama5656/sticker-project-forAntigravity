import csv
from datetime import datetime
import os

rows = [
    # ヘッダー行
    ['No', 'theme', 'title_en', 'desc_en', 'title_ja', 'desc_ja', 'copy_right', 'ai_flag', 'taste_category', 'character_category', 'zip_path'],
    
    # 省エネ返信シリーズ 10個（スタンダードワードを配合）
    ['1', '爆速・基本の省エネ返信', 'Fast Reply Huge Font: Basics', "Essential daily replies in huge fonts. Includes standard words like 'OK', 'Yes', and 'No'. Perfect for busy people to reply with one tap.", '【デカ文字】爆速！基本の省エネ返信・サラリーマン', '「了解」「はい」「いいえ」など、絶対に使う基本ワードをデカ文字化！省エネだけど失礼のない、毎日の必須返信をタップ一発で終わらせる最強の時短スタンプです。', '©ryo', 'TRUE', '挨拶', '男性キャラ', ''],
    ['2', '気遣い・敬語の省エネ', 'Polite Energy Saving Huge Font', "Polite standard words like 'Thank you' and 'Sorry' in huge fonts. Be respectful even when you are too busy to type a long message.", '丁寧な省エネ。上司・取引先へ送る極太敬語返信', '「承知いたしました」「ありがとうございます」等の重要敬語をデカ文字に！忙しい時でも丁寧さは忘れたくない、デキる大人のための省エネ敬語セット。汎用性抜群です！', '©ryo', 'TRUE', '敬語・丁寧', '男性キャラ', ''],
    ['3', 'お疲れ様・労いの省エネ', 'Good Job! Huge Font Survival', "Standard greetings like 'Good job' and 'Take care' for coworkers. Huge fonts make your support clear with minimal effort during a long day.", '省エネお疲れ様！同僚を労うサラリーマンの極太語', '「お疲れ様です」「無理しないで」など、職場での必須挨拶を網羅。ヘトヘトな時も、デカ文字スタンプがあれば仲間とのコミュニケーションを省エネで継続できます。', '©ryo', 'TRUE', '挨拶', '男性キャラ', ''],
    ['4', '日常・生存報告の省エネ', 'Daily Life Signs Huge Font', "Basic daily words like 'Going home', 'Eat', and 'Sleep' in huge fonts. Tell your family and friends your status with zero typing effort.", '生きるための省エネ。帰宅・飯・寝るのデカ文字', '「帰ります」「飯」「寝る」など、プライベートで毎日使うスタンダードな生存報告。文字を打つ気力もない仕事帰り、家族への連絡を最小限の力で完結させます。', '©ryo', 'TRUE', 'ほんわか・癒し', '男性キャラ', ''],
    ['5', '感情とリアクションの省エネ', 'Easy Reactions Huge Font', "Standard reactions like 'I see', 'Wow', and 'Nice' in huge fonts. Keep the chat alive with zero mental load. Perfect for any conversation.", '省エネ相槌！感情をのせたデカ文字リアクション', '「なるほど」「確かに」「すごい！」など、会話に必須の相槌・反応をデカ文字化。深く考えずにポンポン返せるから、忙しい合間のチャットもこれ一つでスマートに。', '©ryo', 'TRUE', 'シュール', '男性キャラ', ''],
    ['6', '保留・多忙のアピール', 'Hold On Huge Font: Busy Life', "Standard busy words like 'Checking now' and 'Wait a sec'. Huge fonts to manage expectations when you're overwhelmed with work tasks.", '今は無理…多忙を伝える省エネ保留デカ文字', '「確認します」「ちょっと待って」「会議中」など、即レスできない時の標準フレーズ。相手を待たせている罪悪感を、愛嬌のあるデカ文字キャラが省エネで和らげてくれます。', '©ryo', 'TRUE', '敬語・丁寧', '男性キャラ', ''],
    ['7', '謝罪と反省の省エネ', 'Apology Standard Huge Font', "Standard apologies like 'Sorry' and 'My bad'. Huge fonts deliver your sincerity even with minimal effort. Essential for everyday office life.", '省エネ謝罪。一言で許しを請うサラリーマンの平謝り', '「すみません」「申し訳ない」「反省」など、日常のちょっとしたミスに使える謝罪ワード。デカ文字の視覚効果で、言葉を尽くすよりも誠実（？）に、かつ省エネに謝意が伝わります。', '©ryo', 'TRUE', 'シュール', '男性キャラ', ''],
    ['8', '疑問・確認の省エネ', 'Quick Questions Huge Font', "Essential questions like 'Where?', 'When?', and 'What?'. Huge fonts for efficient information gathering with your busy colleagues.", '省エネ質問！一瞬で確認をとる極太クエスチョン', '「いつ？」「どこ？」「OK？」など、確認事項をデカ文字だけで。余計な言葉を削ぎ落とした省エネスタイルで、忙しい相手からも爆速で回答を引き出すための実用セット。', '©ryo', 'TRUE', '面白い・ネタ', '男性キャラ', ''],
    ['9', '肯定・同意のバリエーション', 'Agree! Efficiency Huge Font', "Standard agreement words like 'I agree', 'Same here', and 'Good'. Huge fonts to show your support with minimal energy during group chats.", '全力同意！省エネで賛成するサラリーマンのデカ文字', '「賛成」「それな」「いいですね」など、同意のバリエーションを網羅。グループチャットの議論を省エネで盛り上げ、自分の存在感をしっかり示せるビジネスマンの味方。', '©ryo', 'TRUE', 'ほんわか・癒し', '男性キャラ', ''],
    ['10', '会話終了・挨拶の省エネ', 'Sign Off Huge Font: Goodbye', "Standard closings like 'See ya', 'Good night', and 'Bye'. Huge fonts to end the conversation politely without wasting your energy.", '省エネで締める！会話をスマートに終えるデカ文字', '「また明日」「おやすみ」「さらば」など、やり取りを締めくくる標準ワード。ダラダラ続くチャットを角を立てずに切り上げ、自分の時間を省エネで確保するための必需品。', '©ryo', 'TRUE', '挨拶', '男性キャラ', '']
]

output_dir = 'd:/sticker-project/outputs'
os.makedirs(output_dir, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'{output_dir}/package_info_{timestamp}.csv'

with open(filename, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        
print(f'Successfully wrote CSV to {filename}')
