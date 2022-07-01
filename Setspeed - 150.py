# -*- coding: utf-8 -*-
"""
Spyder Editor   
This is a temporary script file.
"""

import ctypes
import win32process
import win32api
import win32security
import win32com.client
import time


dm = win32com.client.Dispatch('dm.dmsoft')
# hwnd = dm.FindWindow("","魔力寶貝") 
hwnd = dm.EnumWindow(0,"魔力寶貝","",1+4+8+16)
hwnd = hwnd.split(',')
while 1:
	for i in hwnd:
		speed = dm.ReadInt(i,"F70950",0)
		if speed == 100 :
			dm.WriteInt(i,"F70950",0,130)
	time.sleep(3)
		# dm.WriteInt(i,"F70950",0,100)

<<<<<<< HEAD
	
=======
# a5 db a4 c6 a7 f0 c0 bb
>>>>>>> 2ae8223ca4bff982c5e57c924c39f004a3a9dd1f
