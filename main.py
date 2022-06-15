from glob import glob
from tkinter.tix import MAIN
from unicodedata import name
import win32com.client
import time
import ctypes
import win32security
import win32api
import win32process
from icecream import ic
import zhconv

class main():
    def __init__(self):
        pass

    # def reggame(self):
    #     '''注册游戏'''
    #     dm_ret = dm.BindWindow(hwnd, "gdi", "windows", "windows", 0)
    
    ###############################人物信息

    def Get_player_name(self):
        '''人物名称'''
        global player_name
        player_name = dm.ReadString(hwnd,"00F6F7B8",0,12).encode('gb18030').decode('big5')
        player_name = self.Change_GBK(player_name)
        return player_name

    def Get_player_job(self):
        '''职业'''
        global job_name
        job_name = dm.ReadString(hwnd,"00EB01E8",0,20).encode('gb18030').decode('big5')
        job_name = self.Change_GBK(job_name)
        if "弓" in job_name :
            job_name = "gongjianshou"
        elif "格" in job_name :
            job_name = "gedou"
        elif "魔" in job_name :
            job_name = "mofashi"
        elif "驯兽" in job_name :
            job_name = "xunshou"
        elif "教" in job_name or "牧师" in job_name :
            job_name = "chuanjiao"
        elif "巫" in job_name :
            job_name = "wushi"
        elif "咒" in job_name or "降头" in job_name:
            job_name = "zhoushu"
        elif "战斧" in job_name :
            job_name = "zhanfu"
        elif "封印" in job_name :
            job_name = "fengyin"
        elif "检" in job_name :
            job_name = "jianshi"
        else :
            return "other"
        return job_name

    def Get_player_hpmp(self):
        '''人物血魔'''
        # global s_minhp,s_maxhp,s_minmp,s_maxmp
        #人物hp
        hp = dm.ReadString(hwnd, "00CD47D0", 0, 12)
        s_hp = hp.split("/")
        self.s_minhp = int(s_hp[0])
        self.s_maxhp = int(s_hp[1])
        #人物mp
        mp = dm.ReadString(hwnd, "00CD9A08", 0, 12)
        s_mp = mp.split("/")
        self.s_minmp = int(s_mp[0])
        self.s_maxmp = int(s_mp[1])
        return self.s_minhp,self.s_maxhp,self.s_minmp,self.s_maxmp
    
    def Get_player_moving(self):
        '''人物是否正在移动'''
        global is_moving
        is_moving = dm.ReadInt(hwnd,"0055BEA8",0)
        if is_moving != 65535 :
            is_moving = 1
        else :
            is_moving = 0
        return is_moving

    def Get_player_pos(self):
        '''人物坐标'''
        global mapx,mapy
        self.mapx = int(dm.ReadFloat(hwnd,"0096CDF4")/64)
        self.mapy = int(dm.ReadFloat(hwnd,"0096CDF8")/64)
        return self.mapx,self.mapy

    ######################################################################################################
    ###############################地图信息
    def Get_map_name(self):
        '''地图名称'''
        global map_name
        map_name = dm.ReadString(hwnd,"0096CDD8",0,15).encode('gb18030').decode('big5')
        return self.Change_GBK(map_name)
    ######################################################################################################
    # def click_memu(self,memu_name):
    #     if memu_name == '状态':
    #         dm.moveto(500,645)
    #         dm.leftclick()
    ######################################################################################################
    ##############################战斗信息
    def Get_is_fight(self):
        '''自动战斗标识(战斗中3 战斗结束画面1 非战斗0)'''
        global is_fight
        is_fight = 0
        get_is_fight = lambda is_fight : dm.ReadInt(hwnd,"0073AE20",0)
        return get_is_fight(is_fight)

    def Get_whois_act(self):
        '''判断是谁的回合(人物行动1 宠物行动4 结束战斗5)'''
        global whos_act
        whos_act = dm.ReadInt(hwnd,"005A7DC4",0)
        return whos_act

    def Get_fight_round(self):
        fight_round = dm.ReadInt(hwnd,"005A7D90",0)
        return fight_round

    def Get_monster_info(self):
        '''统计怪物情况'''
        # global gw_cnt,monsters_list_front,monsters_list_back,monsters
        global is_lv1
        monster_mess=dm.ReadString(hwnd, "0059FBA8", 0, 5000).encode('gb18030').decode('big5')
        monster_mess = monster_mess.split('|')
        #去掉前面两位
        del monster_mess[0:2]
        monster_mess = list(enumerate(monster_mess))
        #去掉最后一位
        del monster_mess[-1]
        monsters_list = []
        monsters = {}

        for i in monster_mess :
            j = i[0]
            if j % 12 == 0 :
                index = int(i[1],16)
                for k in range(12):
                    # 姓名
                    if k % 12 == 1 :
                        monsters_list.append(self.Change_GBK(monster_mess[j+k][1]))
                    # 等级
                    elif k % 12 == 4 :
                        monsters_list.append(int(monster_mess[j+k][1],16))
                    # minhp
                    elif k % 12 == 5 :
                        monsters_list.append(int(monster_mess[j+k][1],16))
                    # maxhp
                    elif k % 12 == 6 :
                        monsters_list.append(int(monster_mess[j+k][1],16))
                    # minmp
                    elif k % 12 == 7 :
                        monsters_list.append(int(monster_mess[j+k][1],16))
                    # maxmp
                    elif k % 12 == 8 :
                        monsters_list.append(int(monster_mess[j+k][1],16))
                monsters[index] = monsters_list
                monsters_list = []

        self.is_lv1 = 0
        for i in monsters.keys():
            lv = monsters[i][1]
            if lv == 1:
                self.is_lv1 = 1

        player_name = self.Get_player_name()
        for i in monsters.keys():
            if monsters[i][0][1:4] == player_name[1:4] :
                player_hp,player_maxhp,player_mp,player_maxmp = monsters[i][2],monsters[i][3],monsters[i][4],monsters[i][5]
                player_sn = int(i)
                pet_sn = (player_sn) + 5 if (player_sn) < 5 else (player_sn - 5)
                if pet_sn in monsters.keys():
                    pet_hp,pet_maxhp,pet_mp,pet_maxmp = monsters[pet_sn][2],monsters[pet_sn][3],monsters[pet_sn][4],monsters[pet_sn][5]

        self.monsters_list_front = []
        # 前排怪物列表
        for i in monsters.keys() :
            if i >= 15 :
                self.monsters_list_front.append(i)
        # 后排怪物列表
        self.monsters_list_back = []
        for i in monsters.keys() :
            if i >= 10 and i < 15:
                self.monsters_list_back.append(i)
        gw_cnt = len(self.monsters_list_front) + len(self.monsters_list_back)

        self.monsters_list_all = self.monsters_list_front + self.monsters_list_back


        mess_info = gw_cnt,player_hp,player_maxhp,player_mp,player_maxmp,pet_hp,pet_maxhp,pet_mp,pet_maxmp
        self.gw_cnt = mess_info[0]
        self.player_hp = mess_info[1]
        self.player_maxhp = mess_info[2]
        self.player_mp = mess_info[3]
        self.player_maxmp = mess_info[4]
        self.pet_hp = mess_info[5]
        self.pet_maxhp = mess_info[6]
        self.pet_mp = mess_info[7]
        self.pet_maxmp = mess_info[8]

        # ic('有{}个怪物!'.format(gw_cnt))

        return self.gw_cnt,self.player_hp,self.player_maxhp,self.player_mp,self.player_maxmp,self.pet_hp,self.pet_maxhp,self.pet_mp,self.pet_maxmp,self.monsters_list_front,self.monsters_list_back,self.is_lv1,\
               self.monsters_list_all

    def arrange_summoner_skill(self):
        global summoner_spell_dict,summoner_skill_name,summoner_skill_index,summoner_skill_level
        '''遍历人物技能'''
        spell_dict = {}
        NameBase = 0xEB0204
        IdBase = NameBase + 0x30
        LevelNumberBase = NameBase + 0x1C
        Offset = 0x4C4C
        LevelOffset = 0x94
        LevelNameBase= NameBase+0x3C
        LevelCostBase =NameBase + 0xB8
        LevelOffset = 0x94

        for i in range(15):
            # 技能名称
            Name = NameBase + Offset * i
            Name = hex(Name)
            Name = dm.ReadString(hwnd,Name,0,30).encode('gb18030').decode('big5')
            # 技能ID:
            Id = IdBase + Offset * i
            Id = hex(Id)
            Id = dm.ReadInt(hwnd,Id,0)
            # 技能等级
            Level = LevelNumberBase + Offset * i
            Level = hex(Level)
            Level = dm.ReadInt(hwnd,Level,0) - 1
            # MpCost
            MpCost = LevelCostBase + Offset * i + LevelOffset * Level
            MpCost = hex(MpCost)
            MpCost = dm.ReadInt(hwnd,MpCost,0)
            print(Name,Id,Level+1,MpCost)

######################################其他
    def Change_GBK(self,string) :
        words = zhconv.convert(string,'zh-cn')
        return words

    def Return_panel(self):
        '''按F12恢复位置'''
        time.sleep(0.3)
        dm.keydown(17)
        time.sleep(0.05)
        dm.keypress(123)
        dm.keyup(17)
        time.sleep(0.2)

    def Get_panel(self,panel_name):
        '''获取面板情况'''
        global is_panel
        intX = 0
        intY = 0
        result = dm.FindPic(0,0,2000,2000,"./pic/{}.bmp".format(panel_name),"000000",0.9,0,intX,intY)
        self.is_panel = 1 if result[0] == 0 else 0
        return self.is_panel

    def Get_nurse_window(self):
        color1 = dm.getcolor(101,109)
        color2 = dm.getcolor(318,319)
        is_window_open = 1 if color1 == "bbac9d" and color2 == "346875" else 0
        return is_window_open

    def Get_talk_type(self):
        talk_type = dm.readint(hwnd,"C88264",0)
        return talk_type

    def Get_npc_nurse(self):
        nurse_type = dm.readint(hwnd,"C552F0",0)
        return nurse_type


dm = win32com.client.Dispatch('dm.dmsoft')
time.sleep(0.1)
hwnd = dm.GetMousePointWindow()
dm_ret = dm.SetDict(0,"font.txt")
dm_ret = dm.BindWindow(hwnd, "gdi", "windows", "windows", 0)
game = main()
# item_base = 0xF75B34
# print(dm.readint(hwnd,"F75B34",0))
# item_name = 0xF75B36
# item_num = 0xF76778
# offset = 0xC5C

# for i in range(20):
#     is_have_item = 0
#     item_base = hex(item_base)
#     is_have_item = dm.readint(hwnd,item_base,0)
#     print(is_have_item)

# main()
# print(main().Get_nurse_window())
# print(hwnd)
# player_name = dm.ReadString(hwnd,"00F6F7B8",0,12).encode('gb18030').decode('big5')
# print(player_name)
# main().reggame()
# color = dm.GetColor(383,30)
# print(color)
# NameBase = 0xEB0204
# NameBase = hex(NameBase)
# name = dm.ReadString(hwnd,NameBase,0,12).encode('gb18030').decode('big5')
# print(name)
# main().reggame()
# x = 0
# y = 0
# dm_ret = dm.FindStr(0,0,2000,2000,'LV3',"ffffff-000000",1.0,x,y)
# print(dm_ret)