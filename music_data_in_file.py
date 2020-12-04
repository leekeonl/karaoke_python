# -*- coding: utf-8 -*-

import os, sys

class musician:
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

class musician_manager:
	def __init__ (self):
		self.musicians = []

	def insert_musician (self, musician):
		self.musicians.append (musician)

	def delete_musician_by_name (self, name):
		for i in range (0, len(self.musicians)):
			if musician.get_name () == name:
				self.musicians.pop (i)
				break

	def search_musics_by_musician_name (self, musician_name):
		for musician in self.musicians:
			if musician.get_name () == musician_name:
				return musician.get_musics ()

	def search_musician_names_by_music_name (self, music_name):
		musician_names = []
		
		for musician in self.musicians:
			musics = musician.get_musics ()
			if music_name in musics:
				musician_names.append (musician.get_name())

		return musician_names

if __name__ == '__main__':
	
	manager = musician_manager ()

	fp = open (sys.argv[1], 'r')
	for line in fp:
		line = line.strip ()
		if line == '':
			continue

		tokens = line.split (',')
		if len (tokens) >= 2:
			name = tokens.pop(0).strip ()
			musics = tokens

			mus = musician (name, musics.pop(0).strip())
			for m in musics:
				mus.insert_music (m.strip())

			manager.insert_musician (mus)
	fp.close ()
#	
#	musician_names = manager.search_musician_names_by_music_name ('나팔바지')
#	for name in musician_names:
#		print name
