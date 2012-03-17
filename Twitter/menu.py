#!/usr/bin/python

# This is a part of the external Twitter applet for Cairo-Dock
#
# Author: Eduardo Mucelli Rezende Oliveira
# E-mail: edumucelli@gmail.com or eduardom@dcc.ufmg.br

import gtk, os

class Menu(gtk.Menu):

  def __init__(self, messages, callback):
    gtk.Menu.__init__(self)
        
    for message in messages:
      text = "<b>%s</b>\n%s" % (message.sender, message.text)
      item = gtk.ImageMenuItem()
      # the true label is set after with set_markup()
      item.set_label(message.sender)
      item.set_image(gtk.image_new_from_file(os.path.abspath("./data/received_menu.png")))
      item.get_children()[0].set_markup(text)
      item.connect('activate', callback)
      self.append(item)
      item.show()
      # add a separator if mail is not last in list
      if messages.index(message) != len(messages) - 1:
        separator = gtk.SeparatorMenuItem()
        self.append(separator)

    self.show_all()
    
  def pop_up(self, icon):
    self.icon = icon
    self.popup(parent_menu_shell=None, parent_menu_item=None, func=self.get_xy, data=(400, 400), button=1, activate_time=0)

  def get_xy(self, m, data):
    # fetch icon geometry
    icondata = self.icon.GetAll()
    iconContainer  = icondata['container']
    iconOrientation = icondata['orientation']
    iconWidth = icondata['width']
    iconHeight = icondata['height']
    iconPosX = icondata['x']
    iconPosY = icondata['y']

    # get menu geometry
    menuWidth, menuHeight = m.size_request()

    # adapt to container and orientation
    if iconContainer == 1:  # Then it's a desklet, always oriented in a bottom-like way.
      if iconPosY['y'] < (gtk.gdk.screen_height() / 2):
        iconOrientation = 1
      else:
        iconOrientation = 0

    if iconOrientation == 0:
      # compute position of menu
      x = iconPosX - (menuWidth / 2)
      y = iconPosY - (iconHeight / 2) - menuHeight

    else:
      x = iconPosX - (menuWidth / 2)
      y = iconPosY + (iconHeight / 2)

    return (x, y, True)