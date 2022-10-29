import random
print("こんにちは。これは、コンピュータと１対１でかぶったらだめよゲームです")
print("持ち札の言葉を選んでいき、被った時点でアウトです")
print("一度使った持ち札は再度使用することはできません")
print("あなたがコンピュータと被らない回数がいつまで続くのか・・・")
print("記録更新を目指して頑張ってください")

prayername=input("あなたの名前を教えてください。")
print("あなたの名前は",prayername,"さんですね。")

a="music音楽"
b="fruitsフルーツ"
c="food食べ物"
d="country国名"
e="prefectures都道府県"
#genreという変数に代入する値を入力してもらう
genre=input("好きなジャンルを",a,b,c,d,e,"の中から教えてください。")

print(prayername, "さんは", genre, "がお好きなんですね。")
print("ここからゲームが始まります")
print("準備はよろしいですか？")
print("よーいドン！")

prayer=input("都道府県名")
