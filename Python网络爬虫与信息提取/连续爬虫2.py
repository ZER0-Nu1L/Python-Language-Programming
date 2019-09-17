import requests
import time
def crawler(url,num):
    start_time=time.time()
    for i in range(1,num):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            #print(r.text)
        except:
            print('Exception')
        else:
            print('第{}次'.format(i))
    end_time=time.time()
    print(end_time - start_time)
 
url='https://www.baidu.com'
crawler(url,101)
