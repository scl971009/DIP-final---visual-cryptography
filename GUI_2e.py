import argparse
import random
import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_random(list, n):
	#random.seed('DIP')
	ran = random.sample(list, n)
	return ran

def setk(k):
	if k == 1:
		return 0, 0
	if k == 2:
		return 1, 0
	if k == 3:
		return 2, 0
	if k == 4:
		return 0, 1
	if k == 5:
		return 1, 1
	if k == 6:
		return 2, 1
	if k == 7:
		return 0, 2
	if k == 8:
		return 1, 2
	if k == 9:
		return 2, 2

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
            self.master.FM1.fm11.secretname = Label(self.master.FM1.fm11, text="機密圖")
            self.master.FM1.fm11.secretname.pack(side=LEFT)
            self.master.FM1.fm11.path = Label(self.master.FM1.fm11)
            self.master.FM1.fm11.choosebutton = Button(self.master.FM1.fm11, text="選擇檔案", command=self.choose_secret)
            self.master.FM1.fm11.choosebutton.pack(side=RIGHT)

            self.master.FM1.fm12 = Frame(self.master.FM1)
            self.master.FM1.fm12.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM1.fm12.imagelabel = Label(self.master.FM1.fm12)
            self.master.FM1.fm12.imagelabel.pack(side=LEFT)

            self.master.FM1.fm13 = Frame(self.master.FM1)
            self.master.FM1.fm13.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM1.fm13.text = Label(self.master.FM1.fm13, text = "機密圖為須透過解密才能得到的隱藏圖")
            self.master.FM1.fm13.text.pack(side=TOP)

            self.master.FM1.fm15 = Frame(self.master.FM1)
            self.master.FM1.fm15.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM1.fm15.text = Label(self.master.FM1.fm15, text = "機密圖和兩張偽裝圖的長寬皆須相同")
            self.master.FM1.fm15.text.pack(side=TOP)

            self.master.FM1.fm14 = Frame(self.master.FM1)
            self.master.FM1.fm14.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM1.fm14.button = Button(self.master.FM1.fm14, text="生成分享圖", command=self.make_output)
            self.master.FM1.fm14.button.pack(side=RIGHT)


            self.master.FM2 = Frame(self.master)
            self.master.FM2.pack(side=LEFT, fill=BOTH, expand=YES)
            self.master.FM2.fm21 = Frame(self.master.FM2)
            self.master.FM2.fm21.pack(side = TOP, fill=BOTH, expand=YES)
            self.master.FM2.fm21.fakename_1 = Label(self.master.FM2.fm21, text = "偽裝圖1")
            self.master.FM2.fm21.fakename_1.pack(side=LEFT)
            self.master.FM2.fm21.path = Label(self.master.FM2.fm21)
            self.master.FM2.fm21.choosebutton = Button(self.master.FM2.fm21, text="選擇檔案", command=self.choose_fake1)
            self.master.FM2.fm21.choosebutton.pack(side=RIGHT)

            self.master.FM2.fm22 = Frame(self.master.FM2)
            self.master.FM2.fm22.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM2.fm22.imagelabel = Label(self.master.FM2.fm22)
            self.master.FM2.fm22.imagelabel.pack(side=LEFT)

            self.master.FM2.fm23 = Frame(self.master.FM2)
            self.master.FM2.fm23.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM2.fm23.fakename_2 = Label(self.master.FM2.fm23, text = "偽裝圖2")
            self.master.FM2.fm23.fakename_2.pack(side = LEFT)
            self.master.FM2.fm23.path = Label(self.master.FM2.fm23)
            self.master.FM2.fm23.choosebutton = Button(self.master.FM2.fm23, text="選擇檔案", command=self.choose_fake2)
            self.master.FM2.fm23.choosebutton.pack(side=RIGHT)

            self.master.FM2.fm24 = Frame(self.master.FM2)
            self.master.FM2.fm24.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM2.fm24.imagelabel = Label(self.master.FM2.fm24)
            self.master.FM2.fm24.imagelabel.pack(side=LEFT)


            self.master.FM3 = Frame(self.master)
            self.master.FM3.pack(side=LEFT, fill=BOTH, expand=YES)
            self.master.FM3.fm31 = Frame(self.master.FM3)
            self.master.FM3.fm31.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM3.fm31.sharename_1 = Label(self.master.FM3.fm31, text = "分享圖1")
            self.master.FM3.fm31.sharename_1.pack(side=LEFT)
            self.master.FM3.fm31.save = Button(self.master.FM3.fm31, text="儲存檔案", command=self.save_1)
            self.master.FM3.fm31.save.pack(side=RIGHT)

            self.master.FM3.fm32 = Frame(self.master.FM3)
            self.master.FM3.fm32.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM3.fm32.imagelabel = Label(self.master.FM3.fm32)
            self.master.FM3.fm32.imagelabel.pack(side=LEFT)

            self.master.FM3.fm33 = Frame(self.master.FM3)
            self.master.FM3.fm33.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM3.fm33.sharename_2 = Label(self.master.FM3.fm33, text = "分享圖2")
            self.master.FM3.fm33.sharename_2.pack(side=LEFT)
            self.master.FM3.fm33.save = Button(self.master.FM3.fm33, text="儲存檔案", command=self.save_2)
            self.master.FM3.fm33.save.pack(side=RIGHT)

            self.master.FM3.fm34 = Frame(self.master.FM3)
            self.master.FM3.fm34.pack(side=TOP, fill=BOTH, expand=YES)
            self.master.FM3.fm34.imagelabel = Label(self.master.FM3.fm34)
            self.master.FM3.fm34.imagelabel.pack(side=LEFT)

        def choose_secret(self):
            default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
            fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
            self.master.FM1.fm11.path.configure(text=fname)
            self.master.FM1.fm11.path.text=fname
            img = Image.open(fname)
            width, height = img.size
            img = img.convert("1")
            resized = img.resize((320, 320*height//width), Image.ANTIALIAS)
            imgr = ImageTk.PhotoImage(resized)
            self.master.FM1.fm12.imagelabel.configure(image = imgr)
            self.master.FM1.fm12.imagelabel.image = imgr

        def choose_fake1(self):
            default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
            fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
            self.master.FM2.fm21.path.configure(text=fname)
            self.master.FM2.fm21.path.text=fname
            img = Image.open(fname)
            width, height = img.size
            img = img.convert("1")
            resized = img.resize((320, 320*height//width), Image.ANTIALIAS)
            imgr = ImageTk.PhotoImage(resized)
            self.master.FM2.fm22.imagelabel.configure(image = imgr)
            self.master.FM2.fm22.imagelabel.image = imgr

        def choose_fake2(self):
            default_dir = r"\Users\scl971009\Desktop\desktop\DIP\final project\DIP-final---visual-cryptography"
            fname = tkinter.filedialog.askopenfilename(title=u"", initialdir=(os.path.expanduser(default_dir)))
            self.master.FM2.fm23.path.configure(text=fname)
            self.master.FM2.fm23.path.text=fname
            img = Image.open(fname)
            width, height = img.size
            img = img.convert("1")
            resized = img.resize((320, 320*height//width), Image.ANTIALIAS)
            imgr = ImageTk.PhotoImage(resized)
            self.master.FM2.fm24.imagelabel.configure(image = imgr)
            self.master.FM2.fm24.imagelabel.image = imgr

        def make_output(self):
            original_share1 = Image.open(self.master.FM2.fm21.path.text)
            original_share1 = original_share1.convert("1")
            original_s1_pixels = original_share1.load()

            original_share2 = Image.open(self.master.FM2.fm23.path.text)
            original_share2 = original_share2.convert("1")
            original_s2_pixels = original_share2.load()

            secret = Image.open(self.master.FM1.fm11.path.text)
            secret = secret.convert("1")
            se_pixels = secret.load()

            share1 = Image.new("1", (original_share1.size[0] * 3, original_share1.size[1] * 3))
            s1_pixels = share1.load()

            share2 = Image.new("1", (original_share2.size[0] * 3, original_share2.size[1] * 3))
            s2_pixels = share2.load()

            for i in range(original_share1.size[0]):
                    for j in range(original_share1.size[1]):
                            if original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] != 0:
                                    bc = get_random(seq, 4)
                                    wc = [x for x in seq if x not in bc]
				
                                    for k in bc:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] != 0 and se_pixels[i, j] == 0:
                                    bc = get_random(seq, 4)
                                    wc = [x for x in seq if x not in bc]
                                    bb = get_random(wc, 4)
                                    wb = [x for x in seq if x not in bb]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] != 0:
                                    bb = get_random(seq, 6)
                                    wb = [x for x in seq if x not in bb]
                                    bc = get_random(bb, 4)
                                    wc = [x for x in seq if x not in bc]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] !=0 and se_pixels[i, j] == 0:
                                    bb = get_random(seq, 6)
                                    wb = [x for x in seq if x not in bb]
                                    bc = get_random(bb, 1)
                                    for x in wb:
                                            bc.append(x)
                                    wc = [x for x in seq if x not in bc]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] != 0:
                                    bc = get_random(seq, 6)
                                    wc = [x for x in seq if x not in bc]
                                    bb = get_random(bc, 4)
                                    wb = [x for x in seq if x not in bb]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] != 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] == 0:
                                    bc = get_random(seq, 6)
                                    wc = [x for x in seq if x not in bc]
                                    bb = get_random(bc, 1)
                                    for x in wc:
                                            bb.append(x)
                                    wb = [x for x in seq if x not in bb]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                            elif original_s1_pixels[i, j] == 0 and original_s2_pixels[i, j] == 0 and se_pixels[i, j] != 0:
                                    bb = get_random(seq, 6)
                                    wb = [x for x in seq if x not in bb]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255				
                            else:
                                    bb = get_random(seq, 6)
                                    wb = [x for x in seq if x not in bb]
                                    bc = get_random(bb, 3)
                                    for x in wb:
                                            bc.append(x)
                                    wc = [x for x in seq if x not in bc]
                                    for k in bb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wb:
                                            m, n = setk(k)
                                            s1_pixels[i * 3 + m, j * 3 + n] = 255
                                    for k in bc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 0
                                    for k in wc:
                                            m, n = setk(k)
                                            s2_pixels[i * 3 + m, j * 3 + n] = 255
                                            
            self.master.FM2.fm22.image = share1
            self.master.FM3.fm32.image = share2
            width, height = original_share1.size
            height = 320*height//width
            width1, height1 = share1.size
            resized1 = share1.resize((height*width1//height1, height),Image.ANTIALIAS)
            imgr1 = ImageTk.PhotoImage(resized1)
            self.master.FM3.fm32.imagelabel.configure(image=imgr1)
            self.master.FM3.fm32.imagelabel.image=imgr1
            width2, height2 = share2.size
            resized2 = share2.resize((height*width1//height1, height),Image.ANTIALIAS)
            imgr2 = ImageTk.PhotoImage(resized2)
            self.master.FM3.fm34.imagelabel.configure(image=imgr2)
            self.master.FM3.fm34.imagelabel.image=imgr2

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
    root.title("加密2")
    app = Application(root)
    root.mainloop()
