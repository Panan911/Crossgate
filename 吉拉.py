from turtle import begin_fill
from main import *
import Game_call as gc
import time
from icecream import ic
import random
import sys

def begin():
    if player.Get_map_name() == '法兰城' :
        pos = player.Get_player_pos()
        x = pos[0]
        y = pos[1]
        if x == 141 and y == 148:
            Goto_竞技场()
        elif x == 162 and y == 130 :
            while player.Get_is_fight() != 0 :
                time.sleep(0.5)
            gc.Goto(157,133)
            gc.Goto(152,136)
            gc.Goto(149,141)
            gc.Goto(145,145)
            gc.Goto(141,148)
            Goto_竞技场()
        elif x == 233 and y == 78 :
            while player.Get_is_fight() != 0 :
                time.sleep(0.5)
            gc.MovetoRightClick(157,103)
        elif x == 72 and y == 123 :
            while player.Get_is_fight() != 0 :
                time.sleep(0.5)
            gc.MovetoRightClick(418,145)
    if player.Get_map_name() == '竞技预赛会场' :
        talk_jl()
        time.sleep(0.5)
        while player.Get_is_fight() > 0 :
            auto_fight()
        print('战斗结束')
        drop_手环()



def Goto_竞技场():
    gc.Goto(137,152)
    gc.Goto(133,156)
    gc.Goto(129,160)
    gc.Goto(123,161)
    while 1:
        time.sleep(0.1)
        if player.Get_player_moving() == 0 :
            time.sleep(0.2)
            break
    # 竞技场的入口
    gc.Goto(16,18)
    gc.Goto(21,15)
    gc.Goto(27,15)
    while 1:
        time.sleep(0.1)
        if player.Get_player_moving() == 0 :
            time.sleep(0.2)
            break
    # 治愈的广场
    gc.Goto(10,28)
    gc.Goto(11,23)
    gc.Goto(15,19)
    gc.Goto(20,16)
    gc.Goto(25,13)
    dm.moveto(471,127)
    time.sleep(0.1)
    dm.rightclick()
    while 1:
        time.sleep(0.1)
        if player.Get_color(295,320) == "346875" :
            break
    gc.MovetoClick(295,320)
    while 1:
        time.sleep(0.1)
        if player.Get_color(233,320) == "346875" :
            break
    gc.MovetoClick(233,320)
    while 1:
        time.sleep(0.1)
        if player.Get_color(318,320) == "336975" :
            break
    gc.MovetoClick(318,320)
    # 竞技场
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(18,14)
    gc.Goto(22,14)
    time.sleep(0.2)
    gc.Goto(22,13)
    time.sleep(1)
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(19,15)
    gc.Goto(16,10)
    gc.Goto(15,8)
    time.sleep(1)
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(16,15)
    gc.Goto(22,15)
    gc.Goto(22,9)
    time.sleep(0.2)
    gc.Goto(22,8)
    time.sleep(1)
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(22,15)
    gc.Goto(16,15)
    gc.Goto(15,9)
    time.sleep(0.2)
    gc.Goto(15,8)
    time.sleep(1)
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(18,14)
    gc.Goto(21,16)
    time.sleep(0.2)
    gc.Goto(22,16)
    time.sleep(1)
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(17,12)
    # 和教官对话
    dm.moveto(114,212)
    time.sleep(0.1)
    dm.rightclick()
    while 1:
        time.sleep(0.1)
        if player.Get_color(230,320) == "346875" :
            gc.MovetoClick(230,320)
            break
    time.sleep(0.2)
    while 1:
        time.sleep(0.1)
        if player.Get_color(320,320) == "336975" :
            gc.MovetoClick(320,320)
            break
    time.sleep(0.2)
    # 休息室   
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "休息室" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(15,11)
    gc.Goto(8,10)
    gc.Goto(6,7)
    gc.Goto(6,4)
    gc.Goto(12,4)
    gc.Goto(16,5)
    time.sleep(0.2)
    dm.moveto(322,337)
    time.sleep(0.1)
    dm.rightclick()
    while 1:
        time.sleep(0.1)
        if player.Get_color(375,320) == "346875" :
            gc.MovetoClick(375,320)
            break
    time.sleep(0.1)
    dm.moveto(554,66)
    time.sleep(0.1)
    dm.rightclick()
    while 1:
        time.sleep(0.1)
        if player.Get_color(240,320) == "346875" :
            gc.MovetoClick(240,320)
            break
    while 1:
        time.sleep(0.1)
        if player.Get_color(320,320) == "336975" :
            gc.MovetoClick(320,320)
            break
    while 1:
        time.sleep(0.1)
        if player.Get_map_name() == "竞技预赛会场" and player.Get_player_moving() == 0:
            time.sleep(1)
            break
    gc.Goto(31,24)

def talk_jl():
    r_pos = random.randint(1,20)
    dm.moveto(320,70 - r_pos)
    time.sleep(0.1)
    dm.rightclick()
    while 1:
        time.sleep(0.1)
        if player.Get_color(240,320) == "346875" :
            r_pos = random.randint(1,10)
            gc.MovetoClick(240 + r_pos,320)
            break
    time.sleep(0.2)
    while 1:
        time.sleep(0.1)
        if player.Get_color(320,320) == "336975" :
            r_pos = random.randint(1,5)
            gc.MovetoClick(320 + r_pos,320)
            break
    
def auto_fight():
    while 1:
        time.sleep(0.1)
        if player.Get_whois_act() == 1 :
            print('人物攻击')
            r_pos = random.randint(1,20)
            gc.MovetoClick(153,163 - r_pos)
            time.sleep(0.3)
            while 1 :
                time.sleep(0.1)
                if player.Get_whois_act() == 4:
                    pet_act()
                    break
                elif player.Get_whois_act() == 2:
                    time.sleep(0.1)
        elif player.Get_whois_act() == 4 :
            pet_act()
        elif player.Get_whois_act() == 5:
            break
        


def pet_act() :
    print('宠物攻击')
    while player.Get_whois_act() != 4 :
        time.sleep(0.1)
    if player.Get_color(588,55) == "93bb6c" :
        time.sleep(0.1)
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,'攻击',"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        gc.MovetoClick(x + 20,y + 3)
    r_pos = random.randint(1,20)
    gc.MovetoClick(153,163 - r_pos)

def drop_手环():
    while player.Get_color(41,46) != "00cf1f" :
        time.sleep(0.1)
    time.sleep(0.3)
    r_pos = random.randint(1,5)
    gc.MovetoClick(319,250 - r_pos)
    r_pos = random.randint(1,10)
    gc.MovetoClick(175 + r_pos,470)
    time.sleep(0.1)
    while 1:
        time.sleep(0.1)
        x = 0
        y = 0
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/手环.bmp","000000",0.9,3,x,y)
        if dm_ret[0] == 0 :
            x = dm_ret[1]
            y = dm_ret[2]
            break
    r_pos = random.randint(1,5)
    gc.MovetoClick(x + r_pos,y + r_pos)
    time.sleep(0.2)
    r_pos = random.randint(1,10)
    gc.MovetoClick(240 - r_pos,139 - r_pos)
    r_pos = random.randint(1,10)
    gc.MovetoClick(175 + r_pos,470)

global act_cnt
act_cnt = 0
if __name__ == '__main__':
    player = main()
    while 1 :
        begin()
        act_cnt += 1
        print(act_cnt)