import os
from tkinter import Tk, Label, Button, Radiobutton,IntVar,StringVar,filedialog, OptionMenu, Entry, Checkbutton, ttk
import ROMtools

class ROMToolGUI:
    def __init__(self, master):
        self.master = master
        master.title("petrie's Happy Fun Time ROM Tool")
        master.wm_iconbitmap(os.getcwd() + "/eyeballfrog.ico")
        
        #Handle initialization of directories
        
        if(os.path.isfile(os.getcwd() +'/settings.ini')):
            settingsfile = open(os.getcwd() + '/settings.ini','r')
            settings = settingsfile.readlines()
            settingsfile.close()
            self.initarray = [x.rstrip() for x in settings]
        else:
            self.initarray = ['./','./','./','./','./']
        
        [self.EngToDebug,self.DebugToEng] = ROMtools.makeDEdict()
        
        #set up notebook tabs
        
        self.Tabs = ttk.Notebook(master)
        self.CompFrame = ttk.Frame(self.Tabs)
        self.DecompFrame = ttk.Frame(self.Tabs)
        self.ExtractFrame = ttk.Frame(self.Tabs)
        self.InjectFrame = ttk.Frame(self.Tabs)
        self.Tabs.add(self.InjectFrame,text ='Inject Files')
        self.Tabs.add(self.ExtractFrame,text ='Extract Files')
        self.Tabs.add(self.CompFrame,text ='Compress ROM')
        self.Tabs.add(self.DecompFrame,text ='Decompress ROM')
        self.Tabs.grid(row = 1, column = 0, columnspan = 4)
        
        self.close_button = Button(master, text="Done", command=master.destroy)
        self.close_button.grid(column = 1, row = 2, pady = 10,columnspan = 2)
        
        self.master = master
        
        #ROM compression frame
        
        self.compROMlabel = Label(self.CompFrame,text = "Decompressed ROM:",width = 30)
        self.compROMlabel.grid(row = 0, column = 0, columnspan = 1,pady = 10)
        
        self.compROMtext = StringVar(master = self.master)
        self.compROMtext.set("No ROM selected")        
        self.compROMname = Label(self.CompFrame,textvariable=self.compROMtext,width = 30, wraplength = 150)
        self.compROMname.grid(row = 1, column = 0, columnspan = 1,pady = 10)
        
        self.compROMtypelabel = Label(self.CompFrame,text = "ROM type:")
        self.compROMtypelabel.grid(row = 0, column = 1, columnspan = 1,pady = 10)
        
        self.compROMtype = StringVar(master = self.master)
        self.compROMtype.set("")        
        self.compROMtypedisp = Label(self.CompFrame,textvariable=self.compROMtype)
        self.compROMtypedisp.grid(row = 1, column = 1, columnspan = 2,pady = 10)
        
        self.compROMpath = "" 
        self.selectcompROM = Button(self.CompFrame,text = "Select ROM", command = self.setcompROM)
        self.selectcompROM.grid(row = 2, column = 0, pady = 10)
        
        self.comp_button = Button(self.CompFrame, text="Compress", command=self.compress, state = 'disabled')
        self.comp_button.grid(row = 2, column = 1,pady = 10)
        
        
        #ROM decompression frame
        
        self.decompROMlabel = Label(self.DecompFrame,text = "Compressed ROM:",width = 30)
        self.decompROMlabel.grid(row = 0, column = 0, columnspan = 1,pady = 10)
        
        self.decompROMtext = StringVar(master = self.master)
        self.decompROMtext.set("No ROM selected")        
        self.decompROMname = Label(self.DecompFrame,textvariable=self.decompROMtext,width = 30, wraplength = 150)
        self.decompROMname.grid(row = 1, column = 0, columnspan = 1,pady = 10)
        
        self.decompROMtable = StringVar(master = self.master)
        self.decompROMtable.set("")
        self.decompROMtablelabel = Label(self.DecompFrame,textvariable = self.decompROMtable,width =20)
        self.decompROMtablelabel.grid(row = 0, column = 1, columnspan = 1,pady = 10)
        
        self.decompROMfiles = StringVar(master = self.master)
        self.decompROMfiles.set("")        
        self.decompROMfiledisp = Label(self.DecompFrame,textvariable=self.decompROMfiles)
        self.decompROMfiledisp.grid(row = 1, column = 1, columnspan = 2,pady = 10)
        
        self.decompROMpath = "" 
        self.selectdecompROM = Button(self.DecompFrame,text = "Select ROM", command = self.setdecompROM)
        self.selectdecompROM.grid(row = 2, column = 0, pady = 10)
        
        self.decomp_button = Button(self.DecompFrame, text="Decompress", command=self.decompress, state = 'disabled')
        self.decomp_button.grid(row = 2, column = 1,pady = 10)
        
        #File Extraction frame
        
        self.extractROMlabel = Label(self.ExtractFrame,text = "Source ROM:",width = 25)
        self.extractROMlabel.grid(row = 0, column = 0, columnspan = 1,pady = 10)
        
        self.extractROMtext = StringVar(master = self.master)
        self.extractROMtext.set("No ROM selected")        
        self.extractROMname = Label(self.ExtractFrame,textvariable=self.extractROMtext,width = 25, wraplength = 150)
        self.extractROMname.grid(row = 1, column = 0, columnspan = 1,pady = 10)
        
        self.extractROMpath = "" 
        self.selectdecompROM = Button(self.ExtractFrame,text = "Select ROM", command = self.setextractROM)
        self.selectdecompROM.grid(row = 3, column = 0, pady = 10)
        
        self.extractROMtypelabel = Label(self.ExtractFrame,text = "ROM type:")
        self.extractROMtypelabel.grid(row = 0, column = 1, columnspan = 1,pady = 10)
        
        self.extractROMtype = StringVar(master = self.master)
        self.extractROMtype.set("")        
        self.extractROMtypedisp = Label(self.ExtractFrame,textvariable=self.extractROMtype)
        self.extractROMtypedisp.grid(row = 1, column = 1,pady = 10)
        
        self.extract_button = Button(self.ExtractFrame, text="Extract", command=self.extract, state = 'disabled')
        self.extract_button.grid(row = 3, column = 2,pady = 20)
        
        self.extractnameslabel = Label(self.ExtractFrame,text = "Scene Names",width = 25)
        self.extractnameslabel.grid(row = 0,column = 2, pady = 10)
        
        self.extractnames = IntVar(master = self.master)
        self.extractR1 = Radiobutton(self.ExtractFrame, text="English", variable=self.extractnames, value=0)
        self.extractR1.grid(column = 2, row = 1)
    
        self.extractR2 = Radiobutton(self.ExtractFrame, text="Debug", variable=self.extractnames, value=1)
        self.extractR2.grid(column = 2,  row = 2)
        
        #File Injection frame
        
        self.injectROMlabel = Label(self.InjectFrame,text = "Host ROM:",width = 20)
        self.injectROMlabel.grid(row = 0, column = 0, columnspan = 1,pady = 10)
        
        self.injectROMtext = StringVar(master = self.master)
        self.injectROMtext.set("No ROM selected")        
        self.injectROMname = Label(self.InjectFrame,textvariable=self.injectROMtext,width = 20, wraplength = 150)
        self.injectROMname.grid(row = 1, column = 0, pady = 10)
        
        self.injectROMpath = "" 
        self.selectinjectROM = Button(self.InjectFrame,text = "Select ROM", command = self.setinjectROM)
        self.selectinjectROM.grid(row = 3, column = 0, pady = 10)
        
        self.injectROMlabel = Label(self.InjectFrame,text = "File Directory:",width = 20)
        self.injectROMlabel.grid(row = 0, column = 1, pady = 10)
        
        self.injectfoldertext = StringVar(master = self.master)
        self.injectfoldertext.set("No directory selected")        
        self.injectfoldername = Label(self.InjectFrame,textvariable=self.injectfoldertext,width = 20, wraplength = 150)
        self.injectfoldername.grid(row = 1, column = 1, pady = 10)
        
        # self.injectROMtypelabel = Label(self.InjectFrame,text = "ROM type:",width = 20)
        # self.injectROMtypelabel.grid(row = 0, column = 2, columnspan = 1,pady = 10)
        
        self.injectROMtypelabel = StringVar(master = self.master)
        self.injectROMtype = ""
        self.injectROMtypelabel.set("")
        self.injectROMtypedisp = Label(self.InjectFrame,textvariable=self.injectROMtypelabel)
        self.injectROMtypedisp.grid(row = 2, column = 0, pady = 10)
        
        self.injectroomstartlabel =  Label(self.InjectFrame,text = "Boot to scene:")
        self.injectroomstartlabel.grid(row = 0, column = 2, columnspan = 1,pady = 10)
        
        self.bootscene = StringVar(master = self.master)
        self.sceneopts = ['Title Screen']
        self.bootscene.set('Title Screen')
        self.scenedict = {}
        self.scenemenu = OptionMenu(self.InjectFrame,self.bootscene,*self.sceneopts)
        self.scenemenu.config(width = 15)
        self.scenemenu.grid(row = 1, column = 2, pady = 10)
        
        self.roomnum = StringVar(master = self.master)
        self.rooment = Entry(self.InjectFrame,textvariable=self.roomnum,exportselection = 0)
        self.rooment.grid(row = 2, column = 2, pady = 10)
        
        self.injectfolderpath = "" 
        self.selectinjectfolder = Button(self.InjectFrame,text = "Directory", command = self.setinjectfolder)
        self.selectinjectfolder.grid(row = 3, column = 1, pady = 10)
        
        self.injectnames = IntVar(master = self.master)
        self.injectnamescheck = Checkbutton(self.InjectFrame,text = "Debug names",variable = self.injectnames)
        self.injectnamescheck.grid(row = 2,column = 1)
        
        self.inject_button = Button(self.InjectFrame, text="Inject", command=self.inject, state = 'disabled')
        self.inject_button.grid(row = 3, column = 2,pady = 10)
    
    def storesettings(self):
        
        settingsfile = open(os.getcwd() + '/settings.ini','w')
        settings = [x + '\n' for x in self.initarray]
        settingsfile.writelines(settings)
        settingsfile.close()
    
    
    def compress(self):
        
        self.comp_button.configure(state = 'disabled')
        
        spath = filedialog.asksaveasfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[0])
        
        if(len(spath) == 0):
            self.comp_button.configure(state = 'normal')
            return -1
        
        if(self.compROMtype.get() == 'Unknown'):
            popupmsg('Warning','Using default compression for unknown ROM. This may cause errors.')
        
        ROMtools.compress(self.compROMpath,spath)
        
        popupmsg('Success','ROM compressed.')
        self.comp_button.configure(state = 'normal')
    
    
    def setcompROM(self):
        rpath = filedialog.askopenfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[0])
        
        if(len(rpath) >  0):
            self.compROMpath = rpath
            
            self.initarray[0] = os.path.dirname(self.compROMpath)
            self.storesettings()
            
            self.compROMtext.set(os.path.basename(self.compROMpath))
            self.comp_button.configure(state = 'normal')
            
            self.compROMtype.set(ROMtools.findROMtype(self.compROMpath)[0])
    
    
    def decompress(self):
        self.decomp_button.configure(state = 'disabled')
        
        spath = filedialog.asksaveasfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[1])
        
        if(len(spath) == 0):
            self.decomp_button.configure(state = 'normal')
            return -1
        
        ROMtools.decompress(self.decompROMpath,spath)
        
        popupmsg('Success','ROM decompressed.')
        self.decomp_button.configure(state = 'normal')
    
    
    def setdecompROM(self):
        rpath = filedialog.askopenfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[1])
        
        if(len(rpath) >  0):
            self.decompROMpath = rpath
            
            self.initarray[1] = os.path.dirname(self.decompROMpath)
            self.storesettings()
            
            self.decompROMtext.set(os.path.basename(self.decompROMpath))
            self.decomp_button.configure(state = 'normal')
            
            ROMtype = ROMtools.findROMtype(self.decompROMpath)
            self.decompROMtable.set('File table at 0x' + '{0:X}'.format(ROMtype[1]))
            self.decompROMfiles.set('Number of files: '  + str(ROMtype[2]))
    
    
    def setextractROM(self):
        rpath = filedialog.askopenfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[2])
        
        if(len(rpath) >  0):
            self.extractROMpath = rpath
            
            self.initarray[2] = os.path.dirname(self.extractROMpath)
            self.storesettings()
            
            self.extractROMtext.set(os.path.basename(self.extractROMpath))
            self.extract_button.configure(state = 'normal')
            
            self.extractROMtype.set(ROMtools.findROMtype(self.extractROMpath)[0])
    
    
    def extract(self):
        self.extract_button.configure(state = 'disabled')
        
        spath = filedialog.askdirectory(initialdir = self.initarray[2])
        
        if(len(spath) == 0):
            self.extract_button.configure(state = 'normal')
            return -1
            
        status = ROMtools.extractall(self.extractROMpath,spath,self.extractnames.get())
        
        if(status == -1):
            popupmsg('Error','This ROM type is currently not supported.')
        if(status == -2):
            popupmsg('Error','ROM info file does not match ROM.')
        else:
            popupmsg('Success','Files Extracted.')
        
        
        self.extract_button.configure(state = 'normal')
    
    
    def setinjectROM(self):
        rpath = filedialog.askopenfilename(filetypes = (("N64 ROM files", "*.z64"),("All files", "*.*")),initialdir = self.initarray[3])
        
        if(len(rpath) >  0):
            self.injectROMpath = rpath
            
            self.initarray[3] = os.path.dirname(self.injectROMpath)
            self.storesettings()
            
            self.injectROMtype = ROMtools.findROMtype(self.injectROMpath)[0]
            self.injectROMtypelabel.set("ROM type: " + self.injectROMtype)
            
            self.injectROMtext.set(os.path.basename(self.injectROMpath))
            
            [scenes,self.scenedict] = ROMtools.makescenedict(self.injectROMtype)
            
            self.sceneopts = [(self.DebugToEng[x]).replace('_',' ') for x in scenes]
            
            self.scenemenu.destroy()
            self.bootscene.set('Title Screen')
            self.scenemenu = OptionMenu(self.InjectFrame,self.bootscene,'Title Screen',*self.sceneopts)
            self.scenemenu.config(width = 15)
            self.scenemenu.grid(row = 1, column = 2, pady = 10)
            
            
            if(len(self.injectfolderpath) > 0):
                self.inject_button.configure(state = 'normal')
    
    
    def setinjectfolder(self):
        spath = filedialog.askdirectory(initialdir = self.initarray[4])
        
        if(len(spath) >  0):
            self.injectfolderpath = spath
            
            self.initarray[4] = spath
            self.storesettings()
            
            ind = spath.rfind('/')+1
            
            self.injectfoldertext.set(spath[ind:])
            
            if(len(self.injectROMpath) > 0):
                self.inject_button.configure(state = 'normal')

    
    def inject(self):
        self.inject_button.configure(state = 'disabled')
            
        status = ROMtools.injectall(self.injectROMpath,self.injectfolderpath,self.injectnames.get())
        
        if(status == -1):
            popupmsg('Error','This ROM type is currently not supported.')
        elif(status == -2):
            popupmsg('Error','ROM info file does not match ROM.')
        elif(status == -3):
            popupmsg('Error','Injected file table does not match ROM file table.\nCheck your ROM version.')
        elif(self.bootscene.get() == 'Title Screen'):
            print('Skipping')
            #ROMtools.fixboot(self.injectROMpath)
        elif(not (self.roomnum.get().isnumeric())):
            popupmsg('Warning','Files injected.\nHowever, starting room number was invalid.')
            ROMtools.fixboot(self.injectROMpath)
        else:
            scenename = self.EngToDebug[self.bootscene.get().replace(' ','_')]
            roomnum = int(self.roomnum.get())
            ent = ROMtools.EntranceDict.get(scenename,'Unknown')
            
            if(ent == 'Unknown'):
                popupmsg('Warning','Files injected.\nHowever, booting to the chosen scene is currently unsupported.')
                ROMtools.fixboot(self.injectROMpath)
                self.inject_button.configure(state = 'normal')
                return
            
            status = ROMtools.loadtoroom(self.injectROMpath,ROMtools.EntranceDict.get(scenename),self.scenedict.get(scenename),roomnum)
            if(status == -1):
                popupmsg('Warning','Files injected.\nHowever, booting to scenes with multiple setups currently unsupported')
                ROMtools.fixboot(self.injectROMpath)
            elif(status == -2):
                popupmsg('Warning','Files injected.\nHowever, the boot modifier did not recognize the ROM. This error should be impossible.')
                ROMtools.fixboot(self.injectROMpath)
            elif(status == -3):
                popupmsg('Warning','Files injected.\nHowever, the room index was out of range.')
                ROMtools.fixboot(self.injectROMpath)
        
        
        self.inject_button.configure(state = 'normal')



def popupmsg(title, msg):
    popup = Tk()
    popup.wm_title(title)
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="OK", command = popup.destroy)
    B1.pack(pady = 10)
    popup.mainloop()

root = Tk()
RT_GUI = ROMToolGUI(root)
root.mainloop()
