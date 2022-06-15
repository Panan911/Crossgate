from main import *
import sys
import random


def Call_npc_nurse():
    '''自动补给'''
    if game.Get_npc_nurse() == 364 : # 364 : 资深 | 328 : 普通
        # 判断是否是生产系 生产系不能在资深处补给
        if game.Get_player_job() in ('other') :
            pass

    elif game.Get_npc_nurse() == 328 :
        if game.Get_player_job() not in ('other') :
            pass

    print('执行脚本第{}行'.format(sys._getframe().f_lineno), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),'开始补给')
    game.Get_player_hpmp()
    if game.s_minmp < game.s_maxmp :
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
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        else :
            dm.moveto(300, 320)
            time.sleep(0.1)
            dm.leftclick()
        time.sleep(0.5)

    game.Get_player_hpmp()
    if game.s_minhp < game.s_maxhp :
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
