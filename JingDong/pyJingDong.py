import requests
from bs4 import BeautifulSoup


def get(i):
    # req = requests.get('https://search.jd.com/Search?keyword=笔记本&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page='+str(i)+'&s=1&click=0')

    req = requests.get('https://search.jd.com/Search?keyword=笔记本&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1&s=1&click=0')
    req.encoding='utf-8'
    req_text = req.text
    print(req_text)
    bs = BeautifulSoup(req_text, 'html.parser')
    gl_item_list = bs.find_all('li', attrs={'class': 'gl-item'})
    print(len(gl_item_list))

    for gl_item in gl_item_list:
        name = gl_item.find_all('div', attrs={'class', 'p-name p-name-type-2'})
        print(name[0].find('em').text)
        print(name[0].find('a')['href'])
        strong=gl_item.find('div', attrs={'class', 'p-price'}).find('strong')
        price = strong.find('i').text
        if price == '':
            price = strong['data-price']
        print(price, strong.find('em').text)

if __name__ == '__main__':
    # for i in range(2):
    #     if i % 2 == 0:
    #         continue
    #     get(i)
    req = requests.get('https://search.jd.com/s_new.php?keyword=笔记本&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=2&s=27&scrolling=y&log_id=1534312319.28849&tpl=1_M&show_items=8477015,5512841,5225346,7435156,7512626,7649997,7341442,7418428,4335139,6736174,7632577,5148309,6463288,6072622,7275691,7271737,6888588,5029717,5148299,4752515,8177706,6830412,7555189,3948470,5363894,7102519,7044365,7886481,7748324,6949959')
    req.encoding='utf-8'
    req_text = req.text
    print(req_text)
