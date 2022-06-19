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
                if player.pet_hp + 40 <= player.pet_maxhp and player.pet_mp >= 20 :
                    pet_act('吸血攻击')
                else :
                    pet_act('攻击')
            else :
                time.sleep(0.3)
    elif player.Get_nurse_window() == 1 :
        gc.Call_npc_nurse()
    elif player.Get_is_fight() not in (1,3):
        if player.Get_talk_type() == 2 and player.Get_nurse_window() == 1 : 
            gc.Call_npc_nurse()
        else :
            time.sleep(0.5)
    else :
        time.sleep(0.1)

def player_act():
    '''人物行动'''
    ic('人物行动')
    # 调整一下鼠标位置
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos,10 + r_pos)
    if player.gw_cnt > summoner_bh_gwcnt and player.player_mp >= summoner_ft_qgskill_ndmp :
        if player.gw_cnt == 3 :
            summoner_ft_qgskill_lv = 1
        elif player.gw_cnt == 4 :
            summoner_ft_qgskill_lv = 2
        elif player.gw_cnt == 5 :
            summoner_ft_qgskill_lv = 3
        else :
            summoner_ft_qgskill_lv = 4
        user_skill(summoner_ft_qgskill,summoner_ft_qgskill_lv)
    else :
        ordinary_acct()

def pet_act(skill_name):
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
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()
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
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()
    # 做一下延迟
    time.sleep(0.2)
    chick_monster()


def user_skill(skill_name,skill_lv):
    ic('使用技能')
    # 选择技能
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos, 10 + r_pos)
    time.sleep(0.3)
    color = dm.GetColor(453,30)
    while color not in ("93bb6c","d4ad6a") :
        time.sleep(0.1)
        color = dm.GetColor(453,30)
    if color == "93bb6c" : # 选中菜单
        ic('执行脚本第{}行'.format(sys._getframe().f_lineno),'技能面板已弹出,选择技能')
    elif color == "d4ad6a" :
        ic('执行脚本第{}行'.format(sys._getframe().f_lineno),'技能面板未弹出,去点击技能菜单')
        r_pos = random.randint(1,5)
        dm.moveto(453 + r_pos,30 + r_pos)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.2)
    # 识别技能
    x = 0
    y = 0
    dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
    while dm_ret[0] != 0 :
        time.sleep(0.1)
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,10)
    dm.moveto(x + r_pos,y + 5)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.3)
    # 移动一下鼠标 做一些延迟
    dm.moveto(10 + r_pos,10 + r_pos)
    time.sleep(0.2)
    # 选择技能等级
    x = 0
    y = 0
    dm_ret = dm.FindStr(0,0,2000,2000,'LV{}'.format(skill_lv),"ffffff-000000",1.0,x,y)
    while dm_ret[0] != 0 :
            time.sleep(0.1)
            dm_ret = dm.FindStr(0,0,2000,2000,'LV{}'.format(skill_lv),"ffffff-000000",1.0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,10)
    dm.moveto(x + r_pos,y + 3)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.1)
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
        time.sleep(0.2)
    time.sleep(0.3)

def chick_monster():
    chose_monster()
    ic(gw_pos,'点击怪物')
    dm.moveto(gw_x,gw_y)
    time.sleep(0.2)
    player.Get_mouse_type()
    chick_num = 0 # 点击满5次还没有点到就退出循环
    while player.Get_mouse_type()!= 2 :
        r_pos = random.randint(1,10)
        dm.moveto(gw_x + r_pos,gw_y - r_pos)
        time.sleep(0.1)
        player.Get_mouse_type()
        chick_num += 1
        if chick_num > 5:
            break
    dm.leftclick()
    r_pos = random.randint(1,30)
    dm.moveto(253 + r_pos,35 + r_pos)

def chose_monster():
    '''选择怪物'''
    global gw_x,gw_y,gw_pos
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
    r_pos = random.randint(1,5)
    gw_x = gw_pos[0] + r_pos
    gw_y = gw_pos[1] - r_pos


# ----------------------------------战斗参数设置---------------------------------------- #
### 人物战斗保护设置
summoner_bh_rate = 0.8
summoner_bh_gwcnt = 2
summoner_bh_skill = "明镜止水"
summoner_bh_skill_lv = 3
summoner_bh_skill_ndmp = 22
### 人物战斗技能设置
summoner_ft_skill = "混乱攻击"
summoner_ft_skill_lv = 5
summoner_ft_skill_ndmp = 25
### 人物群攻技能设置
summoner_ft_qgskill = "乱射"
# summoner_ft_qgskill_lv = 3
summoner_ft_qgskill_ndmp = 20
##  宠物保护设置
pet_bh_rate = 0.9
pet_bh_skill = "吸血攻击"
pet_bh_skill_ndmp = 20
pet_bh_skill_type = 1 if pet_bh_skill in ('吸血攻击') else 2   #保护技能是否需要点击目标(1 = 需要 | 2 = 不需要)

if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    while 1:
        begin()
