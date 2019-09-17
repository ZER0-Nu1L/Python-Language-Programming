#BMI.py
height, weight = eval( input("") )
BMI = weight / height ** 2
print("BMI数值为:{:.2f}".format(BMI))

if BMI > 30:
    print("BMI指标为:国际'肥胖',国内'肥胖'")
elif BMI > 28:
    print("BMI指标为:国际'偏胖',国内'肥胖'")
elif BMI > 25:
    print("BMI指标为:国际'偏胖',国内'偏胖'")
elif BMI > 24:
    print("BMI指标为:国际'正常',国内'肥胖'")
elif BMI > 18.5:
    print("BMI指标为:国际'正常',国内'正常'")
else:
    print("BMI指标为:国际'偏瘦',国内'偏瘦'")
