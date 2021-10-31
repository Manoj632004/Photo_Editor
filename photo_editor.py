import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from PIL import ImageDraw as IMD
from PIL import ImageFilter as IMF
from PIL import ImageEnhance as IME
from PIL import ImageOps as IMO

def editor():
    window=Tk()
    window.geometry("1100x650")
    window.title("SAMP PHOTO EDITOR")
    bg_img=PhotoImage(file=r"bg_img4.PNG")#only PNG format
    bg_label=Label(window,image=bg_img)
    bg_label.place(x=0,y=0,relwidth=1,relheight=1)
    
    canvas=Canvas(window,bg="black",width=500,height=470)
    canvas.place(x=220,y=70)

    mainLabel=Label(window,text="FILTERS",font=('calibre'))
    mainLabel.place(x=55,y=30)
    Label2=Label(window,text="PREVIEW",font=('calibre'))
    Label2.place(x=440,y=30)
    ilabel=Label(window,text="(Only one filter can be used at a time)",font=('calibre',8))
    ilabel.place(x=543,y=545)
  
    file_path = filedialog.askopenfilename() 
    img=Image.open(file_path)
    Fimg = ImageTk.PhotoImage(img)
    Label3=Label(window,text="ORIGINAL IMAGE",font=('calibre'))
    Label3.place(x=755,y=220)
    Dimg=Label(window,image=Fimg)
    Dimg.place(x=755,y=250)
    
    def simple_img():
        Pimg=img
        return Pimg
    def get_img(x=simple_img()):
        Fimg = ImageTk.PhotoImage(x)
        canvas.create_image(0,0,anchor=NW,image=Fimg)
        window.mainloop()
        return get_img
    def SAVE():
        print(window.size())
        slocat=temp.filename=filedialog.asksaveasfile(initialdir = "/",
                                            title="Select File",
                                            filetypes = (('JPEG', ('.jpg','.jpeg','.jpe','.jfif')),('PNG', '.png')),
                                            defaultextension ='.jpg' )
        temp.save(slocat)
        subwindow=Tk()
        sublab=Label(subwindow,text="image saved",font=('calibre'))
        sublab.pack()
###########################BUTTONS||FILTERS##########################
#ROTATE
    varotate=IntVar()
    def rotat():
        if varotate.get()==1:
            var_MB=StringVar(window)
            var_MB.set("                   ")
            MB=OptionMenu(window,
                          var_MB,
                          "rotate right","rotate left","   flip   ")
            MB.place(x=95,y=75)
            def sub_rotat():
                global temp
                if var_MB.get()=='rotate right':
                    img=simple_img()
                    temp=Image.fromarray(np.rot90(img))

                    save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                    save.place(x=755,y=150)  
                    canvas.delete("all")
                    get_img(temp)
                elif var_MB.get()=='rotate left':
                    img=simple_img()
                    temp=Image.fromarray(np.rot90(img,3))
                    save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                    save.place(x=755,y=150) 
                    canvas.delete("all")
                    get_img(temp)
                elif var_MB.get()=="   flip   ":
                    img=simple_img()
                    temp=Image.fromarray(np.rot90(img,2))

                    save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                    save.place(x=755,y=150) 

                    canvas.delete("all")
                    get_img(temp)
                else:
                    get_img()
            okB=Button(window,text="ok",
                          fg='black',
                          font=('comicsans'),
                          command=sub_rotat)
            okB.place(x=202,y=75)
        if varotate.get()==0:
            canvas.delete("all")
            get_img(simple_img())
    rotate=Checkbutton(window,text="rotate",
                     fg='purple',bg='black',
                     font=('comicsans', 14),
                     variable=varotate,
                     command=rotat)
    rotate.place(x=15,y=70)

    #EMBROSS
    varembross=IntVar()
    def Emboss():
        global temp
        if varembross.get()==1:
            x=simple_img()
            temp=x.filter(IMF.EMBOSS)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)            
        if varembross.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass            
    emb=Checkbutton(window,text="emboss",
                  fg='purple',bg='black',
                  font=('comicsans', 14),
                  variable=varembross,
                  command=Emboss)
    emb.place(x=15,y=110)
    
    #BLUR
    varblur=IntVar()    
    def Blur():
        global temp
        if varblur.get()==1:
            x=simple_img()
            temp=x.filter(IMF.BLUR)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if varblur.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass            
    blur=Checkbutton(window,text="blur",
                   fg='purple',bg='black',
                   font=('comicsans', 14),
                   variable=varblur,
                   command=Blur)
    blur.place(x=15,y=150)

    #CONTOUR
    var_contr=IntVar()
    def contour():
        global temp
        if var_contr.get()==1:
            x=simple_img()
            temp=x.filter(IMF.CONTOUR)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_contr.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    contr=Checkbutton(window,text="contour",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_contr,
                    command=contour)
    contr.place(x=15,y=190)

    #SMOOTH
    var_smooth=IntVar()
    def smoothen():
        global temp
        if var_smooth.get()==1:
            x=simple_img()
            temp=x.filter(IMF.SMOOTH)
            canvas.delete("all")

            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_smooth.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    smooth=Checkbutton(window,text="smoothen edges",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_smooth,
                    command=smoothen)
    smooth.place(x=15,y=230)

    #MIRROR
    var_invert=IntVar()
    def mirror():
        global temp
        if var_invert.get()==1:
            x=simple_img()
            temp=IMO.mirror(x)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_invert.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    invert=Checkbutton(window,text="mirror image",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_invert,
                    command=mirror)
    invert.place(x=15,y=270)

    #SHARPEN IMAGE
    var_sharp=IntVar()
    def sharpen():
        global temp
        if var_sharp.get()==1:
            x=simple_img()
            temp=x.filter(IMF.EDGE_ENHANCE)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_sharp.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    sharp=Checkbutton(window,text="sharpen image",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_sharp,
                    command=sharpen)
    sharp.place(x=15,y=310)

    #SOLARIZE
    var_solar=IntVar()
    def Solarize():
        global temp
        if var_solar.get()==1: 
            x=simple_img()
            temp=IMO.solarize(x,threshold=128)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_solar.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    solar=Checkbutton(window,text="solarize image",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_solar,
                    command=Solarize)
    solar.place(x=15,y=350)

    #GRAYSCALE
    var_GS=IntVar()
    def grayscale_():
        global temp
        if var_GS.get()==1:
            x=simple_img()
            temp=IMO.grayscale(x)
            canvas.delete("all")
            save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
            save.place(x=755,y=150) 
            get_img(temp)
        if var_GS.get()==0:
            try:
                canvas.delete("all")
                get_img()
            except TclError:
                pass
    GS_but=Checkbutton(window,text="grayscale",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_GS,
                    command=grayscale_)
    GS_but.place(x=15,y=390)

    #BRIGHTNESS
    var_BR=IntVar()
    def BRIGHTNESS_():
        box=Spinbox(window,from_=1,to=5,width=7)
        box.place(x=140,y=440)
        def sub_bright():
            global temp
            lim=float(box.get())
            if var_BR.get()==1:
                x=simple_img()
                x2=IME.Brightness(x)
                canvas.delete("all")
                temp=x2.enhance(lim)

                save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                save.place(x=755,y=150) 
                get_img(temp)
            if var_BR.get()==0:
                try:
                    canvas.delete("all")
                    get_img()
                except TclError:
                    pass
        ok_but=Button(window,text="OK",
                        fg="black",
                        font=('comicsans',9),
                        command=sub_bright)
        ok_but.place(x=200,y=435)
    BR_but=Checkbutton(window,text="brightness",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_BR,
                    command=BRIGHTNESS_)
    BR_but.place(x=15,y=430)

    #CROP
    var_crop=IntVar()
    def Crop():
        if var_crop.get()==1:
            spinbox=IntVar()
            spinbox=Spinbox(window,from_=0,to=250,width=7)
            spinbox.place(x=85,y=480)           
            def sub_crop():
                global temp
                borderX=int(spinbox.get())
                x=simple_img()
                temp=IMO.crop(x,border=borderX)
                canvas.delete("all")
                save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                save.place(x=755,y=150) 
                get_img(temp)
            cropB=Button(window,text="ok",
                         fg="black",
                         font=('comicsans'),
                         command=sub_crop)
            cropB.place(x=150,y=473)            
        if var_crop.get()==0:
            canvas.delete("all")
            get_img()        
    cropB=Checkbutton(window,text="crop",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_crop,
                    command=Crop)
    cropB.place(x=15,y=470)

    #IMGCOLOUR
    var_IC=IntVar()
    def imgcolour():
        if var_IC.get()==1: 
            var_MB=StringVar(window)
            var_MB.set("          ")
            MB=OptionMenu(window,
                          var_MB,
                          " red   ","green"," blue ")
            MB.place(x=25,y=550)
            def sub_imgcolour():
                global temp
                if var_MB.get()==" red   ":
                        img=np.array(simple_img())
                        out=img.copy()
                        out[:,:,(1,2)]=0
                        temp=Image.fromarray(out)
                        canvas.delete("all")

                        save=Button(window,text="save image",
                                        fg='purple',bg='black',
                                        font=('comicsans', 14),
                                        command=SAVE)
                        save.place(x=755,y=150) 
                        get_img(temp)
                elif var_MB.get()=="green":
                    img=np.array(simple_img())
                    out=img.copy()
                    out[:,:,(0,2)]=0
                    temp=Image.fromarray(out)
                    canvas.delete("all")

                    save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                    save.place(x=755,y=150) 
                    get_img(temp)
                elif var_MB.get()==" blue ":
                    img=np.array(simple_img())
                    out=img.copy()
                    out[:,:,(0,1)]=0
                    temp=Image.fromarray(out)
                    canvas.delete("all")
                    save=Button(window,text="save image",
                                    fg='purple',bg='black',
                                    font=('comicsans', 14),
                                    command=SAVE)
                    save.place(x=755,y=150) 
                    get_img(temp)                
                else:
                    get_img()
            okB=Button(window,text="ok",
                          fg='black',
                          font=('comicsans'),
                          command=sub_imgcolour)
            okB.place(x=105,y=550)
        if var_IC.get()==0:
            canvas.delete("all")
            get_img()                
    IC_but=Checkbutton(window,text="Image colour",
                    fg='purple',bg='black',
                    font=('comicsans', 14),
                    variable=var_IC,
                    command=imgcolour)
    IC_but.place(x=15,y=510)

    #QUIT
    quitt=Button(window,text="QUIT",
                    fg='red',bg='black',
                    font=('comicsans', 14),
                    command=window.destroy)
    quitt.place(x=420,y=580)
    window.mainloop()


try:
    editor()
except AttributeError or NameError or RuntimeError as e:
    print(e)

