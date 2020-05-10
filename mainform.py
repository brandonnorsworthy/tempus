from tkinter import *

#adobe colors
colorDown = '#31deb5'
colorMain = '#42f498'
colorUp = '#31de53'
colorMenuShade = '#2c2d32'
colorBodyShade = '#222226'
colorMenuHighlight = '#5f626e'

class Window(object):
    def __init__(self, master):
        self.master = master
        self.master.title("tempus")
        self.master.geometry("630x405+300+200")
        self.master.config(bg='#fff')

        self.master.resizable(0,0)

        self.AddWidgets()
    
    def AddWidgets(self):

        self.count = 0
        self.radioVar = IntVar() #radiobuttion for

        #menu bar, home, skills, cash, settings, help
        self.MenuBar = Frame(self.master, bg=colorMenuShade, width=630, height=35)
        self.MenuBar.pack(fill=X)

        self.Overview = Button(self.MenuBar, text='Overview', font='Roboto', bd=0, bg=colorMain, activebackground=colorMain, highlightcolor=colorMenuHighlight, fg='#fff', command=self.overviewPushed, state=DISABLED)
        self.Overview.pack(side=LEFT,fill=BOTH,expand=Y)
        self.Scripts = Button(self.MenuBar, text='Scripts', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMain, highlightcolor=colorMenuHighlight, fg='#fff', command=self.scriptsPushed)
        self.Scripts.pack(side=LEFT,fill=BOTH,expand=Y)
        self.Settings = Button(self.MenuBar, text='Settings', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMain, highlightcolor=colorMenuHighlight, fg='#fff')
        self.Settings.pack(side=LEFT,fill=BOTH,expand=Y)
        self.Help = Button(self.MenuBar, text='Help', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMain, highlightcolor=colorMenuHighlight, fg='#fff')
        self.Help.pack(side=LEFT,fill=BOTH,expand=Y)

        self.BodyFrame = Frame(self.master, bg=colorBodyShade, width=630)
        self.BodyFrame.pack(fill=BOTH,expand=Y)

        self.BodyLeftFrame = self.BodyFrame = Frame(self.master, bg=colorBodyShade)
        self.BodyLeftFrame.pack(fill=Y,expand=Y,padx=10,pady=10)
        self.BodyCenterFrame = self.BodyFrame = Frame(self.master, bg=colorBodyShade)
        self.BodyCenterFrame.pack(fill=Y,expand=Y,padx=10,pady=10)
        self.BodyRightFrame = self.BodyFrame = Frame(self.master, bg=colorBodyShade)
        self.BodyRightFrame.pack(fill=Y,expand=Y,padx=10,pady=10)

        self.label = Label(self.BodyFrame, text='hghhehgerhearhghhehgerhearhghhehgerhearhghhehgerhearhghhehgerhear', bg=colorBodyShade, fg='#fff')
        self.label.pack(fill=X)

    def overviewPushed(self):
        if (self.Overview['state'] == NORMAL):
            self.Overview['state'] = DISABLED
            self.Overview['bg'] = colorMain
            self.Scripts['bg'] = colorMenuShade
            self.Scripts['state'] = NORMAL
            self.Settings['bg'] = colorMenuShade
            self.Settings['state'] = NORMAL
            self.Help['bg'] = colorMenuShade
            self.Help['state'] = NORMAL
        else:
            self.Overview['state'] = NORMAL
            self.Overview['bg'] = colorMenuShade

    def scriptsPushed(self):
        if (self.Scripts['state'] == NORMAL):
            self.Scripts['state'] = DISABLED
            self.Scripts['bg'] = colorMain
            self.Overview['bg'] = colorMenuShade
            self.Overview['state'] = NORMAL
            self.Settings['bg'] = colorMenuShade
            self.Settings['state'] = NORMAL
            self.Help['bg'] = colorMenuShade
            self.Help['state'] = NORMAL
        else:
            self.Scripts['state'] = NORMAL
            self.Scripts['bg'] = colorMenuShade

    
    


        

app = Tk()
app.iconbitmap('src/tempus.ico')
Window = Window(app)
app.mainloop()