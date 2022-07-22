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
            # if player.is_lv1 == 1 :
            #     print('有1级怪，停止自动战斗')
            #     quit()
            if player.Get_whois_act() == 1 :
                chose_monster()
                player_act()
                while player.Get_whois_act() not in (4,5) :
                    time.sleep(0.1)
                    if player.Get_whois_act() == 4 :
                        break
                    else :
                        break
            elif player.Get_whois_act() == 4 :
                if player.pet_hp / player.pet_maxhp <= pet_bh_rate and player.pet_mp >= pet_bh_skill_ndmp :
                    pet_act(pet_bh_skill)
                else :
                    pet_act('攻击')
                    gc.chick_monster(gw_x,gw_y)
                time.sleep(0.1)
            else :
                time.sleep(0.2)
    elif player.Get_nurse_window() == 1 :
        gc.Call_npc_nurse()
    elif player.Get_is_fight() not in (1,3):
        if player.Get_talk_type() == 2 and player.Get_nurse_window() == 1 : 
            gc.Call_npc_nurse()
        else :
            time.sleep(0.1)
    else :
        time.sleep(0.1)

def player_act():
    '''人物行动'''
    # ic('人物行动')
    # 调整一下鼠标位置
    r_pos = random.randint(1,20)
    dm.moveto(253 + r_pos,35 + r_pos)
    # 怪物数量 >= 某个值，群攻魔法值足够，使用群攻技能
    if player.gw_cnt >= 6 and player.player_mp >= summoner_qt_skill_ndmp :
        gc.use_skill(summoner_qt_skill,summoner_qt_skill_lv)
        gc.chick_monster(gw_x,gw_y)
    # 怪物数量在某个阈值内，并且有强力点，强力技能魔法足够，使用强力魔法技能：
    elif player.gw_cnt in (4,5) and is_qld == 1 and player.player_mp >= summoner_ql_skill_ndmp :
        gc.use_skill(summoner_ql_skill,summoner_ql_skill_lv)
        gc.chick_monster(gw_x,gw_y)
    # 怪物数量 <= 某个数值，怪物保护魔法足够，使用人物保护技能
    elif player.gw_cnt <= summoner_bh_gwcnt and player.player_mp >= summoner_bh_skill_ndmp and player.player_hp / player.player_maxhp < 0.8 :
        gc.use_skill(summoner_bh_skill,summoner_bh_skill_lv)
        gc.chick_monster(gw_x,gw_y)
    # 使用单体技能
    elif player.player_mp >= summoner_ft_skill_ndmp :
        gc.use_skill(summoner_ft_skill,summoner_ft_skill_lv)
        gc.chick_monster(gw_x,gw_y)
    else :
        gc.ordinary_acct(gw_x,gw_y)

def pet_act(skill_name):
    # 调整一下鼠标位置
    r_pos = random.randint(1,20)
    dm.moveto(253 + r_pos,35 + r_pos)
    '''宠物攻击'''
    # ic('宠物攻击')
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
    time.sleep(0.5)

def user_skill(skill_name,skill_lv):
    ic('使用技能')
    # 选择技能
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos, 10 + r_pos)
    time.sleep(0.1)
    color = dm.GetColor(453,30)
    while color not in ("93bb6c","d4ad6a") :
        time.sleep(0.1)
        color = dm.GetColor(453,30)
    if color == "93bb6c" : # 选中菜单
        ic('执行脚本第{}行'.format(sys._getframe().f_lineno),'技能面板已弹出,选择技能')
    elif color == "d4ad6a" :
        ic('执行脚本第{}行'.format(sys._getframe().f_lineno),'技能面板未弹出,去点击技能菜单')
        r_pos = random.randint(1,5)
        gc.MovetoClick(453 + r_pos,30 + r_pos)
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
    r_pos = random.randint(10,20)
    gc.MovetoClick(x + r_pos,y + 5)
    time.sleep(0.1)
    # 移动一下鼠标 做一些延迟
    dm.moveto(10 + r_pos,10 + r_pos)
    time.sleep(0.1)
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
    gc.MovetoClick(x + r_pos,y + 3)
    time.sleep(0.1)
    gc.chick_monster(gw_x,gw_y)

def ordinary_acct():
    ic('人物普攻')
    color = dm.GetColor(383,30)
    if color == "93bb6c" :
        gc.chick_monster(gw_x,gw_y)
    elif color == "d4ad6a" :
        r_pos = random.randint(1,5)
        dm.moveto(383 + r_pos,30 + 3)
        time.sleep(0.1)
        dm.leftclick()
        gc.chick_monster(gw_x,gw_y)
    else :
        time.sleep(0.5)
    time.sleep(0.5)


def chose_monster():
    '''选择怪物'''
    global gw_x,gw_y,is_qld,gw_pos,acct_monster_sn
    ic(player.monsters_list_all)


    rang_list = {
                  10 : [11,12,15] ,
                  11 : [10,13,16] ,
                  12 : [10,14,17] ,
                  15 : [10,16,17] ,
                  16 : [11,15,18] ,
                  17 : [12,15,19] ,
                  13 : [11,18] ,
                  14 : [12,19] ,
                  18 : [13,16] ,
                  19 : [14,17] 
                  }

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

    if player.gw_cnt not in (4,5) :
        if len(player.monsters_list_front) > 0 :
            acct_monster_sn = random.choice(player.monsters_list_front)
            gw_pos = pos_dict[acct_monster_sn]
            gw_x = gw_pos[0]
            gw_y = gw_pos[1]
            print('执行脚本第{}行'.format(sys._getframe().f_lineno), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),acct_monster_sn,gw_x,gw_y)
        else :
            acct_monster_sn = random.choice(player.monsters_list_back)
            gw_pos = pos_dict[acct_monster_sn]
            gw_x = gw_pos[0]
            gw_y = gw_pos[1]
            print('执行脚本第{}行'.format(sys._getframe().f_lineno), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),acct_monster_sn,gw_x,gw_y)
    else :
        is_qld = 0
        for i in player.monsters_list_all:
            list1 = rang_list[i]
            if i in (10,11,12,15,16,17) :
                a1 = 1 if list1[0] in player.monsters_list_all else 0
                a2 = 1 if list1[1] in player.monsters_list_all else 0
                a3 = 1 if list1[2] in player.monsters_list_all else 0
                a_sum = a1 + a2 + a3
                if a_sum == 3:
                    x = pos_dict[i][0]
                    y = pos_dict[i][1]
                    gw_pos = pos_dict[i]
                    gw_x = gw_pos[0]
                    gw_y = gw_pos[1]
                    is_qld = 1
            elif i in (13,14,18,19) :
                a1 = 1 if list1[0] in player.monsters_list_all else 0
                a2 = 1 if list1[1] in player.monsters_list_all else 0
                a_sum = a1 + a2
                if a_sum == 2:
                    x = pos_dict[i][0]
                    y = pos_dict[i][1]
                    gw_pos = pos_dict[i]
                    gw_x = gw_pos[0]
                    gw_y = gw_pos[1]
                    is_qld = 1


        if is_qld == 0 :
            if len(player.monsters_list_front) > 0 :
                print(player.monsters_list_front,len(player.monsters_list_front))
                print('选择前排')
                acct_monster_sn = random.choice(player.monsters_list_front)
                gw_pos = pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
            else :
                print(player.monsters_list_back,len(player.monsters_list_back))
                print('选择后排')
                acct_monster_sn = random.choice(player.monsters_list_back)
                gw_pos = pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
    

# ----------------------------------战斗参数设置---------------------------------------- #
### 人物战斗保护设置
summoner_bh_rate = 0.8
summoner_bh_gwcnt = 4
summoner_bh_skill = "吸血魔法"
summoner_bh_skill_lv = 3
summoner_bh_skill_ndmp = 30
### 人物单体技能设置
summoner_ft_skill = "陨石魔法"
summoner_ft_skill_lv = 4
summoner_ft_skill_ndmp = 20
### 人物强力魔法
summoner_ql_skill = "强力冰冻魔法"
summoner_ql_skill_lv = 3
summoner_ql_skill_ndmp = 30
### 人物全体技能设置
summoner_qt_skill = "超强风刃魔法"
summoner_qt_skill_lv = 3
summoner_qt_skill_ndmp = 60
##  宠物保护设置
pet_bh_rate = 0.8
pet_bh_skill = "明镜"
pet_bh_skill_ndmp = 75
pet_bh_skill_type = 1 if pet_bh_skill in ('吸血攻击') else 2   #保护技能是否需要点击目标(1 = 需要 | 2 = 不需要)

if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    while 1:
        begin()
