import tkinter.simpledialog
import time, ctypes
from tkinter import messagebox

time.sleep(2)


def convert_format_second(second):
    remaining_seconds = second % 60
    minutes = second // 60
    hours = minutes // 60
    remaining_minutes = minutes % 60

    time_str = f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}"
    return time_str


def refresh_label_text():
    label.config(text=convert_format_second(time))


def refresh_setting_text():
    setting.config(text="倒计时: " + str(time) + " 秒")


def setting_run():
    minute_value = tkinter.simpledialog.askinteger(
        title='',
        prompt='间隔(分钟):',
        initialvalue=5,
        parent=root,
        minvalue=1,
        maxvalue=180
    )
    global time
    if minute_value:
        time = minute_value * 60
        time = 10
    if time > 0:
        refresh_setting_text()
        refresh_label_text()


def show_popup():
    # messagebox.showinfo("喝水", "喝水提醒")
    popup = tkinter.Toplevel(root)
    popup.title("喝水提醒")
    popup.lift()
    popup.geometry("600x200")

    tip = tkinter.Label(popup, text="喝水时间到了")
    tip.config(font=("Arial", 48))
    tip.pack(pady=60)


def update_label_text():
    global time
    if time >= 0:
        refresh_setting_text()
        refresh_label_text()
        time -= 1
        root.after(1000, update_label_text)
    else:
        show_popup()


def start_run():
    setting.config(state='disabled')
    start.config(state='disabled')
    update_label_text()


def reset_run():
    global time
    time = 0
    setting.config(state='normal')
    start.config(state='normal')


root = tkinter.Tk()

time = 0

# 上方布局
frame_buttons = tkinter.Frame(root)
frame_buttons.pack(side=tkinter.TOP)

setting = tkinter.Button(frame_buttons, text="设置间隔时间", command=lambda: setting_run())
start = tkinter.Button(frame_buttons, text="开始", command=lambda: start_run())
reset = tkinter.Button(frame_buttons, text="重置", command=lambda: reset_run())

setting.pack(side=tkinter.LEFT, padx=20, pady=20)
start.pack(side=tkinter.LEFT, padx=20, pady=20)
reset.pack(side=tkinter.LEFT, padx=20, pady=20)

setting.config(width=18, height=2)
start.config(width=18, height=2)
reset.config(width=18, height=2)

# 下方标签布局
frame_label = tkinter.Frame(root)
frame_label.pack()

label = tkinter.Label(frame_label, text="00:00:00")
label.config(font=("Arial", 48))
label.pack()

root.minsize(600, 200)
root.resizable(False, False)
root.title('喝水')
root.geometry("600x200+1100+150")
root.mainloop()
