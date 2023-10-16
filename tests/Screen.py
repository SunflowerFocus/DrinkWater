import unittest
from PyQt5.QtWidgets import QApplication
import win32api
import tkinter as tk
import pygame
import wx


class ScreenCase(unittest.TestCase):

    def test_qt5(self):
        app = QApplication([])
        screenRect = app.desktop().screenGeometry()
        width, height = screenRect.width(), screenRect.height()
        print("屏幕长: ", width)
        print("屏幕宽: ", height)

    def test_winapi(self):
        width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        print("屏幕长：", width)
        print("屏幕宽：", height)

    def test_tkinter(self):
        root = tk.Tk()
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        print("屏幕长：", width)
        print("屏幕宽：", height)

    def test_pygame(self):
        pygame.init()
        infoObject = pygame.display.Info()
        width, height = infoObject.current_w, infoObject.current_h
        print("屏幕长：", width)
        print("屏幕宽：", height)

    def test_wx(self):
        app = wx.App()
        screen = wx.ScreenDC()
        size = screen.GetSize()
        width, height = size[0], size[1]
        print("屏幕长：", width)
        print("屏幕宽：", height)


if __name__ == '__main__':
    unittest.main()
