"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
import math

def test(num):
    for i in range(2,num+1):
        if num %i ==0:
            return i
    
        
num = int(input("请输入需要检测的数字："))
source = num
n = [1]
m = ("")
run = True

while test(num) != num:
    n.append(test(num))
    i = test(num)
    num = int(num/i)
for i in range(len(n)):
    m += str(n[i]) + " * "
m+= str(num)
print("%d=%s" % (source, m))

print("Done")
    
    
