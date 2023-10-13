import tkinter


def windows_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


if __name__ == '__main__':
    tk = tkinter.Tk()
    print("屏幕长：", windows_size(tk))
