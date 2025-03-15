import sys
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN

# Paths to check for web shells
Pathlist = ['/wp-includes/rest-api/about.php', '/wp-content/languages/about.php', '/wp-content/banners/about.php', '/wp-includes/Text/about.php', '/wp-includes/css/dist/niil.php', '/asd.php', '/1.php', '/ws.php', '/wp-includes/css/index.php', '/cgi-bin/wp-login.php', '/wp-content/cong.php', '/wp-admin/classwithtostring.php', '/wp-includes/images/wp-login.php', '/wp-includes/Requests/network.php', '/wp-content/radio.php', '/wp-admin/dropdown.php', '/login.php', '/hehehehe.php', '/simple.php', '/wp-includes/fonts/about.php', '/wp-content/admin.php', '/xmlrpc.php', '/atomlib.php', '/lv.php', '/wp-includes/Text/index.php', '/content.php', '/.well-known/acme-challenge/about.php', '/goat.php', '/.well-known/acme-challenge/admin.php', '/wp-content/uploads/about.php', '/wp-admin/maint/index.php', '/dropdown.php', '/sad/about.php', '/radio.php', '/wp-admin/admin.php', '/wp-includes/IXR/index.php', '/classwithtostring.php', '/install.php', '/wp-content/x/index.php', '/wp-includes/Requests/about.php', '/wp-admin/includes/index.php', '/wp-login.php', '/wp-includes/js/jcrop/Jcrop.php', '/wp-admin/images/about.php', '/wp-includes/ID3/index.php', '/wp-admin.php', '/wp-includes/assets/index.php', '/lock.php', '/index/function.php', '/.well-known/content.php', '/cong.php', '/wp-includes/js/index.php', '/wp-content/plugins/index.php', '/wp-content/index.php', '/about/function.php', '/wp-includes/customize/index.php', '/wp-admin/index.php', '/wp-content/themes/index.php', '/about.php', '/wp-includes/autoload_classmap.php', '/themes.php', '/wp-mail.php', '/cgi-bin/index.php', '/wp-content/plugins/admin.php', '/admin.php', '/wp-includes/content.php', '/wp-admin/css/index.php', '/wp-admin/images/index.php', '/wp-includes/index.php', '/wp-content/uploads/index.php', '/mah.php', '/wp-blog-header.php', '/wp-content/plugins/ioxi/alfa-ioxi.php', '/wp-admin/user/index.php', '/wp-includes/plugins.php', '/wp-includes/js/thickbox/thickbox.php', '/goat1.php', '/wp-includes/certificates/index.php', '/.well-known/index.php', '/wp-admin/network/index.php', '/wp-includes/sitemaps/providers/index.php', '/.well-knownold/index.php', '/wp-includes/js/crop/index.php', '/wp-includes/Text/Diff/index.php', '/images/index.php', '/wp-includes/widgets/index.php', '/.well-known/pki-validation/index.php', '/.well-known/acme-challenge/index.php', '/wp-includes/rest-api/index.php', '/wp-includes/pomo/index.php']


class EvaiLCode:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'}

    def URLdomain(self, site):
        if site.startswith("http://"):
            site = site.replace("http://", "")
        elif site.startswith("https://"):
            site = site.replace("https://", "")
        pattern = re.compile('(.*)/')
        while re.findall(pattern, site):
            sitez = re.findall(pattern, site)
            site = sitez[0]
        return site

    def checker(self, site):
        try:
            url = "http://" + self.URLdomain(site)
            for Path in Pathlist:
                check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
                if any(keyword in check for keyword in ["Uname:", "x3x3x3x_5h3ll", "Yanz Webshell!", "403WebShell", "{Ninja-Shell}", "FilesMAn", "Powered By Indonesian Darknet", "BlackDragon", "Upload File : <input type=\"file\" name=\"file\"", "Doc Root:", "AnonSec Shell", "UnknownSec Shell", "Shal Shell Kontol:V", "Mr.Combet Webshell", "<title>Vim Patior</title>", "Graybyt3 Was Here", "Zerion Mini Shell", "Gel4y Mini Shell", "[ HOME SHELL ]", "Current dir:"]):
                    print(f'Target: {url} --> {fg}[Successfully]')
                    open('shell.txt', 'a').write(url + Path + "\n")
                    break
                else:
                    print(f'Target: {url} --> {fr}[Failed]')
        except:
            pass

Control = EvaiLCode()

def RunUploader(site):
    try:
        Control.checker(site)
    except:
        pass

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit(f'\n  [!] Enter <{path[len(path) - 1]}> <sites.txt>')

mp = Pool(90)
mp.map(RunUploader, target)
mp.close()
mp.join()