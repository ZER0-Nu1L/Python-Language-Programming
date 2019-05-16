#词云乡村.py
import jieba
import wordcloud
from scipy.misc import imread

def main():
    txt = getText()
    mask = imread("熊 (1).jpg")
    w = wordcloud.WordCloud(font_path = 'MSYH.TTC', width = 1000,\
                        height =700, background_color = 'white',\
                        mask = mask)
    words = jieba.lcut(txt)
    txt = " ".join(words)
    w.generate(txt)
    w.to_file("熊云.png")

def getText():
    f = open("梅.txt","r", encoding = "gb18030")
    txt = f.read()
    f.close()
    return txt

main()
