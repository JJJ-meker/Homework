import requests
import parsel

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
#get post 请求
#函数编程
"""下载一个音频"""
def download_media(media_url,media_name):
    """代码块"""
    res=requests.get(media_url,headers=headers)
    with open(f'{media_name}.mp4',mode='wb') as f:
        f.write(res.content)
    
"""media_url='https://fdfs.xmcdn.com/group64/M04/5F/BF/wKgMaV12-bODtRstAB0CHeSWOOc256.m4a'  """
def media_api(trackId):
    """面向对象
        从网页中获取下载地址--请求接口
    """
    api_url=f'https://www.ximalaya.com/revision/play/v1/audio?id={trackId}&ptype=1'
    """
    ###找到接口
    """
    res=requests.get(api_url,headers=headers)
    data=res.json()
    """
    ###date 是json数据，是一个字典
        从字典中获取src
    """
    src=data['data']['src']
    return src


def get_total_page(page_url):
    res=requests.get(page_url,headers=headers)
    sel=parsel.Selector(res.text)
    sound_list=sel.css('.sound-list ul li a')
    for sound in sound_list[:30]:
        media_url=sound.css('a::attr(href)').extract_first()
        media_url=media_url.split('/')[-1]
        media_name=sound.css('a::attr(title)').extract_first()
        #print(media_url,media_name)
        yield media_url,media_name
    """
    split???[-1]最后一个，列表索引
    extract_first()用来提取里面的文字
    yield 接收
    """

if __name__=='__main__':
    """
        面向对象编程 class
    http://www.xiamalaya.com/youshengshu/16411402/p3/
    """
    for page in range(1,130):
        medias=get_total_page(f'https://www.ximalaya.com/youshengshu/28752644/p{page}')
        for media_id,media_name in medias:
            media_url=media_api(media_id)
            download_media(media_url,media_name)
        

"""print(media_api(211030401))        调试"""
"""批量下载，要批量获取接口"""

#print(res.text)

'''
Created on 2019-11-6

@author: jjj
'''
