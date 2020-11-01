from aip import AipSpeech
#from playsound import playsound
#from IPython.display import Audio

APP_ID='22449036'
API_KEY='pmWWOEXgwy8lHozplI9gQhtk'
SECRET_KEY='53T7PPvdVP7w0IsMi82SK14fqV2OQKBY'

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
'''
s='你好，百度'
speak=client.synthesis(s,'zh',1,{'vol': 5})

if not isinstance(speak,dict):
    with open('myspeech.mp3','wb') as f:
        f.write(speak)
    #print('speaking...')
    #playsound('my.mp3')
'''
result=client.synthesis('你好，中国','zh',1,{
    'vol': 5,
    'per': 3
})
if not isinstance(result,dict):   #网络请求的问题
    with open('auido.mp3','wb') as f:
        f.write(result)
        print('ok')
#Audio('auido.mp3')