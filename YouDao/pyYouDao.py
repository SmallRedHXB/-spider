import urllib.request
import urllib.parse
import time
import random
import hashlib


def Search(i):
    timestamp = int(time.time() * 1000 + random.randint(0, 10))

    client = 'fanyideskweb'
    salt = timestamp
    D = "ebSeFb%=XZ%T[KZ)c(sy!"

    sign = hashlib.md5((client + i + str(salt) + D).encode('utf-8')).hexdigest

    data = {
        'i': i,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': client,  # 'fanyideskweb',
        'salt': timestamp,  # '1522738287898',
        'sign': sign,  # 'df1dcadc0b98e9fdc9a410f7ffa50079',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false',
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    res=urllib.request.Request(url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null',
                               method='POST', data = data)
    response = urllib.request.urlopen(res)
    return response.read()#.decode('utf-8')
    # print(response.read().decode('utf-8'))

if __name__ == '__main__':
    i = input('请输入要翻译的内容：')
    res = Search(i)
    print(res)




