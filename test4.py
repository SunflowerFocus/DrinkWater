import threading
import tkinter as tk
import pystray
from PIL import Image


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('喝水')
        self.root.geometry("600x200+1100+150")
        # 当用户点击窗口右上角的关闭按钮时，Tkinter 将自动发送 WM_DELETE_WINDOW 关闭事件。通过对其进行处理并调用 self.hide_window() 方法，可以改为将窗口隐藏到系统托盘中。
        # 该方法用于将程序窗口隐藏到系统托盘中而非直接退出应用程序
        self.root.protocol('WM_DELETE_WINDOW', self.hide_window)
        # 添加菜单和图标
        self.create_systray_icon()
        # 绘制界面
        self.interface()

    def interface(self):
        """"界面编写位置"""
        pass

    def create_systray_icon(self):
        menu = (
            pystray.MenuItem('显示面板', self.show_window, default=True),
            pystray.Menu.SEPARATOR,  # 在系统托盘菜单中添加分隔线
            pystray.MenuItem('退出', self.quit_window))
        self.icon = pystray.Icon("icon", Image.open("icon.png"), "图标名称", menu)
        threading.Thread(target=self.icon.run, daemon=True).start()

    # 关闭窗口时隐藏窗口，并将 Pystray 图标放到系统托盘中。
    def hide_window(self):
        self.root.withdraw()

    # 从系统托盘中恢复 Pystray 图标，并显示隐藏的窗口。
    def show_window(self):
        self.icon.visible = True
        self.root.deiconify()

    def quit_window(self, icon: pystray.Icon):
        """
        退出程序
        """
        icon.stop()  # 停止 Pystray 的事件循环
        self.root.quit()  # 终止 Tkinter 的事件循环
        self.root.destroy()  # 销毁应用程序的主窗口和所有活动


if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()
