from main import *
import time
from icecream import ic
import random

def begin():
    # 自动战斗
    if player.Get_is_fight() in (1,3):
        # ic('战斗中')
        if player.Get_whois_act() in (1,4) :
            player.Get_monster_info()
            if player.Get_whois_act() == 1 :
                player_act()
                time.sleep(0.3)
            else : 
                if player.Get_fight_round() + 1 == 1 :
                    pet_act('防御')
                else :
                    pet_act('攻击')
            r_pos = random.randint(1,20)
            dm.moveto(324 + r_pos,209 + r_pos)
    else :
        # ic('未在战斗')
        pass


def player_act():
    '''人物行动'''
    if player.Get_fight_round() + 1 == 1 :
        player_def()
    else :
        ordinary_acct()

def pet_act(skill_name):
    '''宠物攻击'''
    chose_monster()
    color = dm.GetColor(590,57)
    while color not in ("93bb6c","d4ad6a"):
        time.sleep(0.1)
        color = dm.GetColor(590,57)
    if color == "93bb6c" :
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()
    else :
        dm.rightclick()
        time.sleep(0.5)
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 5)
        time.sleep(0.05)
        dm.leftclick()
    chick_monster()


def user_skill(skill_name,skill_lv):
    ic('使用技能',skill_name,skill_lv)
    while dm.GetColor(453,30) not in ("93bb6c","d4ad6a"):
        time.sleep(0.1)
        color = dm.GetColor(453,30)
    # 选择技能
    color = dm.GetColor(453,30)
    if color == "93bb6c" :
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        ic(dm_ret)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()
    elif color == "d4ad6a" :
        dm.moveto(453,30)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.2)
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        ic(dm_ret)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()   
    else :
        time.sleep(0.2)
    # 选择技能等级
    dm.moveto(324,209)
    time.sleep(0.1)
    x = 0
    y = 0
    dm_ret = dm.FindStr(0,0,2000,2000,'LV{}'.format(skill_lv),"ffffff-000000",1.0,x,y)
    ic(dm_ret)
    x = dm_ret[1]
    y = dm_ret[2]
    dm.moveto(x,y)
    dm.leftclick()
    chick_monster()

def ordinary_acct():
    ic('人物普攻')
    color = dm.GetColor(383,30)
    if color == "93bb6c" :
        chick_monster()
    elif color == "d4ad6a" :
        dm.moveto(383,30)
        time.sleep(0.1)
        dm.leftclick()
        chick_monster()
    else :
        time.sleep(0.5)

def player_def():
    ic('人物防御')
    r_pos = random.randint(1,10)
    color = dm.GetColor(383,54)
    if color == "d4ad6a" :
        dm.moveto(383 + r_pos,54)
        time.sleep(0.1)
        dm.leftclick()


def chick_monster():
    chose_monster()
    dm.moveto(gw_x,gw_y)
    time.sleep(0.1)
    dm.leftclick()

def chose_monster():
    '''选择怪物'''
    global gw_x,gw_y
    pos_dict = {10:[145,153],
                11:[211,115],
                12:[85,185],
                13:[284,80],
                14:[20,225],
                15:[205,208],
                16:[271,170],
                17:[143,240],
                18:[336,133],
                19:[77,280]}
    if len(player.monsters_list_front) > 0 :
        acct_monster_sn = random.choice(player.monsters_list_front)
    else :
        acct_monster_sn = random.choice(player.monsters_list_back)
    gw_pos = pos_dict[acct_monster_sn]
    gw_x = gw_pos[0]
    gw_y = gw_pos[1]


# ----------------------------------战斗参数设置---------------------------------------- #


if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    # player.reggame()
    while 1:
        begin()
