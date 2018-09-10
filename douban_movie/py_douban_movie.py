import requests
import json
import xlwt

j = 1
def spider_doubang_movie(worksheet, type, limit = 1000):
    url = 'https://movie.douban.com/j/chart/top_list?type='+ str(type) +'&interval_id=100%3A90&action=&start=0&limit=1000'
    response = requests.get(url)

    res = response.content.decode('utf-8')

    js = json.loads(res)

    for i in js:
        global j
        # print(i)
        print(j, ':', i['title'])
        print(i['url'])
        print(i['score'])
        print(i['types'])
        print(i['actors'])
        print('*' * 80)
        worksheet.write(j, 0, j)
        worksheet.write(j, 1, i['title'])
        worksheet.write(j, 2, i['url'])
        worksheet.write(j, 3, i['score'])
        worksheet.write(j, 4, i['types'])
        worksheet.write(j, 5, i['release_date'])
        worksheet.write(j, 6, i['is_playable'])
        worksheet.write(j, 7, i['actors'])
        j += 1

if __name__ == '__main__':
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('movie')
    worksheet.write(0, 0, 'movieid')
    worksheet.write(0, 1, 'moviename')
    worksheet.write(0, 2, 'movieurl')
    worksheet.write(0, 3, 'moviescore')
    worksheet.write(0, 4, 'movietypes')
    worksheet.write(0, 5, 'movie_release_date')
    worksheet.write(0, 6, 'movie_s_playable')
    worksheet.write(0, 7, 'movieactors')

    for i in range(20):
        spider_doubang_movie(worksheet, i)
    workbook.save('movie.xls')
    # spider_doubang_movie('', 4)