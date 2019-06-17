import argparse
import random
import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog

if __name__ == '__main__':

        class Application(tk.Frame):
                def __init__(self, master):
                        self.master = master
                        self.initWidgets()
                    
                def initWidgets(self):
                        self.master.FM1 = Frame(self.master)
                        self.master.FM1.pack(side=LEFT, fill=BOTH, expand=YES)
                        fm1 = Frame(self.master.FM1)
                        fm1.pack(side=TOP, fill=BOTH, expand=YES)
                        hello = Label(fm1, text="機密圖", width="10", height="3")
                        hello.pack(side=LEFT)
                        fm1.button = tk.Button(fm1)
                        fm1.button["text"] = "選擇檔案"
                        fm1.button["command"] = self.popup_hello
                        fm1.button.pack(side=LEFT)
                        self.master.FM1.fm2 = Frame(self.master.FM1)
                        self.master.FM1.fm2.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM1.fm2.imagelabel = Label(self.master.FM1.fm2)
                        self.master.FM1.fm2.imagelabel.pack(side=LEFT)

                def popup_hello(self):
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
                        #picture = PhotoImage(file=fname)
                        img = Image.open(fname)
                        width, height = img.size
                        resized = img.resize((320, 320*height//width),Image.ANTIALIAS)
                        imgr = ImageTk.PhotoImage(resized)
                        self.master.FM1.fm2.imagelabel.configure(image=imgr)
                        self.master.FM1.fm2.imagelabel.image=imgr
                        
        root = tk.Tk()
        app = Application(root)
        root.mainloop()

	#default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
	#fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))

	#print(fname)
	#print(tkFileDialog.askdirectory())
