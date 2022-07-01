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

def MovetoChick(pos_x,pos_y):
    dm.moveto(pos_x,pos_y)
    time.sleep(0.05)
    dm.leftclick()
call = main()
