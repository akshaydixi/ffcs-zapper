from gi.repository import Gtk
from browser import Browser
from BeautifulSoup import BeautifulSoup
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

def secondButtonPress(widget):
    global flow
    coursecode_text = objects['coursecode'].get_text()
    serialno_text = objects['serialno'].get_text()
    theUrl = bnextUrl+coursecode_text
    r = br.open(theUrl)
    br.select_form(nr=0)
    br.submit()
    html =  br.response().read()
    soup = BeautifulSoup(html)
    print soup.prettify()

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

