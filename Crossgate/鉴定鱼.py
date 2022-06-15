import main as game
from main import *
import Game_call as call
import random

def begin():
    if game.Get_map_name() == '拿潘食品店':
        game.Get_player_hpmp()
        if game.s_minmp < 10 :
            pass
        game.Get_player_pos()
        if game.mapx == 10 and game.mapy == 14 :
            item_name = dm.ReadString(hwnd,"F75B36",0,20).encode('gb18030').decode('big5')
            if "？" in item_name :
                run_jd()
            
def run_jd():
    

def chick_skill_memu():
    r_pos = random.randint(1,5)
    color = dm_getcolor(100,465)
    if color == "f8f4e6" :
        dm.moveto(100 + r_pos,465 + r_pos)
        time.sleep(0.1)
        dm.leftclick()
    time.sleep(1)
    x = 0
    y = 0
    dm_ret = dm.FindStr(0,0,2000,2000,"鉴定","ffffff-000000",1.0,x,y)
    print(dm_ret)
    dm.moveto(x + r_pos, y + r_pos)
    dm.leftclick()
    time.sleep(0.1)
    dm.leftclick()
    




if __name__ == '__main__':
    # jd = main()
    # while 1:
    #     begin()
    # call.Call_npc_nurse()
    item_name = dm.ReadString(hwnd,"F75B36",0,20).encode('gb18030').decode('big5')
    print(item_name)