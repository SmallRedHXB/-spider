from bs4 import BeautifulSoup
import requests
import csv
import time

# req=requests.get('http://hz.ganji.com/fang1/o1/') //爬取整个网页
# print(req.text)


url = 'http://hz.ganji.com/fang1/o'
urladd = 'http://hz.ganji.com'

if __name__ == '__main__':
    end_page = 50
    with open('ganjiwang.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        page = 10
        print('开始')
        while page <= end_page:
            time.sleep(1)
            print(page)
            page = page + 1

            response = requests.get(url + str(page))
            html = BeautifulSoup(response.text, 'html.parser')

            house_list = html.select('.f-list > .f-list-item > .f-list-item-wrap')

            if not house_list:
                break

            for house in house_list:
                house_title = house.select('.dd-item > a')[0].string#.encode('utf-8')
                # print(house_title)
                house_area = house.select('.dd-item > .area > a')[-1].string#.encode('utf-8')
                # print(house_area)
                house_price = house.select('.dd-item > .price > .num')[0].string#.encode('utf-8')
                # print(house_price)
                house_url = (urladd + house.select('.dd-item > a')[0]['href'])#.encode('utf-8')
                # print(house_url)
                house_detail_list=[]
                for i in range(0, 11):
                    # if i % 2 == 0:
                    #     print(i)
                    try:
                        house_detail=house.select('.dd-item > span')[i].string
                    except:
                        break
                    if  house_detail != None:
                        house_detail_list.append(house.select('.dd-item > span')[i].string)
                # print(house_detail_list)


                csv_writer.writerow([house_title, house_area, house_price, house_url]+house_detail_list)

        print('结束')


