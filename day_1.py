import random
secret = random.randint(1,10)
count = 0
print('-------------AHUT CS--------------')
temp = input('猜一个数字：')   
guess = int(temp)
if guess == secret:
    print("猜对了！")
while guess != secret:    
    if guess > secret:
        print("大了！大了！~~")
        temp = input('重新输入一次吧：')
        guess = int(temp)
    else:
        print("小了！小了！~~")
        temp = input('重新输入一次吧：')
        guess = int(temp)
print('游戏结束啦！')
