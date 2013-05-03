__author__ = 'Dmitry K'
import vkontakte
import mainwindow
class BrowseData():
    def __init__(self,token):
        self.token = token
        self.apicom()
        tm = mainwindow.Timeline(self.myprofile[0],self.friends,self.notify,self.audio)
        tm.main()

    def apicom(self):
        fragment = str(self.token).split('#')[1]
        self.infodict = {}
        for item in fragment.split('&'):
            info = item.split('=')
            self.infodict[info[0]] = info[1]
        myid=int(self.infodict['user_id'])
        vk = vkontakte.API(token=self.infodict['access_token'])
        self.myprofile = vk.getProfiles(uids=myid)
        self.friends = vk.friends.get(fields="first_name, last_name, bdate, contacts, photo_big", order='name')
        self.notify = vk.notifications.get(filters="wall,mentions,comments,likes,reposts,followers,friends")
        self.audio = vk.audio.get(uid=myid,count=10)


