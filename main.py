import tkinter
# 导入消息对话框子模块
import tkinter.simpledialog

import time

# 创建主窗口
tk = tkinter.Tk()
# 设置窗口大小
tk.minsize(300, 300)


def format_time(number):
    return number * 60


def water():
    number = tkinter.simpledialog.askinteger(title='获取信息', prompt='间隔(分钟)：', initialvalue=5)
    number = format_time(number)

    while number > 0:
        print("倒计时: " + str(number) + '秒')
        # start.config(text="倒计时: " + str(number) + '秒')
        time.sleep(1)
        number -= 1


# 添加按钮
start = tkinter.Button(tk, text='开始', width=100, command=water)
end = tkinter.Button(tk, text='结束', width=100, command=water)
start.pack()
end.pack()

tk.title('喝水')

# 加入消息循环
tk.mainloop()
