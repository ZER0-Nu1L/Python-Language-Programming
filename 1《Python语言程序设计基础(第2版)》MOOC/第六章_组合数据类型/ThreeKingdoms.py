#ThreeKingdoms.py
import jieba

def main():
    txt = getText("Threekingdoms.txt")
    counts = {}
    item = Statistics(counts, txt)
    printInfo(item)

def getText(file):
    f = open(file, "r",encoding = "gb18030")
    txt = f.read()
    f.close()
    return txt

def Statistics(counts, txt):
    words = jieba.lcut(txt)
    excludes = {"主公","将军","却说","丞相","二人","不可","荆州",\
            "不能","如此","商议","如何","军士","左右","军马",\
            "引兵","次日","大喜","天下","东吴","于是","今日",\
            "不敢","魏兵","陛下","一人","都督","人马","不知",\
            "汉中","只见","众将","后主","蜀兵","上马","大叫",\
            "太守","夫人","先主","后人","背后","城中","此人",\
            "天子","一面","何不","大军","忽报"}
    for word in words:
        if len(word) == 1:
            continue
        elif word =="诸葛亮" or word == "孔明曰":
            rword = "孔明"
        elif word =="关公" or word == "云长":
            rword = "关羽"
        elif word =="玄德" or word == "玄德曰":
            rword = "刘备"
        elif word =="孟德" or word == "丞相曰":
            rword = "曹操"
        else:
            rword = word
        counts[rword] = counts.get(rword,0)+1
    for word in excludes:
        del counts[word]
    item = list(counts.items())
    item.sort(key = lambda x:x[1], reverse = True)
    return item

def printInfo(item):
    for i in range(14):
        word, count = item[i]
        print("{:<10} {:>5}".format(word, count))

main()
