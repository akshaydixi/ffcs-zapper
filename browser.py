import mechanize
import subprocess
from PIL import Image
import cookielib
from BeautifulSoup import BeautifulSoup
import sys
import time
class Browser:
    def __init__(self,url=None):
        self.browser = mechanize.Browser()
        self.cj = cookielib.LWPCookieJar()
        self.browser.set_handle_equiv(True)
        self.browser.set_handle_redirect(True)
        self.browser.set_handle_referer(True)
        self.browser.set_handle_robots(False)
        if(url):
            self.response = self.browser.open(url)
    def open(self,url):
        try:
            self.response = self.browser.open(url)
        except Exception,e:
            print '[-] Error: ',str(e)
    def read(self):
        try:
            return self.response.read()
        except Exception,e:
            print '[-] Error: ',str(e)
            return
    def getSoup(self):
        try:
            soup = BeautifulSoup(self.response.read())
            return soup
        except Exception,e:
            print '[-] Error: ',str(e)
    def getBrowser(self):
        return self.browser



def saveCaptcha(br,captchaurl):
   with open('captcha.bmp','w')  as f:
        f.write(br.open_novisit(captchaurl).read())

def login(regno,passwd):
    browser = Browser()
    br = browser.getBrowser()
    br.open(mainurl)
    br.select_form(nr=0)
    br['regno']=regno
    br['passwd']=passwd
    saveCaptcha(br,captchaurl)
    p = subprocess.Popen(['display','captcha.bmp'])
    vrfcd  = raw_input('Enter Verification Code : ')
    p.kill()
    br['vrfcd']=vrfcd
    br.submit()
    soup = BeautifulSoup(br.response().read())
    print soup

mainurl = 'https://academics.vit.ac.in/student'
captchaurl = 'https://academics.vit.ac.in/student/captcha.asp'
def testing():
    regno = 'LOL'
    passwd = 'asifimthatstupid'
    login(regno,passwd)

if __name__ == '__main__':
    testing()
