# -*- coding:utf-8 -*-
from fake_useragent import UserAgent

# 浏览器尺寸，伪装之一
windows_sizes = [
    {
        'w': 1366,
        'h': 768
    },
    {
        'w': 1600,
        'h': 900
    },
]

# 窗口大小
windows_size = None

# chrome启动地址
debugger_address = None

# chrome语言(lang=en-US,en)
lang = None

# chrome配置
chrome_arguments = [
    '--disable-blink-features=AutomationControlled',
    f'--user-agent={UserAgent().chrome}'
]
