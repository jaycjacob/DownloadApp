import tkinter as tk
import requests
import urllib.request

root = tk.Tk()

file_name = ''
dwn_link = ''


def download():
    global dwn_link
    global file_name
    print(dwn_link)
    put()
    urllib.request.urlretrieve(dwn_link, file_name)


class Gui:
    def __init__(self, master):
        self.master = master
        master.title("Download App")

        self.label = tk.Label(master, text='Paste URL')
        self.label.grid(row=0,
                        column=0,
                        sticky=tk.W,
                        pady=4)
        self.label = tk.Label(master, text='video name').grid(row=1,
                                                              column=0)
        self.user_input = tk.Entry(master)
        self.user_input.grid(row=0,
                             column=1)
        self.user_input1 = tk.Entry(master)
        self.user_input1.grid(row=1,
                              column=1)
        self.button = tk.Button(master, text="Download", command=download).grid(row=2,
                                                                                column=1,
                                                                                sticky=tk.W,
                                                                                pady=4)


my_gui = Gui(root)


def put():
    global dwn_link
    global file_name
    dwn_link = my_gui.user_input.get()
    print(dwn_link)
    file_name = my_gui.user_input1.get()


root.mainloop()
