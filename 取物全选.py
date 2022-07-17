from main import *
import sys
import random
import Game_call as gc


def choice_all():
	item_pos = {
				1 : [60,90],
				2 : [110,90],
				3 : [160,90],
				4 : [210,90],
				5 : [260,90],
				6 : [60,140],
				7 : [110,140],
				8 : [160,140],
				9 : [210,140],
				10 :[260,140],
				11: [60,190],
				12: [110,190],
				13 :[160,190],
				14 :[210,190],
				15 :[260,190],
				16 :[60,240],
				17 :[110,240],
				18 :[160,240],
				19 :[210,240],
				20 :[260,240]
	}
	for i,k in item_pos.items():
		x = k[0]
		y = k[1]
		dm.keydown(17)
		time.sleep(0.1)
		gc.MovetoDoubleChick(x,y)
		time.sleep(0.3)

if __name__ == '__main__':
	choice_all()