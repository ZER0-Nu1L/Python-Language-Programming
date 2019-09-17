#MatchAnalysisSports.py
import random
def main():
    printIntro()
    proA, proB, n = getInputs()
    #print(proA);print(proB);print(n)
    WinA, WinB = simNGames(proA, proB, n)
    print(WinA);print(WinB)
    printSummary(WinA, WinB)

def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n

def simNGames(proA, proB, n):
    winA, winB = 0.0, 0.0
    for i in range(n):
        scoreA, scoreB =  simOneGame(proA, proB)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1
    return winA, winB
def simOneGame(proA, proB):
    serving = 'A'
    scoreA, scoreB = 0, 0
    while not GameOver(scoreA, scoreB):
        if serving == 'A':
            if random.random() < proA:
                scoreA += 1
            else:
                serving = 'B'
        elif serving == 'B':
            if random.random() < proB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def GameOver(scoreA, scoreB):
#    if scoreA == 15 or scoreB == 15:
#        return True
    return scoreA == 15 or scoreB == 15

def printSummary(winA, winB):
    print("竞技分析开始，共模拟{}场比赛".format(winA, winB))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winA, winA/(winA+winB)))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winB, winB/(winA+winB)))

main()

