#-*- coding: UTF-8 -*-
__author__ = 'Dmitry K'

import gtk
import gobject

import gtk


def button_clicked(button):
    print 'Hello World!'


def main():
    gobject.threads_init()
    window = gtk.Window()
    window.set_title("PyVK::Вконтакте")
    window.set_default_size(250, 400)
    window.connect('destroy', lambda w: gtk.main_quit())

    button_friends = gtk.Button('Друзья')
    button_friends.connect('clicked', button_clicked)
    button_friends.show()

    window.add(button_friends)
    window.present()

    gtk.main()


if __name__ == '__main__':
    main()
