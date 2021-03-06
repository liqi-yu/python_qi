import os
import requests
from bs4 import BeautifulSoup

download_path='./douban'
if not os.path.exists(download_path):
    os.makedirs(download_path)


def download_pic(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,'lxml')
    content=soup.find('div',class_='article')
    images=content.find_all('img')
    pic_link_list=[image['src'] for image in images]
    pic_name_list=[image['alt'] for image in images]
    for name,link in zip(pic_name_list,pic_link_list):
        # urlretrieve(link,f'{download_path}/{name}.jpg')
        html=requests.get(link)
        with open(f'{download_path}/{name}.jpg','wb') as f:
            f.write(html.content)
    print(f'{url}所有下载完成')


def main():
    start_urls=['https://movie.douban.com/top250']

    for i in range(1,10):
        start_urls.append(f'https://movie.douban.com/top250?start={25*i}&filter=')
    for url in start_urls:
        download_pic(url)


if __name__=='__main__':
    main()