from main import *
import Game_call as gc
import time
from icecream import ic
import random

def begin():
    # 自动战斗
    if player.Get_is_fight() in (1,3):
        if player.Get_whois_act() in (1,4) :
            player.Get_monster_info()
            if player.Get_whois_act() == 1 :
                player_act()
            elif player.Get_whois_act() == 4 :
                pet_ac4018304916t('攻击')
                time.sleep(0.1)
            else :
                time.sleep(0.3)
    elif player.Get_talk_window() == 1 :
        gc.Call_npc_nurse()
    elif player.Get_is_fight() not in (1,3):
        if player.Get_talk_type() == 2 and player.Get_talk_window() == 1 : 
            gc.Call_npc_nurse()
        else :
            time.sleep(0.5)
    else :
        time.sleep(1)

def player_act():
    '''人物行动'''
    # 怪物 < 一定数量时自我保护
    # if player.gw_cnt <= summoner_bh_gwcnt and player.player_hp/player.player_maxhp < summoner_bh_rate and player.player_mp >= summoner_bh_skill_ndmp :
    #     ic('人物战斗保护')
    #     user_skill(summoner_bh_skill,summoner_bh_skill_lv)
    # # 非自我保护时怪物 > 一定数量时放群攻技能
    # elif player.gw_cnt > summoner_bh_gwcnt and player.player_mp >= summoner_ft_qgskill_ndmp :
    #     ic('人物群攻')
    #     user_skill(summoner_ft_qgskill,summoner_ft_qgskill_lv)
    # # 非自我保护时怪物 > 一定数量时放单体技能
    # elif player.player_mp >= summoner_ft_skill_ndmp:
    #     ic('人物技能攻击')
    #     user_skill(summoner_ft_skill,summoner_ft_skill_lv)
    # # 普攻
    # else :
    #     ordinary_acct()
    ic('人物行动')
    if player.gw_cnt > summoner_bh_gwcnt and player.player_mp >= summoner_ft_qgskill_ndmp :
        user_skill(summoner_ft_qgskill,summoner_ft_qgskill_lv)
    else :
        ordinary_acct()

def pet_act(skill_name):
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
        player.Return_panel()
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
        time.sleep(0.3)
        player.Return_panel()
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 5)
        time.sleep(0.1)
        dm.leftclick()
    # 做一下延迟
    time.sleep(0.5)
    chick_monster()


def user_skill(skill_name,skill_lv):
    ic('使用技能')
    # 选择技能
    color = dm.GetColor(453,30)
    while color not in ("93bb6c","d4ad6a") :
        time.sleep(0.1)
        color = dm.GetColor(453,30)
        if color in ("93bb6c","d4ad6a") :
            break
    if color == "93bb6c" : # 选中菜单
        player.Return_panel() # 恢复面板位置
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 3)
        time.sleep(0.1)
        dm.leftclick()
    elif color == "d4ad6a" :
        dm.moveto(453,30)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.2)
        player.Return_panel()
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        dm.moveto(x + 20,y + 3)
        time.sleep(0.1)
        dm.leftclick()
    # 移动一下鼠标 做一些延迟
    rd_pos = random.randint(0,200)
    dm.moveto(324 + rd_pos,209 + rd_pos)
    time.sleep(0.2)
    # 选择技能等级
    x = 0
    y = 0
    dm_ret = dm.FindStr(0,0,2000,2000,'LV{}'.format(skill_lv),"ffffff-000000",1.0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    dm.moveto(x,y)
    dm.leftclick()
    time.sleep(0.05)
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
    time.sleep(0.5)

def chick_monster():
    chose_monster()
    dm.moveto(gw_x,gw_y)
    time.sleep(0.1)
    # mouse_type = dm.randint(hwnd,"00937FEC",0)
    # if mouse_type == 2 :
    #     dm.leftclick()
    # else :
    #     while 1 :
    #         chose_monster()
    #         dm.moveto(gw_x,gw_y)
    #         time.sleep(0.1)
    #         mouse_type = dm.randint(hwnd,"00937FEC",0)
    #         if mouse_type == 2 :
    #             dm.leftclick()
    #             break
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
summoner_ft_qgskill_lv = 3
summoner_ft_qgskill_ndmp = 15
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
