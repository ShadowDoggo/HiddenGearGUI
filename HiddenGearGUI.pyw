import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from threading import Thread as thr
import socket, struct
    
class HiddenGearGUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.withdraw()
        self.master.title("HiddenGearGUI v1.1")
        try:
            self.master.iconbitmap("icon.ico")
        except:
            pass
        msg.showwarning(title = "HiddenGearGUI", message = "WARNING: Using hidden gear online will get you banned. Backup your save before unlocking anything.")
        self.master.deiconify()
        self.create_widgets()
        self.hide_gear()
        self.state = 0

    #Lists containing all the addresses of the gear.
    allunlock = [0x12BD0800, 0x12BDB0B8, 0x12BA90A0, 0x12BD0688, 0x12BDAF40, 0x12BA8F28, 0x12BD94D0, 0x12BA7050, 0x12BC4D78, 0x12BD8D78, 0x12BA71C8, 0x12BC4EF0, 0x12BD8EF0, 0x12BA7340, 0x12BC5068, 0x12BD9068, 0x12BB9BC0, 0x12BD2820, 0x12BA0F60]
    srlunlock = [0x12BD0800, 0x12BDB0B8, 0x12BA90A0]
    srlslots = [0x12CD2A60, 0x12CD7D70, 0x12CD8AF0]
    testfunlock = [0x12BD0688, 0x12BDAF40, 0x12BA8F28]
    testfslots = [0x12CD1DA0, 0x12CD4DA0, 0x12CD7DA0]
    eliteunlock = [0x12BD94D0]
    eliteslot = [0x12CDAD70]
    lv1unlock = [0x12BA7050, 0x12BC4D78, 0x12BD8D78]
    lv1slots = [0x12CD2A90, 0x12CD63C0, 0x12CD8B20]
    lv2unlock = [0x12BA71C8, 0x12BC4EF0, 0x12BD8EF0]
    lv2slots = [0x12CD2AC0, 0x12CD6480, 0x12CD8B50]
    lv3unlock = [0x12BA7340, 0x12BC5068, 0x12BD9068]
    lv3slots = [0x12CD2AF0, 0x12CD64B0, 0x12CD8B80]
    nogearunlock = [0x12BB9BC0, 0x12BD2820, 0x12BA0F60]
    nogearslots = [0x12CD70B0, 0x12CD3EA0, 0x12CD8BB0]

    #Magic that unlocks the gear.
    def allgear(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.allunlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.srlslots], 0x0000733D) #Adds gear slots.
            self.serialPoke([x + diff for x in self.testfslots], 0x0000733C) #Adds gear slots.
            self.serialPoke([x + diff for x in self.eliteslot], 0x00006D61) #Adds gear slot.
            self.serialPoke([x + diff for x in self.lv1slots], 0x00006979) #Adds gear slots.
            self.serialPoke([x + diff for x in self.lv2slots], 0x0000697A) #Adds gear slots.
            self.serialPoke([x + diff for x in self.lv3slots], 0x0000697B) #Adds gear slots.
            self.serialPoke([x + diff for x in self.nogearslots], 0x00000000) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked all gear")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def srl(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.srlunlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.srlslots], 0x0000733D) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked SRL gear")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def testfire(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.testfunlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.testfslots], 0x0000733C) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Testfire gear")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def elite(self):
        try:
            gecko = TCPGecko(self.e0.get())
            diff = self.get_diff()
            gecko.pokemem(self.eliteunlock + diff, 0x00000004) #Unlocks gear.
            gecko.pokemem(self.eliteslot + diff, 0x00006D61) #Adds gear slot.
            gecko.s.close()
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Elite Octoling gear")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))
    def lv1(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.lv1unlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.lv1slots], 0x00006979) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV1 Hero Armor")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def lv2(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.lv2unlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.lv2slots], 0x0000697A) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV2 Hero Armor")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def lv3(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.lv3unlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.lv3slots], 0x0000697B) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked LV3 Hero Armor")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    def nogear(self):
        try:
            diff = self.get_diff()
            self.serialPoke([x + diff for x in self.nogearunlock], 0x00000004) #Unlocks gear.
            self.serialPoke([x + diff for x in self.nogearslots], 0x00000000) #Adds gear slots.
            msg.showinfo(title = "HiddenGearGUI", message = "Unlocked Invisible gear")
        except Exception as exception:
            msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))

    #Functions that make the magic work.
    def connect(self): #Doesn't really connect, just checks if a connection can be established.
        if self.state == 0:
            try:
                gecko = TCPGecko(self.e0.get())
                self.state = 1
                gecko.s.close()
                self.s0.set("Disconnect")
                self.hide_connect()
                msg.showinfo(title = "HiddenGearGUI", message = "Connected.")
            except Exception as exception:
                msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))
        elif self.state == 1:
            try:
                self.state = 0
                self.s0.set("Connect")
                self.hide_gear()
                msg.showinfo(title = "HiddenGearGUI", message = "Disconnected.")
            except Exception as exception:
                msg.showerror(title = "HiddenGearGUI", message = "An error has occured: {0}".format(exception))
        else:
            msg.showerror(title = "HiddenGearGUI", message = "Something went wrong.")

    def get_diff(self): #Sets the memory offset difference (diff).
        gecko = TCPGecko(self.e0.get())
        JRPointer = int.from_bytes(gecko.readmem(0x106E975C, 4), "big") 
        if JRPointer in range(0x12000000, 0x14000000): 
            JRAddr = JRPointer + 0x92D8 
            if int.from_bytes(gecko.readmem(JRAddr, 4), "big") == 0x000003F2: 
                diff = JRAddr - 0x12CDADA0 
            else:
                raise Exception("Failed to get offset. The value in the JR's address didn't match.")
        else:
            raise Exception("Failed to get offset. The JR's address is out of range.")
        return diff
 
    def serialPoke(self, addressTable, value):
        gecko = TCPGecko(self.e0.get())
        for address in addressTable:
            if type(address) == int:
                gecko.pokemem(address, value)
            else:
                raise Exception("The address is not an integer.")
        gecko.s.close()

    #tkinter stuff.
    def create_widgets(self):
        self.s0 = tk.StringVar()
        self.s1 = tk.StringVar()
        self.s2 = tk.StringVar()
        self.s3 = tk.StringVar()
        self.s4 = tk.StringVar()
        self.s5 = tk.StringVar()
        self.s6 = tk.StringVar()
        self.s7 = tk.StringVar()
        self.s8 = tk.StringVar()
        self.s0.set("Connect")
        self.s1.set("Unlock Everything")
        self.s2.set("Unlock SRL Gear")
        self.s3.set("Unlock Testfire Gear")
        self.s4.set("Unlock Elite Octoling Gear")
        self.s5.set("Unlock LV1 Hero Armor")
        self.s6.set("Unlock LV2 Hero Armor")
        self.s7.set("Unlock LV3 Hero Armor")
        self.s8.set("Unlock Invisible Gear")
        self.f0 = ttk.Labelframe(self.master, text = "TCPGecko", width = 300, height = 100)
        self.l0 = ttk.Label(self.f0, text = "Wii U IP address:")
        self.e0 = ttk.Entry(self.f0, width = 15)
        self.f1 = ttk.Labelframe(self.master, text = "Gear", width = 325, height = 140)
        self.l1 = ttk.Label(self.f1, text = "HiddenGearGUI v1.1 by Shadow Doggo") 
        self.b0 = ttk.Button(self.f0, width = 15, textvariable = self.s0, command = lambda: thr(target = self.connect).start())
        self.b1 = ttk.Button(self.f1, width = 25, textvariable = self.s1, command = lambda: thr(target = self.allgear).start())
        self.b2 = ttk.Button(self.f1, width = 25, textvariable = self.s2, command = lambda: thr(target = self.srl).start())
        self.b3 = ttk.Button(self.f1, width = 25, textvariable = self.s3, command = lambda: thr(target = self.testfire).start())
        self.b4 = ttk.Button(self.f1, width = 25, textvariable = self.s4, command = lambda: thr(target = self.elite).start())
        self.b5 = ttk.Button(self.f1, width = 25, textvariable = self.s5, command = lambda: thr(target = self.lv1).start())
        self.b6 = ttk.Button(self.f1, width = 25, textvariable = self.s6, command = lambda: thr(target = self.lv2).start())
        self.b7 = ttk.Button(self.f1, width = 25, textvariable = self.s7, command = lambda: thr(target = self.lv3).start())
        self.b8 = ttk.Button(self.f1, width = 25, textvariable = self.s8, command = lambda: thr(target = self.nogear).start())
        self.f0.pack(pady = 5, padx = 5)
        self.l0.place(x = 100, y = 0) #I'm using place for every widget cause grid and pack mess up the label frame.
        self.e0.place(x = 100, y = 20)
        self.f1.pack(pady = 5, padx = 5)
        self.l1.place(x = 55, y = 100) #Useless fun fact: I centered this text using a ruler.
        self.b0.place(x = 98, y = 50)
        self.b1.place(x = 0, y = 0)
        self.b2.place(x = 160, y = 0)
        self.b3.place(x = 0, y = 25)
        self.b4.place(x = 160, y = 25)
        self.b5.place(x = 0, y = 50)
        self.b6.place(x = 160, y = 50)
        self.b7.place(x = 0, y = 75)
        self.b8.place(x = 160, y = 75)

    def hide_gear(self):
        self.e0.config(state="normal")
        self.b0.config(state="normal")
        self.b1.config(state="disabled")
        self.b2.config(state="disabled")
        self.b3.config(state="disabled")
        self.b4.config(state="disabled")
        self.b5.config(state="disabled") 
        self.b6.config(state="disabled")
        self.b7.config(state="disabled")
        self.b8.config(state="disabled")

    def hide_connect(self):
        self.b1.config(state="normal")
        self.b2.config(state="normal")
        self.b3.config(state="normal")
        self.b4.config(state="normal")
        self.b5.config(state="normal")
        self.b6.config(state="normal")
        self.b7.config(state="normal")
        self.b8.config(state="normal")
        self.e0.config(state="disabled")

#Start of pyGecko code.

#The MIT License (MIT)

#Copyright (c) 2015 wiiudev

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

class TCPGecko:
    def __init__(self, *args):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        print("Connecting to " + str(args[0]) + ":7331")
        self.s.connect((str(args[0]), 7331)) #IP, 1337 reversed, Cafiine uses 7332+
        print("Connected!")

    def readmem(self, address, length): #Number of bytes
        if length == 0: raise BaseException("Reading memory requires a length (# of bytes)")
        if not self.validrange(address, length): raise BaseException("Address range not valid")
        if not self.validaccess(address, length, "read"): raise BaseException("Cannot read from address")
        ret = b""
        if length > 0x400:
            print("Length is greater than 0x400 bytes, need to read in chunks")
            print("Start address:   " + self.hexstr0(address))
            for i in range(int(length / 0x400)): #Number of blocks, ignores extra
                self.s.send(b"\x04") #cmd_readmem
                request = struct.pack(">II", address, address + 0x400)
                self.s.send(request)
                status = self.s.recv(1)
                if   status == b"\xbd": ret += self.s.recv(0x400)
                elif status == b"\xb0": ret += b"\x00" * 0x400
                else: raise BaseException("Something went terribly wrong")
                address += 0x400;length -= 0x400
                print("Current address: " + self.hexstr0(address))
            if length != 0: #Now read the last little bit
                self.s.send(b"\x04")
                request = struct.pack(">II", address, address + length)
                self.s.send(request)
                status = self.s.recv(1)
                if   status == b"\xbd": ret += self.s.recv(length)
                elif status == b"\xb0": ret += b"\x00" * length
                else: raise BaseException("Something went terribly wrong")
            print("Finished!")
        else:
            self.s.send(b"\x04")
            request = struct.pack(">II", address, address + length)
            self.s.send(request)
            status = self.s.recv(1)
            if   status == b"\xbd": ret += self.s.recv(length)
            elif status == b"\xb0": ret += b"\x00" * length
            else: raise BaseException("Something went terribly wrong")
        return ret

    def pokemem(self, address, value): #Only takes 4 bytes, may need to run multiple times
        if not self.validrange(address, 4): raise BaseException("Address range not valid")
        if not self.validaccess(address, 4, "write"): raise BaseException("Cannot write to address")
        self.s.send(b"\x03") #cmd_pokemem
        request = struct.pack(">II", int(address), int(value))
        self.s.send(request) #Done, move on
        return

    def validrange(self, address, length):
        if   0x01000000 <= address and address + length <= 0x01800000: return True
        elif 0x0E000000 <= address and address + length <= 0x10000000: return True #Depends on game
        elif 0x10000000 <= address and address + length <= 0x50000000: return True #Doesn't quite go to 5
        elif 0xE0000000 <= address and address + length <= 0xE4000000: return True
        elif 0xE8000000 <= address and address + length <= 0xEA000000: return True
        elif 0xF4000000 <= address and address + length <= 0xF6000000: return True
        elif 0xF6000000 <= address and address + length <= 0xF6800000: return True
        elif 0xF8000000 <= address and address + length <= 0xFB000000: return True
        elif 0xFB000000 <= address and address + length <= 0xFB800000: return True
        elif 0xFFFE0000 <= address and address + length <= 0xFFFFFFFF: return True
        else: return False

    def validaccess(self, address, length, access):
        if   0x01000000 <= address and address + length <= 0x01800000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0x0E000000 <= address and address + length <= 0x10000000: #Depends on game, may be EG 0x0E3
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0x10000000 <= address and address + length <= 0x50000000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return True
        elif 0xE0000000 <= address and address + length <= 0xE4000000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xE8000000 <= address and address + length <= 0xEA000000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xF4000000 <= address and address + length <= 0xF6000000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xF6000000 <= address and address + length <= 0xF6800000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xF8000000 <= address and address + length <= 0xFB000000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xFB000000 <= address and address + length <= 0xFB800000:
            if access.lower() == "read":  return True
            if access.lower() == "write": return False
        elif 0xFFFE0000 <= address and address + length <= 0xFFFFFFFF:
            if access.lower() == "read":  return True
            if access.lower() == "write": return True
        else: return False

    def hexstr0(self, data): #0xFFFFFFFF, uppercase hex string
        return "0x" + hex(data).lstrip("0x").rstrip("L").zfill(8).upper()

#End of pyGecko code.
 
if __name__ == "__main__":
    root = tk.Tk()
    app = HiddenGearGUI(master = root)
    app.mainloop()
