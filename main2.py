import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

import time

import tkinter as tk
import time


def update_button_text(count):
    if count > 0:
        button.config(text=str(count))
        count -= 1
        root.after(1000, update_button_text, count)
    else:
        button["text"] = "倒计时结束"


root = tk.Tk()

root.minsize(300, 300)


button = tk.Button(root, text="开始倒计时", command=lambda: update_button_text(10))
button.pack()

root.mainloop()
