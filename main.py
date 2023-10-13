import tkinter as tk
import pystray
from PIL import Image
import threading
import tkinter.simpledialog


class GUI:
    def __init__(self, title):
        self.icon = None
        self.time = 0
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("600x200")
        self.adaption_window_center()
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.hide_window)
        self.interface()
        self.create_systray_icon()

    def adaption_window_center(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 600) // 2
        y = (screen_height - 200) // 2
        self.root.geometry(f"+{x}+{y}")

    def create_systray_icon(self):
        menu = (
            pystray.MenuItem('显示面板', self.show_window, default=True),
            pystray.Menu.SEPARATOR,  # 在系统托盘菜单中添加分隔线
            pystray.MenuItem('退出', self.quit_window)
        )
        self.icon = pystray.Icon("icon", Image.open("icon.png"), "喝水提醒", menu)

    def interface(self):
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(side=tk.TOP)
        setting = tk.Button(frame_buttons, text="设置间隔时间", command=lambda: self.setting_run(), width=18, height=2)
        start = tk.Button(frame_buttons, text="开始", command=lambda: self.start_run(), width=18, height=2)
        reset = tk.Button(frame_buttons, text="重置", command=lambda: self.reset_run(), width=18, height=2)
        setting.pack(side=tk.LEFT, padx=20, pady=20)
        start.pack(side=tk.LEFT, padx=20, pady=20)
        reset.pack(side=tk.LEFT, padx=20, pady=20)

        frame_label = tk.Frame(self.root)
        frame_label.pack(side=tk.TOP)
        label = tk.Label(frame_label, text="00:00:00")
        label.config(font=("Arial", 48))
        label.pack()

    def setting_run(self):
        minute_value = tk.simpledialog.askinteger(
            title='',
            prompt='间隔(分钟):',
            initialvalue=5,
            parent=self.root,
            minvalue=1,
            maxvalue=180
        )
        if minute_value:
            self.time = minute_value * 60
        if self.time > 0:
            self.refresh_setting_text()
            self.refresh_label_text()

    def start_run(self):
        return 1

    def reset_run(self):
        return 1

    def refresh_setting_text(self):
        setting.config(text="倒计时: " + str(time) + " 秒")

    def refresh_label_text(self):
        label.config(text=convert_format_second(time))



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
    gui = GUI('喝水提醒')
    gui.start()
