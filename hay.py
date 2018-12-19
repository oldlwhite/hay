import asyncio
import time
from pyppeteer.launcher import launch
from pyppeteer import errors
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
class browser():
    def __init__(self,headless=True,ignoreHTTPSErrors=True):
        self.headless=headless
        self.ignoreHTTPSErrors=ignoreHTTPSErrors
        self.loop=asyncio.get_event_loop()
    def goto(self,url,timeout=20,waitlevel=1):
        if not hasattr(self, "browser") or not hasattr(self, "page"):
            self.browser,self.page=self.loop.run_until_complete(self.__create_browser(headless=self.headless,ignoreHTTPSErrors=self.ignoreHTTPSErrors))
        self.loop.run_until_complete(self.__goto(url,timeout=timeout,waitlevel=waitlevel))
    async def __content(self):
        return await self.page.content()
    def send(self,selector,text):
        self.loop.run_until_complete(self.__send(selector,text))
    async def __send(self,selector,text):
        await self.page.type(selector,text)
    def click(self,selector,waitlevel=1,timeout=20):
        self.loop.run_until_complete(self.__click(selector,waitlevel=waitlevel,timeout=timeout))
    async def __click(self,selector,waitlevel=1,timout=20):
        if type(waitlevel)==list:
            waitUntil=[]
            if 0 in waitlevel:
                waitUntil.append("domcontentloaded")
            if 1 in waitlevel:
                waitUntil.append("load")
            if 2 in waitlevel:
                waitUntil.append("networkidle2")
            if 3 in waitlevel:
                waitUntil.append("networkidle0")
        else:
            if 0 == waitlevel:
                waitUntil="domcontentloaded"
            elif 1 == waitlevel:
                waitUntil="load"
            elif 2 == waitlevel:
                waitUntil="networkidle2"
            elif 3 == waitlevel:
                waitUntil="networkidle0"
            else:
                waitUntil=[]
        await asyncio.wait([
            self.page.click(selector),
            self.page.waitForNavigation(options={'timeout': int(timeout * 1000),"waitUntil":waitUntil})
            ])
    @property
    def content(self):
        return self.loop.run_until_complete(self.__content())
    @property
    def cookies(self):
        return self.loop.run_until_complete(self.__cookies())

    async def __cookies(self):
        cookies={}
        cks=await self.page.cookies()
        for ck in cks:
            cookies[ck["name"]]=ck["value"]
        return cookies
    async def __goto(self,url,timeout=20,waitlevel=1):
        if type(waitlevel)==list:
            waitUntil=[]
            if 0 in waitlevel:
                waitUntil.append("domcontentloaded")
            if 1 in waitlevel:
                waitUntil.append("load")
            if 2 in waitlevel:
                waitUntil.append("networkidle2")
            if 3 in waitlevel:
                waitUntil.append("networkidle0")
        else:
            if 0 == waitlevel:
                waitUntil="domcontentloaded"
            elif 1 == waitlevel:
                waitUntil="load"
            elif 2 == waitlevel:
                waitUntil="networkidle2"
            elif 3 == waitlevel:
                waitUntil="networkidle0"
            else:
                waitUntil=[]
        await self.page.goto(url,options={'timeout': int(timeout * 1000),"waitUntil":waitUntil})
    async def __create_browser(self,headless=True,ignoreHTTPSErrors=True):
        browser= await launch(headless=headless,ignoreHTTPSErrors=ignoreHTTPSErrors)
        pages = await browser.pages()
        page=pages[0]
        await page.setUserAgent(DEFAULT_USER_AGENT)
        return browser,page
    async def __close_browser(self):
        await self.browser.close()
    def __del__(self):
        if hasattr(self, "browser") and hasattr(self, "page"):
            self.loop.run_until_complete(self.__close_browser())
    def exit(self):
        if hasattr(self, "browser") and hasattr(self, "page"):
            self.loop.run_until_complete(self.__close_browser()) 
if __name__ == '__main__':
# b=browser(headless=True,ignoreHTTPSErrors=True) 

# 创建一个浏览器，
# 默认参数headless=True,bool开启无头浏览器
# 默认参数ignoreHTTPSErrors=True，忽略https错误


# b.goto(url,timeout=20,wait=False)     
# 打开网址
# 必须参数url，
# 默认参数 timeout=20，等待加载完毕最高等待20秒
# 默认参数 waitlevel=1, 等待级别，
# 0为domload 触发事件结束
# 1为load 触发事件结束
# 2为连接数量不超过2个结束
# 3为没有连接结束
# 参数给定列表多值，则触发所有列表内事件结束


# b.content
# 返回网页源码


# b.cookies 
# 返回cookies 


# b.send(selector,text)
# 对网页元素发送内容
# 必须参数selecotr, css选择器
# 必须参数text    ,发送的内容

# b.click(selector,waitlevel=1,timeout=20)
# 点击网页元素
# 必须参数 selecotr ,css选测器
# 默认参数 waitlevel=1, 等待级别，
# 0为domload 触发事件结束
# 1为load 触发事件结束
# 2为连接数量不超过2个结束
# 3为没有连接结束
# 参数给定列表多值，则触发所有列表内事件结束
# 默认参数 timeout=20，默认等待20秒
