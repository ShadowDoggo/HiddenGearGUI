import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from threading import Thread as th
from tcpgecko import TCPGecko

class HiddenGearGUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_window()
    
    def init_window(self):
        self.master.withdraw()
        self.master.title("HiddenGearGUI v1.0")
        try:
            self.master.iconbitmap("icon.ico")
        except:
            pass
        msg.showwarning(title = "HiddenGearGUI", message = "Using hidden gear online will get you banned regardless of mode. Only use this tool for messing around offline. You have been warned.")
        self.master.deiconify()
        self.init_widgets()

    def init_widgets(self):
        self.c1 = tk.StringVar()
        self.c1.set("Test Connection")
        self.c2 = tk.StringVar()
        self.c2.set("Unlock Everything")
        self.c3 = tk.StringVar()
        self.c3.set("Unlock SRL Gear")
        self.c4 = tk.StringVar()
        self.c4.set("Unlock Testfire Gear")
        self.c5 = tk.StringVar()
        self.c5.set("Unlock Elite Octoling Gear")
        self.c6 = tk.StringVar()
        self.c6.set("Unlock LV1 Hero Armor")
        self.c7 = tk.StringVar()
        self.c7.set("Unlock LV2 Hero Armor")
        self.c8 = tk.StringVar()
        self.c8.set("Unlock LV3 Hero Armor")
        self.c9 = tk.StringVar()
        self.c9.set("Unlock Invisible Gear")
        self.f1 = ttk.Labelframe(self.master, text = "TCPGecko", width = 300, height = 100)
        self.f1.pack(pady = 5, padx = 5)
        self.l1 = ttk.Label(self.f1, text = "Wii U IP address:")
        self.l1.place(x = 100, y = 0) #I'm using place for every widget cause grid and pack mess up the label frame.
        self.e1 = ttk.Entry(self.f1, width = 15)
        self.e1.place(x = 100, y = 20)
        self.f2 = ttk.Labelframe(self.master, text = "Gear", width = 325, height = 140)
        self.f2.pack(pady = 5, padx = 5)
        self.l2 = ttk.Label(self.f2, text = "HiddenGearGUI v1.0 by Shadow Doggo") #Fun fact: I centered this text using a ruler.
        self.l2.place(x = 55, y = 100)
        self.b1 = ttk.Button(self.f1, width = 15, textvariable = self.c1, command = lambda: th(target = self.connect).start())
        self.b1.place(x = 98, y = 50)
        self.b2 = ttk.Button(self.f2, width = 25, textvariable = self.c2, command = lambda: th(target = self.allgear).start())
        self.b2.place(x = 0, y = 0)
        self.b3 = ttk.Button(self.f2, width = 25, textvariable = self.c3, command = lambda: th(target = self.srl).start())
        self.b3.place(x = 160, y = 0)
        self.b4 = ttk.Button(self.f2, width = 25, textvariable = self.c4, command = lambda: th(target = self.testfire).start())
        self.b4.place(x = 0, y = 25)
        self.b5 = ttk.Button(self.f2, width = 25, textvariable = self.c5, command = lambda: th(target = self.elite).start())
        self.b5.place(x = 160, y = 25)
        self.b6 = ttk.Button(self.f2, width = 25, textvariable = self.c6, command = lambda: th(target = self.lv1).start())
        self.b6.place(x = 0, y = 50)
        self.b7 = ttk.Button(self.f2, width = 25, textvariable = self.c7, command = lambda: th(target = self.lv2).start())
        self.b7.place(x = 160, y = 50)
        self.b8 = ttk.Button(self.f2, width = 25, textvariable = self.c8, command = lambda: th(target = self.lv3).start())
        self.b8.place(x = 0, y = 75)
        self.b9 = ttk.Button(self.f2, width = 25, textvariable = self.c9, command = lambda: th(target = self.nogear).start())
        self.b9.place(x = 160, y = 75)

    def getdiff(self): #Sets the memory offset difference.
        ip = self.e1.get()
        JRPointer = int.from_bytes(TCPGecko(ip).readmem(0x106E975C, 4), "big") #Get the address from 0x106E975C (appears to be a pointer to the Splattershot JR's address).
        if JRPointer in range(0x12000000, 0x14000000): #Check the address to make sure it's not too far out.
            JRAddr = JRPointer + 0x92D8 #Get the JR's address. 
            if int.from_bytes(TCPGecko(ip).readmem(JRAddr, 4), "big") == 0x000003F2: #Check the value of the JR's address. If it's not 0x3F2 the offset may be too large or something else went wrong.
                diff = JRAddr - 0x12CDADA0 #Get the offset.
        return diff
     
    def connect(self):
        try:
            ip = self.e1.get()
            self.c1.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            TCPGecko(ip).s.close
            self.c1.set("Test Connection")
            msg.showinfo(title = "HiddenGearGUI", message = "Connected")
        except:
            self.c1.set("Test Connection")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def allgear(self):
        try:
            ip = self.e1.get()
            self.c2.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c2.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BD0800 + diff, 0x00000004) #Unlocks SRL gear.
            TCPGecko(ip).pokemem(0x12BDB0B8 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA90A0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2A60 + diff, 0x0000733D) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD7D70 + diff, 0x0000733D)
            TCPGecko(ip).pokemem(0x12CD8AF0 + diff, 0x0000733D)
            TCPGecko(ip).pokemem(0x12BD0688 + diff, 0x00000004) #Unlocks Testfire gear.
            TCPGecko(ip).pokemem(0x12BDAF40 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA8F28 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD1DA0 + diff, 0x0000733C) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD4DA0 + diff, 0x0000733C)
            TCPGecko(ip).pokemem(0x12CD7DA0 + diff, 0x0000733C)
            TCPGecko(ip).pokemem(0x12BD94D0 + diff, 0x00000004) #Unlocks Elite Octoling Goggles.
            TCPGecko(ip).pokemem(0x12CDAD70 + diff, 0x00006D61) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12BA7050 + diff, 0x00000004) #Unlocks LV1 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC4D78 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD8D78 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2A90 + diff, 0x00006979) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD63C0 + diff, 0x00006979)
            TCPGecko(ip).pokemem(0x12CD8B20 + diff, 0x00006979)
            TCPGecko(ip).pokemem(0x12BA71C8 + diff, 0x00000004) #Unlocks LV2 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC4EF0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD8EF0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2AC0 + diff, 0x0000697A) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD6480 + diff, 0x0000697A)
            TCPGecko(ip).pokemem(0x12CD8B50 + diff, 0x0000697A)
            TCPGecko(ip).pokemem(0x12BA7340 + diff, 0x00000004) #Unlocks LV3 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC5068 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD9068 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2AF0 + diff, 0x0000697B) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD64B0 + diff, 0x0000697B)
            TCPGecko(ip).pokemem(0x12CD8B80 + diff, 0x0000697B)
            TCPGecko(ip).pokemem(0x12BB9BC0 + diff, 0x00000004) #Unlocks Invisible gear.
            TCPGecko(ip).pokemem(0x12BD2820 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA0F60 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD70B0 + diff, 0x00000000) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD3EA0 + diff, 0x00000000)
            TCPGecko(ip).pokemem(0x12CD8BB0 + diff, 0x00000000)
            TCPGecko(ip).s.close()
            self.c2.set("Unlock Everything")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked all gear")
        except:
            self.c2.set("Unlock Everything")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def srl(self):
        try:
            ip = self.e1.get()
            self.c3.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c3.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BD0800 + diff, 0x00000004) #Unlocks SRL gear.
            TCPGecko(ip).pokemem(0x12BDB0B8 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA90A0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2A60 + diff, 0x0000733D) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD7D70 + diff, 0x0000733D)
            TCPGecko(ip).pokemem(0x12CD8AF0 + diff, 0x0000733D)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x0000733D) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x0000733D)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x0000733D)
            TCPGecko(ip).s.close()
            self.c3.set("Unlock SRL Gear")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked SRL gear")
        except:
            self.c3.set("Unlock SRL Gear")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def testfire(self):
        try:
            ip = self.e1.get()
            self.c4.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c4.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BD0688 + diff, 0x00000004) #Unlocks Testfire gear.
            TCPGecko(ip).pokemem(0x12BDAF40 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA8F28 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD1DA0 + diff, 0x0000733C) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD4DA0 + diff, 0x0000733C)
            TCPGecko(ip).pokemem(0x12CD7DA0 + diff, 0x0000733C)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x0000733C) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x0000733C)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x0000733C)
            TCPGecko(ip).s.close()
            self.c4.set("Unlock Testfire Gear")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Testfire gear")
        except:
            self.c4.set("Unlock Testfire Gear")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def elite(self):
        try:
            ip = self.e1.get()
            self.c5.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c5.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BD94D0 + diff, 0x00000004) #Unlocks Elite Octoling Goggles.
            TCPGecko(ip).pokemem(0x12CDAD70 + diff, 0x00006D61) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x00006D61) #Puts the gear on the player.
            TCPGecko(ip).s.close()
            self.c5.set("Unlock Elite Octoling Gear")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Elite Octoling gear")
        except:
            self.c5.set("Unlock Elite Octoling Gear")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def lv1(self):
        try:
            ip = self.e1.get()
            self.c6.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c6.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BA7050 + diff, 0x00000004) #Unlocks LV1 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC4D78 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD8D78 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2A90 + diff, 0x00006979) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD63C0 + diff, 0x00006979)
            TCPGecko(ip).pokemem(0x12CD8B20 + diff, 0x00006979)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x00006979) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x00006979)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x00006979)
            TCPGecko(ip).s.close()
            self.c6.set("Unlock LV1 Hero Armor")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV1 Hero Armor")
        except:
            self.c6.set("Unlock LV1 Hero Armor")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def lv2(self):
        try:
            ip = self.e1.get()
            self.c7.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c7.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BA71C8 + diff, 0x00000004) #Unlocks LV2 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC4EF0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD8EF0 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2AC0 + diff, 0x0000697A) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD6480 + diff, 0x0000697A)
            TCPGecko(ip).pokemem(0x12CD8B50 + diff, 0x0000697A)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x0000697A) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x0000697A)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x0000697A)
            TCPGecko(ip).s.close()
            self.c7.set("Unlock LV2 Hero Armor")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV2 Hero Armor")
        except:
            self.c7.set("Unlock LV2 Hero Armor")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def lv3(self):
        try:
            ip = self.e1.get()
            self.c8.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c8.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BA7340 + diff, 0x00000004) #Unlocks LV3 Hero Armor.
            TCPGecko(ip).pokemem(0x12BC5068 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BD9068 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD2AF0 + diff, 0x0000697B) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD64B0 + diff, 0x0000697B)
            TCPGecko(ip).pokemem(0x12CD8B80 + diff, 0x0000697B)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x0000697B) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x0000697B)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x0000697B)
            TCPGecko(ip).s.close()
            self.c8.set("Unlock LV3 Hero Armor")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV3 Hero Armor")
        except:
            self.c8.set("Unlock LV3 Hero Armor")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

    def nogear(self):
        try:
            ip = self.e1.get()
            self.c9.set("Connecting...")
            exception = "Could not connect."
            TCPGecko(ip) #Tests if a connection with TCPGecko can be established.
            exception = "Could not get diff."
            diff = self.getdiff()
            self.c9.set("Unlocking...")
            exception = "Could not unlock."
            TCPGecko(ip).pokemem(0x12BB9BC0 + diff, 0x00000004) #Unlocks Invisible gear.
            TCPGecko(ip).pokemem(0x12BD2820 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12BA0F60 + diff, 0x00000004)
            TCPGecko(ip).pokemem(0x12CD70B0 + diff, 0x00000000) #Adds gear slots.
            TCPGecko(ip).pokemem(0x12CD3EA0 + diff, 0x00000000)
            TCPGecko(ip).pokemem(0x12CD8BB0 + diff, 0x00000000)
            TCPGecko(ip).pokemem(0x12CD1D80 + diff, 0x00000000) #Puts the gear on the player.
            TCPGecko(ip).pokemem(0x12CD1D84 + diff, 0x00000000)
            TCPGecko(ip).pokemem(0x12CD1D88 + diff, 0x00000000)
            TCPGecko(ip).s.close()
            self.c9.set("Unlock Invisible Gear")
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Invisible gear")
        except:
            self.c9.set("Unlock Invisible Gear")
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured. {0}".format(exception))

if __name__ == "__main__":
    root = tk.Tk()
    app = HiddenGearGUI(master = root)
    app.mainloop()
