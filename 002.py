"""
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部
分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
求应发放奖金总数？
"""

i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i ==0:
        break
    elif i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        i=arr[idx]
        print("1 %d" % r)
    elif i==arr[idx]:
        r+=(i-arr[idx+1])*rat[idx+1]
        i=arr[idx+1]
        print("2 %d" % r)
print (r)










"""
profit = int(input("清输入当月利润："))
if profit <=  100000:
    bonus = profit * 0.1
elif profit <= 200000:
    bonus = 100000* 0.1 + (profit -100000) * 0.075
elif profit <= 400000:
    bouns = 100000* 0.1 + (200000-100000) * 0.075 + (profit - 200000) * 0.05
elif profit <= 600000:
    bonus =100000* 0.1 + (200000-100000) * 0.075 + (400000 - 200000) * 0.05 + (profit - 400000) * 0.03
elif profit <= 1000000:
    bonus = 100000* 0.1 + (200000-100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + (profit - 600000) * 0.015
else:
    bonus = 100000* 0.1 + (200000-100000) * 0.075 + (400000 - 200000) * 0.05 + (600000 - 400000) * 0.03 + (1000000 - 600000) * 0.015 + (profit - 1000000)*0.01
print("应发奖金总数为：%d" % bonus)

"""
