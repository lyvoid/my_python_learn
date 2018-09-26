#!urs/bin/env/python3
# -*- coding:utf-8 -*-

import time
import win32api
import win32con
import win32gui
import my_win_controller.config as config


def change_to_end(win_front_, win_back_, win_controller_):
    # 
    (left, top, right, bottom) = win32gui.GetWindowRect(win_back_)
    # set focus on my windows and click in the center of my window
    win32gui.SetForegroundWindow(win_back_)
    win32api.SetCursorPos((left + (right - left) // 2, top + (bottom - top) // 2))
    time.sleep(0.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.002)
    # 
    win32gui.SetForegroundWindow(win_front_)
    time.sleep(0.005)
    # go to cmd win
    win32gui.SetForegroundWindow(win_controller_)
    (left, top, right, bottom) = win32gui.GetWindowRect(win_controller_)
    win32api.SetCursorPos((left + (right - left) // 2, top + (bottom - top) // 2))
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.005)
    # type enter key (cmd win get focus)
    win32api.keybd_event(13, 0, 0, 0)
    time.sleep(0.005)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


def change_to_second(win_back_, win_controller_):
    # get window
    (left, top, right, bottom) = win32gui.GetWindowRect(win_back_)
    # set focus and click in the center of window
    win32gui.SetForegroundWindow(win_back_)
    win32api.SetCursorPos((left + (right - left) // 2, top + (bottom - top) // 2))
    time.sleep(0.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.002)
    # go to cmd win
    win32gui.SetForegroundWindow(win_controller_)
    (left, top, right, bottom) = win32gui.GetWindowRect(win_controller_)
    win32api.SetCursorPos((left + (right - left) // 2, top + (bottom - top) // 2))
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.005)
    # type enter key (cmd win get focus)
    win32api.keybd_event(13, 0, 0, 0)
    time.sleep(0.005)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    str_ = "___"
    win_back = win32gui.FindWindow(None, config.back_name)
    win_front = win32gui.FindWindow(None, config.front_name)
    win_controller = win32gui.FindWindow(None, config.win_controller_name)
    print("%s,%s" % (win_back, win_front))
    while True:
        if input() == "":
            change_to_end(win_front, win_back, win_controller)
            print(str_)
        else:
            change_to_second(win_back, win_controller)
            print(str_)
