import random

secret = random.randint(1, 10)
temp = input("猜一个数字：")
guess = int(temp)

while guess != secret:
    temp = input("猜错了，重新输入：")
    guess = int(temp)

    if guess == secret:
        print("猜对了!")
    else:
        if guess > secret:
            print("猜大了!")
        else:
            print("猜小了")

print("游戏结束！")

