import tkinter

import pystray  # 导入 PyStray 库
from PIL import Image  # 导入 Python Imaging Library 的 Image 类
import time
from tkinter import messagebox


class MyMessageBox(tkinter.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.title(title)

        # 创建消息文本标签
        self.message_label = tkinter.Label(self, text=message, padx=20, pady=20)
        self.message_label.pack()

        # 创建确定按钮，并绑定回调函数
        self.ok_button = tkinter.Button(self, text="确定", command=self.destroy)
        self.ok_button.pack(pady=10)

# 定义点击菜单项的回调函数
def click_menu(icon, item):
    time.sleep(3)
    # message_box = MyMessageBox("提示信息", "你是否确定要关闭程序？")
    # message_box.mainloop()
    messagebox.showwarning("喝水", "喝水提醒")
    print("点击了", item)


# 定义退出菜单项的回调函数
def on_exit(icon, item):
    icon.stop()


# 定义通知内容的回调函数
def notify(icon: pystray.Icon):
    icon.notify(title="喝水提醒", message="该喝水了")


# 创建菜单项
menu = (
    pystray.MenuItem('菜单A', click_menu),  # 第一个菜单项
    pystray.MenuItem('菜单B', click_menu),  # 第二个菜单项
    pystray.MenuItem(text='菜单C', action=click_menu, enabled=False),  # 第三个菜单项
    pystray.MenuItem(text='发送通知', action=notify),  # 第四个菜单项
    pystray.MenuItem(text='点击托盘图标显示', action=click_menu, default=True, visible=False),  # 第五个菜单项
    pystray.MenuItem(text='退出', action=on_exit),  # 最后一个菜单项
)

# 创建图标对象
image = Image.open("icon_2.png")  # 打开并读取图片文件
icon = pystray.Icon("name", image, "鼠标移动到\n托盘图标上\n展示内容", menu)  # 创建图标对象并绑定菜单项
# 显示图标并等待用户操作
icon.run()
