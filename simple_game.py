#! /usr/bin/env python

import time
import curses
from curses import wrapper
import sys

import locale
locale.setlocale(locale.LC_ALL, '')


class Player():
	
	'''	Defines the Player class. All characters and enemies 
		should be of this class type.
	'''
	
	def __init__(self,pos,lvl,symb,stage):
		self.pos = pos
		self.prevpos = 1,1   # Very ad hoc wont work in general
		self.hp = 2*lvl
		self.symb = symb
		self.lvl = lvl
		self.type = 'obj'
		self.stage = stage
		stage.add(self)
		
	
	def move(self,a,stage):
		self.prevpos = self.pos
		temp = self.pos[0]+a[0],self.pos[1]+a[1]
		
		if temp[0] in range(0,stage.size[0]-1) and temp[1] in range(0,stage.size[1]):
			self.pos = temp
		else:
			pass
	 
	def shoot(self,direction,stage):
		if direction == 'none':
			pass
		else:
			prj = Arrow(self.pos,direction,stage)
			


asymbls = {curses.KEY_UP:'|',curses.KEY_LEFT:u'\u2014',curses.KEY_RIGHT:u'\u2014',curses.KEY_DOWN:'|'}


class Arrow():

	'''	Defines an Arrow class
	'''	
	
	def __init__(self,pos,trj,stage):
		self.pos = pos
		self.trj = trj
		self.symb = asymbls[trj]
		self.type = 'obj'
		stage.add(self)


class Stage():

	'''	This sets a "stage" that keeps track of all objects placed on it.
		All objects placed on a "stage" should minimally have a 'type' 
		'pos', 'prevpos' and 'symb' attributes. 		
		
		Predefined attributes:
		'num': returns the number of objects on 'stage'
		'objlist': returns a list of all objects on 'stage'
		'size': returns the size of the stage as (height, width)
		
		Predfined functions:
		add(obj): adds obj to the stage
		rmv(obj): removes obj from the stage
	'''

	def __init__(self,stdscr):
		self.num = 0
		self.objlist = []
		self.size = stdscr.getmaxyx()
		
	def add(self,obj):
		
		if obj.type == 'obj':
			self.num+=1
			self.objlist+=[obj]
		else:
			raise AttributeError, "%s's type is not 'obj'" % obj
				
	def rmv(self,obj):
		try:
			self.objlist.remove(obj)
			self.num+=-1
		except ValueError:
			
			print " %s is not on the stage" % str(obj)

def enemy_ai(stage, enemy, player):
	
	#= stage.objlist.index(player)
	#enemy.move()
	True


def get_action(stdscr):
	
	try:
		return stdscr.getch()
		
		
	except:
		return 'None'

def handle_action(action, player, stdscr, stage):
	
	if action == 'None':
		pass
	elif action == ord('q'):
		sys.exit()
	elif action == curses.KEY_UP:
		player.move((-1,0),stage)
	elif action == curses.KEY_DOWN:
		player.move((1,0),stage)
	elif action == curses.KEY_RIGHT:
		player.move((0,1),stage)
	elif action == curses.KEY_LEFT:
		player.move((0,-1),stage)
	elif action == ord('a'):
		curses.halfdelay(10)
		direction = 'none'
		try:
			direction = get_action(stdscr)
		except:
			pass
		player.shoot(direction,stage)
		print direction

def draw_frame(stdscr,stage):
	
	stage.size = stdscr.getmaxyx()
	
	try:
		objlist = stage.objlist
		for i in range(stage.num):
			
			if True:
				y,x = objlist[i].pos
				yp,xp = objlist[i].prevpos
				
				
				try:
					stdscr.addch(y,x,objlist[i].symb)
									
				except:
					pass
				if objlist[i].pos != objlist[i].prevpos:
					try:
						stdscr.addch(yp,xp," ")
					except:
						pass
					
											
		stdscr.refresh()

	except NameError:
		stdscr.clear()
		stdscr.addst(0,0,'The stage is not set, something is missing')
		



def main(stdscr):
	
	curses.curs_set(False)
	stdscr.nodelay(True)

	stage = Stage(stdscr)
	player = Player((0,0),1,'X',stage)
	action = 'None'
	
	
		
	stdscr.addstr(5,5,u'\u2615'.encode('utf_8'))
	try:
		stdscr.addstr((stage.size[0]-1),0,u'\u203E'.encode('utf-8')*stage.size[1])
	except:
		pass
	

	while True:
		action = get_action(stdscr)
		handle_action(action, player, stdscr, stage)
		#try:
		draw_frame(stdscr,stage)
		#except:
			#print '''\n\n\rFailed to draw screen. Press "q" to quit \n\rPlayer is at %s''' % str(player.pos)
			#stdscr.nodelay(False)
			#while True:
			#	actn = stdscr.getch()
			#	if actn == ord('q'):
			#		break
			#	else:
			#		pass
			#break		
		

if __name__=="__main__":
	
	wrapper(main)



