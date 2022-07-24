from main import *
import Game_call as gc
import random

def start():
    global is_pic
    # open item panel
    x = 0
    y = 0
    is_pic = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
    if is_pic[0] == 0 :
        call_jd()
    elif is_pic[0] == -1 :
        jd.Find_str("鉴定LV")
        if jd.is_str[0] == 0 :
            x = jd.is_str[1]
            y = jd.is_str[2]
            gc.MovetoClick(x,y)
            time.sleep(0.3)
        elif jd.is_str[0] == -1 :
            if jd.Get_color(99,469) != "aaa69d" :
                gc.MovetoClick(100,470)
                time.sleep(0.1)
            jd.Find_str("鉴定")
            time.sleep(0.05)
            x = jd.is_str[1]
            y = jd.is_str[2]
            gc.MovetoClick(x,y)
            time.sleep(0.1)
            dm.leftclick()

def call_jd():
    jd.arrange_package()
    for i in jd.package_info.keys():
        print(jd.package_info)
        if "？" in jd.package_info[i][0] or "？" in jd.package_info[i][0]:
            find_item_pos(i)
            x = item_pos[0]
            y = item_pos[1]
            gc.MovetoDoubleClick(x,y)
            jd.Get_player_hpmp()
            # jd.Get_jd_ndmp()
            if jd.s_minmp >= 50 :
                x = 0
                y = 0
                dm_ret = dm.FindPic(0,0,2000,2000,"./pic/执行.bmp","000000",0.9,0,x,y)
                x = dm_ret[1]
                y = dm_ret[2]
                gc.MovetoClick(x,y)
                r_pos = random.randint(1,10)
                dm.moveto(0 + r_pos, 10 + r_pos)
                call_wait()
                while 1 :
                    time.sleep(0.1)
                    x = 0
                    y = 0
                    time.sleep(0.1)
                    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
                    if dm_ret[0] == 0 :
                        x = dm_ret[1] + 10
                        y = dm_ret[2] + 3
                        gc.MovetoClick(x,y)
                        break
            else :
                dm.keydown(16)
                time.sleep(0.05)
                dm.keypress(123)
                dm.keyup(16)
                time.sleep(0.1)
                dm.moveto(177,238)
                time.sleep(0.5)
                dm.rightclick()
                time.sleep(1)
                gc.Call_npc_nurse()
                time.sleep(0.5)

def find_item_pos(item_sn):
    global item_pos
    x = is_pic[1] + 75
    y = is_pic[2] + 22
    item_pos_dict = {}
    for i in range(0,5) :
        item_pos_dict[i + 1] = [x + i * 50 , y]
    for i in range(5,10) :
        item_pos_dict[i + 1] = [x + (i - 5) * 50 , y + 50]
    for i in range(10,15) :
        item_pos_dict[i + 1] = [x + (i - 10) * 50 , y + 100]
    for i in range(15,20) :
        item_pos_dict[i + 1] = [x + (i - 15) * 50 , y + 150]
    item_pos = item_pos_dict[item_sn]
    return item_pos

def call_wait():
    jd.Get_player_hpmp()
    mp_now = jd.s_minmp
    while 1:
        time.sleep(0.5)
        jd.Get_player_hpmp()
        mp_finish = jd.s_minmp
        if mp_finish < mp_now :
            break

if __name__ == '__main__':
    jd = main()
    dm_ret = dm.SetWindowText(hwnd,hwnd) 
    while 1:
        start()
