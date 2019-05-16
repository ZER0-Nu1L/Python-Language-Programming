#CalStatistics.py
from math import sqrt
def getNum():
    nums = []
    iNumStr = input("请输入数字(直接输入回车退出)")#
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(直接输入回车退出)")
    return nums
def mean(numbers):
    sum = 0.0
    n = len(numbers)
    for num in numbers:
        sum += num
    return sum / n
def dev(numbers):
    mean_numbers = mean(numbers)
    sdev = 0.0
    count = 0
    for num in numbers:
        sdev += (mean_numbers - num)**2
    return sqrt(sdev/(len(numbers)-1))
'''
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev += (mean - num)**2
    return sqrt(sdev/(len(numbers)-1))
'''
def midian(numbers):
    sorted(numbers)
    n = len(numbers)
    return (numbers[n//2-1] + numbers[n//2])/2 if n%2 == 0 else numbers[n//2]

'''    if n % 2 == 0:
        med = (numbers[n//2-1] + numbers[n//2])/2
    else:
        numbers[n//2]
'''
def main():
    n = getNum()
    print("平均值:{:.2f},方差:{:.2f},中位数:{}".format( \
        mean(n), dev(n), midian(n)))
    print("最大值是:{}, 最小值是:{}".format(max(n), min(n)))
main()

#name 'nubmers' is not defined
