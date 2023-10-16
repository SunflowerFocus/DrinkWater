import time
import tkinter as tk
import tkinter.simpledialog
import threading
import pystray
from PIL import Image
from functools import partial
from tkinter import messagebox


def convert_format_second(second):
    remaining_seconds = second % 60
    minutes = second // 60
    hours = minutes // 60
    remaining_minutes = minutes % 60

    time_str = f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}"

    return time_str


def show_popup():
    messagebox.showinfo("喝水", "喝水提醒")


class GUI:
    icon = None
    original_second: int = 0
    second: int = 0
    setting_btn = None
    start_btn = None
    reset_btn = None
    second_label = None
    screen_width = 0
    screen_height = 0

    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("600x200")
        x, y = self.adaption_window_center(600, 200)
        self.root.geometry(f"+{x}+{y}")
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.root.attributes('-topmost', 1)
        self.interface()
        self.create_systray_icon()

    def adaption_window_center(self, width: int, height: int):
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        return (self.screen_width - width) // 2, (self.screen_height - height) // 2

    def create_systray_icon(self):
        menu = (
            pystray.MenuItem('显示面板', self.show_window, default=True),
            pystray.Menu.SEPARATOR,  # 在系统托盘菜单中添加分隔线
            pystray.MenuItem('退出', self.quit_window)
        )
        self.icon = pystray.Icon("icon", Image.open("images/icon.png"), "喝水提醒", menu)

    def interface(self):
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(side=tk.TOP)
        self.setting_btn = tk.Button(frame_btn, text="设置间隔时间", command=lambda: self.setting_run(), width=18,
                                     height=2)
        self.setting_btn.pack(side=tk.LEFT, padx=20, pady=20)
        self.start_btn = tk.Button(frame_btn, text="开始", command=lambda: self.start_run(), width=18, height=2)
        self.start_btn.pack(side=tk.LEFT, padx=20, pady=20)
        self.reset_btn = tk.Button(frame_btn, text="重置", command=lambda: self.reset_run(), width=18, height=2)
        self.reset_btn.pack(side=tk.LEFT, padx=20, pady=20)

        frame_label = tk.Frame(self.root)
        frame_label.pack(side=tk.TOP)
        self.second_label = tk.Label(frame_label, text="00:00:00", font=("Arial", 48))
        self.second_label.pack()

    def setting_run(self):
        minute_value = tk.simpledialog.askinteger(
            title='喝水',
            prompt='间隔(分钟):',
            parent=self.root,
            initialvalue=5,
            minvalue=1,
            maxvalue=180
        )
        if minute_value:
            self.second = minute_value * 60
        if self.second > 0:
            self.refresh_setting_text()
            self.refresh_label_text()

    def update_label_text(self):
        if self.original_second == 0 and self.second == 0:
            return
        if self.second >= 1:
            self.second -= 1
            self.refresh_setting_text()
            self.refresh_label_text()
            self.root.after(1000, self.update_label_text)
        else:
            self.show_popup()

    def show_popup(self):
        reminder_window = tkinter.Toplevel(self.root)
        reminder_window.title("喝水提醒")
        reminder_window.geometry("1280x460")
        x, y = self.adaption_window_center(1280, 460)
        reminder_window.geometry(f"+{x}+{y}")
        reminder_window.resizable(False, False)
        reminder_window.grab_set()
        reminder_window.focus_force()
        reminder_window.attributes('-topmost', 1)  # 设置为最前面

        tip_text = tkinter.Label(reminder_window, text="记得多喝水，保持身体健康")
        tip_text.config(font=("Arial", 68))
        tip_text.pack(pady=160)
        tip_text1 = tkinter.Label(reminder_window, text="关闭当前窗口继续提醒")
        tip_text1.pack()

        reminder_window.protocol("WM_DELETE_WINDOW", partial(self.close_show_popup,
                                                             reminder_window,
                                                             self.original_second,
                                                             self.second)
                                 )

    def close_show_popup(self, reminder_window: tkinter.Toplevel, original_second: int, second: int):
        reminder_window.destroy()
        if original_second != 0 and second == 0:
            self.second = original_second
            self.update_label_text()

    def start_run(self):
        if self.original_second == 0 and self.second == 0:
            return
        self.original_second = self.second
        self.setting_btn.config(state='disabled')
        self.start_btn.config(state='disabled')
        self.update_label_text()

    def reset_run(self):
        self.original_second = self.second = 0
        self.setting_btn.config(state='normal')
        self.start_btn.config(state='normal')
        self.refresh_label_text()
        self.reset_label_text()

    def refresh_setting_text(self):
        minute = self.second // 60
        if self.second % 60 != 0:
            minute += 1
        self.setting_btn.config(text="倒计时: " + str(minute) + " 分钟")

    def refresh_label_text(self):
        self.second_label.config(text=convert_format_second(self.second))

    def reset_label_text(self):
        self.setting_btn.config(text='设置间隔时间')

    def start(self):
        threading.Thread(target=self.icon.run, daemon=True).start()
        self.root.mainloop()

    def show_window(self):
        self.icon.visible = True
        self.root.deiconify()

    def quit_window(self, icon: pystray.Icon):
        icon.stop()  # 停止 Pystray 的事件循环
        self.root.quit()  # 终止 Tkinter 的事件循环
        self.root.destroy()  # 销毁应用程序的主窗口和所有活动

    def hide_window(self):
        self.root.withdraw()


if __name__ == '__main__':
    print('正在启动...')
    gui = GUI('喝水')
    gui.start()
