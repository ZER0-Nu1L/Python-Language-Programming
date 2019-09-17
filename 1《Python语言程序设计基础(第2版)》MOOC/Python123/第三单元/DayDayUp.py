#DayDayUp.py
dayupA = pow(1+0.01, 365)

def DayUp(df):
    scale = 0.01
    dayup = 1.0
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup *= 1 - scale
        else:
            dayup *= 1 + df
    return dayup

hardwork = 0.01
while(DayUp(hardwork) < dayupA):
    hardwork += 0.001

print("{:.3f}".format(hardwork))
