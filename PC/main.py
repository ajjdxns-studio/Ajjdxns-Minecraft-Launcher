'''
Ajjdxns minecraft launcher
(C) 2024 Ajjdxns
'''

import os
from console_start import console
import requests
import zipfile
import json
import logging
from tqdm import tqdm
from rich.table import Table

logging.basicConfig(level=logging.INFO,format='[%(asctime)s][%(threadname)s/%(levelname)s]%(message)s')
UserHeads = {"requestUser":"true"}
log = logging.getLogger('MainLogger')

def start():
    pass

def debug(func):
    def wrapper():
        logging.debug("run {}()".format(func.__name__))
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
        elif command == 'download minecraft':
            #下载
            log.info("游戏开始下载...")
            with open(r'minecraft.zip','w') as f:
                f.write('')
            download('https://ajjdxns.github.io/download/default.zip','minecraft.zip')
            log.info("主文件下载完成。")
            log.info('即将开始解压文件至"./.minecraft/defaultversion"文件夹（应该没人会往里面放什么东西吧）。')
            with zipfile.ZipFile("minecraft.zip",'r') as f:
                for file in f.namelist():
                    log.info("输出文件：", file)
                    f.extract(file,"./.minecraft/defaultversion/")  
            
        elif command == 'start game':
            start()

        elif command == 'login':
            #登录
            log.info("开始登录...")
            log.info("正在读取配置文件...")
            try:
                with open('config.json') as f:
                    config = json.load(f)
            except:
                log.error("对不起，您使用了错误的方法打开程序，请重新尝试。")
                os._exit()
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
            UserName = console.input("请输入账号：")
            PassWord = console.input("请输入密码：")
            log.info("开始登录")
            sendlogin = {
                "username":UserName,
                "password":PassWord,
                "clientToken":"ajjdxnsminecraftlauncher",
                "requestUser":False,
              	"agent":{
                    "name":"Minecraft",
                    "version":1
                }
            }
            sendloginjson = json.dumps(sendlogin)
            loginbackjson = requests.post(APIRoot+"/authserver/authenticate",data=sendloginjson)
            loginback = json.loads(loginbackjson.text)
            if loginback['selectedProfile'] == '':
                log.warn('登录失败，请重试')
                continue
            config['login']['accessToken'] = loginback['accessToken']
            log.info('登录成功！可以启动游戏了！')

if __name__ == "__main__":
    main()