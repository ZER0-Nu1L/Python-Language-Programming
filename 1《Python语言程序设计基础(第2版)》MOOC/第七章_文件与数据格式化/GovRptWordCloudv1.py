#GovRptWordCloudv1.py
import jieba
import wordcloud
from scipy.misc import imread

mask = imread("timg.jpg")
f = open("新时代中国特色社会主义.txt", "r", encoding = "gb18030")
txt = f.read()
f.close()
lst = jieba.lcut(txt)
txt = " ".join(lst)
w = wordcloud.WordCloud(font_path = 'MSYH.TTC', width = 1000,\
                        height =700, background_color = 'white',\
                        mask = mask,)
w.generate(txt)
w.to_file("grwordcloud1.png")
