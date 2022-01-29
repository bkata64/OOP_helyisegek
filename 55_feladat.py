import tkinter as tk

class Helyiseg:
    def __init__(self, szelesseg, hosszusag, magassag):
        self.szelesseg = szelesseg
        self.magassag = magassag
        self.hosszusag = hosszusag

    def alapterulet(self):
        return self.szelesseg * self.hosszusag

    def falterulet(self):
        return (self.hosszusag * self.magassag + self.szelesseg) * 2

    def festett_felulet(self):
        return self.falterulet() + self.alapterulet()


def rogzit():    
    sz = float(ent_sz.get())
    h = float(ent_h.get())
    m = float(ent_m.get())    
    helyiseg = Helyiseg(sz, h, m)
    helyisegek.append(helyiseg)
    megjelenit()    

def modosit():        
    sz = float(ent_sz.get())
    h = float(ent_h.get())
    m = float(ent_m.get()) 
    helyisegek[sorszam].szelesseg = sz   
    helyisegek[sorszam].hosszusag = h
    helyisegek[sorszam].magassag = m
    megjelenit()

def beolvas():
    global sorszam
    #helyisegek = []
    with open("helyisegek.txt", "r") as file:
        for sor in file:
            adatok = sor.strip().split()
            sz = float(adatok[0])
            h = float(adatok[1])
            m = float(adatok[2])
            helyiseg = Helyiseg(sz, h, m)
            helyisegek.append(helyiseg)
    sorszam = len(helyisegek) - 1
    megjelenit()

def kiiras():    
    with open("helyisegek.txt", "w", encoding="UTF-8") as outfile:
        for helyiseg in helyisegek:
            outfile.write(f"{helyiseg.szelesseg} {helyiseg.hosszusag} {helyiseg.magassag}\n")            

def megjelenit():
    ent_sz.delete(0,5)
    ent_h.delete(0,5) 
    ent_m.delete(0,5)
    if sorszam < len(helyisegek):
        ent_sz.insert(0, helyisegek[sorszam].szelesseg)
        ent_h.insert(0, helyisegek[sorszam].hosszusag)
        ent_m.insert(0, helyisegek[sorszam].magassag)
        lbl_b["text"] = f"Padlóburkoló: {round(helyisegek[sorszam].alapterulet())}m2"
        lbl_f["text"] = f"Festék: {round(helyisegek[sorszam].festett_felulet() * mennyiseg_m2)} l"
        btn_rogzit["text"] = "Módosít"
        btn_rogzit["command"] = modosit
    else:
        btn_rogzit["text"] = "Rögzít"
        btn_rogzit["command"] = rogzit
        lbl_b["text"] = "Padlóburkoló:"
        lbl_f["text"] = "Festék:"
    lbl_record["text"] = f"{sorszam + 1}/{len(helyisegek)}"    

def vissza():
    global sorszam
    if sorszam > 0:
        sorszam -= 1
        megjelenit()

def elore():
    global sorszam
    if sorszam < len(helyisegek):
        sorszam += 1
        megjelenit()



helyisegek = []
sorszam = -1
mennyiseg_m2 = 0.13
window = tk.Tk()
window.title("Helyiségek kalkulátor")
lblCim = tk.Label(text="Helyiségek festése, kövezése", font=("Arial", 20))
lblCim.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
btnBeolv = tk.Button(text="Adatok beolvasása", command=beolvas)
btnBeolv.grid(row=1, column=0)
btnKiir = tk.Button(text="Adatok kiírása", command=kiiras)
btnKiir.grid(row=1, column=1)

lbl_sz = tk.Label(text="Szélesség")
ent_sz = tk.Entry(width=15)
lbl_b = tk.Label(text="Padlóburkoló:", font=("Arial",12))
lbl_sz.grid(row=2, column=0)
ent_sz.grid(row=2, column=1)
lbl_b.grid(row=2, column=2)
lbl_h = tk.Label(text="Hosszúság")
ent_h = tk.Entry(width=15)
lbl_f = tk.Label(text="Festék:", font=("Arial",12))
lbl_h.grid(row=3, column=0)
ent_h.grid(row=3, column=1)
lbl_f.grid(row=3, column=2)
lbl_m = tk.Label(text="Magasság")
ent_m = tk.Entry(width=15)
lbl_m.grid(row=4, column=0)
ent_m.grid(row=4, column=1)


frm_buttons = tk.Frame()
frm_buttons.grid(row=5, column=0, columnspan=3)
btn_vissza = tk.Button(master=frm_buttons, text="<", command=vissza)
btn_vissza.grid(row=0, column=0)
lbl_record = tk.Label(master=frm_buttons, text=f"{sorszam}/{len(helyisegek)}")
lbl_record.grid(row=0, column=1)
btn_elore = tk.Button(master=frm_buttons, text=">", command=elore)
btn_elore.grid(row=0, column=2)
btn_rogzit = tk.Button(master=frm_buttons, text="Rögzít", command=rogzit)
btn_rogzit.grid(row=0, column=3)

window.mainloop()



