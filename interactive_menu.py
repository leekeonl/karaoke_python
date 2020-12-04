# -*- coding: utf-8 -*-

import os, sys

class singer:
	 def __init__ (self, name, music):
                 self.name = name
                 self.musics = [music]

        def get_name (self):
                 return self.name

        def set_name (self, name):
                 self.name = name

        def insert_music (self, music):
                 self.musics.append (music)

        def exist_music (self, music):
                if music in self.musics:
                         return True
                return False

        def get_musics (self):
                return self.musics

class singer_manager:
	def __init__ (self):
		self.singers =[]
 
	def insert_singer (self, singer):
		self.singers.append (singer)
	
	def delete_singer_by_name (self, name):
		for i in range (0, len(self.singers)):
			if self.singers[i].get_name () == name:
				return singer.get_musics ()
	
	def search_musics_by_singer_name (self, singer_name):
		music_names = []
		for singer in self.singers:
			if singer.get_name () == singer_name:
				music_names = singer.get_musics ()
		return music_names

	def search_singer_names_by_music_name (self, title_name):
            singer_names = []

            for singer in self.singers:
                music_names  = singer.get_musics ()
                if title_name in music_names:
                        singer_names.append (singer.get_name())

            return singer_names

def print_main_menu ():
	print 'Music Interactive Menu'
	print '======================='
	print '1. Type Singers song'
	print '2. Type song of singer'
	print '3. Terminate the program'
	print

def get_user_choice ():
	choice = raw_input ('Choose the number from Menu : ')
	choice = choice.strip ()
	menu_num = int (choice)
	return menu_num

def menu_search_singer (manager):
	print
	singer_name = raw_input ('Type singer name: ')

	print
	print 'From now we will find the song that [%s] sang' % (singer_name)
	print
	print

	title_names = manager.search_musics_by_singer_name (singer_name)

	names_str = title_names.pop(0)
	for name in title_names:
		names_str = names_str + ', ' + name

	print 'Singer [%s] sing [%s] ' % (singer_name, names_str)
	print
	print

def menu_search_title (manager):
	print
	title_name = raw_input ('Type the song: ')

	print
	print 'From now we will find the singer that  sang [%s]...' % (title_name)
	print
	print

	singer_names = manager.search_singer_names_by_music_name (title_name)
	
	names_str = singer_names.pop(0)
	for name in singer_names:
		names_str = names_str + ', ' + name

	print '[%s] song was sang by [%s]' % (title_name, names_str)
	print
	print

def menu_exit ():
	print
	print 'Program is over. Thank You'''
	print
	print

if __name__ == '__main__':

	manager = singer_manager ()

	fp = open (sys.argv[1], 'r')
	for line in fp:
		line = line.strip ()
		if line == '':
			continue

		tokens = line.split (',')
		if len (tokens) >= 2:
			name = tokens.pop(0).strip()
			musics = tokens	

			sing = singer (name, musics.pop(0).strip())
			for m in musics:
				sing.insert_music(m.strip())

			manager.insert_singer (sing)
	fp.close ()

	while True:
		print_main_menu ()

		menu_num = get_user_choice ()
		
		if menu_num == 1:
			menu_search_singer (manager)
		elif menu_num == 2:
			menu_search_title (manager)
		elif menu_num == 3:
			menu_exit ()
			break 
