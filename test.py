from main import *
import sys
import random
import Game_call as gc

def mvto(x,y):
    '''移动到某个坐标'''
    dm.WriteData(hwnd, "00C081EC", "B8 00 00 00 00")
    dm.WriteData(hwnd, "00489431", "BA 00 00 00 00 90")
    dm.WriteInt(hwnd, "00C081EC", 0, x)
    dm.WriteInt(hwnd, "00C082B4", 0, y)
    dm.WriteInt(hwnd, "00C153D8", 0, 1)
    time.sleep(0.5)
    dm.WriteInt(hwnd, "00C153D8", 0, 0)
    dm.WriteData(hwnd, "0048940D", "A1 90 89 CB 00")
    dm.WriteData(hwnd, "00489431", "8B 15 88 89 CB 00")

mvto(144,155)