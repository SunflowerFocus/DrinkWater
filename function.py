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
