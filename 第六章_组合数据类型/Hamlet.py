#Hamlet.py
def main():
    txt = getText("Hamlet.txt")
    counts = {}
    item = Statistics(txt, counts)
    printInfo(item)

def getText(file):
    f = open(file, "r")
    txt = f.read()
    txt = txt.lower()
    for ch in '~!@#$%^&*()_+|}{:?><",./;[]\=-`':
        txt.replace(ch, "")
    f.close()
    return txt

def Statistics(txt, counts):
    words = txt.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    item = list(counts.items())
    item.sort(key = lambda x:x[1], reverse = True)#
    return item

def printInfo(item):
    for i in range(10):
        word, count = item[i]
        print("{:<10} {:>5}".format(word, count))
main()
