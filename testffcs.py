from gi.repository import Gtk
from browser import Browser
browser = Browser()
br = browser.getBrowser()
mainUrl = 'https://academics.vit.ac.in/student'
captchaUrl = 'https://academics.vit.ac.in/student/captcha.asp'
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
    if '11BCE0244' in br.response().read():
        print 'here'
        flow = True
    Gtk.main_quit()

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
    handlers = {
        "onDeleteWindow" : Gtk.main_quit
        }
    builder.connect_signals(handlers)
    Gtk.main()

if __name__ == "__main__" :
    first()
    print flow
    if flow:
        second()

