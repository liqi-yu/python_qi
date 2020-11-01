"""
@author：hynev
@datetime：2019/11/28 19:47
"""
from urllib import parse,request
# pip install requests
import requests
import json
import os


def main():
  base_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1554457680964"
  headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
  }
  resp = requests.get(base_url,headers=headers)
  result = json.loads(resp.text)
  objectList = result['List']
  img_url_list = []
  for object in objectList:
    for x in range(1,9):
      imgNo = "sProdImgNo_" + str(x)
      img_url = object[imgNo]
      img_url = parse.unquote(img_url)
      img_url = img_url.replace("200", "0")
      img_url_list.append(img_url)
    hero_name = object['sProdName']
    hero_name = parse.unquote(hero_name)
    base_dir_name = os.path.dirname(__file__)
    # 获取文件夹路径
    hero_dir_name = os.path.join(base_dir_name, "images", hero_name)
    # 创建文件夹
    os.mkdir(hero_dir_name)
    for index,img_url in enumerate(img_url_list):
      request.urlretrieve(img_url,os.path.join(hero_dir_name,"%s.jpg"%index))



if __name__ == '__main__':
    main()
