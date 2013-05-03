from vkauth import vkauth
from vkgui import browse

__author__ = 'Dmitry K'

if __name__ == '__main__':
    vkauth.browser()
    browse.BrowseData(vkauth.URI)