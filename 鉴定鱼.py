import main as game
from main import *
import Game_call as call
import random
from icecream import ic
import sys

def begin():
    jd.Get_player_hpmp()
    if jd.s_minmp < 10 :
        call_去东医()
    jd.Get_player_pos()
    if jd.mapx == 10 and jd.mapy == 14 :
        is_open = dm.ReadInt(hwnd,"CFD228",0)
        is_item = dm.readint(hwnd,"F76C64",1)
        item_name = dm.ReadString(hwnd,"F76C66",0,20).encode('gb18030').decode('big5')
        if is_item == 0 :
            pick_fish()
        elif is_item == 1 and "？" in item_name and is_open < 2 :
            run_jd()
        elif is_item == 1 and "？" in item_name and is_open == 2 :
            redo_fish()
            wait_succ()
        else :
            drop_fish()

def run_jd():
    chick_skill_memu()
    chick_fish()
    wait_succ()


def chick_skill_memu():
    ic('点击技能菜单')
    is_open = dm.ReadInt(hwnd,"CFD228",0)
    if is_open == 0 :
        ic(is_open)
        r_pos = random.randint(1,5)
        # 判断技能是否已经被点开(f8f4e6 未点开 aaa69d 点开了)
        color = dm.getcolor(100, 470)
        if color == "f8f4e6":
            dm.moveto(100 + r_pos, 470)
            time.sleep(0.1)
            dm.leftclick()
        elif color == "aaa69d" :
            pass
        # 等待查找技能
        time.sleep(0.3)
        x = 0
        y = 0
        dm_ret = dm.FindStrFast(0,0,2000,2000,'鉴定',"ffffff-000000",1.0,x,y)
        ic(format(sys._getframe().f_lineno),dm_ret)
        while dm_ret[0] == -1 :
            ic(format(sys._getframe().f_lineno))
            time.sleep(0.2)
            dm_ret = dm.FindStr(0,0,2000,2000,'鉴定',"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        # 找到技能后点击技能
        r_pos = random.randint(1,5)
        dm.moveto(x + r_pos, y + r_pos)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.3)
        dm.leftclick()
        # 等待弹出鉴定物品面板
        x = 0
        y = 0
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
        while dm_ret[0] == -1 :
            time.sleep(0.1)
            dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
    elif is_open == 1 :
        ic(is_open)
        # 等待查找技能
        x = 0
        y = 0
        dm_ret = dm.FindStr(0,0,2000,2000,'鉴定',"ffffff-000000",1.0,x,y)
        ic(format(sys._getframe().f_lineno),dm_ret)
        while dm_ret[0] == -1 :
            time.sleep(0.2)
            dm_ret = dm.FindStr(0,0,2000,2000,'鉴定',"ffffff-000000",1.0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        # 找到技能后点击技能
        r_pos = random.randint(1,5)
        dm.moveto(x + r_pos, y + r_pos)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.3)
        # 等待弹出鉴定物品面板
        x = 0
        y = 0
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
        while dm_ret[0] == -1 :
            time.sleep(0.1)
            dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
    # 调整一下面板位置
    x = 0
    y = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鉴定面板.bmp","000000",0.9,0,x,y)
    if dm_ret[2] < 200 :
        dm.moveto(dm_ret[1],dm_ret[2])
        time.sleep(0.2)
        dm.LeftDown()
        time.sleep(0.1)
        r_pos = random.randint(1,5)
        dm.moveto(277 + r_pos,220 + r_pos)
        time.sleep(0.1)
        dm.leftup()


def chick_fish():
    ic('鉴定鱼')
    x = 0
    y = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鱼.bmp","000000",0.9,0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,5)
    dm.moveto(x + r_pos, y + r_pos)
    time.sleep(0.1)
    dm.LeftDoubleClick()
    time.sleep(0.3)
    # 查看是否点击成功(界面上有没有出现执行图片)
    x = 0
    y = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/执行.bmp","000000",0.8,0,x,y)
    ic(dm_ret)
    if dm_ret[0] == -1 :
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    time.sleep(0.1)
    r_pos = random.randint(10,30)
    dm.moveto(x + r_pos, y + 5)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.2)
    r_pos = random.randint(1,10)
    dm.moveto(395 + r_pos , 140 + r_pos)

    
def pick_fish():
    ic('拿鱼')
    r_pos = random.randint(1,20)
    dm.moveto(450 + r_pos,50 + r_pos)
    time.sleep(0.1)
    dm.rightclick()
    time.sleep(0.1)
    # 点击拿鱼
    coloe = '000000'
    while dm.Getcolor(225,320) != "346875" :
        time.sleep(0.1)
        dm.Getcolor(225,320)
    r_pos = random.randint(1,10)
    call.MovetoChick(225 + r_pos, 320)
    # 点击确定
    coloe = '000000'
    while dm.Getcolor(300,320) != "336975" :
        time.sleep(0.1)
        dm.Getcolor(300,320)
    r_pos = random.randint(1,10)
    call.MovetoChick(300 + r_pos, 320)


def wait_succ():
    jd.Get_player_hpmp()
    mp_old = jd.s_minmp
    mp_new = mp_old
    while mp_new == mp_old :
        time.sleep(0.5)
        jd.Get_player_hpmp()
        mp_new = jd.s_minmp


def drop_fish():
    ic('扔鱼')
    is_open = dm.ReadInt(hwnd,"CFD228",0)
    if is_open == 0:
        chick_skill_memu()
    elif is_open == 1 :
        chick_skill_memu()
    elif is_open == 2:
        ic('重试')
        r_pos = random.randint(1,10)
        x = 0
        y = 0
        dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
        x = dm_ret[1]
        y = dm_ret[2]
        r_pos = random.randint(1,10)
        dm.moveto(x + r_pos , y + 2)
        time.sleep(0.1)
        dm.leftclick()
        time.sleep(0.1)
        
        # dm.leftclick()

    # 找到鱼
    x = 0
    y = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/鱼.bmp","000000",0.9,0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,5)
    dm.moveto(x + r_pos, y + r_pos)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.3)
    r_pos = random.randint(1,10)
    dm.moveto(395 + r_pos , 140 + r_pos)
    time.sleep(0.3)
    dm.leftclick()
    time.sleep(0.3)
    while dm.readint(hwnd,"F76C64",1) != 0 :
        time.sleep(0.1)

def redo_fish():
    ic('重来')
    x = 0
    y = 0
    dm_ret = dm.FindPic(0,0,2000,2000,"./pic/重试.bmp","000000",0.9,0,x,y)
    x = dm_ret[1]
    y = dm_ret[2]
    r_pos = random.randint(1,5)
    dm.moveto(x + r_pos,y + r_pos)
    time.sleep(0.1)
    dm.leftclick()
    time.sleep(0.3)
    chick_fish()

def call_去东医():
    dm.WriteInt(hwnd,"F70950",0,150)
    call.Goto(3,13)
    while jd.Get_map_name() != '法兰城' :
        time.sleep(1)
    time.sleep(1.5)
    call.Goto(214,53)
    time.sleep(1)
    call.Goto(214,60)
    time.sleep(1.5)
    call.Goto(214,67)
    time.sleep(1.5)
    call.Goto(214,75)
    time.sleep(1.5)
    call.Goto(214,83)
    time.sleep(1.5)
    call.Goto(221,85)
    time.sleep(0.3)
    call.Goto(221,83)
    
    while jd.Get_map_name() != '医院' :
        time.sleep(1)
    time.sleep(0.5)
    call.Goto(11,36)
    time.sleep(1.5)
    call.Goto(8,32)
    time.sleep(1)

    dm.moveto(131,94)
    time.sleep(0.1)
    dm.rightclick()
    time.sleep(1)
    call.Call_npc_nurse()
    time.sleep(1)

    # 回去
    dm.WriteInt(hwnd,"F70950",0,150)
    call.Goto(9,35)
    time.sleep(0.5)
    call.Goto(12,39)
    time.sleep(1)
    call.Goto(12,42)
    while jd.Get_map_name() != '法兰城' :
        time.sleep(1)
    time.sleep(1)
    call.Goto(214,83)
    time.sleep(1.5)
    call.Goto(214,78)
    time.sleep(1.5)
    call.Goto(214,72)
    time.sleep(2)
    call.Goto(214,67)
    time.sleep(1.5)
    call.Goto(214,61)
    time.sleep(1.5)
    call.Goto(214,54)
    time.sleep(1)
    call.Goto(217,53)
    time.sleep(1)

    while jd.Get_map_name() != '拿潘食品店' :
        time.sleep(1)
    call.Goto(10,14)
    time.sleep(1.5)




if __name__ == '__main__':
    jd = main()
    while 1:
        begin()
