from main import *
import Game_call as gc
import time
from icecream import ic
import random
import sys

def begin():
    player.Get_player_hpmp()
    while player.Get_is_fight() not in (1,3) and player.s_minmp >= 50 and player.Get_map_name() == '莎莲娜':
        gc.auto_walk(181,163)
        player.Get_player_hpmp()
    # 回去补给
    if player.Get_is_fight() not in (1,3) and (player.s_minmp < 50 or player.s_minhp < 100) and player.Get_map_name() == '莎莲娜':
        print('没魔了，回城补给')
        while player.Get_player_moving() != 0 :
            time.sleep(0.5)
        gc.MovetoClick(318,237)
        time.sleep(0.5)
        call_goto_hospital()
        gc.Call_npc_nurse()
        if len(player.arrange_package()) >= 18 :
            print(len(player.arrange_package()))
            print('石头满了')
    if player.Get_is_fight() not in (1,3) and player.Get_player_pos()[0] == 14 and player.Get_player_pos()[1] == 10 :  
        time.sleep(0.5)
        call_goto_技能点()

    # 自动战斗
    if player.Get_is_fight() in (1,3):
        player.Get_monster_info()
        if player.Get_whois_act() == 1 :
            player_act()
            time.sleep(0.3)
        elif player.Get_whois_act() == 4 : 
            if player.gw_cnt > 1 and player.pet_mp >= 38:
                pet_act('连击')
                chick_monster()
            elif player.gw_cnt == 1 and player.player_mp < summoner_ft_skill_ndmp :
                pet_act('攻击')
                chick_monster()
            else :
                pet_act('防御')
        else :
            time.sleep(0.2)


def player_act():
    ic('人物行动')
    # 获取战斗信息
    if player.player_hp > 500 and player.player_mp >= summoner_ft_skill_ndmp:
        gc.use_skill(summoner_ft_skill,summoner_ft_skill_lv)
        r_pos = random.randint(5,10)
        gc.MovetoClick(412,324 - r_pos) # 寵物位置
    elif player.player_hp > 500 and player.player_mp < summoner_ft_skill_ndmp and player.player_mp >= 48:
        gc.use_skill(summoner_ft_skill,4)
        r_pos = random.randint(5,10)
        gc.MovetoClick(475,348 - r_pos) # 寵物位置
    else :
        gc.ordinary_acct(gw_x,gw_y)

def player_user_lv1(skill_name,skill_lv):
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
        print('未弹出')
        time.sleep(0.1)
        dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,10)
    gc.MovetoClick(x + r_pos,y + 5)
    time.sleep(0.05)
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
    r_pos = random.randint(5,10)
    gc.MovetoClick(412,324 - r_pos) # 寵物位置

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

def pet_click_player():
    r_pos = random.randint(1,10)
    gc.MovetoClick(475,348 - r_pos)

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
        gc.movtochlick(453 + r_pos,30 + r_pos)
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
    gc.movtochlick(x + r_pos,y + 5)
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
    gc.movtochlick(x + r_pos,y + 3)
    time.sleep(0.1)
    chick_monster()

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

def call_goto_hospital():
    gc.Goto(183,161)
    time.sleep(1)
    while player.Get_map_name() != '阿巴尼斯村' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(40,66)
    time.sleep(1.5)
    gc.Goto(43,64)
    time.sleep(1.5)
    gc.Goto(47,64)
    time.sleep(1)
    while player.Get_map_name() != '医院' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(8,9)
    time.sleep(2)
    gc.Goto(14,10)
    time.sleep(1.5)
    dm.moveto(162,105) # 右键资深医生
    time.sleep(0.1)
    dm.rightclick()
    color = ""
    color = dm.Getcolor(294,319)
    while color != '346875' :
        time.sleep(0.1)
        color = dm.Getcolor(294,319)

def call_goto_技能点():
    gc.Goto(9,10)
    time.sleep(1.5)
    gc.Goto(1,9)
    time.sleep(2)
    while player.Get_map_name() != '阿巴尼斯村' :
        time.sleep(2)
    time.sleep(1)
    gc.Goto(41,65)
    time.sleep(1.5)
    gc.Goto(38,69)
    time.sleep(1.5)
    gc.Goto(38,71)
    time.sleep(1.5)
    while player.Get_map_name() != '莎莲娜' :
        time.sleep(2)
    
# ----------------------------------战斗参数设置---------------------------------------- #
### 人物战斗保护设置
summoner_bh_rate = 0.8
summoner_bh_gwcnt = 2
summoner_bh_skill = "补血"
summoner_bh_skill_lv = 4
summoner_bh_skill_ndmp = 60
### 人物战斗技能设置
summoner_ft_skill = "超强补血"
summoner_ft_skill_lv = 5
summoner_ft_skill_ndmp = 120
### 人物群攻技能设置
summoner_ft_qgskill = "乱射"
summoner_ft_qgskill_lv = 5
summoner_ft_qgskill_ndmp = 25
##  宠物保护设置
pet_bh_rate = 0.9
pet_bh_skill = "吸血攻击"
pet_bh_skill_ndmp = 20
pet_bh_skill_type = 1 if pet_bh_skill in ('吸血攻击') else 2   #保护技能是否需要点击目标(1 = 需要 | 2 = 不需要)


if __name__ == '__main__':
    ic.configureOutput(includeContext=True) #调试
    # player.reggame()信息
    player = main()
    while 1:
        begin()
