import tkinter as tk
import tkinter.simpledialog


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


def convert_format_second(second):
    remaining_seconds = second % 60
    minutes = second // 60
    hours = minutes // 60
    remaining_minutes = minutes % 60

    time_str = f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}"

    return time_str


def dialog_askinteger(root: tk.Tk, second: int):
    minute_value = tk.simpledialog.askinteger(
        title='喝水',
        prompt='间隔(分钟)',
        parent=root,
        initialvalue=1,
        minvalue=1,
        maxvalue=480
    )

    return second if minute_value is None else minute_value
