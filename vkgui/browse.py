__author__ = 'Dmitry K'
import vkontakte

class BrowseData():
    def __init__(self,token):
        self.token = token
        self.apicom()

    def apicom(self):
        fragment = str(self.token).split('#')[1]
        self.infodict = {}
        for item in fragment.split('&'):
            info = item.split('=')
            self.infodict[info[0]] = info[1]
        myid=int(self.infodict['user_id'])
        vk = vkontakte.API(token=self.infodict['access_token'])
        myprofile = vk.getProfiles(uids=myid)
        friends = vk.friends.get(fields="first_name, last_name, bdate, contacts, photo_big", order='name')
        notify = vk.notifications.get(filters="wall,mentions,comments,likes,reposts,followers,friends")
        audio = vk.audio.get(uid=myid,count=10)

