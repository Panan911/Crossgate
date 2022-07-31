from main import *
import random
import Game_call as gc

def 来回走路():
	while player.Get_player_moving() == 0 :
		x = 26
		y = 8
		gc.Goto(x,y)
		time.sleep(0.8)
		gc.Goto(x ,y + 5)
		time.sleep(0.8)

if __name__ == '__main__':
	player = main()
	while 1:
		来回走路()
