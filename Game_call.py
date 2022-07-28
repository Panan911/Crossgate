from main import *
import sys
import random
import main as game


def Call_npc_nurse():
    '''自动补给'''
    if call.Get_npc_nurse() == 364 : # 364 : 资深 | 328 : 普通
        # 判断是否是生产系 生产系不能在资深处补给
        if call.Get_player_job() in ('other') :
            pass

    elif call.Get_npc_nurse() == 328 :
        if call.Get_player_job() not in ('other') :
            pass

    print('执行脚本第{}行'.format(sys._getframe().f_lineno), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'开始补给')
    call.Get_player_hpmp()
    if call.s_minmp < call.s_maxmp :
        # 恢复mp
        dm.moveto(245,195)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.2)
        while dm.Getcolor(223,314) != "346875" and dm.Getcolor(293, 313) != "336975" :
            time.sleep(0.1)
        if dm.Getcolor(223,314) == "346875" :
            dm.moveto(223, 314)
            time.sleep(0.1)
            dm.leftclick()
            while dm.Getcolor(296,320) != "336975" :
                time.sleep(0.1)
            time.sleep(0.2)
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        else :
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        time.sleep(0.5)

    call.Get_player_hpmp()
    if call.s_minhp < call.s_maxhp :
        # 恢复hp
        dm.moveto(245,230)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.2)
        while dm.Getcolor(223,314) != "346875" and dm.Getcolor(293, 313) != "336975" :
            time.sleep(0.1)
        if dm.Getcolor(223,314) == "346875" :
            dm.moveto(223, 314)
            time.sleep(0.1)
            dm.leftclick()
            while dm.Getcolor(296,320) != "336975" :
                time.sleep(0.1)
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        else :
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        time.sleep(0.5)

    # 恢复宠物
    dm.moveto(245,273)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.2)
    while dm.Getcolor(223,314) != "346875" and dm.Getcolor(293, 313) != "336975" :
        time.sleep(0.1)
    if dm.Getcolor(223,314) == "346875" :
        dm.moveto(223, 314)
        time.sleep(0.1)
        dm.leftclick()
        while dm.Getcolor(296,320) != "336975" :
            time.sleep(0.1)
        dm.moveto(300, 320)
        time.sleep(0.1)
        dm.leftclick()
    else :
        dm.moveto(300, 320)
        time.sleep(0.1)
        dm.leftclick()
    time.sleep(0.5)

    # 关闭窗口
    time.sleep(0.5)
    dm.leftclick()
    print('执行脚本第{}行'.format(sys._getframe().f_lineno), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'结束补给!')

def auto_walk(pos_x,pos_y):
    while call.Get_is_fight() not in (1,3) :
        x = pos_x
        y = pos_y
        Goto(x,y)
        print(x,y)
        time.sleep(0.8)
        Goto(x + 5,y)
        print(x + 5,y)
        time.sleep(0.8)

def Goto(pos_x,pos_y):
    '''去某个坐标'''
    call.Get_player_pos()
    d1 = {}
    for k in range(9) :
        x = call.mapx
        y = call.mapy
        x1 = x - k
        y1 = y - 9 + k
        offset1 = 64
        offset2 = 48
        posy = 23 + k * offset2
        for i in range(0,10):
            posx = 30 + offset1 * i
            d1[x1,y1] = (posx,posy) 
            x1 = x1 + 1
            y1 = y1 + 1      
    for k in range(9) :
        x = call.mapx
        y = call.mapy
        x1 = x - k
        y1 = y - 8 + k
        offset1 = 64
        offset2 = 48
        posy = 23 + 24 + (offset2 * k)
        for i in range(0,9):
            posx = 30 + 32 + offset1 * i
            d1[x1,y1] = (posx,posy) 
            x1 = x1 + 1
            y1 = y1 + 1
    tag_x = pos_x
    tag_y = pos_y
    chick_pos_x = d1[(tag_x,tag_y)][0]
    chick_pos_y = d1[(tag_x,tag_y)][1]
    r_pos = random.randint(1,10)
    dm.moveto(chick_pos_x + r_pos,chick_pos_y + r_pos)
    dm.leftclick()

def MovetoClick(pos_x,pos_y):
    '''移动并且点击'''
    dm.moveto(pos_x,pos_y)
    time.sleep(0.05)
    dm.leftclick()
    time.sleep(0.05)

def MovetoDoubleClick(pos_x,pos_y):
    '''移动并且点击'''
    dm.moveto(pos_x,pos_y)
    time.sleep(0.05)
    dm.LeftDoubleClick()
    time.sleep(0.05)

def use_skill(skill_name,skill_lv):
    # 选择技能
    ## 等待面板出现
    r_pos = random.randint(1,20)
    dm.moveto(10 + r_pos, 10 + r_pos)
    time.sleep(0.05)
    x = 0
    y = 0
    pic = dm.FindPic(0,0,2000,2000,"./pic/玩家指令.bmp","000000",0.9,0,x,y)
    while pic[0] == -1 :
        time.sleep(0.1)
        pic = dm.FindPic(0,0,2000,2000,"./pic/玩家指令.bmp","000000",0.9,0,x,y)
    color = dm.GetColor(453,30)
    if color == "d4ad6a" :
        r_pos = random.randint(1,5)
        MovetoClick(453 + r_pos,30 + r_pos)
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
    if x < 15 or x > 200 or y < 90 or y > 300 :
        call.Return_panel()
    dm_ret = dm.FindStr(0,0,2000,2000,skill_name,"ffffff-000000",1.0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(10,20)
    MovetoClick(x + r_pos,y + 5)
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
    MovetoClick(x + r_pos,y + 3)
    time.sleep(0.1)

def ordinary_acct(gwpos_x,gwpos_y):
    ic('人物普攻')
    gw_x = gwpos_x
    gw_y = gwpos_y
    color = dm.GetColor(383,30)
    if color == "93bb6c" :
        chick_monster(gw_x,gw_y)
    elif color == "d4ad6a" :
        r_pos = random.randint(1,5)
        dm.moveto(383 + r_pos,30 + 3)
        time.sleep(0.1)
        dm.leftclick()
        chick_monster(gw_x,gw_y)

def chick_monster(gw_x,gw_y):
    '''点击怪物'''
    MovetoClick(gw_x,gw_y)
    r_pos = random.randint(1,30)
    dm.moveto(253 + r_pos,35 + r_pos)

def Get_gzq():
    # color = ""
    color = dm.getcolor(295,320)
    while color != "346875" :
        time.sleep(0.1)
        color = dm.getcolor(295,320)
    time.sleep(0.3)
    MovetoClick(295,320)
    time.sleep(1)
    dm.leftclick()
    time.sleep(1)
    dm.leftclick()
    time.sleep(1)
    MovetoClick(230,320)
    time.sleep(1)
    dm.leftclick()
    time.sleep(1)
    MovetoClick(295,320)
    time.sleep(2)
call = main()