import random

number = random.randint(1,100) #1~100のランダムな整数。
if number == 1:         #1なら当たり。
    print("1等　当たり")
elif number <= 3:      #2,3なら当たり。
    print("2等　当たり")
elif number <= 5:      #4,5なら当たり。
    print("3等　当たり") 
elif number <= 8:      #6,7,8ら当たり。
    print("4等　当たり") 
elif number < 12:       #9,10,11なら当たり。
    print("5等　当たり") 
else:
    print("はずれ") 