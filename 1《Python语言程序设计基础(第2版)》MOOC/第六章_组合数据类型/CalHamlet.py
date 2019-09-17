#CalHamlet.py
def getText():
    txt = open("Hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"##$%&()*+，./:;<=>?@[]\\^_{}':
        txt = txt.replace(ch, " ")
    return txt

def main():
    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    item  = list(counts.items())#元组的形式存储
    item.sort(key = lambda x:x[1], reverse = True)

    for i in range(10):
        word, count = item[i]
        print("{0:<10}{1:>5}".format(word, count))
main()
