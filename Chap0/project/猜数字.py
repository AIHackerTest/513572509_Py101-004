# -*- coding:utf-8 -*-

import random
randn= random.randint(1,20)


print("游戏规则是：")
print(" - 程序生成1—20之间的随机数，输入数字进行猜测")
print(" - 一共有十次机会，猜对会用完机会，游戏结束")

for i in range(0,10):
    inputn = int(input("输入1-20之间的数字 : "))
    if(inputn > randn):
        print("你输入的数字大了,你还剩下%d 次机会" %(9-i) )
    elif(inputn < randn):
        print("你输入的数字小了,你还剩下%d 次机会" %(9-i) )
    else:
        print("恭喜你完成游戏，一共使用 %d 次机会" %(i + 1) )
        exit(0)
print("已经用完10次机会,正确的答案是"%(randn))
