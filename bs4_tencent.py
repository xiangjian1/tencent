#coding:utf8
from bs4 import BeautifulSoup
import requests
import urllib2
import json

base_url = 'http://hr.tencent.com/position.php?start='
headers = {
    "Host" : "hr.tencent.com",
    "Connection" : "keep-alive",
    "Pragma" : "no-cache",
    "Cache-Control" : "no-cache",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Upgrade-Insecure-Requests" : "1",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #"Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-CN,zh;q=0.8",
    "Cookie" : "PHPSESSID=f5acq8estgloi0kf3mq08fp376; pgv_info=ssid=s6388083265; ts_last=hr.tencent.com/position.php; pgv_pvid=4199643208; ts_uid=7666324899"

}
#response = requests.get(base_url,headers=headers)

with open('position.json','w') as f:
    for i in range(0,100,10):
        fullurl = base_url + str(i)
        request = urllib2.Request(fullurl,headers=headers)
        response = urllib2.urlopen(request)
        html = BeautifulSoup(response,'lxml')
        tr_list = html.select('tr[class="even"] , tr[class="odd"]')

        for tr in tr_list:
            item = {}
            td_list = tr.find_all('td')
            item['position_name'] = td_list[0].text
            item['position_type'] = td_list[1].text
            item['position_num'] = td_list[2].text
            item['location'] = td_list[3].text
            item['time'] = td_list[4].text
            item['href'] = td_list[0].a['href'] # 提取连接地址

            f.write(json.dumps(item,ensure_ascii=False).encode('utf-8') + '\n')



