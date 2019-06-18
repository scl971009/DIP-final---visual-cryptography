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
                        self.master.FM1.fm11 = Frame(self.master.FM1)
                        self.master.FM1.fm11.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM1.fm11.secret_txt = Label(self.master.FM1.fm11, text="分享圖1")
                        self.master.FM1.fm11.secret_txt.pack(side=LEFT)
                        self.master.FM1.fm11.path = Label(self.master.FM1.fm11)
                        #self.master.FM1.fm11.path.pack(side=LEFT)
                        self.master.FM1.fm11.button = Button(self.master.FM1.fm11)
                        self.master.FM1.fm11.button["text"] = "選擇檔案"
                        self.master.FM1.fm11.button["command"] = self.choose_input_1
                        self.master.FM1.fm11.button.pack(side=RIGHT)
                        self.master.FM1.fm12 = Frame(self.master.FM1)
                        self.master.FM1.fm12.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM1.fm12.imagelabel = Label(self.master.FM1.fm12)
                        self.master.FM1.fm12.imagelabel.pack(side=LEFT)
                        self.master.FM1.fm13 = Frame(self.master.FM1)
                        self.master.FM1.fm13.pack(side=TOP)
                        self.master.FM1.fm13.warning = Label(self.master.FM1.fm13, text="請選擇完兩張分享圖再點選-生成機密圖")
                        self.master.FM1.fm13.warning.pack(side=LEFT)
                        

                        self.master.FM2 = Frame(self.master)
                        self.master.FM2.pack(side=LEFT, fill = BOTH, expand=YES)
                        self.master.FM2.fm21 = Frame(self.master.FM2)
                        self.master.FM2.fm21.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM2.fm21.secret_txt = Label(self.master.FM2.fm21, text="分享圖2")
                        self.master.FM2.fm21.secret_txt.pack(side=LEFT)
                        self.master.FM2.fm21.path = Label(self.master.FM2.fm21)
                        self.master.FM2.fm21.button = Button(self.master.FM2.fm21)
                        self.master.FM2.fm21.button["text"] = "選擇檔案"
                        self.master.FM2.fm21.button["command"] = self.choose_input_2
                        self.master.FM2.fm21.button.pack(side=RIGHT)
                        self.master.FM2.fm22 = Frame(self.master.FM2)
                        self.master.FM2.fm22.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM2.fm22.imagelabel = Label(self.master.FM2.fm22)
                        self.master.FM2.fm22.imagelabel.pack(side=LEFT)
                        self.master.FM2.fm23 = Frame(self.master.FM2)
                        self.master.FM2.fm23.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM2.fm23.button = Button(self.master.FM2.fm23)
                        self.master.FM2.fm23.button["text"]="生成機密圖"
                        self.master.FM2.fm23.button["command"]=self.make_output
                        self.master.FM2.fm23.button.pack(side=RIGHT)
                        


                        self.master.FM3 = Frame(self.master)
                        self.master.FM3.pack(side=LEFT, fill=BOTH, expand=YES)
                        self.master.FM3.fm30 = Frame(self.master.FM3)
                        self.master.FM3.fm30.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM3.fm30.share2_txt = Label(self.master.FM3.fm30, text="機密圖")
                        self.master.FM3.fm30.share2_txt.pack(side=LEFT)
                        self.master.FM3.fm31 = Frame(self.master.FM3)
                        self.master.FM3.fm31.pack(side=TOP, fill=BOTH, expand=YES)
                        
                        self.master.FM3.fm31.share2 = Label(self.master.FM3.fm31)
                        self.master.FM3.fm31.share2.pack(side=TOP)
                        self.master.FM3.fm32 = Frame(self.master.FM3)
                        self.master.FM3.fm32.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM3.fm32.button = Button(self.master.FM3.fm32)
                        self.master.FM3.fm32.button["text"]="儲存機密圖"
                        self.master.FM3.fm32.button["command"]=self.save
                        self.master.FM3.fm32.button.pack(side=RIGHT)
                        self.master.FM3.fm32.real = Label(self.master.FM3.fm32)
                        

                def choose_input_1(self):
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
                        #picture = PhotoImage(file=fname)
                        self.master.FM1.fm11.path.configure(text=fname)
                        self.master.FM1.fm11.path.text=fname
                        img = Image.open(fname)
                        width, height = img.size
                        img = img.convert("1")
                        resized = img.resize((320, 320*height//width),Image.ANTIALIAS)
                        imgr = ImageTk.PhotoImage(resized)
                        self.master.FM1.fm12.imagelabel.configure(image=imgr)
                        self.master.FM1.fm12.imagelabel.image=imgr

                def choose_input_2(self):
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
                        #picture = PhotoImage(file=fname)
                        self.master.FM2.fm21.path.configure(text=fname)
                        self.master.FM2.fm21.path.text=fname
                        img = Image.open(fname)
                        width, height = img.size
                        img = img.convert("1")
                        resized = img.resize((320, 320*height//width),Image.ANTIALIAS)
                        imgr = ImageTk.PhotoImage(resized)
                        self.master.FM2.fm22.imagelabel.configure(image=imgr)
                        self.master.FM2.fm22.imagelabel.image=imgr

                def make_output(self):
                        #print("OUTPUT")
                        first = Image.open(self.master.FM1.fm11.path.text)
                        f_pixels = first.load()
                        first.convert("1")

                        second = Image.open(self.master.FM2.fm21.path.text)
                        second.convert("1")
                        s_pixels = second.load()
    
                        third = Image.new("1", (first.size[0], int(first.size[1]/2)))
                        t_pixels = third.load()

                        for i in range(third.size[0]):
                            for j in range(third.size[1]):
                                if f_pixels[i, j * 2] + s_pixels[i, j * 2] == 0 or f_pixels[i, j * 2 + 1] + s_pixels[i, j * 2 + 1] == 0:
                                    t_pixels[i,j] = 255
                                else:
                                    t_pixels[i,j] = 0
                        

                        self.master.FM3.fm32.image = third
                        width, height = third.size

                        width1, height1 = first.size
                        height1 = 320*height1//width1
                        resized1 = third.resize((height1*width//height, height1),Image.ANTIALIAS)
                        imgr1 = ImageTk.PhotoImage(resized1)
                        self.master.FM3.fm31.share2.configure(image=imgr1)
                        self.master.FM3.fm31.share2.image=imgr1


                def save(self):
                        image = self.master.FM3.fm32.image
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        toSave = tkinter.filedialog.asksaveasfile(mode='wb',defaultextension='.png')
                        image.save(toSave)
                        
                        
        root = tk.Tk()
        root.title("解密1")
        app = Application(root)
        root.mainloop()

	#default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
	#fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))

	#print(fname)
	#print(tkFileDialog.askdirectory())
