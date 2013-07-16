import mechanize
import string
import smtplib
import re
import unicodedata
from gi.repository import Gtk
from browser import Browser
from BeautifulSoup import BeautifulSoup

#------------------
HOST = "smtp.gmail.com"
SUBJECT = "SEAT KHALI"
TO = "akshaydixi@gmail.com"
FROM = "info.adixit@gmail.com"
text = "GOT IT ! SEAT KHAALI! JALDI!!"
BODY = string.join(("From : %s" % FROM,
                    "To : %s" % TO,
                    "Subject : %s" % SUBJECT,
                    "",
                    text), "\r\n")
#------------------

browser = Browser()
br = browser.getBrowser()
mainUrl = 'http://academics2.vit.ac.in/addrop/ffcs_login.asp'
captchaUrl = 'http://academics2.vit.ac.in/addrop/captcha.asp'
anextUrl ='http://academics2.vit.ac.in/addrop/courselist.asp?cropt=1&srhby=2&srhstr=cse202'
bnextUrl='http://academics2.vit.ac.in/addrop/courselist.asp?cropt=1&srhby=2&srhstr='
flow = False
objects = {}
def initialize():
    br.open(mainUrl)
    with open('captcha.bmp','w') as f:
        f.write(br.open_novisit(captchaUrl).read())

def asciify2(s):
    matches = re.findall("&#\d+;",s)
    if len(matches) > 0:
        hits = set(matches)
        for hit in hits:
            name = hit[2:-1]
            try:
                entnum = int(name)
                s = s.replace(hit,unichr(entnum))
            except ValueError:
                pass
    matches = re.findall("&\w+;",s)
    hits = set(matcheS)
    amp = "&amp;"
    hits.remove(amp)
    for hit in hits:
        name = hit[1:-1]
        if htmlentitydefs.name2codepoint.has_key(name):
            s = s.replace(hit, "")
    s = s.replace(amp,"&")
    return s



def getsoup(html):
    soup = BeautifulSoup(html)
    return soup



def hello(widget):
    global flow
    regno_text = objects['regno'].get_text()
    passwd_text = objects['passwd'].get_text()
    vrfcd_text = objects['vrfcd'].get_text()
    br.select_form(nr=0)
    br['regno']=regno_text
    br['passwd']=passwd_text
    br['vrfcd']=vrfcd_text
    br.submit()
    flow = True
    Gtk.main_quit()
def sendMail(body):
    text = body
    server = smtplib.SMTP(HOST,587)
    server.ehlo()
    server.starttls()
    server.login('info.adixit@gmail.com','thisisarandompassword')
    server.sendmail(FROM,[TO],BODY)
    server.quit()
def secondButtonPress(widget):
    global flow
    coursecode_text = objects['coursecode'].get_text()
    serialno_text = objects['serialno'].get_text()
    theUrl = bnextUrl+coursecode_text
    value = 0
    ctr = 0
    if coursecode_text == 'CSE304' :
        indexes = ['1','2','3','4']
    while True:
     r = br.open(theUrl)
     br.select_form(nr=value)
     br.submit()
     response =  br.response()
     html = response.read()
     soup = getsoup(html)
     if value == 0:
      for xserialno_text in indexes:
         tds = [a.renderContents() for a in soup.findAll('table')[2].findAll('font',attrs={'color':'black'})]
         index = (eval(xserialno_text)-1)*9 + 8
         venue = (eval(xserialno_text)-1)*9 + 3
         print tds[venue],venue

         if eval(tds[index]) > 0 : 
             body = coursecode_text + ":" +  serialno_text
             sendMail(body)
             value = 1
             continue
         else:
             ctr+=1
             print ctr
             continue
      continue
     if value == 1:
         tds = soup.findAll('td',attrs={'align' : 'center'})
         start = 5
         index = 0
         while start < len(tds):
            if venue == tds[start]:
                break
            start+=5
         inputs = soup.findAll('input',attrs = {'type' : 'radio'})
         inp = inputs[index]
         val = inp['value']
         forms = mechanize.ParseResponse(br.response(),backwards_compat=False)
         form = forms[0]
         br.select_form(nr = 0)
         br.form.set_value([val],name='clsnbr1')
         br.submit()
         print br.response().read()
         break
    exit(0)

    


def first():
    initialize()
    builder = Gtk.Builder()
    builder.add_from_file("ffcs.glade")
    window = builder.get_object("window1")
    regno = builder.get_object('regno')
    passwd = builder.get_object('passwd')
    vrfcd = builder.get_object('vrfcd')
    objects['regno']=regno
    objects['passwd']=passwd
    objects['vrfcd']=vrfcd
    window.show_all()
    handlers = {
        "onDeleteWindow" : Gtk.main_quit,
        "onButtonPressed" : hello
        }
    builder.connect_signals(handlers)
    Gtk.main()


def second():
    builder = Gtk.Builder()
    builder.add_from_file("ffcs2.glade")
    window = builder.get_object("window1")
    window.show_all()
    objects['coursecode']=builder.get_object('coursecode')
    objects['serialno']=builder.get_object('serialno')
    handlers = {
        "onDeleteWindow" : Gtk.main_quit,
        "onButtonPressed" : secondButtonPress}
    builder.connect_signals(handlers)
    Gtk.main()

if __name__ == "__main__" :
    first()
    if flow:
        second()

