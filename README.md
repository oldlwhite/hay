<h1>这是一个操控chromenium的库</h1>
b=browser(headless=True,ignoreHTTPSErrors=True) 创建一个浏览器，<br>
默认参数headless=True,bool开启无头浏览器<br>
默认参数ignoreHTTPSErrors=True，忽略https错误<br>

b.goto(url,timeout=20,wait=False)     打开网址 <br>
必须参数url，<br>
默认参数 timeout=20，等待加载完毕最高等待20秒<br>
默认参数 waitlevel=1, 等待级别，0为domload 触发事件结束,1为load 触发事件结束,2为连接数量不超过2个结束,3为没有连接结束参数给定列表多值，则触发所有列表内事件结束<br>
<br>
b.content  返回网页源码<br>
<br>
b.cookies   返回cookies <br>
<br>
b.send(selector,text) 对网页元素发送内容<br>
必须参数selecotr, css选择器<br>
必须参数text    ,发送的内容<br>
<br>
b.click(selector,waitlevel=1,timeout=20) 点击网页元素<br>
必须参数 selecotr ,css选测器<br>
默认参数 timeout=20，默认等待20秒<br>
默认参数 waitlevel=1, 等待级别，0为domload 触发事件结束,1为load 触发事件结束,2为连接数量不超过2个结束,3为没有连接结束参数给定列表多值，则触发所有列表内事件结束</text><br>
