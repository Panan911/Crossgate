from main import *
import random
import Game_call as gc

def 来回走路():
	while player.Get_is_fight() not in (1,3) :
		x = 180
		y = 163
		gc.Goto(x,y)
		time.sleep(0.8)
		gc.Goto(x + 5,y)
		time.sleep(0.8)

if __name__ == '__main__':
	player = main()
	while 1:
		来回走路()
