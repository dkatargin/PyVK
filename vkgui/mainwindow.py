#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk

# Объявление своего класса, без наследования
# от какого-либо другого.
class Timeline:
    """ Автодокументирование описания этого класса
        располагается здесь, в любых тройных кавычках
    """

    def __init__(self,myprofile,friends,notify,audio):
        self.userprofile = myprofile
        self.friends = friends
        self.notify = notify
        self.audio = audio

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(250,350)
        self.window.set_border_width(10)
        self.window.set_title('PyVK')

        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)


        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)


        sw_music = gtk.ScrolledWindow()
        sw_music.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview_music = gtk.TextView()
        textbuffer_music = textview_music.get_buffer()
        sw_music.add(textview_music)
        sw_music.show()
        textview_music.show()

        notebook.append_page(self.userprofile_tab(),gtk.Label('Я'))
        notebook.append_page(self.audio_tab(),gtk.Label('Музыка'))

        self.button_exit = gtk.Button("Выход")
        self.button_exit.connect("clicked", self.hello)
        self.button_exit.connect_object("clicked", gtk.Widget.destroy, self.window)

        self.button_settings = gtk.Button("Настройки")
        self.button_settings.connect("clicked", self.hello)
        self.button_settings.connect_object("clicked", gtk.Widget.destroy, self.window)

        vbox = gtk.VBox(homogeneous=False, spacing=0)
        hbox = gtk.HBox(homogeneous=True, spacing=0)

        hbox.pack_start(self.button_exit)
        hbox.pack_end(self.button_settings)

        vbox.pack_start(notebook)
        vbox.pack_end(hbox,expand=False, fill=False)
        #textbuffer.set_text('Hallo!')
        textbuffer_music.set_text('UnHallo!')


        self.window.add(vbox)
        self.window.show_all()

    def userprofile_tab(self):
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()
        textbuffer.set_text('Имя: %s \nФамилия: %s \nUID: %d' %
                            (self.userprofile['first_name'],self.userprofile['last_name'],self.userprofile['uid']))
        return sw

    def audio_tab(self):
        tb = ''
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        textview = gtk.TextView()
        textbuffer = textview.get_buffer()
        sw.add(textview)
        sw.show()
        textview.show()
        for songinfo in self.audio:
            tb += '%s-%s(Url:%s)\n' % (songinfo['artist'],songinfo['title'],songinfo['url'])
        textbuffer.set_text(tb)
        return sw

    def hello(self, widget):
        ''' Печатает на стандартный вывод (в консоль) текст
        '''
        print 'Hello World'

    def delete_event(self, widget, event, data=None):
        ''' Обработчик события удаления объекта.
        '''
        print "delete event occurred"

        # Если вернуть True, то приложение не завершит
        # свою работу.
        return False

    def destroy(self, widget, data=None):
        ''' Обработчик сигнала завершения приложения.
        '''
        print "destroy signal occurred"

        # Библиотека gtk завершает работу главного окна.
        gtk.main_quit()

    def main(self):
        ''' Метод, начинающий работу главного окна.
        '''
        gtk.main()


if __name__ == "__main__":
    # создание именованного экземпляра класса HelloWorld.
    hello = Timeline()
    # Исполнение метода, получившегося экземпляра.
    hello.main()