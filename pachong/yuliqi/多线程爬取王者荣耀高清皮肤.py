# -*- coding: utf-8 -*- 
# @Time : 2020/10/20 13:37 
# @Author : 余礼奇 
# @File : 多线程爬取王者荣耀高清皮肤.py
#通过https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=4&totalpage=0&page=0&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17106800022943651303_1603171852431&iAMSActivityId=51991&_everyRead=true&iTypeId=1&iFlowId=267733&iActId=2735&iModuleId=2735&_=1603171852588
#可以获取到高清壁纸的url
#获取高清的url后，通过parse.unquote可以进行解码，然后将最后的200改为0，就可以得到真实的高清壁纸的图片
#获取图片的url里有一个page参数，修改page值可以翻页，默认从0开始
#page最多只有23页，因此区间为【0，22】
# from urllib import parse
# result=parse.unquote('http%3A%2F%2Fshp.qpic.cn%2Fishow%2F2735102010%2F1603161756_84828260_6594_sProdImgNo_3.jpg%2F200')
# http://shp.qpic.cn/ishow/2735102010/1603161873_84828260_28416_sProdImgNo_8.jpg/0
# http://shp.qpic.cn/ishow/2735102010/1603161756_84828260_6594_sProdImgNo_3.jpg/200
# print(result)

import requests
from urllib import parse
import os
from urllib import request

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','cookie': 'RK=FZ6ku9E3UC; ptcz=408210ab7c3a6f2ca9c52e8d67bd5c786f2bc3320cee5f4cbdb1a48e3a9bf6e0; pgv_pvi=1993008128; pgv_pvid=2851668486; pac_uid=1_735260051; XWINDEXGREY=0; o_cookie=735260051; eas_sid=H1e5s9f053V3Y3T2L3A9B659R2; iip=0; pgv_info=ssid=s7946080640; LW_sid=q106c0E3m14731g3t3Q6C7u0m4; LW_uid=r126R0B3F1B7g1W3A336t7X1a1; pgv_si=s71010304; pvpqqcomrouteLine=index_wallpaper_wallpaper_wallpaper_wallpaper_wallpaper_wallpaper'
}

def extract_imgges(data):
    image_urls=[]
    for x in range(1,9):
        image_url=parse.unquote(data['sProdImgNo_%d'%x]).replace("200", "0")
        image_urls.append(image_url)
    return image_urls



def main():
    page_url='https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1603174442970'
    resp=requests.get(page_url,headers=headers)
    # print(resp.json())
    result=resp.json()
    datas=result['List']
    for data in datas:
        image_urls=extract_imgges(data)
        name=parse.unquote(data['sProdName']).replace("1:1","").strip()#删掉文件名里的英文冒号，空格
        # print(name)
        # print(image_urls)
        os.mkdir('images')
        dirpath=os.path.join(r'D:\python_work\pachong\yuliqi\images',name)
        os.mkdir(dirpath)
        for index,image_url in enumerate(image_urls):
            request.urlretrieve(image_url,os.path.join(dirpath,'%d.jpg'%(index+1)))
            # print('%s 下载完成'%(image_url))





if __name__ == '__main__':
    main()


