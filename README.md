## 简介
- 采用selenium + chrome + python 开发
- 掩盖爬虫特征(不保证100%隐藏,毕竟一山还有一山高🤣)
- 自动安装chrome web driver,无需担心chrome自动更新后web driver版本不一致

### 依赖
```
pip install selenium
pip install webdriver-manager
pip install fake-useragent
```

### Tips
+ 如何启动chrome调试模式?
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222
并在ChromeConfig中配置debugger_address


### chrome部分启动参数
根据实际情况配置chrome argument
| 序号 | 参数 | 说明 |
| --- |---|---|
|1	|--allow-outdated-plugins|	不停用过期的插件。|
|2	|--allow-running-insecure-content	|默认情况下，https 页面不允许从 http 链接引用 javascript/css/plug-ins。添加这一参数会放行这些内容。|
|3	|--allow-scripting-gallery	|允许拓展脚本在官方应用中心生效。默认情况下，出于安全因素考虑这些脚本都会被阻止。|
|4	|--disable-desktop-notifications	|禁用桌面通知，在 Windows 中桌面通知默认是启用的。|
|5	|--disable-file-system	|停用 FileSystem API。|
|6	|--disable-preconnect	|停用 TCP/IP 预连接。|
|7	|--disable-remote-fonts	|关闭远程字体支持。SVG 中字体不受此参数影响。|
|8	|--disable-web-security	|不遵守同源策略。|
|9	|--disk-cache-dir	|将缓存设置在给定的路径。|
|10	|--disk-cache-size	|设置缓存大小上限，以字节为单位。|
|11	|--dns-prefetch-disable	|停用DNS预读。|
|12	|--enable-print-preview	|启用打印预览。|
|13	|--extensions-update-frequency	|设定拓展自动更新频率，以秒为单位。|
|14	|--incognito	|让浏览器直接以隐身模式启动。|
|15	|--keep-alive-for-test	|最后一个标签关闭后仍保持浏览器进程。（某种意义上可以提高热启动速度，不过你最好得有充足的内存）|
|16	|--kiosk	|启用kiosk模式。（一种类似于全屏的浏览模式）|
|17	|--lang	|使用指定的语言。|
|18	|--no-displaying-insecure-content	|默认情况下，https 页面允许从 http 链接引用图片/字体/框架。添加这一参数会阻止这些内容。|
|19	|--no-referrers	|不发送 Http-Referer 头。|
|20	|--no-startup-window	|启动时不建立窗口。|
|21	|--proxy-server	|使用给定的代理服务器，这个参数只对 http 和 https 有效。|
|22	|--start-maximized	|启动时最大化。|
|23	|--single-process	|以单进程模式运行 Chromium。（启动时浏览器会给出不安全警告）。|
|24	|--user-agent	|使用给定的 User-Agent 字符串。|
|25	|--process-per-tab	|每个分页使用单独进程。|
|26	|--process-per-site|	每个站点使用单独进程。|
|27	|--in-process-plugins|	插件不启用单独进程。|
|28	|--disable-popup-blocking|	禁用弹出拦截。|
|29	|--disable-javascript|	禁用JavaScript。|
|30	|--disable-java	|禁用Java。|
|31	|--disable-plugins|	禁用插件。|
|32	|–disable-images|	禁用图像。|

### 效果
运行test.py查看实际效果
[Intoli](intoli.png)
[sannysoft](sannysoft.png)

### 未来计划
+ 添加验证码识别

### 参考链接
https://mp.weixin.qq.com/s/Bge-_yiatSq4CQq7fRvjdQ
