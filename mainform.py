from tkinter import *
import shellconnect

#adobe colors
colorDown = '#31deb5'
colorMain = '#42f498'
colorUp = '#31de53'
colorMenuShade = '#2c2d32'

colorShadeLighter = '#5f626e'
colorShadeNormal = '#383940'
colorShadeDarker = '#222226'

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
        self.MenuBar = Frame(self.master, bg=colorMenuShade, width=630, height=40)
        self.MenuBar.pack(fill=X)

        self.btnOverview = Button(self.MenuBar, text='Overview', font='Roboto', bd=0, bg=colorMain, activebackground=colorMenuShade, activeforeground='#fff', highlightcolor=colorShadeLighter, fg='#fff', command=self.overviewPushed, state=DISABLED)
        self.btnOverview.pack(side=LEFT,fill=BOTH,expand=Y)
        self.btnScripts = Button(self.MenuBar, text='Scripts', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMenuShade, activeforeground='#fff', highlightcolor=colorShadeLighter, fg='#fff', command=self.scriptsPushed)
        self.btnScripts.pack(side=LEFT,fill=BOTH,expand=Y)
        self.btnSettings = Button(self.MenuBar, text='Settings', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMenuShade, activeforeground='#fff', fg='#fff', command=self.settingsPushed)
        self.btnSettings.pack(side=LEFT,fill=BOTH,expand=Y)
        self.btnHelp = Button(self.MenuBar, text='Help', font='Roboto', bd=0, bg=colorMenuShade, activebackground=colorMenuShade, activeforeground='#fff', fg='#fff', command=self.helpPushed)
        self.btnHelp.pack(side=LEFT,fill=BOTH,expand=Y)

        self.BodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=10)
        self.BodyFrame.pack(fill=BOTH, expand=Y)

        self.lblAmountConnected = Label(self.BodyFrame, text='please refresh', font='Roboto, 10', padx=10, pady=10, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblAmountConnected.pack(side=LEFT, anchor=NW)

        self.btnRefreshEmulators = Button(self.BodyFrame, text='Refresh', font='Roboto', bd=0, bg=colorMain, activebackground=colorShadeLighter, activeforeground='#fff', command=self.btnRefreshEmulatorsPushed)
        self.btnRefreshEmulators.pack(side=RIGHT, anchor=NE)

        self.BodyCenterFrame = Frame(self.BodyFrame, bg=colorShadeNormal, borderwidth=10)
        self.BodyCenterFrame.pack(fill=BOTH, expand=Y)

        self.lblTitle = Label(self.BodyCenterFrame, text='This is where you can monitor your bots live with Tasks, Scripts, and whether they are Connected.', pady=35, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.pack(fill=X, anchor=N)



    def overviewPushed(self):
        if (self.btnOverview['state'] == NORMAL):
            self.lblTitle['text'] = 'This is where you can monitor your bots live with Tasks, Scripts, and whether they are Connected.'
            self.btnScripts['bg'] = colorMenuShade
            self.btnScripts['state'] = NORMAL
            self.btnSettings['bg'] = colorMenuShade
            self.btnSettings['state'] = NORMAL
            self.btnHelp['bg'] = colorMenuShade
            self.btnHelp['state'] = NORMAL
            self.btnOverview['state'] = DISABLED
            self.btnOverview['bg'] = colorMain
        else:
            self.btnOverview['state'] = NORMAL
            self.btnOverview['bg'] = colorMenuShade

    def scriptsPushed(self):
        if (self.btnScripts['state'] == NORMAL):
            self.lblTitle['text'] = 'This contains all Skilling and Money Making scripts.'
            self.btnOverview['bg'] = colorMenuShade
            self.btnOverview['state'] = NORMAL
            self.btnSettings['bg'] = colorMenuShade
            self.btnSettings['state'] = NORMAL
            self.btnHelp['bg'] = colorMenuShade
            self.btnHelp['state'] = NORMAL
            self.btnScripts['state'] = DISABLED
            self.btnScripts['bg'] = colorMain
        else:
            self.btnScripts['state'] = NORMAL
            self.btnScripts['bg'] = colorMenuShade
            
    def settingsPushed(self):
        if (self.btnSettings['state'] == NORMAL):
            self.lblTitle['text'] = 'Fine tunings of the tempus.'
            self.btnSettings['state'] = DISABLED
            self.btnSettings['bg'] = colorMain
            self.btnOverview['bg'] = colorMenuShade
            self.btnOverview['state'] = NORMAL
            self.btnScripts['bg'] = colorMenuShade
            self.btnScripts['state'] = NORMAL
            self.btnHelp['bg'] = colorMenuShade
            self.btnHelp['state'] = NORMAL
        else:
            self.btnSettings['state'] = NORMAL
            self.btnSettings['bg'] = colorMenuShade

    def helpPushed(self):
        if (self.btnHelp['state'] == NORMAL):
            self.lblTitle['text'] = 'Help reguarding Setting up and Tips to keep your bots alive longer.'
            self.btnHelp['state'] = DISABLED
            self.btnHelp['bg'] = colorMain
            self.btnOverview['bg'] = colorMenuShade
            self.btnOverview['state'] = NORMAL
            self.btnSettings['bg'] = colorMenuShade
            self.btnSettings['state'] = NORMAL
            self.btnScripts['bg'] = colorMenuShade
            self.btnScripts['state'] = NORMAL
        else:
            self.btnHelp['state'] = NORMAL
            self.btnHelp['bg'] = colorMenuShade

    def btnRefreshEmulatorsPushed(self):
        self.btnRefreshEmulators['state'] = DISABLED
        connected = shellconnect.connectToBluestacks()
        if len(connected) > 0:
            self.lblAmountConnected['text'] = 'Device(s) Connected: ' + str(len(connected))
        else:
            self.lblAmountConnected['text'] = 'Nothing connected, are you sure BlueStacks is running?'
        print(connected)
        self.btnRefreshEmulators['state'] = ACTIVE

app = Tk()
app.iconbitmap('src/tempus.ico')
Window = Window(app)
app.mainloop()