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
                        self.master.FM1.fm11.secret_txt = Label(self.master.FM1.fm11, text="機密圖")
                        self.master.FM1.fm11.secret_txt.pack(side=LEFT)
                        self.master.FM1.fm11.path = Label(self.master.FM1.fm11)
                        self.master.FM1.fm11.path.pack(side=LEFT)
                        self.master.FM1.fm11.button = Button(self.master.FM1.fm11)
                        self.master.FM1.fm11.button["text"] = "選擇檔案"
                        self.master.FM1.fm11.button["command"] = self.choose_input
                        self.master.FM1.fm11.button.pack(side=LEFT)
                        self.master.FM1.fm12 = Frame(self.master.FM1)
                        self.master.FM1.fm12.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM1.fm12.imagelabel = Label(self.master.FM1.fm12)
                        self.master.FM1.fm12.imagelabel.pack(side=LEFT)
                        self.master.FM1.fm13 = Frame(self.master.FM1)
                        self.master.FM1.fm13.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM1.fm13.button = Button(self.master.FM1.fm13)
                        self.master.FM1.fm13.button["text"]="生成分享圖"
                        self.master.FM1.fm13.button["command"]=self.make_output
                        self.master.FM1.fm13.button.pack(side=RIGHT)

                        self.master.FM2 = Frame(self.master)
                        self.master.FM2.pack(side=LEFT, fill = BOTH, expand=YES)
                        self.master.FM2.fm21 = Frame(self.master.FM2)
                        self.master.FM2.fm21.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM2.fm21.share1_txt = Label(self.master.FM2.fm21, text="分享圖1")
                        self.master.FM2.fm21.share1_txt.pack(side=TOP)
                        self.master.FM2.fm21.share1 = Label(self.master.FM2.fm21)
                        self.master.FM2.fm21.share1.pack(side=TOP)
                        self.master.FM2.fm22 = Frame(self.master.FM2)
                        self.master.FM2.fm22.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM2.fm22.button = Button(self.master.FM2.fm22)
                        self.master.FM2.fm22.button["text"]="儲存分享圖1"
                        self.master.FM2.fm22.button["command"]=self.save_1
                        self.master.FM2.fm22.button.pack(side=RIGHT)
                        self.master.FM2.fm22.real = Label(self.master.FM2.fm22)


                        self.master.FM3 = Frame(self.master)
                        self.master.FM3.pack(side=LEFT, fill=BOTH, expand=YES)
                        self.master.FM3.fm31 = Frame(self.master.FM3)
                        self.master.FM3.fm31.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM3.fm31.share2_txt = Label(self.master.FM3.fm31, text="分享圖2")
                        self.master.FM3.fm31.share2_txt.pack(side=TOP)
                        self.master.FM3.fm31.share2 = Label(self.master.FM3.fm31)
                        self.master.FM3.fm31.share2.pack(side=TOP)
                        self.master.FM3.fm32 = Frame(self.master.FM3)
                        self.master.FM3.fm32.pack(side=TOP, fill=BOTH, expand=YES)
                        self.master.FM3.fm32.button = Button(self.master.FM3.fm32)
                        self.master.FM3.fm32.button["text"]="儲存分享圖2"
                        self.master.FM3.fm32.button["command"]=self.save_2
                        self.master.FM3.fm32.button.pack(side=RIGHT)
                        self.master.FM3.fm32.real = Label(self.master.FM3.fm32)
                        

                def choose_input(self):
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

                def make_output(self):
                        #print("OUTPUT")
                        original = Image.open(self.master.FM1.fm11.path.text)
                        original = original.convert("1")
                        o_pixels = original.load()
                        first = Image.new("1", (original.size[0], original.size[1] * 2))
                        f_pixels = first.load()

                        second = Image.new("1", (original.size[0], original.size[1] * 2))
                        s_pixels = second.load()

                        for i in range(original.size[0]):
                                for j in range(original.size[1]):
                                    if o_pixels[i,j] == 0:
                                        if random.randint(0, 1):
                                            f_pixels[i,j * 2    ] = 255
                                            f_pixels[i,j * 2 + 1] = 0
                                            s_pixels[i,j * 2    ] = 0
                                            s_pixels[i,j * 2 + 1] = 255
                                        else:
                                            f_pixels[i,j * 2    ] = 0
                                            f_pixels[i,j * 2 + 1] = 255
                                            s_pixels[i,j * 2    ] = 255
                                            s_pixels[i,j * 2 + 1] = 0
                                    else:
                                        if random.randint(0, 1):
                                            f_pixels[i,j * 2    ] = 0
                                            f_pixels[i,j * 2 + 1] = 255
                                            s_pixels[i,j * 2    ] = 0
                                            s_pixels[i,j * 2 + 1] = 255
                                        else:
                                            f_pixels[i,j * 2    ] = 255
                                            f_pixels[i,j * 2 + 1] = 0
                                            s_pixels[i,j * 2    ] = 255
                                            s_pixels[i,j * 2 + 1] = 0
                        
                        self.master.FM2.fm22.image = first
                        #first.save("test.png")
                        self.master.FM3.fm32.image = second
                        width, height = original.size
                        height = 320*height//width
                        width1, height1 = first.size
                        resized1 = first.resize((height*width1//height1, height),Image.ANTIALIAS)
                        imgr1 = ImageTk.PhotoImage(resized1)
                        self.master.FM2.fm21.share1.configure(image=imgr1)
                        self.master.FM2.fm21.share1.image=imgr1
                        width2, height2 = second.size
                        resized2 = second.resize((height*width1//height1, height),Image.ANTIALIAS)
                        imgr2 = ImageTk.PhotoImage(resized2)
                        self.master.FM3.fm31.share2.configure(image=imgr2)
                        self.master.FM3.fm31.share2.image=imgr2

                def save_1(self):
                        image = self.master.FM2.fm22.image
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        toSave = tkinter.filedialog.asksaveasfile(mode='wb',defaultextension='.png')
                        image.save(toSave)

                def save_2(self):
                        image = self.master.FM3.fm32.image
                        default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
                        toSave = tkinter.filedialog.asksaveasfile(mode='wb',defaultextension='.png')
                        image.save(toSave)
                        
                        
        root = tk.Tk()
        app = Application(root)
        root.mainloop()

	#default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
	#fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))

	#print(fname)
	#print(tkFileDialog.askdirectory())
