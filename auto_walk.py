from main import *
import random
import Game_call as gc

def 来回走路():
	while player.Get_player_moving() == 0 :
		x = 116
		y = 104
		gc.Goto(x,y)
		gc.Goto(x + 5,y)

if __name__ == '__main__':
	player = main()
	while 1:
		来回走路()
