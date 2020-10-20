"""
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

程序分析：999999 / 13 = 76923
"""

num = int(input("请输入一个奇数"))
n = "9"
while int(n)%num != 0:
    n += "9"
print("最少需要%d个9除于%s的结果为整数" % (len(n), num))