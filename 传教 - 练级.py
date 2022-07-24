from main import *
import Game_call as gc
import time
from icecream import ic
import random
import sys

def begin():

    # 自动战斗
    if player.Get_is_fight() in (1,3):
        if player.Get_whois_act() in (1,4) :
            player.Get_monster_info()
            if player.is_lv1 == 1 :
                print('有1级怪，停止自动战斗')
                quit()
            if player.Get_whois_act() == 1 :
                player_act()
                while player.Get_whois_act() not in (4,5):
                    time.sleep(0.05)
                    break
            if player.Get_whois_act() == 4 :
                pet_act('攻击')
                gc.chick_monster(gw_x,gw_y)
            else :
                time.sleep(0.3)
    elif player.Get_nurse_window() == 1 :
        gc.Call_npc_nurse()
    elif player.Get_is_fight() not in (1,3):
        if player.Get_talk_type() == 2 and player.Get_nurse_window() == 1 : 
            gc.Call_npc_nurse()
        elif player.Get_map_name() == "香蒂的房间" :
            gc.Get_gzq()
        else :
            time.sleep(0.5)
    else :
        time.sleep(0.1)

def player_act():
    '''人物行动'''
    ic('人物行动')
    # 获取战斗信息
    chose_monster()
    # 调整一下鼠标位置
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos,10 + r_pos)
    gc.ordinary_acct(gw_x,gw_y)

def pet_act(skill_name):
    # 获取一下怪物信息
    chose_monster()
    # 调整一下鼠标位置
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos,10 + r_pos)
    '''宠物攻击'''
    ic('宠物攻击')
    intX = 0
    intY = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/宠物指令.bmp","000000",0.9,0,intX,intY)
    while intX < 0 or intY < 0 :
        time.sleep(0.1)
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/宠物指令.bmp","000000",0.9,0,intX,intY)
        if intX > 0 and intY > 0 :
            break
    color = dm.GetColor(590,57)
    if color == "93bb6c" :
        # player.Return_panel()
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        while x < 0 or intY < 0 :
            time.sleep(0.1)
            dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
            if x > 0 and y > 0 :
                break
        x = dm_ret[1]
        y = dm_ret[2]
        gc.MovetoClick(x + 20,y + 5)
    else :
        dm.rightclick()
        time.sleep(0.3)
        # player.Return_panel()
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        while x < 0 or intY < 0 :
            time.sleep(0.1)
            dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
            if x > 0 and y > 0 :
                break
        x = dm_ret[1]
        y = dm_ret[2]
        gc.MovetoClick(x + 20,y + 5)

def chose_monster():
    '''选择怪物'''
    global gw_x,gw_y,gw_pos
    if len(player.monsters_list_front) > 0 :
        acct_monster_sn = random.choice(player.monsters_list_front)
    else :
        acct_monster_sn = random.choice(player.monsters_list_back)
    gw_pos = gw_pos_dict[acct_monster_sn]
    r_pos = random.randint(1,3)
    gw_x = gw_pos[0] + r_pos
    r_pos = random.randint(1,10)
    gw_y = gw_pos[1] - r_pos


# ----------------------------------战斗参数设置---------------------------------------- #


if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    while 1:
        begin()
