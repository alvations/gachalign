*GaChalign* (ガチャalign) is a python implementation of [Gale-Church (1993)](http://acl.ldc.upenn.edu/J/J93/J93-1004.pdf) sentence aligner with options for _variable parameters_ (viz. _mean_, _variance_, _penalty_). 

Our experiment with English-Japanese corpus from [Nanyang Technological University - Multilingual Corpus (NTU-MC)](https://github.com/alvations/NTU-MC) has shown that 
  * aligning syllabic/logographic language (JPN) to alphabetic language (ENG) is a challenge for Gale-Church algorithm (f-score peaks at 62.9%)
  * using the calculated character mean from the unaligned text improves precision and recall of the algorithm
  * using the calculated alignment type penalties from a sample gold corpus also improves fscore 

(see the full details on the experiment [here](https://drive.google.com/file/d/1XxCLxA99MRJbF6xzWS8WDR9igrz-m2q8/view?usp=sharing))

Usage
====

To run Gale-Church algorithm with default settings as per the original paper.

```
$ python gale_church.py source_corpus target_corpus (mean) (variance) (penalties)
```

To run Gale-Church algorithm that automatically calculates character mean from the input source and target corpora

```
$ python gale_church.py source_corpus target_corpus gacha
```


Input Corpora format
====
The format for raw corpora for GaChalign is one sentence per line and paragraphs separated by "#". For example:

*source_corpus.txt*

```
# NTU-MC/Fun
Have an awesome time in Singapore , with countless activities for a fun-filled day .
Bounce around with the animals , fly around with the birds and enjoy city views from the Singapore Flyer .
Then discover Sentosa and the Universal Studios , to see Shreks castle and the roller coasters .
Plan your trip now for animals , thrills and spills that will surely put a smile on your face .
# NTU-MC/maxwell-road-hawker-centre
Experience an authentically Singaporean dining experience by having a meal at a food centre here .
Located in the heart of Chinatown , Maxwell Road Hawker Centre has over 100 stalls , providing one of the biggest varieties of local food in Singapore .
Even with the influx of vendors , the stalls offerings are very varied and you will easily spoilt for choice here .
Some must-try items here at Maxwell Road Hawker Market include the famous Tian Tian Chicken Rice , the traditional congee with pork and century egg from Zhen Zhen Porridge stall and the popular char kway teow from the Marina South Delicious Food stall .
```

*target_corpus.txt*

```
# NTU-MC/Fun
シンガポール で 数え 切れ ない ほど の アクティビティー を 体験 し 、 楽し さいっぱい の 素晴 らしい 一時 を 過ごし ましょ う 。
動物 たち と 遊び 回り 、 鳥 たち と 飛び 回り 、 シンガポール ・ フライ から シティー ・ ビュー を 楽しみ ましょ う 。
そし て 次 は セントサ と ユニバーサル ・ スタジオ を 発見 し 、 シュレック の 城 と ローラー ・ コースター を 見 に 行き ましょ う 。
笑顔 が こぼれる よう な 、 動物 と エキサイティング な 体験 の 旅 を 今す ぐ 計画 しましょ う 。
# NTU-MC/maxwell-road-hawker-centre
フードセンター で 食事 を し 、 シンガポール 人 に なっ た 気分 を 味わい ましょ う 。
チャイナタウン の 中心 に ある 「 マックスウェル ・ ロード ・ ホーカーセンター 」 に は 、 100 以上 もの 屋台 が あり ます 。
ここ は 、 シンガポール 国内 で 最も 多く の 地元 料理 が 楽しめる 場所 の 一つ と 言え ます 。
お店 の 数 が 多い こと も さる こと ながら 、 各屋 台 が 提供 する メニュー の 種類 も 豊富 な ので 、 選択 肢 に 困る こと は 全く あり ませ ん 。
「 マックスウェル ・ ロード ・ ホーカー ・ マーケット 」 で 絶対 に 試し て おき たい アイテム の 一つ は 、「 真真 粥品 （Zhen Zhen Porridge ）」 で 食べ られる 、 伝統的 なお粥 に 豚肉 や センチュリーエッグ が 入っ た テンテン ・ チキンライス です 。
人気 の 「 マリーナ ・ サウス ・ デリシャス ・ フード 」 の チャー ・ クェイ ・ ティオ も お勧め です 。
```

The format for human-aligned corpus for GaChalign is one sentence-pair per line and source-target delimited by "\t"; paragraphs separated by "#". For example:

```
# NTU-MC/Fun
Have an awesome time in Singapore , with countless activities for a fun-filled day .	シンガポールで数え切れないほどのアクティビティーを体験し、楽しさいっぱいの素晴らしい一時を過ごしましょう。
Bounce around with the animals , fly around with the birds and enjoy city views from the Singapore Flyer .	動物たちと遊び回り、鳥たちと飛び回り、シンガポール・フライからシティー・ビューを楽しみましょう。
Then discover Sentosa and the Universal Studios , to see Shreks castle and the roller coasters .	そして次はセントサとユニバーサル・スタジオを発見し、シュレックの城とローラー・コースターを見に行きましょう。
Plan your trip now for animals , thrills and spills that will surely put a smile on your face .	笑顔がこぼれるような、動物とエキサイティングな体験の旅を今すぐ計画しましょう。
# NTU-MC/maxwell-road-hawker-centre
Experience an authentically Singaporean dining experience by having a meal at a food centre here .	フードセンターで食事をし、シンガポール人になった気分を味わいましょう。
Located in the heart of Chinatown , Maxwell Road Hawker Centre has over 100 stalls , providing one of the biggest varieties of local food in Singapore .	チャイナタウンの中心にある「マックスウェル・ロード・ホーカーセンター」には、100以上もの屋台があります。ここは、シンガポール国内で最も多くの地元料理が楽しめる場所の一つと言えます。
Even with the influx of vendors , the stalls offerings are very varied and you will easily spoilt for choice here .	お店の数が多いこともさることながら、各屋台が提供するメニューの種類も豊富なので、選択肢に困ることは全くありません。
Some must-try items here at Maxwell Road Hawker Market include the famous Tian Tian Chicken Rice , the traditional congee with pork and century egg from Zhen Zhen Porridge stall and the popular char kway teow from the Marina South Delicious Food stall .	「マックスウェル・ロード・ホーカー・マーケット」で絶対に試しておきたいアイテムの一つは、「真真粥品（ZhenZhenPorridge）」で食べられる、伝統的なお粥に豚肉やセンチュリーエッグが入ったテンテン・チキンライスです。人気の「マリーナ・サウス・デリシャス・フード」のチャー・クェイ・ティオもお勧めです
```

Gale-Church Algorithm
====

Sentence alignment is a pre-processing task for Machine Translation or Crosslingual NLP tasks. The length based approach for sentence alignment are attractive because it is language independent; it can be carried out without external knowledge/data such as bilingual dictionary or human-aligned sentence pairs.  
[Gale-Church (1993)](http://acl.ldc.upenn.edu/J/J93/J93-1004.pdf) one such length-based methods. It works on the principle that equivalent sentences should roughly correspond in length—that is, longer sentences in one language should correspond to longer sentences in the other language. It assume that each character in the source language generates c characters in the target
language (aka mean) with variance, s2 and distance function:

```
δ = (len(source_sentence) − len(target_sentence)*c) / sqrt(len(source_sentence)*s2)
```

By defining the prior probabilities for different alignment types P(aligntype):

```
P(aligntype = 1 : 1) = 0.89   # 1 source sentence aligns with 1 target sentence
P(aligntype = 1 : 0) = 0.0099 # 1 source sentence aligns with no target sentence
P(aligntype = 0 : 1) = 0.0099 # no source sentence aligns with 1 target sentence
P(aligntype = 2 : 1) = 0.089  # 2 source sentences aligns with 1 target sentence
P(aligntype = 1 : 2) = 0.089  # 1 source sentence aligns with 2 target sentences
P(aligntype = 2 : 2) = 0.011  # 2 source sentences aligns with 2 target sentences
```

The Gale-Church algorithm calculate the alignment cost (aka penalty) for all possible sentence pairs:

```
logP(aligntype)P(δ|aligntype)
```

Attribution
====

This code is largely based on https://github.com/vchahun/galechurch 

Citation
====
The technical manual for GaChalign and the experiment results can be found in https://db.tt/LLrul4zP

To cite the GaChalign software or the technical manuscript or a scientific paper describing the software, please use:

Liling Tan and Francis Bond. 2014. NTU-MC Toolkit: Annotating a Linguistically Diverse Corpus. In Proceedings of 25th International Conference on Computational Linguistics (COLING 2014). Dublin, Ireland. 

```
@InProceedings{tan-bond:2014:ColingDemo,
  author    = {Tan, Liling  and  Bond, Francis},
  title     = {NTU-MC Toolkit: Annotating a Linguistically Diverse Corpus},
  booktitle = {Proceedings of COLING 2014, the 25th International Conference on Computational Linguistics: System Demonstrations},
  month     = {August},
  year      = {2014},
  address   = {Dublin, Ireland},
  publisher = {Dublin City University and Association for Computational Linguistics},
  pages     = {86--89},
  url       = {http://www.aclweb.org/anthology/C14-2019}
}
```
