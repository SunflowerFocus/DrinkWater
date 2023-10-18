import tkinter as tk
import tkinter.simpledialog
import Water


def adaption_window_center(root, width: int, height: int):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return (screen_width - width) // 2, (screen_height - height) // 2


def create_water_gui(title: str):
    root = tk.Tk()
    root.title(title)
    root.geometry("800x200")
    x, y = adaption_window_center(root, 800, 200)
    root.geometry(f"+{x}+{y}")
    root.resizable(False, False)
    root.iconbitmap("images/icon.ico")
    root.attributes('-topmost', 1)

    return root


def create_reminder_window(root: tk.Tk):
    window = tk.Toplevel(root)
    window.title("喝水提醒")
    window.geometry("1280x520")
    x, y = adaption_window_center(root, 1280, 520)
    window.geometry(f"+{x}+{y}")
    window.resizable(False, False)
    window.iconbitmap("images/icon.ico")
    window.grab_set()
    window.focus_force()
    window.attributes('-topmost', 1)

    return window


def create_about(root: tk.Tk):
    window = tk.Toplevel(root)
    window.title("关于喝水")
    window.geometry("520x200")
    x, y = adaption_window_center(root, 520, 200)
    window.geometry(f"+{x}+{y}")
    window.resizable(False, False)
    window.iconbitmap("images/icon.ico")
    window.grab_set()
    window.focus_force()
    window.attributes('-topmost', 1)

    return window


def convert_format_second(second):
    remaining_seconds = second % 60
    minutes = second // 60
    hours = minutes // 60
    remaining_minutes = minutes % 60

    time_str = f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}"

    return time_str


def dialog_askinteger(app: Water):
    initial_value = None
    if app.original_second is not None:
        initial_value = app.original_second // 60
    minute_value = tk.simpledialog.askinteger(
        title='喝水',
        prompt='间隔时长(分钟)',
        parent=app.root,
        initialvalue=initial_value,
        minvalue=0,
        maxvalue=480
    )
    if minute_value is not None:
        app.second = app.original_second = minute_value * 60


def refresh_second_text(app: Water):
    second = app.second if app.second is not None else 0
    app.second_label.config(text=convert_format_second(second))


def refresh_setting_btn_text(app: Water):
    if app.original_second is None:
        btn_text = '设置间隔时长'
    else:
        btn_text = "间隔时长: " + str(app.original_second // 60) + " 分钟"
    app.setting_btn.config(text=btn_text)


def cancel_after(app: Water):
    if app.after_id is not None:
        app.root.after_cancel(app.after_id)


def deiconify_root(app: Water):
    if app.root.state != "normal":
        app.root.deiconify()


def setting_run(app: Water):
    dialog_askinteger(app)  # 设置间隔时间
    refresh_setting_btn_text(app)  # 显示间隔时间
    refresh_second_text(app)  # 显示秒数
    if app.second is not None and app.original_second is not None and not app.is_run:
        app.start_btn.config(state='normal')


def reset_run(app: Water):
    app.second = app.original_second = None  # 重置时间
    refresh_setting_btn_text(app)  # 显示间隔时间
    refresh_second_text(app)  # 显示秒数
    cancel_after(app)  # 取消定时事件
    app.is_run = False  # 重置运行标记
    app.start_btn.config(state='disabled', text='开始')
    app.stop_btn.config(state='disabled')


def start_run(app: Water):
    if app.second is None or app.original_second is None:
        return
    app.is_run = True  # 重置运行标记
    app.start_btn.config(state='disabled')  # 禁用开始按钮
    app.stop_btn.config(state='normal')  # 开启停止按钮
    app.exec()  # 开始执行


def stop_run(app: Water):
    app.is_run = False  # 重置运行标记
    cancel_after(app)  # 取消定时事件
    app.start_btn.config(state='normal', text='继续')
    app.stop_btn.config(state='disabled')
    if app.second == 0:  # 重新计算时间
        app.second = app.original_second
        refresh_second_text(app)


def refresh_gui(app: Water, command: str):
    if command == 'setting_run':
        setting_run(app)

    if command == 'reset_run':
        reset_run(app)

    if command == 'start_run':
        start_run(app)

    if command == 'stop_run':
        stop_run(app)


def refresh_run_popup(app: Water, command: str):
    app.reminder_window.destroy()  # 关闭当前界面
    if command == 'reset_run_popup':
        reset_run(app)
        deiconify_root(app)  # 显示主界面

    if command == 'stop_run_popup':
        stop_run(app)
        deiconify_root(app)  # 显示主界面

    if command == 'close_run_popup':
        app.second = app.original_second  # 重置时间
        refresh_second_text(app)  # 显示秒数
        start_run(app)  # 重新开始
