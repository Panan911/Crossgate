from main import *
import Game_call as gc
import time
from icecream import ic
import random
import sys



from main import *
import Game_call as gc
import time
from icecream import ic
import random
import sys


def begin():
    player.Get_player_hpmp()
    if player.Get_is_fight() == 0 and player.s_minmp >= 100 and player.Get_map_name() == '莎莲娜':
        while 1:
            gc.auto_walk(115,102)
            if player.Get_is_fight() > 0 :
                print('开始战斗')
                break
    # 回去补给
    if player.Get_is_fight() not in (1,3) and (player.s_minmp < 100 or player.s_minhp < 100) and player.Get_map_name() == '莎莲娜':
        print('没魔了，回城补给')
        while player.Get_player_moving() != 0 :
            time.sleep(0.5)
        gc.MovetoClick(318,237)
        time.sleep(0.5)
        call_goto_hospital()
        gc.Call_npc_nurse()
        if len(player.arrange_package()) >= 10 :
            print(len(player.arrange_package()))
            time.sleep(1)
            call_goto_sell()
            call_goto_技能点()
    if player.Get_is_fight() not in (1,3) and player.Get_player_pos()[0] == 33 and player.Get_player_pos()[1] == 48 :
        call_goto_技能点()
    
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
                if player.pet_hp / player.pet_maxhp < pet_bh_rate and player.pet_mp >= pet_bh_skill_ndmp :
                    pet_act('明镜')
                else :
                    pet_act('攻击')
                    gc.chick_monster(gw_x,gw_y)
                # elif player.gw_cnt == 1 and player.player_mp > 50 :
                #     pet_act('护卫')
                # #     gc.chick_player()
                # else :
                #     pet_act('攻击')
                #     gc.chick_monster(gw_x,gw_y)
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
    if player.gw_cnt >= 5 and player.player_mp >= summoner_qt_skill_ndmp :
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
    # time.sleep(0.5)
    # if pet_bh_skill_type == 1 :
    #     gc.chick_monster(gw_x,gw_y)

def chose_monster():
    '''选择怪物'''
    global gw_x,gw_y,is_qld,gw_pos,acct_monster_sn
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

    if player.gw_cnt <= summoner_bh_gwcnt :
        first_act_list = []
        for name in player.monsters.items():
            if first_act_monster in name[1][0] : 
                first_act_list.append(name[0])
            if len(first_act_list) > 0 :
                acct_monster_sn = random.choice(first_act_list)
                gw_pos = gw_pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
            elif len(player.monsters_list_front) > 0 :
                acct_monster_sn = random.choice(player.monsters_list_front)
                gw_pos = gw_pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
            else :
                acct_monster_sn = random.choice(player.monsters_list_back)
                gw_pos = gw_pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]

    elif player.gw_cnt not in (4,5) :
        if len(player.monsters_list_front) > 0 :
            acct_monster_sn = random.choice(player.monsters_list_front)
            gw_pos = gw_pos_dict[acct_monster_sn]
            gw_x = gw_pos[0]
            gw_y = gw_pos[1]
        else :
            acct_monster_sn = random.choice(player.monsters_list_back)
            gw_pos = gw_pos_dict[acct_monster_sn]
            gw_x = gw_pos[0]
            gw_y = gw_pos[1]
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
                    x = gw_pos_dict[i][0]
                    y = gw_pos_dict[i][1]
                    gw_pos = gw_pos_dict[i]
                    gw_x = gw_pos[0]
                    gw_y = gw_pos[1]
                    is_qld = 1
            elif i in (13,14,18,19) :
                a1 = 1 if list1[0] in player.monsters_list_all else 0
                a2 = 1 if list1[1] in player.monsters_list_all else 0
                a_sum = a1 + a2
                if a_sum == 2:
                    x = gw_pos_dict[i][0]
                    y = gw_pos_dict[i][1]
                    gw_pos = gw_pos_dict[i]
                    gw_x = gw_pos[0]
                    gw_y = gw_pos[1]
                    is_qld = 1


        if is_qld == 0 :
            if len(player.monsters_list_front) > 0 :
                print(player.monsters_list_front,len(player.monsters_list_front))
                print('选择前排')
                acct_monster_sn = random.choice(player.monsters_list_front)
                gw_pos = gw_pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
            else :
                print(player.monsters_list_back,len(player.monsters_list_back))
                print('选择后排')
                acct_monster_sn = random.choice(player.monsters_list_back)
                gw_pos = gw_pos_dict[acct_monster_sn]
                gw_x = gw_pos[0]
                gw_y = gw_pos[1]
    
def call_goto_hospital():
    gc.Goto(118,100)
    while player.Get_map_name() != '魔法大学' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(75,165)
    gc.Goto(75,159)
    gc.Goto(75,153)
    gc.Goto(75,147)
    gc.Goto(75,141)
    gc.Goto(75,136)
    gc.Goto(75,130)
    gc.Goto(73,124)
    gc.Goto(75,120)
    gc.Goto(75,114)
    gc.Goto(75,108)
    gc.Goto(75,102)
    gc.Goto(75,96)
    gc.Goto(75,93)
    while player.Get_map_name() != '魔法大学内部' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(40,53)
    gc.Goto(37,50)
    gc.Goto(33,48)
    time.sleep(0.5)
    dm.moveto(162,105) # 右键资深医生
    time.sleep(0.1)
    dm.rightclick()
    color = ""
    color = dm.Getcolor(294,319)
    while color != '346875' :
        time.sleep(0.1)
        color = dm.Getcolor(294,319)
    # gc.Call_npc_nurse()

def call_goto_技能点():
    time.sleep(1)
    gc.Goto(39,51)
    gc.Goto(39,59)
    while player.Get_map_name() != '魔法大学' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(74,100)
    gc.Goto(74,108)
    gc.Goto(74,116)
    gc.Goto(74,122)
    gc.Goto(72,125)
    gc.Goto(74,128)
    gc.Goto(75,135)
    gc.Goto(75,142)
    gc.Goto(75,149)
    gc.Goto(75,153)
    gc.Goto(75,160)
    gc.Goto(75,166)
    gc.Goto(75,172)
    while player.Get_map_name() != '莎莲娜' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(116,102)
    time.sleep(0.2)

def call_goto_sell():
    '''去卖东西'''
    gc.Goto(40,49)
    gc.Goto(46,49)
    gc.Goto(49,46)
    gc.Goto(51,43)
    while player.Get_map_name() != '技术室' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(8,12)
    gc.Goto(14,9)
    gc.Goto(20,10)
    time.sleep(1)
    dm.moveto(412,352)
    time.sleep(0.05)
    dm.rightclick()
    color = ""
    color = dm.GetColor(246,242)
    while color != "8c6100" :
        time.sleep(0.5)
        color = dm.GetColor(246,242)
    time.sleep(0.5)
    gc.MovetoClick(315,264)
    time.sleep(0.5)
    color = ""
    color = dm.GetColor(484,372)
    while color != "346875" :
        time.sleep(0.5)
        color = dm.GetColor(484,372)
    gc.MovetoClick(388,373)
    time.sleep(0.5)
    gc.MovetoClick(322,371)
    time.sleep(0.5)
    gc.MovetoClick(322,371)
    time.sleep(0.5)
    gc.MovetoClick(120,390)
    time.sleep(1)
    gc.Goto(23,15)
    gc.Goto(23,18)
    while player.Get_map_name() != '魔法大学内部' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(63,48)
    gc.Goto(56,49)
    gc.Goto(50,49)
    gc.Goto(43,50)

# ----------------------------------战斗参数设置---------------------------------------- #
### 人物战斗保护设置
summoner_bh_rate = 0.9
summoner_bh_gwcnt = 3
summoner_bh_skill = "吸血魔法"
summoner_bh_skill_lv = 4
summoner_bh_skill_ndmp = 40
### 人物单体技能设置
summoner_ft_skill = "火焰魔法"
summoner_ft_skill_lv = 6
summoner_ft_skill_ndmp = 30
### 人物强力魔法
summoner_ql_skill = "强力冰冻魔法"
summoner_ql_skill_lv = 3
summoner_ql_skill_ndmp = 30
### 人物全体技能设置
summoner_qt_skill = "超强冰冻魔法"
summoner_qt_skill_lv = 5
summoner_qt_skill_ndmp = 100
##  宠物保护设置
pet_bh_rate = 0.6
pet_bh_skill = "明镜"
pet_bh_skill_ndmp = 75
pet_bh_skill_type = 1 if pet_bh_skill in ('吸血攻击') else 2   #保护技能是否需要点击目标(1 = 需要 | 2 = 不需要)
## 优先攻击怪物
first_act_monster = '烈风鸟人'

if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试信息
    player = main()
    pos_x = player.Get_player_pos()[0]
    pos_y = player.Get_player_pos()[1]
    while 1:    
        begin()
        time.sleep(0.001)
