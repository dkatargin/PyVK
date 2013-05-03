__author__ = 'dmitry'
import gtk
import webkit
import gobject

URI = ''

class WebV(webkit.WebView):
    def __init__(self):
        webkit.WebView.__init__(self)
        self.connect("navigation-policy-decision-requested",self._nav_request_policy_decision_cb)
        self.l_uri=None
    def _nav_request_policy_decision_cb(self,view,frame,net_req,nav_act,pol_dec):
        urireq=net_req.get_uri()
        if "#access_token" in urireq:
            global URI
            URI = urireq
            gtk.main_quit()

def browser():
    gobject.threads_init()
    win = gtk.Window()
    bro = WebV()
    scope = ['friends','audio','video','offline','status','wall','notifications','messages']
    bro.open("http://oauth.vk.com/oauth/authorize?" + \
            "redirect_uri=http://oauth.vk.com/blank.html&response_type=token&" + \
            "client_id=%s&scope=%s&display=wap" % (3620494, ",".join(scope)))

    win.add(bro)
    win.show_all()
    gtk.main()
    locuri = URI
    return locuri
