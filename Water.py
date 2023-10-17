import pystray
import threading
from PIL import Image
from functools import partial
from App import *
from Function import *


class GUI:
    icon = None
    original_second: int = 0
    second: int = 0
    setting_btn = None
    start_btn = None
    stop_btn = None
    reset_btn = None
    second_label = None
    screen_width = 0
    screen_height = 0
    reminder_window = None
    flag = True
    after_id = None

    def __init__(self, title):
        self.root = create_water_gui(title)
        self.root.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.create_gui_content()
        self.create_systray_icon()

    def create_systray_icon(self):
        self.icon = pystray.Icon("icon", Image.open("images/icon.png"), "喝水提醒", (
            pystray.MenuItem('显示面板', self.show_window, default=True),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('暂停', self.show_window),
            pystray.MenuItem('重置', self.show_window),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('退出', self.quit_window)
        ))

    def create_gui_content(self):
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(side=tk.TOP)
        self.setting_btn = tk.Button(frame_btn, text="设置间隔时间", width=18,height=2)
        self.setting_btn.config(command=lambda: self.setting_run())
        self.setting_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.start_btn = tk.Button(frame_btn, text="开始", command=lambda: self.start_run(), width=18, height=2)
        self.start_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.stop_btn = tk.Button(frame_btn, text="暂停", command=lambda: self.stop_run(), width=18, height=2, state='disabled')
        self.stop_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.reset_btn = tk.Button(frame_btn, text="重置", command=lambda: self.reset_run(), width=18, height=2, state='disabled')
        self.reset_btn.pack(side=tk.LEFT, padx=20, pady=20)

        frame_label = tk.Frame(self.root)
        frame_label.pack(side=tk.TOP)
        self.second_label = tk.Label(frame_label, text="00:00:00", font=("Arial", 48))
        self.second_label.pack()

    def update_label_text(self):
        if self.second >= 1 and self.flag:
            self.second -= 1
            refresh_second_text(self)
            self.after_id = self.root.after(1000, self.update_label_text)
        else:
            self.show_popup()

    def show_popup(self):
        self.reminder_window = create_reminder_window(self.root)

        menubar = tk.Menu(self.reminder_window)
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='选项', menu=file_menu, command=self.reset_show_popup)
        file_menu.add_command(label='重置', command=self.reset_show_popup)
        self.reminder_window.config(menu=menubar)

        frame_title = tk.Frame(self.reminder_window)
        frame_title.pack(side=tk.TOP)
        tip_text1 = tkinter.Label(frame_title, text="记得多喝水，保持身体健康")
        tip_text1.config(font=("Arial", 68))
        tip_text1.pack(pady=160)

        frame_btn = tk.Frame(self.reminder_window)
        frame_btn.pack(side=tk.TOP)
        reset_btn = tk.Button(frame_btn, text="重置", command=lambda: self.reset_run(), width=16, height=1)
        reset_btn.pack(side=tk.LEFT, padx=5, pady=5)
        close_btn = tk.Button(frame_btn, text="关闭", command=lambda: self.reset_run(), width=16, height=1)
        close_btn.pack(side=tk.LEFT)

        frame_end = tk.Frame(self.reminder_window)
        frame_end.pack(side=tk.TOP)
        tip_text2 = tkinter.Label(frame_end, text="关闭当前窗口继续提醒")
        tip_text2.pack()

        self.reminder_window.protocol("WM_DELETE_WINDOW", partial(self.close_show_popup,
                                                             self.reminder_window,
                                                             self.original_second,
                                                             self.second)
                                 )

    def close_show_popup(self, reminder_window: tkinter.Toplevel, original_second: int, second: int):
        reminder_window.destroy()
        if original_second != 0 and second == 0:
            self.second = original_second
            self.update_label_text()

    def setting_run(self):
        refresh_gui(self, 'setting')

    def start_run(self):
        refresh_gui(self, 'start')
        self.update_label_text()

    def stop_run(self):
        refresh_gui(self, 'stop')

    def reset_run(self):
        refresh_gui(self, 'reset')

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

    def reset_show_popup(self):
        print(22)


if __name__ == '__main__':
    print('正在启动...')
    gui = GUI('喝水')
    gui.start()
