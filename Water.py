import pystray
import threading
from PIL import Image
from functools import partial
from Helper import *
import inspect


class GUI:
    icon = None
    original_second: int = None
    second: int = None
    setting_btn = None
    start_btn = None
    stop_btn = None
    reset_btn = None
    second_label = None
    reminder_window = None
    is_run = False
    after_id = None

    def __init__(self, title):
        self.root = create_water_gui(title)
        self.create_menubar()
        self.root.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.create_gui_content()
        self.create_systray_icon()

    def create_systray_icon(self):
        menus = (
            pystray.MenuItem('显示面板', self.show_window, default=True, visible=True),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem('退出', self.quit_window)
        )
        self.icon = pystray.Icon("icon", Image.open("images/icon.png"), "喝水提醒", menus)

    def create_gui_content(self):
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(side=tk.TOP)
        frame_label = tk.Frame(self.root)
        frame_label.pack(side=tk.TOP)

        self.setting_btn = tk.Button(frame_btn, text="设置间隔时长", command=lambda: self.setting_run(), width=18,
                                     height=2)
        self.setting_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.start_btn = tk.Button(frame_btn, text="开始", command=lambda: self.start_run(), width=18, height=2,
                                   state='disabled')
        self.start_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.stop_btn = tk.Button(frame_btn, text="暂停", command=lambda: self.stop_run(), width=18, height=2,
                                  state='disabled')
        self.stop_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.reset_btn = tk.Button(frame_btn, text="重置", command=lambda: self.reset_run(), width=18, height=2)
        self.reset_btn.pack(side=tk.LEFT, padx=20, pady=20)

        self.second_label = tk.Label(frame_label, text="00:00:00", font=("Arial", 48))
        self.second_label.pack()

    def create_menubar(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=True)
        file_menu.add_command(label='关于', command=self.about)
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=self.quit_window)
        menubar.add_cascade(label='帮助', menu=file_menu)
        self.root.config(menu=menubar)

    def show_popup(self):
        self.reminder_window = create_reminder_window(self.root)

        frame_title = tk.Frame(self.reminder_window)
        frame_title.pack(side=tk.TOP)
        frame_btn = tk.Frame(self.reminder_window)
        frame_btn.pack(side=tk.TOP)
        frame_end = tk.Frame(self.reminder_window)
        frame_end.pack(side=tk.TOP)

        tip_text1 = tkinter.Label(frame_title, text="记得多喝水，保持身体健康")
        tip_text1.config(font=("Arial", 72))
        tip_text1.pack(pady=160)

        reset_btn = tk.Button(frame_btn, text="重置", command=lambda: self.reset_run_popup(), width=16, height=2)
        reset_btn.pack(side=tk.LEFT, pady=6, padx=26)

        close_btn = tk.Button(frame_btn, text="关闭", command=lambda: self.close_run_popup(), width=16, height=2)
        close_btn.pack(side=tk.LEFT, pady=6, padx=26)

        stop_btn = tk.Button(frame_btn, text="暂停", command=lambda: self.stop_run_popup(), width=16, height=2)
        stop_btn.pack(side=tk.LEFT, pady=6, padx=26)

        tip_text2 = tkinter.Label(frame_end, text="关闭当前窗口继续提醒")
        tip_text2.pack()

        self.reminder_window.protocol("WM_DELETE_WINDOW", partial(self.close_run_popup))

    def exec_after(self):
        self.second -= 1
        refresh_second_text(self)
        self.exec()

    def exec(self):
        if self.second >= 1 and self.is_run:
            self.after_id = self.root.after(1000, self.exec_after)
        else:
            self.show_popup()

    def setting_run(self):
        refresh_gui(self, inspect.currentframe().f_code.co_name)

    def start_run(self):
        refresh_gui(self, inspect.currentframe().f_code.co_name)

    def stop_run(self):
        refresh_gui(self, inspect.currentframe().f_code.co_name)

    def reset_run(self):
        refresh_gui(self, inspect.currentframe().f_code.co_name)

    def reset_run_popup(self):
        refresh_run_popup(self, inspect.currentframe().f_code.co_name)

    def stop_run_popup(self):
        refresh_run_popup(self, inspect.currentframe().f_code.co_name)

    def close_run_popup(self):
        refresh_run_popup(self, inspect.currentframe().f_code.co_name)

    def start(self):
        threading.Thread(target=self.icon.run, daemon=True).start()
        self.root.mainloop()

    def show_window(self):
        self.root.deiconify()

    def quit_window(self):
        self.icon.stop()
        self.root.quit()
        self.root.destroy()

    def hide_window(self):
        self.root.withdraw()

    def about(self):
        about_window = create_about(self.root)
        tip_text1 = tkinter.Label(about_window, text="喝水有宜健康")
        tip_text1.config(font=("Arial", 26))
        tip_text1.pack(pady=62)
        tip_text2 = tkinter.Label(about_window, text="Powered by Pan")
        tip_text2.pack()


if __name__ == '__main__':
    gui = GUI('喝水')
    gui.start()
