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
    print('点击坐标为 : {},{}'.format(chick_pos_x + r_pos,chick_pos_y + r_pos))
    dm.leftclick()

def MovetoChick(pos_x,pos_y):
    '''移动并且点击'''
    dm.moveto(pos_x,pos_y)
    time.sleep(0.05)
    dm.leftclick()
    time.sleep(0.05)

def MovetoDoubleChick(pos_x,pos_y):
    '''移动并且点击'''
    dm.moveto(pos_x,pos_y)
    time.sleep(0.05)
    dm.LeftDoubleClick()
    time.sleep(0.05)

def use_skill(skill_name,skill_lv):
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
        MovetoChick(453 + r_pos,30 + r_pos)
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
    MovetoChick(x + r_pos,y + 5)
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
    MovetoChick(x + r_pos,y + 3)
    time.sleep(0.1)

def chick_monster(gw_x,gw_y):
    '''点击怪物'''
    MovetoChick(gw_x,gw_y)
    # time.sleep(0.2)
    # call.Get_mouse_type()
    # chick_num = 0 # 点击满5次还没有点到就退出循环
    # while call.Get_mouse_type()!= 2 :
    #     r_pos = random.randint(1,10)
    #     dm.moveto(gw_x + r_pos,gw_y - r_pos)
    #     time.sleep(0.1)
    #     call.Get_mouse_type()
    #     chick_num += 1
    #     if chick_num > 5:
    #         break
    # dm.leftclick()
    r_pos = random.randint(1,30)
    dm.moveto(253 + r_pos,35 + r_pos)

call = main()
