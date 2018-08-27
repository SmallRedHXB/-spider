import requests
from bs4 import BeautifulSoup
import urllib.request



def DownLoadImg(url):
    list = url.split('/')
    file = 'doutuimg' + '/' +list[-1]
    urllib.request.urlretrieve(url, filename= file)

def GetUrl(url):
    response = requests.get(url)
    con = response.content
    soup = BeautifulSoup(con , 'lxml')
    image_list = soup.find_all('img', attrs={'class' : 'lazy image_dtb img-responsive'})
    for img in image_list:
        try:
            urlImg = img['data-original']
            if not ('http' in urlImg):
                urlImg = 'http:' + urlImg
            DownLoadImg(urlImg)
        except:
            continue


for i in range(1, 10):
    print(i)
    url = 'https://www.doutula.com/article/list/?page='+str(i)
    GetUrl(url)