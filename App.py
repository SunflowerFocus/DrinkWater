from Water import GUI
from Function import *


def refresh_second_text(app: GUI):
    btn_text = '设置间隔时间'
    if app.second > 0:
        minute = app.second // 60 if app.second % 60 == 0 else (app.second // 60 + 1)
        btn_text = "倒计时: " + str(minute) + " 分钟"
    app.setting_btn.config(text=btn_text)
    app.second_label.config(text=convert_format_second(app.second))


def cancel_after(app: GUI):
    if app.after_id is not None:
        app.root.after_cancel(app.after_id)


def refresh_gui(app: GUI, command: str):
    if command == 'setting':
        app.second = dialog_askinteger(app.root, app.second)
        if app.second > 0:
            refresh_second_text(app)

    if command == 'start':
        app.flag = True
        app.original_second = app.second
        app.setting_btn.config(state='disabled')
        app.start_btn.config(state='disabled')
        app.stop_btn.config(state='normal')
        app.reset_btn.config(state='normal')

    if command == 'reset':
        app.original_second = 0
        app.second = 0
        refresh_second_text(app)
        cancel_after(app)
        app.flag = True
        app.setting_btn.config(state='normal')
        app.start_btn.config(state='normal', text='开始')
        app.stop_btn.config(state='disabled')
        app.reset_btn.config(state='disabled')

    if command == 'stop':
        app.flag = False
        cancel_after(app)
        app.setting_btn.config(state='disabled')
        app.start_btn.config(state='normal', text='继续')
        app.stop_btn.config(state='disabled')
        app.reset_btn.config(state='normal')
