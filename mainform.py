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

currentlyConnectedEmulators = [['not connected','','','']]

class Window(object):
    def __init__(self, master):

        self.master = master
        self.master.title("tempus")
        self.master.geometry("630x405+300+200")
        self.master.configure(bg=colorShadeNormal)

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

        #TOP FULL BODY FRAME
        self.OverviewBodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=2)
        self.OverviewBodyFrame.pack(fill=BOTH, expand=Y)

        #TOP BODY SHOWING CONNECTED
        self.OverviewTopBodyFrame = Frame(self.OverviewBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.OverviewTopBodyFrame.pack(fill=X, anchor=N)
        
        self.lblAmountConnected = Label(self.OverviewTopBodyFrame, text='Device(s) Connected: 0, Please Refresh', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblAmountConnected.place(relx=0, x=0, y=0, anchor=NW)
        self.btnRefreshEmulators = Button(self.OverviewTopBodyFrame, text='Refresh', font='Roboto, 10', padx=5, pady=2, bd=0, bg=colorMenuShade, activebackground=colorMenuShade, highlightcolor=colorShadeLighter, activeforeground='#fff', fg='#fff', command=self.btnRefreshEmulatorsPushed)
        self.btnRefreshEmulators.place(relx=1, x=0,y=0, anchor=NE)
        self.btnDelEmulators = Button(self.OverviewTopBodyFrame, text='Delete', font='Roboto, 10', padx=5, pady=2, bd=0, bg=colorMenuShade, activebackground=colorMenuShade, highlightcolor=colorShadeLighter, activeforeground='#fff', fg='#fff', command=self.overviewDestroyAllLabels)
        self.btnDelEmulators.place(relx=1, x=-65,y=0, anchor=NE)

        #OVERVIEW CENTER BODY
        self.OverviewBodyCenterFrame = Frame(self.OverviewBodyFrame, bg=colorShadeNormal, bd=0)
        self.OverviewBodyCenterFrame.pack(fill=BOTH, expand=Y)

        self.overviewCreateTitleLabels()

        self.btnRefreshEmulatorsPushed()

        self.OverviewBodyCenterFrame.columnconfigure(0, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(1, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(2, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(3, weight=0)
        #BOTTOM BODY
        self.BodyBottomFrame = Frame(self.OverviewBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.BodyBottomFrame.pack(fill=X, anchor=S)

        self.lblTitle = Label(self.BodyBottomFrame, text='This is where you can monitor your bots live with current Tasks, Thoughts, and whether they are Connected.', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.place(relx=0, rely=1, x=0, y=0, anchor=SW)

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
        self.btnRefreshEmulators['bg'] = colorMain
        self.lblAmountConnected['text'] = 'Device(s) Connected: Refreshing'
        connected = shellconnect.connectToBluestacks()

        self.lblAmountConnected['text'] = 'Device(s) Connected: ' + str(len(connected))
        self.overviewRecreateConnectedLabels(connected)
        
        self.btnRefreshEmulators['state'] = ACTIVE
        self.btnRefreshEmulators['bg'] = colorMenuShade

    def overviewRecreateConnectedLabels(self, connected):
        self.overviewDestroyAllLabels()
        if len(connected) > 0:
            currentlyConnectedEmulators = [[]]
            for x in range(0, len(connected)):
                currentlyConnectedEmulators.insert(x, ['emulator:' + str(connected[x]),'nothing','nothing','0:00:00'])
                self.overviewCreateConnectedLabels(currentlyConnectedEmulators[x][0],currentlyConnectedEmulators[x][1],currentlyConnectedEmulators[x][2],currentlyConnectedEmulators[x][3],x+1)
        else:
            self.lblAmountConnected['text'] = 'Device(s) Connected: 0, Are you sure BlueStacks is running?'
            self.overviewCreateConnectedLabels('not connected', '', '', '', 1)

    def overviewCreateConnectedLabels(self, name, action, thoughts, runtime, currentRow):
        Label(self.OverviewBodyCenterFrame, text=name, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff').grid(sticky=W, row=currentRow, column=0)
        Label(self.OverviewBodyCenterFrame, text=action, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff').grid(sticky=W, row=currentRow, column=1)
        Label(self.OverviewBodyCenterFrame, text=thoughts, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff').grid(sticky=W, row=currentRow, column=2)
        Label(self.OverviewBodyCenterFrame, text=runtime, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff').grid(sticky=E, row=currentRow, column=3)

    def overviewCreateTitleLabels(self):
        self.lblTitleName = Label(self.OverviewBodyCenterFrame, text='Name', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg=colorShadeLighter).grid(sticky=W, row=0, column=0)
        self.lblCurrentAction = Label(self.OverviewBodyCenterFrame, text='Current Action', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg=colorShadeLighter).grid(sticky=W, row=0, column=1)
        self.lblTitleThoughts = Label(self.OverviewBodyCenterFrame, text='Thoughts', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg=colorShadeLighter).grid(sticky=W, row=0, column=2)
        self.lblTitleRuntime = Label(self.OverviewBodyCenterFrame, text='Runtime', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg=colorShadeLighter).grid(sticky=W, row=0, column=3)

    def overviewDestroyAllLabels(self):
        list = self.OverviewBodyCenterFrame.grid_slaves()
        for l in list:
            l.destroy()
        self.overviewCreateTitleLabels()

app = Tk()
app.iconbitmap('src/tempus.ico')
Window = Window(app)
app.mainloop()