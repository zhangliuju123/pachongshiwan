# -*- coding: utf-8 -*-

# Scrapy settings for lianshou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianshou'

SPIDER_MODULES = ['lianshou.spiders']
NEWSPIDER_MODULE = 'lianshou.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lianshou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENT_LIST = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
PROXY = [
    "188.168.75.254:56899",
    "51.255.28.62:53281",
    "182.253.6.234:8080",
    '213.187.118.184:53281',
    '185.118.26.10:80',
    '50.201.51.216:8080',
    '109.87.30.193:21776',
    '5.189.155.221:80',
    '5.135.164.72:3128',
    '79.111.13.155:50625',
    '212.83.164.85:80',
    '94.242.58.108:1448',
    '140.227.63.122:3128',
    '139.255.129.252:8080',
    '41.222.226.44:80',
    '213.216.73.44:36127',
    '176.215.236.110:3128',
    '139.255.16.171:31773',
    '190.147.208.143:8080',
    '94.242.58.14:1448',
    '37.235.167.66:53281',
    '52.79.239.229:3128',
    '94.242.58.14:10010',
    '190.131.254.91:3128',
    '189.91.231.43:3128',
    '195.208.172.70:8080',
    '176.193.15.94:8080',
    '94.242.57.136:10010',
    '94.242.58.142:10010',
    '5.178.217.227:43779',
    '113.161.173.10:3128',
    '101.50.1.2:80',
    '5.9.58.22:3128',
    '202.179.190.210:8080',
    '82.135.245.222:50739',
    '212.233.232.54:32231',
    '165.165.248.90:8080',
    '188.133.180.25:8080',
    '200.107.35.154:53281',
    '185.22.172.94:10010',
    '94.242.59.135:10010',
    '62.210.149.33:10534',
    '80.87.32.30:8080',
    '185.9.86.186:39345',
    '88.87.72.72:8080',
    '188.35.167.7:45619',
    '45.251.228.122:41418',
    '91.214.31.234:8080',
    '95.87.220.19:15600',
    '203.99.123.25:61502',
    '176.115.197.118:8080'
    '75.146.218.153:55768',
    '75.151.213.85:8080',
    '193.242.178.50:52376',
    '212.200.246.24:80',
    '182.23.7.226:8080',
    '94.242.55.108:1448',
    '198.71.197.159:80',
    '89.189.130.103:32626',
    '36.67.39.47:8080',
    '52.206.108.231:3128',
    '187.95.34.10:8080',
    '176.227.188.66:53281',
    '137.74.254.242:3128',
    '83.215.180.178:32759',
    '185.3.68.239:42672',
    '103.15.51.160:8080',
    '186.47.82.82:53281',
    '217.19.209.253:8080',
    '187.44.1.167:8080',
    '42.115.88.220:53281',
    '188.43.4.117:60577',
    '167.114.180.102:8080',
    '70.35.213.229:36127',
    '93.87.17.1:53281',
    '190.202.24.66:3128',
    '92.61.93.210:31310',
    '213.59.153.19:53281',
    '197.243.34.228:3128',
    '110.50.85.174:8080',
    '92.50.142.70:8080',
    '94.242.59.135:1448',
    '186.42.215.30:53281',
    '103.228.117.244:8080',
    '181.115.241.90:80',
    '146.158.1.63:53281',
    '95.73.62.13:32185',
    '128.199.139.32:8080',
    '116.90.236.126:31284',
    '88.99.149.188:31288',
    '95.158.137.254:57477',
    '188.168.69.186:80',
    '84.19.38.158:51885',
    '94.242.58.142:1448',
    '177.75.161.206:3128',
    '176.221.165.250:31820',
    '188.43.52.166:47362',
    '42.115.88.71:62225',
    '109.173.73.116:8080',
    '200.255.122.170:8080',
    '61.91.189.170:8080',
    '51.38.234.95:8080',
    '188.211.226.118:53281',
    '151.80.65.175:3128',
    '119.28.37.58:80',
    '185.22.172.94:1448',
    '95.210.251.29:53281',
    '94.242.58.108:10010',
    '41.222.226.47:80',
    '95.171.198.206:8080',
    '200.107.59.98:53281',
    '212.22.86.107:3130',
    '195.189.60.23:3128',
    '92.222.83.160:80',
    '24.245.100.212:48678',
    '43.251.170.145:54059',
    '194.38.137.252:3128',
    '85.11.114.135:3128',
    '178.206.224.176:3128',
    '37.187.121.205:3128',
    '185.107.143.99:8080',
    '185.22.174.69:10010',
    '51.38.71.101:8080',
    '46.63.104.139:8080',
    '221.7.255.168:8080',
    '91.203.125.46:8081',
    '36.67.37.203:8080',
    '94.242.57.136:1448',
    '195.91.132.20:19600',
    '193.86.229.230:8080',
    '117.239.146.106:3128',
    '167.99.61.138:3128',
    '54.39.16.236:31289',
    '181.211.191.227:8080',
    '103.78.74.170:3128',
    '178.128.119.73:80',
    '94.242.55.108:10010',
    '164.77.147.93:53281',
    '190.151.94.2:46615',
    '185.91.190.90:8888',
    '176.214.80.153:8080',
    '117.239.218.229:3128',
    '188.235.147.252:32231',
    '101.4.136.34:8080',
    '115.84.179.229:443',
    '185.9.137.114:80',
    '101.255.120.170:6969',
    '60.250.79.187:80',
    '195.239.248.220:8080',
    '117.55.209.126:8080',
    '91.217.202.174:8080',
    '122.155.222.98:3128',
    '202.93.128.98:3128',
    '117.55.209.123:8080',
    '36.37.134.18:80'

]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lianshou.middlewares.LianshouSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'lianshou.middlewares.LianshouDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'lianshou.middlewares.RotateUserAgentMiddleware': 400,
    'lianshou.middlewares.QiDianSeleniumDownloadeMiddleWare': 405
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lianshou.pipelines.LianshouPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DB_SET_MAP = {
    # 'user': 'root',
    # 'passwd': '970215',
    # 'host': '192.168.50.5',
    # 'port': '3306',
    # 'db': 'orange_shop',
    'user': 'root',
    'passwd': 'root',
    'host': '127.0.0.1',
    'port': '3306',
    'db': 'pachong',
}
