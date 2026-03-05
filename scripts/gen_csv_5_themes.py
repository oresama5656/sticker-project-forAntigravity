import csv
import os

os.makedirs('outputs/prompts', exist_ok=True)

themes_data = {
    "和服美人ｘ猫ｘスタンダードあいさつ": [
        [("waking up stretching", "おはよう"), ("bowing politely", "こんにちは"), ("looking at the moon", "こんばんは"), ("presenting a gift smiling", "ありがとう"), ("bowing deeply sincerely", "ごめんなさい"), ("offering hands gently", "よろしく"), ("wiping sweat smiling", "おつかれさま"), ("tying shoes looking back", "いってきます"), ("opening door happily", "ただいま")],
        [("raising hand cheerfully", "はーい"), ("giving a thumbs up", "いいね"), ("making an OK sign", "オッケー"), ("nodding with understanding", "なるほど"), ("tilting head in thought", "えっと"), ("nodding continuously", "ふむふむ"), ("looking convinced", "そうなんだ"), ("pointing finger agreeing", "わかる"), ("pointing directly", "それな")],
        [("sleeping in futon", "おやすみ"), ("waving hand gently", "またね"), ("waving both hands", "ばいばい"), ("seeing someone off", "いってらっしゃい"), ("welcoming someone warmly", "おかえり"), ("stepping inside softly", "おじゃまします"), ("holding chopsticks eagerly", "いただきます"), ("rubbing belly satisfied", "ごちそうさま"), ("smiling elegantly", "どういたしまして")],
        [("jumping up joyfully", "わーい"), ("raising fists in victory", "やったー"), ("clasping hands happily", "うれしい"), ("eyes sparkling", "たのしみ"), ("clapping hands celebrating", "おめでとう"), ("looking impressed", "すごい"), ("thumbs up winking", "さすが"), ("holding tea cups together", "かんぱい"), ("presenting a cake", "お祝い")],
        [("looking surprised round eyes", "えっ"), ("leaning forward interested", "ほんと？"), ("startled jumping back", "びっくり"), ("tilting head slightly", "なんだって"), ("eyes wide open shocked", "まじで"), ("trembling slightly scared", "ひえー"), ("covering mouth in disbelief", "うそでしょ"), ("pale face dropping shoulders", "がーん"), ("crying out loud", "ショック")],
        [("tilting head with question mark", "ん？"), ("looking concerned", "どうしたの？"), ("reaching out comfortingly", "だいじょうぶ？"), ("peeking from corner", "なになに？"), ("eyes glued to something", "きになる"), ("holding a book pointing", "おしえて"), ("scratching head confused", "はてな"), ("looking up pondering", "なんだろう"), ("shrugging shoulders", "わかんない")]
    ],
    "和服美人ｘ猫ｘ気遣いあいさつ": [
        [("patting shoulder gently", "無理しないでね"), ("serving hot tea", "お疲れ様です"), ("tucking into blanket", "ゆっくり休んでね"), ("cheering with pom-poms", "がんばって"), ("holding up a banner", "応援してるよ"), ("pumping fist encouraging", "ファイト"), ("bowing slightly", "いつもありがとう"), ("bowing formally", "助かります"), ("bowing very deeply", "お世話になってます")],
        [("holding a scarf out", "風邪ひかないでね"), ("holding a hot water bottle", "暖かくしてね"), ("waving carefully", "気をつけてね"), ("seeing off with a smile", "いってらっしゃいませ"), ("welcoming back warmly", "お帰りなさいませ"), ("offering medicine", "お大事に"), ("patting back gently", "元気出して"), ("offering a cushion", "リラックスしてね"), ("holding a tea cup", "お茶どうぞ")],
        [("listening attentively", "話聞くよ"), ("holding hands supportively", "ひとりじゃないよ"), ("nodding gently", "うんうん"), ("smiling warmly", "いつでもどうぞ"), ("wiping tears softly", "泣いてもいいよ"), ("holding an umbrella", "傘どうぞ"), ("holding a towel", "拭いてね"), ("looking worried", "心配です"), ("smiling reassuringly", "まかせて")],
        [("clapping hands gently", "がんばったね"), ("giving a gold medal", "えらい"), ("petting the cat", "いいこ"), ("thumbs up smiling", "素晴らしい"), ("looking proudly", "誇らしい"), ("giving a bouquet", "お祝いします"), ("clapping hands warmly", "拍手"), ("smiling brightly", "よかったね"), ("giving a small gift", "プレゼント")],
        [("offering hand", "手伝うよ"), ("looking helpful", "何かできる？"), ("carrying a heavy box", "手伝います"), ("holding a broom", "掃除するね"), ("holding a cooking pan", "ごはん作るね"), ("kneeling politely", "お申し付けを"), ("smiling brightly", "お任せください"), ("pointing upward confidently", "完璧です"), ("wiping sweat", "完了しました")],
        [("looking shy", "邪魔だった？"), ("hiding face slightly", "気にしなくていいよ"), ("shaking head gently", "ううん"), ("waving hand dismissing", "とんでもない"), ("bowing casually", "気にせずに"), ("smiling kindly", "お互い様"), ("touching cheek softly", "優しいね"), ("clasping hands", "ありがとうね"), ("bowing again", "感謝です")]
    ],
    "和服美人ｘ猫ｘ敬語": [
        [("bowing politely morning", "おはようございます"), ("bowing gracefully", "こんにちは"), ("bowing deeply evening", "こんばんは"), ("bowing gratefully", "ありがとうございます"), ("bowing deeply apologizing", "申し訳ありません"), ("bowing formal request", "よろしくお願いします"), ("bowing respectfully", "お疲れ様です"), ("bowing departing", "行ってまいります"), ("bowing returning", "ただいま戻りました")],
        [("giving OK sign formally", "かしこまりました"), ("nodding formally", "承知いたしました"), ("writing on notepad", "拝見いたしました"), ("looking thoughtful", "検討いたします"), ("holding phone securely", "連絡いたします"), ("holding a letter", "お手紙です"), ("bowing waiting", "お待ちしております"), ("handing over document", "お願いいたします"), ("accepting respectfully", "頂戴いたします")],
        [("tilting head respectfully", "いかがなさいますか"), ("looking inquiring", "よろしいでしょうか"), ("offering a seat", "お掛けください"), ("gesturing toward door", "どうぞこちらへ"), ("holding a fan politely", "お気になさらず"), ("serving tea elegantly", "お茶をどうぞ"), ("smiling kindly formally", "お役に立てれば幸いです"), ("bowing slightly grateful", "恐縮です"), ("looking apologetic", "恐れ入ります")],
        [("looking concerned formally", "お加減いかがですか"), ("handing over umbrella", "お気をつけください"), ("bowing softly departure", "お気をつけて"), ("smiling gently", "ご無事で"), ("looking supportive", "応援しております"), ("clapping respectfully", "素晴らしいです"), ("nodding humbly", "お見事です"), ("smiling pleased", "さすがでございます"), ("bowing humbly", "光栄です")],
        [("looking surprised formally", "ええっ"), ("covering mouth politely", "まあ"), ("tilting head wondering", "どういうことでしょう"), ("looking confused formally", "わかりかねます"), ("apologizing gently", "お答えできず"), ("looking sorry", "申し訳ございません"), ("bowing very low", "深くお詫び申し上げます"), ("holding hands apologizing", "ご容赦ください"), ("looking up pleadingly", "お願い申し上げます")],
        [("holding a gift politely", "つまらないものですが"), ("giving a souvenir", "お土産です"), ("serving snacks", "お茶菓子です"), ("enjoying meal formally", "いただきます"), ("putting hands together full", "ごちそうさまでした"), ("cleaning table", "片付けます"), ("bowing goodnight", "おやすみなさいませ"), ("bowing farewell", "またお目にかかります"), ("waving slightly formally", "失礼いたします")]
    ],
    "和服美人ｘ猫ｘ猫好き": [
        [("cat ears headband", "にゃーん"), ("burying face in cat", "猫吸い"), ("rubbing cheek against cat", "もふもふ"), ("showing cat paws", "肉球"), ("eyes sparkling looking at cat", "かわいい"), ("hugging cat tightly", "癒やされる"), ("holding cat up", "ねこしか勝たん"), ("cat purring on lap", "ゴロゴロ"), ("cat rubbing against leg", "すりすり")],
        [("feeding cat", "ごはん"), ("brushing cat", "ブラッシング"), ("playing with cat toy", "遊びたい"), ("taking photo of cat", "パシャ"), ("kissing cat", "チュッ"), ("sleeping with cat", "一緒にお昼寝"), ("cat sitting on shoulder", "重いけど幸せ"), ("watching cat groom", "毛づくろい"), ("holding out cat treat", "おやつだよ")],
        [("cat hiding in kimono", "はこにゃん"), ("cat batting at string", "とれない"), ("cat looking confused", "はてにゃ"), ("cat scratching", "バリバリ"), ("cat yawning big", "ふぁー"), ("laughing at cat", "おもしろにゃ"), ("smiling at silly cat", "どじにゃん"), ("cat bringing a toy", "ほめて"), ("petting cat sleeping", "スヤスヤ")],
        [("putting ribbon on cat", "おしゃれ"), ("walking cat on leash", "おさんぽ"), ("cat running away", "まてこら"), ("cat ignoring", "つれない"), ("cat meowing loudly", "ニャー"), ("giving thumbs up to cat", "いいこいいこ"), ("cat biting gently", "あむっ"), ("cat kneading on lap", "モミモミ"), ("cat looking angry", "シャーッ")],
        [("looking for cat", "どこにゃ"), ("finding cat", "いたいた"), ("cat jumping high", "ジャンプ"), ("cat falling asleep", "うとうと"), ("cat playing piano", "にゃんこピアニスト"), ("cat inside paper bag", "かさかさ"), ("cat chasing tail", "ぐるぐる"), ("cat with a fish", "おさかな"), ("cat drinking milk", "ぺろぺろ")],
        [("wearing matching cat hoods", "おそろい"), ("holding paw", "握手"), ("high fiving cat", "ハイタッチ"), ("reading book with cat", "お勉強"), ("watching tv with cat", "まったり"), ("cat blocking keyboard", "じゃまにゃ"), ("cat looking out window", "パトロール"), ("cat looking guilty", "やっちゃった"), ("laughing together with cat", "にゃはは")]
    ],
    "和服美人ｘ猫ｘいつでも使える": [
        [("nodding yes", "はい"), ("shaking head no", "いいえ"), ("making OK sign", "OK"), ("making X sign", "NG"), ("giving a salute", "了解です"), ("bowing slightly acknowledging", "承知しました"), ("looking at notebook", "確認します"), ("peeking behind wall", "チラッ"), ("staring intently", "ジーッ")],
        [("holding a big question mark", "はてな"), ("raising hand enthusiastically", "質問"), ("clapping hands together", "ひらめいた"), ("pointing finger confidently", "それだ"), ("holding head thinking", "うーん"), ("shrugging playfully", "まあいっか"), ("looking disappointed", "ざんねん"), ("cheering with hands up", "イェーイ"), ("doing a small dance", "ルンルン")],
        [("running fast", "ダッシュ"), ("panting wiping sweat", "ぜえぜえ"), ("typing fast on computer", "カタカタ"), ("holding a stopwatch", "あせあせ"), ("giving a thumbs up casually", "おつ"), ("drinking water", "ごくごく"), ("stretching arms", "のびー"), ("yawning lazily", "ふぁー"), ("sleeping peacefully", "すやすや")],
        [("holding a smartphone turning away", "既読"), ("typing on phone smiling", "返信"), ("looking at watch", "時間だよ"), ("pointing at clock", "いまどこ"), ("holding a calendar", "予定は？"), ("holding money", "お金"), ("holding a bag", "買い物"), ("holding a steering wheel", "運転中"), ("holding a train ticket", "電車乗る")],
        [("looking lonely", "ぽつん"), ("hugging knees", "さみしい"), ("pouting lips", "むっ"), ("puffing cheeks", "ぷんぷん"), ("crying rivers", "ぴえん"), ("laughing hysterically", "爆笑"), ("smiling mysteriously", "ふふっ"), ("smiling warmly gentle", "ニコニコ"), ("winking eye", "ウインク")],
        [("holding a blank signboard", "無地"), ("pointing up", "上"), ("pointing down", "下"), ("pointing right", "右"), ("pointing left", "左"), ("holding a megaphone", "注目"), ("hands together begging", "プリーズ"), ("hands crossed blocking", "ブッブー"), ("hands making a circle", "ピンポーン")]
    ]
}

for theme_name, sets in themes_data.items():
    file_path = f'outputs/prompts/{theme_name}_prompts.csv'
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['prompt'])
        for s in sets:
            row_parts = []
            for i, (eng, jap) in enumerate(s):
                action = f'A beautiful woman in a kimono with a cat {eng}'
                text = jap
                row_parts.append(f'P{i+1}: ACTION/PROPS=\"{action}\" | TEXT=\"{text}\"')
            writer.writerow([" ".join(row_parts)])
