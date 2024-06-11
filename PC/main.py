'''
Ajjdxns minecraft launcher
(C) 2024 Ajjdxns
'''

import os
from console_start import console
import requests
import zipfile
import json
import webbrowser
from tqdm import tqdm

UserHeads = {"requestUser":"true"}
with open('config.json') as con:
    config = json.load(con)

class Logger():

    def _main_(self):
        pass
    
    def input(self,msg):
        return console.input('[INPUT] '+msg)

    def tip(self,msg):
        console.print('[TIP] '+msg)

    def info(self,msg):
        console.print('[INFO] '+msg)
    
    def warn(self,msg):
        console.print('[WARN] '+msg)

    def error(self,msg):
        console.print('[ERROR] '+msg)

log = Logger()

def start():
    pass

def debug(func):
    def wrapper():
        console.print("run {}()".format(func._name_))
        return func()
    return wrapper
  
def download(url: str, fname: str):
    # 用流 stream 的方式获取 url 的数据
    resp = requests.get(url, stream=True)
    # 拿到文件的长度，并把 total 初始化为 0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的 fname 文件 (名字你来传入)
    # 初始化 tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
        ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

def downloadnew():
    log.info("开始进行新下载任务...")
    listUrl = config['download']['apiList'][config['download']['apiNumber']]['versionListUrl']
    versionList = json.loads(requests.get(listUrl).text)
    versionForUser = []
    for i in versionList['versions']:
        versionForUser.append(i)
    log.info("获取版本列表...成功")
    for v in versionForUser:
        console.print(versionForUser.index(v),"版本:",v['id'],"\n","    发行日期:",v['releaseTime'])
    wentDownload = console.input("请输入你想下载的版本前的数字：")
    version = versionForUser[int(wentDownload)]
    versionName = version['id']
    versionIndexUrl = version['url']
    console.print("0Forge\n1fabric\n2neoforge\n3不装加载器")
    loadsName = ['forge','fabric','neo','vanilla']
    loadsChose = loadsName[int(console.input("请输入你想要安装的加载器前面的数字"))]
    if loadsChose == 'forge':
        pass
    elif loadsChose == 'fabric':
        pass
    elif loadsChose == 'neo':
        pass
    else:
        installOF = not(console.input('是否需要安装optifine?(Y/n)') == 'n')
        if installOF:
            pass
        else:
            packName = console.input('请输入版本名称:')
            if os.path.exists('./.minecraft/'+packName):
                console.print('包名存在冲突！安装结束！')
            elif os.path.exists('./.minecraft'):
                os.mkdir('./.minecraft/'+packName)
            else:
                pass

command = ""

console.print("")
console.print("""
Ajjdxns minecraft launcher
Copyright (C) 2024 Ajjdxns studio
本程序没有任何保证，输入“license 15”了解更多。
这是一个自由软件，欢迎再次分发。输入“license 3”了解详情。
随程序应有一份 GPL3.0 协议，如果没有找到，从这里找：https://www.gnu.org/licenses/。

使用命令“version”查看更多协议
""")

def main():
    '''
    主要的核心程序
    '''
    while True:
        command = console.input(">>>")
        if command == "quit":
            with open('config.json','w') as con:
                json.dump(config,con)
            os._exit(1)
        elif command == "version":
            console.print("""Ajjdxns minecraft launcher
            Copyright (C) Ajjdxns studio(电子邮件：wyj121023@163.com，备用地址：ajjdxns@outlook.com)
            ver. alpha 0.1 
            
            基于 GPL 3.0 我们希望这个程序对你有用，但是不保证它真的好用。
            随程序应有一份 GPL3.0 协议，如果没有找到，从这里找：https://www.gnu.org/licenses/。以下简称 AML 启动器。
            AML 启动器根据 GPL3.0 协议，允许您进行软件破解、源代码分发以及分发破解版软件。但是破解版软件并不属于 AML 启动器的一部分，向外分发时请不要使用与本产品相近或类似的名字。在您分发该项目副本时，请注明该文件的源代码地址和分发平台。
            此外，请您遵守附加条款：
            1.修改后的代码与 Ajjdxns studio 没有任何关系，我们也不对此负责。
            2.修改后的代码中请注明代码的原作者。
            3.修改后的代码请不要用 Ajjdxns(代码作者) 的名义宣传。
            4.请让您的软件使用者明白，这个软件是基于 Ajjdxns studio 的源代码修改的，Ajjdxns studio 对其中的 BUG 概不负责。
            5.如果有涉及到钱的修改版，修改版作者将不能继续使用软件最新版进行修改，同时停止作者对修改版软件中未修改部分的支持。
            """)
        elif command == "license 15":
            console.print('''  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.''')
        elif command == "license 3":
            console.print('''  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.
  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.''')
        elif command == 'download':
            #下载
            downloadnew()
            
        elif command == 'start game':
            start()

        elif command == 'login':
            #登录
            log.info("开始登录...")
            log.info("正在读取配置文件...")
            if config['login']['useMicrosoft'] == True:
                log.warn('Minecraft迁移至微软账号的期限已过。自2020年12月起，所有新账号已经使用了新版系统，旧的账号也将在之后迁移。')
                log.info('正在尝试跳转至登录页面...')
                try:
                    webbrowser.open('https://login.live.com/oauth20_authorize.srf?client_id=00000000402b5328&response_type=code&scope=service%3A%3Auser.auth.xboxlive.com%3A%3AMBI_SSL&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf')
                except:
                    log.warn('您貌似没有浏览器呢，请使用下面的URL在浏览器中打开以继续。')
                    log.info('https://login.live.com/oauth20_authorize.srf?client_id=00000000402b5328&response_type=code&scope=service%3A%3Auser.auth.xboxlive.com%3A%3AMBI_SSL&redirect_uri=https%3A%2F%2Flogin.live.com%2Foauth20_desktop.srf')
                    log.tip('这边建议您使用微软的edge呢。')
                backurl = log.input('接下来，请输入重定向后空白页面的链接：')
                begin = backurl.find("code=") + 5
                end = backurl.find("&lc")
                code = str("")
                for i in range(begin, end):
                    code += backurl[i]
                data = {
                    "client_id": "00000000402b5328", 
                    "code": code, 
                    "grant_type": "authorization_code",
                    "redirect_uri": "https://login.live.com/oauth20_desktop.srf",
                    "scope": "service::user.auth.xboxlive.com::MBI_SSL"
                    }
                token_back = requests.post(url='https://login.live.com/oauth20_token.srf',headers={"Content-Type": "application/x-www-form-urlencoded"},data=data)
                token_json = json.loads(token_back.text)
                access_token = token_json["access_token"]
                Xbox_data = {
                    "Properties": {
                        "AuthMethod": "RPS",
                        "SiteName": "user.auth.xboxlive.com",
                        "RpsTicket": "d="+access_token
                        },
                    "RelyingParty": "http://auth.xboxlive.com",
                    "TokenType": "JWT"
                    }
                Xbox_back = requests.post(url='https://user.auth.xboxlive.com/user/authenticate',headers={"Content-Type": "application/json","Accept": "application/json"},data=Xbox_data)
            else:
                log.warn('您似乎正在使用外置登录，外置登录目前功能不稳定，有正版尽量使用正版。')
                APIRoot = config['login']['API Root']
                try:
                    RootGet = requests.get(APIRoot)
                except:
                    #出错后的用户提示
                    log.error("对不起，我们遇到了一个严重错误：网络请求错误。")
                    log.error("请尝试修改配置文件。")
                    os._exit()
                RootGetDirt = json.loads(RootGet.text)
                try:
                    log.info("服务器名称："+RootGetDirt["meta"]["serverName"])
                except:
                    log.warn('对不起，我们遇到了一个问题：服务器未返回"serverName"字段')
                UserName = log.input("请输入账号：")
                PassWord = log.input("请输入密码：")
                log.info("开始登录")
                sendlogin = {
                    "username":UserName,
                    "password":PassWord,
                    "clientToken":"",
                    "requestUser":True,
                  	"agent":{
                        "name":"Minecraft",
                        "version":1
                    }
                }
                sendloginjson = json.dumps(sendlogin)
                loginbackjson = requests.post(APIRoot+"/authserver/authenticate",json=sendloginjson)
                loginback = json.loads(loginbackjson.text)
                try:
                    test = loginback['selectedProfile']
                except:
                    log.warn('登录失败，请重试')
                    continue
                try:
                    test = loginback['availableProfiles']
                except:
                    log.warn('登录失败，该用户未绑定角色')
                    continue
                config['login']['accessToken'] = loginback['accessToken']
                log.info('登录成功！可以启动游戏了！')

if __name__ == "__main__":
    main()