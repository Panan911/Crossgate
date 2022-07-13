from main import *
import sys
import random
import Game_call as gc


def choice_all():
	item_pos = {
				1 : [330,90],
				2 : [380,90],
				3 : [430,90],
				4 : [480,90],
				5 : [530,90],
				6 : [330,140],
				7 : [380,140],
				8 : [430,140],
				9 : [480,140],
				10 :[530,140],
				11: [330,190],
				12: [380,190],
				13 :[430,190],
				14 :[480,190],
				15 :[530,190],
				16 :[330,240],
				17 :[380,240],
				18 :[430,240],
				19 :[480,240],
				20 :[530,240]
	}
	for i,k in item_pos.items():
		x = k[0]
		y = k[1]
		gc.MovetoDoubleChick(x,y)



if __name__ == '__main__':
	choice_all()