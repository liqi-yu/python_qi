# -*- coding: utf-8 -*- 
# @Time : 2020/10/20 14:37 
# @Author : 余礼奇 
# @File : 多线程爬取王者荣耀高清壁纸_v2.py



import requests
from urllib import parse
import os
from urllib import request
import threading
import queue

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36','cookie': 'RK=FZ6ku9E3UC; ptcz=408210ab7c3a6f2ca9c52e8d67bd5c786f2bc3320cee5f4cbdb1a48e3a9bf6e0; pgv_pvi=1993008128; pgv_pvid=2851668486; pac_uid=1_735260051; XWINDEXGREY=0; o_cookie=735260051; eas_sid=H1e5s9f053V3Y3T2L3A9B659R2; iip=0; pgv_info=ssid=s7946080640; LW_sid=q106c0E3m14731g3t3Q6C7u0m4; LW_uid=r126R0B3F1B7g1W3A336t7X1a1; pgv_si=s71010304; pvpqqcomrouteLine=index_wallpaper_wallpaper_wallpaper_wallpaper_wallpaper_wallpaper'
}

class Producer(threading.Thread):
    def __init__(self,page_queue,image_queue,*args,**kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue=page_queue
        self.image_queue=image_queue

    def run(self) -> None:          #是返回None的意思，可以不写
        while not self.page_queue.empty():
            page_url=self.page_queue.get()
            resp = requests.get(page_url, headers=headers)
            # print(resp.json())
            result = resp.json()
            datas = result['List']
            for data in datas:
                image_urls = extract_imgges(data)
                name = parse.unquote(data['sProdName']).replace("1:1", "").strip()  # 删掉文件名里的英文冒号，空格
                # print(name)
                # print(image_urls)
                dirpath = os.path.join('images', name)
                if not os.path.exists(dirpath):
                    os.mkdir(dirpath)
                for index,image_url in enumerate(image_urls):
                    self.image_queue.put({'image_url':image_url,'image_path':os.path.join(dirpath,'%d.jpg'%(index+1))})



class Consumer(threading.Thread):
    def __init__(self,image_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.image_queue=image_queue

    def run(self) -> None:
        while True:
            try:
                image_obj = self.image_queue.get(timeout=10)
                image_url = image_obj.get('image_url')
                image_path = image_obj.get('image_path')
                try:
                    request.urlretrieve(image_url,image_path)
                    print(image_path + '下载完成')
                except:
                    print(image_path+'下载失败')
            except:
                break




def extract_imgges(data):
    image_urls=[]
    for x in range(1,9):
        image_url=parse.unquote(data['sProdImgNo_%d'%x]).replace("200", "0")
        image_urls.append(image_url)
    return image_urls



def main():
    os.mkdir('images')
    image_queue=queue.Queue(1000)   #总的图片数目，自己预估，也可以尽可能的多些
    page_queue=queue.Queue(10)      #存着页面的队列，可以修改
    for x in range(0,10):
        page_url='https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={page}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1603174442970'.format(page=x)
        page_queue.put(page_url)

    for x in range(3):
        th=Producer(page_queue,image_queue,name='生产者%d号'%x)
        th.start()

    for x in range(5):
        th=Consumer(image_queue,name='消费者%d号'%x)
        th.start()



if __name__ == '__main__':
    main()




