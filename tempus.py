from tkinter import *
from tkinter import ttk
import subprocess
import shellconnect
import array

#adobe colors
colorDown = '#31deb5'
colorMain = '#42f498'
colorUp = '#31de53'
colorMenuShade = '#2c2d32'

colorShadeLighter = '#5f626e'
colorShadeNormal = '#383940'
colorShadeDarker = '#222226'

currentlyConnectedEmulators = []
currentlyConnectedPorts = []

class Window(object):

    def __init__(self, master):
        self.scriptsRadioButtonChoice = IntVar(app)
        self.scriptsComboboxChoice = StringVar(app)

        self.master = master
        self.master.title("tempus")
        self.master.geometry("630x405+300+200")
        self.master.configure(bg=colorShadeNormal)

        self.master.resizable(0,0)

        self.AddWidgets()
        self.btnRefreshEmulatorsPushed()

    def AddWidgets(self):

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

        self.createOverviewTab()

    def overviewPushed(self):
        if (self.btnOverview['state'] == NORMAL):
            if (self.btnScripts['state'] == DISABLED):
                self.ScriptsBodyFrame.destroy()
            if (self.btnSettings['state'] == DISABLED):
                self.SettingsBodyFrame.destroy()
            if (self.btnHelp['state'] == DISABLED):
                self.HelpBodyFrame.destroy()
            self.BodyBottomFrame.destroy()
            self.createOverviewTab()
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
            if (self.btnOverview['state'] == DISABLED):
                self.OverviewBodyFrame.destroy()
            if (self.btnSettings['state'] == DISABLED):
                self.SettingsBodyFrame.destroy()
            if (self.btnHelp['state'] == DISABLED):
                self.HelpBodyFrame.destroy()
            self.BodyBottomFrame.destroy()
            self.createScriptsTab()
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
            if (self.btnScripts['state'] == DISABLED):
                self.ScriptsBodyFrame.destroy()
            if (self.btnOverview['state'] == DISABLED):
                self.OverviewBodyFrame.destroy()
            if (self.btnHelp['state'] == DISABLED):
                self.HelpBodyFrame.destroy()
            self.BodyBottomFrame.destroy()
            self.createSettingsTab()
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
            if (self.btnScripts['state'] == DISABLED):
                self.ScriptsBodyFrame.destroy()
            if (self.btnSettings['state'] == DISABLED):
                self.SettingsBodyFrame.destroy()
            if (self.btnOverview['state'] == DISABLED):
                self.OverviewBodyFrame.destroy()
            self.BodyBottomFrame.destroy()
            self.createHelpTab()
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
        self.btnRefreshEmulators['bg'] = colorMain
        self.btnRefreshEmulators['state'] = DISABLED
        self.lblAmountConnected['text'] = 'Device(s) Connected: Refreshing'
        global currentlyConnectedEmulators
        global currentlyConnectedPorts

        currentlyConnectedPorts = shellconnect.connectToBluestacks()
        currentlyConnectedEmulators = []

        if len(currentlyConnectedPorts) > 0:
            for x in range(0, len(currentlyConnectedPorts)):
                currentlyConnectedEmulators.append(['BlueStacks:' + str(currentlyConnectedPorts[x])])
        else:
            currentlyConnectedEmulators = ['nothing connected', '', '', '']

        self.lblAmountConnected['text'] = 'Device(s) Connected: ' + str(len(currentlyConnectedPorts))
        self.overviewRecreateConnectedLabels()

        self.btnRefreshEmulators['state'] = ACTIVE
        self.btnRefreshEmulators['bg'] = colorMenuShade

    def createOverviewTab(self):
        #TOP FULL BODY FRAME
        self.OverviewBodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=2)
        self.OverviewBodyFrame.pack(fill=BOTH, expand=Y)

        #TOP BODY SHOWING CONNECTED
        self.OverviewTopBodyFrame = Frame(self.OverviewBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.OverviewTopBodyFrame.pack(fill=X, anchor=N)

        if len(currentlyConnectedPorts) > 0:
            ammountConnectedString = "Device(s) Connected: "  + str(len(currentlyConnectedPorts))
        else:
            ammountConnectedString = "Device(s) Connected: "  + str(len(currentlyConnectedPorts)) + ", Please Refresh"
        self.lblAmountConnected = Label(self.OverviewTopBodyFrame, text=ammountConnectedString, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblAmountConnected.place(relx=0, x=0, y=0, anchor=NW)
        self.btnRefreshEmulators = Button(self.OverviewTopBodyFrame, text='Refresh', font='Roboto, 10', padx=5, pady=2, bd=0, bg=colorMenuShade, activebackground=colorMenuShade, highlightcolor=colorShadeLighter, activeforeground='#fff', fg='#fff', command=self.btnRefreshEmulatorsPushed)
        self.btnRefreshEmulators.place(relx=1, x=0,y=0, anchor=NE)

        #OVERVIEW CENTER BODY
        self.OverviewBodyCenterFrame = Frame(self.OverviewBodyFrame, bg=colorShadeNormal, bd=0)
        self.OverviewBodyCenterFrame.pack(fill=BOTH, expand=Y)

        self.overviewCreateTitleLabels()
        self.overviewRecreateConnectedLabels()

        self.OverviewBodyCenterFrame.columnconfigure(0, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(1, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(2, weight=3)
        self.OverviewBodyCenterFrame.columnconfigure(3, weight=0)


        #BOTTOM BODY
        self.BodyBottomFrame = Frame(self.master, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.BodyBottomFrame.pack(fill=X, anchor=S)

        self.lblTitle = Label(self.BodyBottomFrame, text='This is where you can monitor your bots live with current Tasks, Thoughts, and whether they are Connected.', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.place(relx=0, rely=1, x=0, y=0, anchor=SW)

    def createScriptsTab(self):
        #TOP FULL BODY FRAME
        self.ScriptsBodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=2)
        self.ScriptsBodyFrame.pack(fill=BOTH, expand=Y)

        #TOP BODY SHOWING CONNECTED
        self.ScriptsTopBodyFrame = Frame(self.ScriptsBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.ScriptsTopBodyFrame.pack(fill=X, anchor=N)

        if len(currentlyConnectedPorts) > 0:
            ammountConnectedString = "Device(s) Connected: "  + str(len(currentlyConnectedPorts))
        else:
            ammountConnectedString = "Device(s) Connected: "  + str(len(currentlyConnectedPorts)) + ", Please Refresh"

        self.lblAmountConnected = Label(self.ScriptsTopBodyFrame, text=ammountConnectedString, font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblAmountConnected.place(relx=0, x=0, y=0, anchor=NW)


        currentlyConnectedCombobox = ttk.Combobox(self.ScriptsTopBodyFrame, width = 35, textvariable = self.scriptsComboboxChoice, takefocus=False, state="readonly") 

        if len(currentlyConnectedPorts) > 0:
            temp = []
            for emulator in range(0,len(currentlyConnectedPorts)):
                temp.append(str(currentlyConnectedEmulators[emulator][0]))
            # Adding combobox drop down list

            currentlyConnectedCombobox['values'] = temp
            currentlyConnectedCombobox['state'] = "readonly"
        else:
            currentlyConnectedCombobox['values'] = ['Please Connect and/or Refresh devices']
            currentlyConnectedCombobox['state'] = DISABLED

        currentlyConnectedCombobox.bind("<<ComboboxSelected>>",lambda e: self.ScriptsBodyFrame.focus())
        currentlyConnectedCombobox.place(relx=1, x=-48, y=2, anchor=NE)
        currentlyConnectedCombobox.current(0)

        #Scripts CENTER BODY
        self.ScriptsBodyCenterFrame = Frame(self.ScriptsBodyFrame, bg=colorShadeNormal, bd=0)
        self.ScriptsBodyCenterFrame.pack(fill=BOTH, expand=Y)

        btnStartScripts = Button(self.ScriptsBodyCenterFrame, text='Start', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeLighter, activebackground=colorMenuShade, activeforeground=colorShadeLighter, fg='#fff', command=self.callBackStartScripts)
        btnStartScripts.grid(sticky=W+E+S, row=0, column=0, columnspan=3, padx=5, pady=5)

        self.lblTitleName = Label(self.ScriptsBodyCenterFrame, text='Categories', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg=colorShadeLighter).grid(sticky=W, row=1, column=0)

        SCRIPT_CATEGORIES = [
            ("Combat"),
            ("Prayer"),
            ("Magic"),
            ("Runecrafting"),
            ("Construction"),
            ("Agility"),
            ("Mining"),
            ("Woodcutting"),
            ("Smithing"),
        ]
        row = 2
        column = 0

        for x in range(0, len(SCRIPT_CATEGORIES)):
            b = Radiobutton(self.ScriptsBodyCenterFrame, text=SCRIPT_CATEGORIES[x], width=30, anchor=W, variable=self.scriptsRadioButtonChoice, 
            activebackground=colorMenuShade, activeforeground=colorShadeLighter, selectcolor=colorMain, fg='#fff', bg=colorShadeLighter, indicatoron=0,
            padx=2, pady=2, value=x, bd=0, relief=RIDGE, command=self.scriptsRecolorAllRadioButtons)
            b.grid(sticky=W, row=row, column=column, padx=5, pady=5)
            column += 1
            if column > 2:
                row += 1
                column = 0

        self.ScriptsBodyCenterFrame.columnconfigure(0, weight=3)
        self.ScriptsBodyCenterFrame.columnconfigure(1, weight=3)
        self.ScriptsBodyCenterFrame.columnconfigure(2, weight=3)

        Button(self.ScriptsBodyCenterFrame, text = "check rads", width=30, bg=colorShadeLighter, activebackground=colorMenuShade, activeforeground=colorShadeLighter, bd=0, compound=LEFT, command=self.scriptsRecolorAllRadioButtons).grid(sticky=E, row=5, column=0, padx=5, pady=5)

        #BOTTOM BODY
        self.BodyBottomFrame = Frame(self.master, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.BodyBottomFrame.pack(fill=X, anchor=S)

        self.lblTitle = Label(self.BodyBottomFrame, text='', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.place(relx=0, rely=1, x=0, y=0, anchor=SW)

    def createSettingsTab(self):
        #TOP FULL BODY FRAME
        self.SettingsBodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=2)
        self.SettingsBodyFrame.pack(fill=BOTH, expand=Y)

        #TOP BODY SHOWING CONNECTED
        self.SettingsTopBodyFrame = Frame(self.SettingsBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.SettingsTopBodyFrame.pack(fill=X, anchor=N)

        #Settings CENTER BODY
        self.SettingsBodyCenterFrame = Frame(self.SettingsBodyFrame, bg=colorShadeNormal, bd=0)
        self.SettingsBodyCenterFrame.pack(fill=BOTH, expand=Y)

        #BOTTOM BODY
        self.BodyBottomFrame = Frame(self.master, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.BodyBottomFrame.pack(fill=X, anchor=S)

        self.lblTitle = Label(self.BodyBottomFrame, text='', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.place(relx=0, rely=1, x=0, y=0, anchor=SW)

    def createHelpTab(self):
        #TOP FULL BODY FRAME
        self.HelpBodyFrame = Frame(self.master, bg=colorShadeNormal, width=630, bd=2)
        self.HelpBodyFrame.pack(fill=BOTH, expand=Y)

        #TOP BODY SHOWING CONNECTED
        self.HelpTopBodyFrame = Frame(self.HelpBodyFrame, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.HelpTopBodyFrame.pack(fill=X, anchor=N)

        #Help CENTER BODY
        self.HelpBodyCenterFrame = Frame(self.HelpBodyFrame, bg=colorShadeNormal, bd=0)
        self.HelpBodyCenterFrame.pack(fill=BOTH, expand=Y)

        #BOTTOM BODY
        self.BodyBottomFrame = Frame(self.master, bg=colorShadeNormal, width=630, height=30, bd=0)
        self.BodyBottomFrame.pack(fill=X, anchor=S)

        self.lblTitle = Label(self.BodyBottomFrame, text='', font='Roboto, 10', padx=5, pady=5, bd=0, bg=colorShadeNormal, fg='#fff')
        self.lblTitle.place(relx=0, rely=1, x=0, y=0, anchor=SW)



    def overviewRecreateConnectedLabels(self):
        self.overviewDestroyAllLabels()
        global currentlyConnectedEmulators
        global currentlyConnectedPorts

        if len(currentlyConnectedPorts) > 0:
            currentlyConnectedEmulators = [[]]
            for x in range(0, len(currentlyConnectedPorts)):
                currentlyConnectedEmulators.insert(x, ['BlueStacks:' + str(currentlyConnectedPorts[x]),'nothing','nothing','0:00:00'])
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

    def scriptsRecolorAllRadioButtons(self):
        list = self.ScriptsBodyCenterFrame.grid_slaves()
        for l in list:
            if l['state'] == 'ACTIVE':
                l['bg'] == colorMain
                l['fg'] == colorShadeNormal
            else:
                l['bg'] == colorShadeNormal
                l['fg'] == '#fff'

    def callBackStartScripts(self):
        stdoutlineformatted = ''
        item = subprocess.Popen([sys.executable, 'shellinterpreter.py', self.scriptsComboboxChoice.get()[self.scriptsComboboxChoice.get().find(':')+1:len(self.scriptsComboboxChoice.get())]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for stdoutline in item.stdout:
            stdoutlineformatted += str(stdoutline, 'utf-8')
        #shellinterpreter.mineIronOreSouthEastVarrock(self.scriptsComboboxChoice.get()[self.scriptsComboboxChoice.get().find(':')+1:len(self.scriptsComboboxChoice.get())],self.scriptsRadioButtonChoice.get())

app = Tk()
app.iconbitmap('src/tempus.ico')
Window = Window(app)
app.mainloop()