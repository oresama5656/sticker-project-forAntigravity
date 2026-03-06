import os
import csv

def generate_csvs():
    os.makedirs('outputs/prompts', exist_ok=True)
    
    # 20テーマの定義 (ファイル名, テーマ名, プロンプトデータの生成用情報)
    themes = [
        ("01_丁寧な敬語", "いつでも使える丁寧な敬語", [
            ("Bowing deeply and gracefully", "左様でございます"),
            ("Nodding gently with a calm smile", "かしこまりました"),
            ("Opening a sliding door (shoji) elegantly", "失礼いたします"),
            ("Pouring tea with precise movements", "お茶をどうぞ"),
            ("Sitting in seiza (kneeling) perfectly", "お呼びでしょうか"),
            ("Holding a closed fan to her chin thoughtfully", "承知いたしました"),
            ("Walking gracefully with hands folded", "お供いたします"),
            ("Presenting a document or scroll with both hands", "こちらでございます"),
            ("Gently waving a hand in a welcoming gesture", "ようこそお越しくださいました")
        ]),
        ("02_優しい言葉", "相手を気遣う優しい言葉", [
            ("Holding a warm drink with both hands", "お疲れ様です"),
            ("Looking concerned with a hand to her cheek", "ご無理なさらず"),
            ("Offering a small sweet on a plate", "甘いものでもいかが？"),
            ("Wiping sweat with a decorative handkerchief", "頑張りすぎですよ"),
            ("Patting a shoulder gently with a soft smile", "お力になりますわ"),
            ("Listening intently with a sympathetic gaze", "お察しいたします"),
            ("Preparing a cozy futon or cushion", "ゆっくりお休みください"),
            ("Lighting a lantern to guide the way", "足元にお気をつけて"),
            ("Smiling warmly with autumn leaves falling", "いつも見ておりますわ")
        ]),
        ("03_おしとやかな承諾", "おしとやかに承諾", [
            ("Nodding with a radiant, soft smile", "承知いたしました"),
            ("Clapping hands softly in a tiny gesture", "喜んで"),
            ("Placing a hand on her chest in compliance", "仰せのままに"),
            ("Starting to work with a determined but graceful look", "取り掛かりますわ"),
            ("Bowing slightly while averting eyes modestly", "異存はございません"),
            ("Preparing a brush to write down a request", "書き留めましたわ"),
            ("Handing over a key or important item", "お任せくださいませ"),
            ("Walking towards a destination with purpose", "ただいま参ります"),
            ("Looking up with a sparkle in her eyes", "願ってもないことです")
        ]),
        ("04_謙虚な感謝", "謙虚な感謝の気持ち", [
            ("Bowing deeply with hands on the floor (ojigi)", "恐縮です"),
            ("Pressing hands together in a subtle prayer", "痛み入ります"),
            ("Blushing slightly with a modest smile", "もったいないお言葉です"),
            ("Holding a small gift close to her heart", "大切にいたしますわ"),
            ("Looking down shyly while folding a fan", "感謝の念に堪えません"),
            ("Offering a deep bow towards the viewer", "おかげさまでございます"),
            ("Smiling with tears of joy in her eyes", "感服いたしました"),
            ("Wiping away a single tear of gratitude", "お心遣いに感謝を"),
            ("Bowing while holding her kimono sleeve", "幸せ者でございます")
        ]),
        ("05_爽やかな朝の挨拶", "爽やかな朝の挨拶", [
            ("Opening window shutters to morning sunlight", "おはようございます"),
            ("Deep breathing in a morning garden with mist", "良き一日を"),
            ("Watering plants with a refreshing smile", "清々しい朝ですわ"),
            ("Folding bedding neatly in the morning breeze", "目が覚めましたの？"),
            ("Preparing a fresh breakfast tray", "朝餉（あさげ）をどうぞ"),
            ("Looking at a morning glory flower blooming", "今日も頑張りましょう"),
            ("Standing straight in a sunbeam", "凛とした朝ですわね"),
            ("Holding a bird feeder for chirping birds", "小鳥も快活です"),
            ("Refreshing her face with a cool cloth", "目覚ましに一杯いかが？")
        ]),
        ("06_雅な夜の挨拶", "雅な夜の挨拶", [
            ("Blowing out a candle flame gently", "おやすみなさいませ"),
            ("Looking at the full moon through a window", "良い夢を"),
            ("Sitting on an engawa (veranda) in the moonlight", "夜風が心地よいですわ"),
            ("Closing a bamboo blind (sudare) slowly", "更けゆく夜に"),
            ("Inhaling the scent of incense smoothly", "安らかな眠りを"),
            ("Reading a scroll by a paper lamp", "夜更かしはいけませんわ"),
            ("Covering someone with a warm haori coat", "お静かにおやすみください"),
            ("Observing fireflies by a stream at night", "また明日お会いしましょう"),
            ("Drinking a nightcap of warm tea", "夢で会いましょう")
        ]),
        ("07_控えめな自己主張", "控えめな自己主張", [
            ("Holding a half-folded fan to her lips", "お言葉ですが"),
            ("Nodding with a knowing, mysterious smile", "存じております"),
            ("Pointing slightly with a decorative hair-pin", "こちらが正解かと"),
            ("Looking firm while sitting in seiza", "私の考えはこうです"),
            ("Touching her collar with a determined hand", "譲れぬ一線がございます"),
            ("Closing her eyes and shaking her head once", "それは致しかねます"),
            ("Standing tall with a dignified gaze", "覚悟はできております"),
            ("Writing a single kanji on a paper strongly", "これが私の本意"),
            ("Watching with a sharp, intelligent look", "お見通しでございます")
        ]),
        ("08_季節の風情を感じる挨拶", "季節の風情を感じる挨拶", [
            ("Feeling a cool breeze on her face", "風が心地よいですね"),
            ("Catching a falling cherry blossom petal", "春の訪れを感じます"),
            ("Holding a wind chime (furin) in summer", "涼をお届けします"),
            ("Looking at red autumn leaves in her hand", "秋も深まりましたわ"),
            ("Standing in a snowy garden with a red umbrella", "お体ご自愛ください"),
            ("Watching the first sunrise of the year", "良き年になりますよう"),
            ("Holding a branch of plum blossoms", "春はもうすぐそこ"),
            ("Enjoying the scent of a summer forest", "緑が美しいですわね"),
            ("Sitting by a warm hibachi heater in winter", "冬の夜は凍えますわね")
        ]),
        ("09_凛としたお断り", "凛としたお断り", [
            ("Raising a palm in a stopping gesture", "致しかねます"),
            ("Bowing slightly but looking away firmly", "ご遠慮申し上げます"),
            ("Closing her fan with a sharp 'snap' sound", "お断りいたします"),
            ("Looking cold and distant with steady eyes", "それは無用なこと"),
            ("Standing behind a bamboo screen (sudare)", "お引き取りください"),
            ("Pouring tea into the sink as a rejection", "ご縁がなかったようです"),
            ("Folding her arms inside her kimono sleeves", "納得しかねますわ"),
            ("Watching someone leave with a stern face", "次はございませんわよ"),
            ("Writing 'No' in beautiful calligraphy", "御免あそばせ")
        ]),
        ("10_上品な喜び", "喜びを上品に表現", [
            ("Smiling brightly with blooming cherry blossoms", "嬉しい限りです"),
            ("Looking at a beautiful sunset with a glow", "感無量でございます"),
            ("Holding a celebratory fan open wide", "吉報ですわ！"),
            ("Clapping hands with a joyful, airy expression", "胸が躍りますわ"),
            ("Twirling around in her colorful kimono", "至福のひとときです"),
            ("Looking up at the sky with a radiant aura", "夢のようでございます"),
            ("Preparing a grand feast to celebrate", "おめでたいですわね"),
            ("Winking with a playful, happy smile", "うふふ、最高です"),
            ("Sticking a victorious flower in her hair", "勝ちどきを上げましょう")
        ]),
        ("11_驚きの仕草", "驚きを隠せない仕草", [
            ("Covering her mouth with a wide kimono sleeve", "あらまあ"),
            ("Eyes widening with a small, cute gasp", "おや、これは"),
            ("Dropping her fan in shock", "まさかそんな"),
            ("Stumbling back slightly with a pale face", "聞き間違いかしら"),
            ("Looking around in confusion with tilted head", "何が起きましたの？"),
            ("Holding both cheeks with her hands in shock", "信じられませんわ"),
            ("A scroll falling from her hands in surprise", "なんですって！"),
            ("Pointing with a trembling finger", "あ、あれは…！"),
            ("Looking bewildered in a crowded street", "都は恐ろしいところ")
        ]),
        ("12_励ましと応援", "励ましと応援", [
            ("Putting a hand on someone's shoulder softly", "陰ながら応援しております"),
            ("Raising a fist inside her sleeve in support", "きっと大丈夫です"),
            ("Smiling with absolute confidence and trust", "信じておりますわ"),
            ("Waving a banner with motivational kanji", "全力で攻めなさい"),
            ("Preparing a recovery meal with energy", "元気を出しなさいな"),
            ("Looking at someone with encouraging eyes", "まだ道は続いております"),
            ("Stamping her foot firmly on the ground", "踏ん張りどころですわ"),
            ("Offering a protective charm (omamori)", "ご加護がありますよう"),
            ("Standing in the wind, cheering silently", "風が味方しております")
        ]),
        ("13_深々としたお詫び", "深々としたお詫び", [
            ("Bowing very deeply in seiza (saikeirei)", "申し訳ございません"),
            ("Lowering her head with a pained expression", "お許しください"),
            ("Pressing her head to the floor (dogeza style)", "合わせる顔がございません"),
            ("Looking down with shadows over her eyes", "弁解の余地もございません"),
            ("Tears falling onto her lap gracefully", "不徳の致すところ"),
            ("Handing over a letter of apology with both hands", "誠意を尽くします"),
            ("Folding her hands in a tight grip of regret", "猛省しております"),
            ("Looking up with pleading, wet eyes", "一度だけチャンスを"),
            ("Bowing towards a closed door in the rain", "二度と繰り返しませんわ")
        ]),
        ("14_期待・楽しみ", "期待に胸を膨らませる", [
            ("Looking at a calendar with a bright face", "楽しみにしております"),
            ("Staring at the door waiting for someone", "待ち遠しいですわ"),
            ("Preparing extra tea and sweets with glee", "わくわくいたします"),
            ("Checking her reflection in a mirror repeatedly", "準備万端ですわ"),
            ("Looking at a cruise ship or carriage approaching", "いよいよですわね"),
            ("Sparkling eyes looking at a closed gift box", "何が入っているかしら"),
            ("Holding a ticket or pass close to her chest", "夢が広がります"),
            ("Tapping her chin with a fan rhythmically", "想像するだけで幸せ"),
            ("Looking towards the horizon with hope", "明日が待ち遠しいわ")
        ]),
        ("15_お祝いの言葉", "お祝いの言葉", [
            ("Throwing colorful confetti into the air", "おめでとうございます"),
            ("Opening a large celebratory scroll", "おめでたいですね"),
            ("Lifting a sake cup for a toast warmly", "祝杯を上げましょう"),
            ("Tai-fish (celebratory fish) on a grand platter", "めでたい尽くしですわ"),
            ("Playing a traditional flute in celebration", "音に祝いを込めて"),
            ("Smiling like a sunbeam surrounded by flowers", "記念すべき日ですわ"),
            ("Handing over a red-and-white envelope", "お祝いの品です"),
            ("Applauding gracefully with both hands", "感服の極みです"),
            ("Looking at the stars in celebration", "世に幸あれ")
        ]),
        ("16_さりげない共感", "さりげない共感", [
            ("Nodding deeply while listening to someone", "左様ですね"),
            ("Looking sympathetic with a gentle gaze", "お察しいたします"),
            ("Placing a hand over her heart in empathy", "私も胸が痛みますわ"),
            ("Sharing a warm drink in a quiet room", "お気持ち分かりますわ"),
            ("Giving a small, understanding nod", "無理もございません"),
            ("Looking at the same view together silently", "同じ思いでございます"),
            ("Wiping away a tear together", "独りではございませんわ"),
            ("Offering a supportive smile during a talk", "あなたの味方です"),
            ("Holding someone's hand through a sleeve", "共に行きましょう")
        ]),
        ("17_謙遜のポーズ", "謙遜するポーズ", [
            ("Waving a hand in front of her face in denial", "滅相もございません"),
            ("Looking up with a thankful but humble face", "おかげさまでございます"),
            ("Bowing slightly while averting her gaze", "私などまだまだ…"),
            ("Pointing to her teacher or master behind her", "皆様のお力添えです"),
            ("Hiding a blush behind a half-closed fan", "過分なお言葉ですわ"),
            ("Taking a back seat in a group photo", "影の存在で十分です"),
            ("Offering the best seat to someone else", "どうぞ、お先に"),
            ("Polishing someone else’s tool carefully", "微力ながら尽くします"),
            ("Looking peaceful while working in the shadow", "分をわきまえております")
        ]),
        ("18_再会の願い", "再会を願う言葉", [
            ("Waving a hand towards a departing carriage", "またお会いしましょう"),
            ("Bowing towards someone leaving a gate", "ごきげんよう"),
            ("Tying a prayer strip to a bamboo tree", "再会を期して"),
            ("Looking at a distant mountain longingly", "健やかにお過ごしください"),
            ("Holding a keepsake given by someone", "ずっと待っておりますわ"),
            ("Writing a letter with a soft expression", "次会う時を夢見て"),
            ("Watching the sun set with a lonely smile", "いつかまた、この場所で"),
            ("Pointing to a date on a scroll with a smile", "約束の日を待っています"),
            ("Walking along a path toward the viewer", "お帰りをお待ちしてました")
        ]),
        ("19_落ち着きを促す", "落ち着きを促す一言", [
            ("Handing out a steaming cup of tea calmly", "まずは一服いかがですか"),
            ("Closing her eyes and breathing deeply", "落ち着いてくださいな"),
            ("Placing a hand on someone's arm to stop them", "一旦、お座りなさい"),
            ("Speaking with a calm, melodic voice", "慌てる必要はございません"),
            ("Preparing an ink stone slowly and rhythmically", "心静かに致しましょう"),
            ("Pointing to a calm, still pond or lake", "水面のような心で"),
            ("Adjusting a flower in a vase carefully", "深呼吸を一つ"),
            ("Looking steady and unshakeable in a crisis", "私がついておりますわ"),
            ("Stroking a cat with a peaceful expression", "静寂を楽しみましょう")
        ]),
        ("20_固い決意", "固い決意の表情", [
            ("Grasping a katana hilt with white knuckles", "覚悟はできております"),
            ("Looking at the target with sharp, intense eyes", "精進いたします"),
            ("Standing tall against a strong storm wind", "一歩も引きませんわ"),
            ("Cutting a strand of her hair with a knife", "退路は断ちました"),
            ("Climbing a steep mountain peak alone", "成し遂げてみせます"),
            ("Writing a vow in red ink with focus", "不退転の決意"),
            ("Facing a large army with a calm, ready pose", "ここが死に場所"),
            ("Tying a headband (hachimaki) firmly", "覚醒の時ですわ"),
            ("Looking at her reflection with a cold fire in eyes", "己に打ち勝つのみ")
        ])
    ]

    for file_name, display_name, prompt_pairs in themes:
        rows = ['prompt']
        
        # 9個のプロンプトを1行に連結
        line = ""
        for i, (action, text) in enumerate(prompt_pairs):
            p_num = f"P{i+1}"
            p_content = f'{p_num}: ACTION/PROPS="{action}" | TEXT="{text}"'
            line += p_content + " "
        
        # 9個×6セットを作成（すべて同じ内容で複製。必要なら少しだけ変更可能だが、指示に忠実にするため1セットを5回複製して計6セットとする）
        for _ in range(6):
            rows.append(line.strip())
            
        full_file_path = f'outputs/prompts/{file_name}_prompts.csv'
        with open(full_file_path, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow([row])
        
        print(f"Generated: {full_file_path}")

if __name__ == "__main__":
    generate_csvs()
