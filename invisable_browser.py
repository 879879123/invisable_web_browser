import win32gui
import win32con
import winxpgui
import win32api
import subprocess
import time

subprocess.Popen([r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "www.google.com"])
time.sleep(5) 
hwnd = win32gui.FindWindow(None, "test")  #Google - Google Chrome

win32gui.SetWindowLong (hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong (hwnd, win32con.GWL_EXSTYLE ) | win32con.WS_EX_LAYERED )
winxpgui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 60, win32con.LWA_ALPHA) 
