from main import *
import random
import Game_call as gc

def 来回走路():
	while player.Get_is_fight() not in (1,3) :
		# r_pos = random.randint(1,20)
		# dm.moveto(221 + r_pos,152)
		# dm.leftclick()
		# time.sleep(1)
		# dm.moveto(426 + r_pos,330)
		# dm.leftclick()
		# time.sleep(1)
		gc.Goto(371,190)
		time.sleep(1)
		gc.Goto(371,185)
		time.sleep(1)

if __name__ == '__main__':
	player = main()
	while 1 :
		来回走路()