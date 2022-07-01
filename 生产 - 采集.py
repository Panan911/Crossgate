from main import *
import time
from icecream import ic
import random
import Game_call as gc

def begin():
    # 自动战斗
    if player.Get_is_fight() in (1,3):
        if player.Get_whois_act() in (1,4) :
            if player.Get_whois_act() == 1 :
                player_act()
                time.sleep(0.3)
            else : 
                pet_act('防御')
            r_pos = random.randint(1,20)
            dm.moveto(324 + r_pos,209 + r_pos)
    else :
        time.sleep(1)


def player_act():
    '''人物行动'''
    ic('player_act')
    player_escape()


def pet_act(skill_name):
    '''宠物攻击'''
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


def player_escape():
    r_pos = random.randint(1,10)
    dm.moveto(570 + r_pos,55)
    time.sleep(0.1)
    dm.leftclick()


# ----------------------------------战斗参数设置---------------------------------------- #


if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    # player.reggame()
    while 1:
        begin()
