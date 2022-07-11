from main import *
import sys
import random
import Game_call as gc


def begin():
	zz.Get_player_hpmp()
	if zz.s_minmp >= 67:
		# 寻找item1
		item_x = find_item(item1,item1_num)[0]
		item_y = find_item(item1,item1_num)[1]
		r_pos = random.randint(5,15)
		gc.MovetoDoubleChick(item_x + r_pos,item_y + r_pos)
		# 寻找item2
		item_x = find_item(item2,item2_num)[0]
		item_y = find_item(item2,item2_num)[1]
		r_pos = random.randint(5,15)
		gc.MovetoDoubleChick(item_x + r_pos,item_y + r_pos)
		# 寻找item3
		item_x = find_item(item3,item3_num)[0]
		item_y = find_item(item3,item3_num)[1]
		r_pos = random.randint(5,15)
		gc.MovetoDoubleChick(item_x + r_pos,item_y + r_pos)
		# # 寻找item4
		# item_x = find_item(item4,item4_num)[0]
		# item_y = find_item(item4,item4_num)[1]
		# r_pos = random.randint(5,15)
		# gc.MovetoDoubleChick(item_x + r_pos,item_y + r_pos)
		x = 0
		y = 0
		dm_ret = dm.FindPic(0,0,2000,2000,"./pic/执行.bmp","000000",0.9,0,x,y)
		x = dm_ret[1]
		y = dm_ret[2]
		gc.MovetoChick(x,y)
		mp_now = zz.s_minmp
		time.sleep(1)
		mp_new = mp_now
		r_pos = random.randint(1,30)
		dm.moveto(0 + r_pos,0 + r_pos)
		while mp_new >= mp_now :
			time.sleep(0.5)
			zz.Get_player_hpmp()
			mp_new = zz.s_minmp
		x = 0
		y = 0
		dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
		x = dm_ret[1]
		y = dm_ret[2]
		gc.MovetoChick(x,y)
	elif zz.s_minmp >= 67:
		dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
		if dm_ret[1] > 0 :
			x = dm_ret[1]
			y = dm_ret[2]
			gc.MovetoChick(x,y)
	else :
		print('mp不够了')
		quit()

def find_item(item_name,item_num):
	zz.arrange_package()
	x = 0
	y = 0
	zz_panel = dm.FindPic(0,0,2000,2000,"./pic/制造.bmp","000000",0.9,0,x,y)
	x = zz_panel[1] + 38
	y = zz_panel[2] + 23
	item_pos_dict = {}
	for i in range(0,5) :
		item_pos_dict[i + 1] = [x + i * 50 , y]
	for i in range(5,10) :
		item_pos_dict[i + 1] = [x + (i - 5) * 50 , y + 50]
	for i in range(10,15) :
		item_pos_dict[i + 1] = [x + (i - 10) * 50 , y + 100]
	for i in range(15,20) :
		item_pos_dict[i + 1] = [x + (i - 15) * 50 , y + 150]
	item_pos = -1
	for k in zz.package_info.items():
		if k[1][0] == item_name and k[1][2] >= item_num :
			item_pos = item_pos_dict[k[0]]
			break
	return item_pos



if __name__ == '__main__':
	zz = main()
	item1 = "蝴蝶花"
	item1_num = 15
	item2 = "果梨"
	item2_num = 5
	item3 = "柠檬草"
	item3_num = 10
	# item4 = "鹿皮"
	# item4_num = 20
	while 1 :
		begin()