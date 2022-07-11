import ctypes, sys
import win32process
import win32api
import win32security
import win32com.client
import time
import random
import zhconv
from tkinter import *


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # 将要运行的代码加到这里
    dm = win32com.client.Dispatch('dm.dmsoft')
    # dm_ret = dm.SetPath("E:\\Down\\soft\\大漠\\Crossgate")
    # dm_ret = dm.SetDict(0,"ml_soft.txt")
    hwnd = dm.GetMousePointWindow()
    dm_ret = dm.BindWindow(hwnd, "gdi", "windows", "windows", 0)
    priv_flags = win32security.TOKEN_ADJUST_PRIVILEGES | win32security.TOKEN_QUERY
    hToken = win32security.OpenProcessToken (win32api.GetCurrentProcess(), priv_flags)
    privilege_id = win32security.LookupPrivilegeValue (None, win32security.SE_DEBUG_NAME)
    old_privs = win32security.AdjustTokenPrivileges (hToken, 0, [(privilege_id, win32security.SE_PRIVILEGE_ENABLED)])
    processid = win32process.GetWindowThreadProcessId(hwnd)
    pshandle = win32api.OpenProcess(2035711,False,processid[1])

    def get_fight_flag():
        '''自动战斗标识(战斗中3 战斗结束画面1 非战斗0)'''
        global is_fight
        is_fight = dm.ReadInt(hwnd,"73BE20",0)

    def clear_text():
        t10.delete(1.0,END)
        t11.delete(1.0,END)
        t12.delete(1.0,END)
        t13.delete(1.0,END)
        t14.delete(1.0,END)
        t15.delete(1.0,END)
        t16.delete(1.0,END)
        t17.delete(1.0,END)
        t18.delete(1.0,END)
        t19.delete(1.0,END)

    def count_monster():
        '''计算怪物数量'''
        global gw_cnt,monsters_list_front,monsters_list_back
        monster_mess=dm.ReadString(hwnd, "5A0BA8", 0, 5000)
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
                        monsters_list.append(monster_mess[j+k][1].encode('gb18030').decode('big5'))
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
        monsters_list_front = []
        # 前排怪物列表
        for i in monsters.keys() :
            if i >= 15 :
                monsters_list_front.append(i)
                if i == 15 :
                    t15.delete(1.0,END)
                    t15.insert(END,monsters[i][0] + "\n","tag_1")
                    t15.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t15.insert(END,"HP : " ,"tag_2")
                    t15.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t15.insert(END,"MP : " ,"tag_3")
                    t15.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t15.update()
                elif i == 16 : 
                    t16.delete(1.0,END)
                    t16.insert(END,monsters[i][0] + "\n","tag_1")
                    t16.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t16.insert(END,"HP : " ,"tag_2")
                    t16.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t16.insert(END,"MP : " ,"tag_3")
                    t16.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t16.update()
                elif i == 17 : 
                    t17.delete(1.0,END)
                    t17.insert(END,monsters[i][0] + "\n","tag_1")
                    t17.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t17.insert(END,"HP : " ,"tag_2")
                    t17.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t17.insert(END,"MP : " ,"tag_3")
                    t17.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t17.update()
                elif i == 18 : 
                    t18.delete(1.0,END)
                    t18.insert(END,monsters[i][0] + "\n","tag_1")
                    t18.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t18.insert(END,"HP : " ,"tag_2")
                    t18.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t18.insert(END,"MP : " ,"tag_3")
                    t18.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t18.update()
                elif i == 19 : 
                    t19.delete(1.0,END)
                    t19.insert(END,monsters[i][0] + "\n","tag_1")
                    t19.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t19.insert(END,"HP : " ,"tag_2")
                    t19.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t19.insert(END,"MP : " ,"tag_3")
                    t19.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t19.update()
        # 后排怪物列表
        monsters_list_back = []
        for i in monsters.keys() :
            if i >= 10 and i < 15:
                monsters_list_back.append(i)
                if i == 10 :
                    t10.delete(1.0,END)
                    t10.insert(END,monsters[i][0] + "\n","tag_1")
                    t10.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t10.insert(END,"HP : " ,"tag_2")
                    t10.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t10.insert(END,"MP : " ,"tag_3")
                    t10.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t10.update()
                elif i == 11 : 
                    t11.delete(1.0,END)
                    t11.insert(END,monsters[i][0] + "\n","tag_1")
                    t11.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t11.insert(END,"HP : " ,"tag_2")
                    t11.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t11.insert(END,"MP : " ,"tag_3")
                    t11.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t11.update()
                elif i == 12 : 
                    t12.delete(1.0,END)
                    t12.insert(END,monsters[i][0] + "\n","tag_1")
                    t12.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t12.insert(END,"HP : " ,"tag_2")
                    t12.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t12.insert(END,"MP : " ,"tag_3")
                    t12.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t12.update()
                elif i == 13 : 
                    t13.delete(1.0,END)
                    t13.insert(END,monsters[i][0] + "\n","tag_1")
                    t13.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t13.insert(END,"HP : " ,"tag_2")
                    t13.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t13.insert(END,"MP : " ,"tag_3")
                    t13.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t13.update()
                elif i == 14 : 
                    t14.delete(1.0,END)
                    t14.insert(END,monsters[i][0] + "\n","tag_1")
                    t14.insert(END,"LV : " + str(monsters[i][1]) + '\n',"tag_1")
                    t14.insert(END,"HP : " ,"tag_2")
                    t14.insert(END,str(monsters[i][2]) + '/ ' + str(monsters[i][3]) + '\n',"tag_1")
                    t14.insert(END,"MP : " ,"tag_3")
                    t14.insert(END,str(monsters[i][4]) + '/ ' + str(monsters[i][5]) ,"tag_1")
                    t14.update()

    win = Tk()
    # 修改窗口标题
    win.title("CrossGate - Monsters")
    # 窗口置顶
    win.wm_attributes('-topmost',1)

    height = 5
    width = 20
    relief = 'ridge'
    fm14 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 0,column = 1)
    fm12 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 0,column = 2)
    fm10 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 0,column = 3)
    fm11 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 0,column = 4)
    fm13 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 0,column = 5)
    fm19 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 1,column = 1)
    fm17 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 1,column = 2)
    fm15 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 1,column = 3)
    fm16 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 1,column = 4)
    fm18 = Frame(height = 60,width = 130,bg = 'white',relief=relief,borderwidth= 1).grid(row = 1,column = 5)
    global t10,t11,t12,t13,t14,t15,t16,t17,t18,t19
    t14 = Text(fm14,width = 17,height = 4,relief = 'flat')
    t14.grid(row = 0,column = 1)
    t14.tag_config("tag_1", justify = "center")
    t14.tag_config("tag_2", foreground="red",justify = "center")
    t14.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t12 = Text(fm12,width = 17,height = 4,relief = 'flat')
    t12.grid(row = 0,column = 2)
    t12.tag_config("tag_1", justify = "center")
    t12.tag_config("tag_2", foreground="red",justify = "center")
    t12.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t10 = Text(fm10,width = 17,height = 4,relief = 'flat')
    t10.grid(row = 0,column = 3)
    t10.tag_config("tag_1", justify = "center")
    t10.tag_config("tag_2", foreground="red",justify = "center")
    t10.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t11 = Text(fm11,width = 17,height = 4,relief = 'flat')
    t11.grid(row = 0,column = 4)
    t11.tag_config("tag_1", justify = "center")
    t11.tag_config("tag_2", foreground="red",justify = "center")
    t11.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t13 = Text(fm13,width = 17,height = 4,relief = 'flat')
    t13.grid(row = 0,column = 5)
    t13.tag_config("tag_1", justify = "center")
    t13.tag_config("tag_2", foreground="red",justify = "center")
    t13.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t19 = Text(fm19,width = 17,height = 4,relief = 'flat')
    t19.grid(row = 1,column = 1)
    t19.tag_config("tag_1", justify = "center")
    t19.tag_config("tag_2", foreground="red",justify = "center")
    t19.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t17 = Text(fm17,width = 17,height = 4,relief = 'flat')
    t17.grid(row = 1,column = 2)
    t17.tag_config("tag_1", justify = "center")
    t17.tag_config("tag_2", foreground="red",justify = "center")
    t17.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t15 = Text(fm15,width = 17,height = 4,relief = 'flat')
    t15.grid(row = 1,column = 3)
    t15.tag_config("tag_1", justify = "center")
    t15.tag_config("tag_2", foreground="red",justify = "center")
    t15.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t16 = Text(fm16,width = 17,height = 4,relief = 'flat')
    t16.grid(row = 1,column = 4)
    t16.tag_config("tag_1", justify = "center")
    t16.tag_config("tag_2", foreground="red",justify = "center")
    t16.tag_config("tag_3", foreground="green",justify = "center")
    """"""
    t18 = Text(fm18,width = 17,height = 4,relief = 'flat')
    t18.grid(row = 1,column = 5)
    t18.tag_config("tag_1", justify = "center")
    t18.tag_config("tag_2", foreground="red",justify = "center")
    t18.tag_config("tag_3", foreground="green",justify = "center")
    """"""


    while 1 :
        get_fight_flag()
        rd = 0
        while is_fight == 3:
            time.sleep(1)
            round =  dm.ReadInt(hwnd,"5A8D90",0) + 1
            if round > rd :
                try :
                    clear_text()
                    count_monster()
                    rd = round
                except :
                    clear_text()
            round = 0
            get_fight_flag()

    win.mainloop()