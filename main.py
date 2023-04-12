import tkinter as tk
from tkinter import messagebox as mb
    
"""



 K O K S 



"""

import random as r
def randnums():
    a = str(r.randint(1, 9))
    for i in range (r.randint(3,5)):
        a = a+ randnum()
    return a

def randnum():
    return str(r.randint(1,9))

class virsotne():
    stavoklis : int
    vecaki: dict = {}
    berni: dict = {}
    punkti1: int
    punkti2: int
    vert: int
    def __init__(self, stavoklis: int) -> None:
        self.stavoklis = stavoklis
        #ja nav šo, tad atceras iepriekšējā objekta vērtības???!
        self.vecaki: dict = {}
        self.berni: dict = {}
        self.punkti1 = 100
        self.punkti2 = 100
        self.vert = -10
    def __init__(self, stavoklis: str) -> None:
        self.stavoklis = int(stavoklis)
        #ja nav šo, tad atceras iepriekšējā objekta vērtības???!
        self.vecaki: dict = {}
        self.berni: dict = {}
        self.punkti1 = 100
        self.punkti2 = 100
        self.vert = -10
"""
funkcija ğenerē koku, izsaucot sevi rekursīvi līdz koks ir sağenerēts
par to ka sağenerēts liecina, ka visi atlikušie bērni ir tikai strupceļa virsotnes
ğenerējot jau 3. līmeņa virsotnes tiek skatīts vai jau šāda stāvokļa virsotne
nav bijusi, un ja ir bijusi, tad uz to tiek novilkts loks, nevis ğenerēta dublicējoša virsotne
"""    
def genkoks(sakne: virsotne, gajiens: int):
    str_stavoklis = str(sakne.stavoklis)
    if(len(str_stavoklis)==1): return
    for i in range(len(str_stavoklis)):
        virs = virsotne(str_stavoklis[0:i]+str_stavoklis[i+1:len(str_stavoklis)])
        if(gajiens%2==1):
            virs.punkti1 = sakne.punkti1 - int(str_stavoklis[i:i+1])
            virs.punkti2 = sakne.punkti2
        else:
            virs.punkti1 = sakne.punkti1
            virs.punkti2 = sakne.punkti2 - int(str_stavoklis[i:i+1])
        if virs not in sakne.berni:
            virs.vecaki[sakne.stavoklis] = sakne
            eksis = geteksisting(virs)
            if eksis== None:
                sakne.berni[virs.stavoklis] = virs
            else:
               eksis.vecaki[sakne.stavoklis] = sakne
               sakne.berni[eksis.stavoklis] = eksis 
    for num, virs in sakne.berni.items():
        if(len(virs.berni) == 0):
            genkoks(virs, gajiens+1)
    return sakne

    """palīgfunkcija koka ğenerēšanai, paskatās vai gadījumā šajā pašā līmenī jau nav šāda virsotne.
    """
def geteksisting(virs: virsotne):
    if(len(virs.vecaki)<1): return None
    if(len(virs.vecaki[list(virs.vecaki.keys())[0]].vecaki)<1): return None
    for i, vir in virs.vecaki.items():
        for j, vir in virs.vecaki[i].vecaki.items():
            for num, vecaks in virs.vecaki[i].vecaki[j].berni.items():
                for num2, eksisting in vecaks.berni.items():
                    if(eksisting.stavoklis == virs.stavoklis and eksisting.punkti1 == virs.punkti1 \
                        and eksisting.punkti2 == virs.punkti2):
                        return eksisting
    return None

    """funkcija, kas piešķir heiristiskos novērtējumus. Ja tā ir strupceļa virsotne, tad
    protams, ka +1 ja tas kas sāka uzvar, bet ja nav strupceļa, tad atkarībā no līmeņa
    izvēlas lielāko vai mazāko no tiešo pēcteču vērtējumiem
    """
def vertkoks(sakne: virsotne, level: int):
    if(sakne.vert != -10): return
    if len(str(sakne.stavoklis))==1:
        if(sakne.punkti1> sakne.punkti2):
            sakne.vert = 1
        elif (sakne.punkti1< sakne.punkti2):
            sakne.vert = -1
        else:
            sakne.vert = 0
        return
    minberns=1
    maxberns = -1
    for num, berns in sakne.berni.items():
        if(berns.vert == -10):
            vertkoks(berns, level+1)
        maxberns = max(maxberns, berns.vert)
        minberns = min (minberns, berns.vert)
    punktuzime = True if (level%2==1) else False
    if punktuzime: sakne.vert = maxberns
    else: sakne.vert = minberns
    return sakne
"""funkcija atgriež kādu no mazākajiem bērniem (heiristiskā vērtējuma ziņā mazākajiem)"""
def getminberns(sakne: virsotne):
    if len(sakne.berni) < 1 : return virsotne
    minberns = sakne.berni[list(sakne.berni.keys())[0]]
    for num, berns in sakne.berni.items():
        if berns.vert < minberns.vert:
            minberns = berns
    return minberns   
"""funkcija atgriež kādu no lielākajiem bērniem (heiristiskā vērtējuma ziņā lielākajiem)"""
def getmaxberns(sakne: virsotne):
    if len(sakne.berni) < 1 : return virsotne
    maxberns = sakne.berni[list(sakne.berni.keys())[0]]
    for num, berns in sakne.berni.items():
        if berns.vert > maxberns.vert:
            maxberns = berns
    return maxberns
"""funkcija atrod virsotni pēc stāvokļa starp dotās virsotnes bērniem"""
def getberns(sakne: virsotne, stavoklis : int):
    if len(sakne.berni) < 1 : return virsotne
    for num, berns in sakne.berni.items():
        if berns.stavoklis == stavoklis:
            return berns
    return None 


"""



 S A S K A R N E 



"""
class logs:
    def __init__(self):
            self.logs = tk.Tk()
            self.logs.title("Atņem ciparu spēle")
            self.logs.geometry("400x300")
            self.pchoice_label = tk.Label(self.logs, text="kas sāk?: ")
            self.pchoice_label.pack()
            self.pchoice = tk.StringVar(value="speletajs")
            self.radio_pirma = tk.Radiobutton(self.logs, text="speletajs", variable=self.pchoice, value="speletajs")
            self.radio_pirma.pack(anchor=tk.W)
            self.radio_otra = tk.Radiobutton(self.logs, text="AI", variable=self.pchoice, value="AI")
            self.radio_otra.pack(anchor=tk.W)
            self.stav_virsraksts = tk.Label(self.logs, text="spēles sākumstāvoklis: ")
            self.stav_virsraksts.pack()
            self.pargeneret_poga = tk.Button(self.logs, text="pārğenerēt", command=self.regen)
            self.pargeneret_poga.pack()
            self.sakumstavoklis = randnums()
            self.stavoklis_ievads = tk.Text(self.logs, height=1, width=30 )
            self.stavoklis_ievads.pack()
            self.stavoklis_ievads.insert(tk.END, self.sakumstavoklis)
                        
            self.sakt_poga = tk.Button(self.logs, text="Sākt spēli", command=self.sakt_speli)
            self.sakt_poga.pack()
            
            self.punkti1 = tk.StringVar(value="P1: 100")
            self.spelet1_virsraksts = tk.Label(self.logs, textvariable=self.punkti1)
            self.spelet1_virsraksts.pack()
            self.punkti2 = tk.StringVar(value="P2: 100")
            self.spelet2_virsraksts = tk.Label(self.logs, textvariable=self.punkti2)
            self.spelet2_virsraksts.pack()
            self.spelet_ievads = tk.Entry(self.logs)
            self.spelet_ievads.pack()
            
            self.rezultats_str = tk.StringVar(value="")
            self.result_label = tk.Label(self.logs, textvariable =self.rezultats_str)
            self.result_label.pack()
            self.gajiena_poga = tk.Button(self.logs, text="Iet", command=self.iet_spelet)
            self.gajiena_poga.pack()
    def regen(self):
        self.sakumstavoklis = randnums()
        self.stavoklis_ievads.delete('0.0',tk.END)
        self.stavoklis_ievads.insert(tk.END, self.sakumstavoklis) 
    
    def sakt_speli(self):
        self.gajiensnr = 1
        self.punkti1.set("P1: 100")
        self.punkti2.set("P2: 100")
        #self.rezultats_str.set("ğenerēju  koku...")
        self.virsotne = genkoks(virsotne(int(self.sakumstavoklis)), self.gajiensnr)
        #self.rezultats_str.set("novērtēju koku...")
        if(self.pchoice.get() == "speletajs"):
            self.virsotne = vertkoks(self.virsotne, self.gajiensnr)
            self.rezultats_str.set("SP gājiens..."+str(self.virsotne.stavoklis))
        else: 
            self.virsotne = vertkoks(self.virsotne, self.gajiensnr)
            self.rezultats_str.set("AI gājiens..."+str(self.virsotne.stavoklis))
            self.iet_ai()

    def vaiuzvara(self):
        if len(str(self.virsotne.stavoklis))==1:
            if(self.pchoice.get() == "speletajs"):
                if(self.virsotne.punkti1> self.virsotne.punkti2):
                    mb.showinfo("Spēlētājs 1 uzvarēja!", message="Spēlētājs 1 uzvarēja!")
                elif (self.virsotne.punkti1 == self.virsotne.punkti2):
                    mb.showinfo("Neizšķirts!", message="Neizšķirts!")
                else:
                    mb.showinfo("AI 2 uzvarēja!", message="AI 2 uzvarēja!")
            else:
                if(self.virsotne.punkti2> self.virsotne.punkti1):
                    mb.showinfo("Spēlētājs 2 uzvarēja!", message="Spēlētājs 2 uzvarēja!")
                elif (self.virsotne.punkti1 == self.virsotne.punkti2):
                    mb.showinfo("Neizšķirts!", message="Neizšķirts!")
                else:
                    mb.showinfo("AI 1 uzvarēja!", message="AI 1 uzvarēja!")
            self.nojauna()
        
    def nojauna(self):
        self.sakumstavoklis = randnums()
        self.stavoklis_ievads.delete('0.0',tk.END)
        self.stavoklis_ievads.insert(tk.END, self.sakumstavoklis) 
        self.sakt_speli()
                    
    def iet_spelet(self):
        self.vaiuzvara()
        num = int(self.spelet_ievads.get())
        strstav = str(self.virsotne.stavoklis)
        if num >0 and num <= len(strstav):
            self.virsotne = getberns(self.virsotne, int(strstav[0:num-1]+strstav[num:len(strstav)]))
            if(self.pchoice.get() == "speletajs"):
                self.punkti1.set( "SP1: "+str(self.virsotne.punkti1))
            else:
                self.punkti2.set("SP2: "+str(self.virsotne.punkti2))
            self.rezultats_str.set("AI gājiens..:"+str(self.virsotne.stavoklis))
            self.iet_ai()
            
    def iet_ai(self):
        self.vaiuzvara()
        if(self.pchoice.get() == "AI"):
            self.virsotne = getmaxberns(self.virsotne)
            self.punkti1.set("AI1: "+str(self.virsotne.punkti1))
        else:
            self.virsotne = getminberns(self.virsotne)
            self.punkti2.set("AI2: "+str(self.virsotne.punkti2))
        self.vaiuzvara()
        self.rezultats_str.set("Sp gājiens..."+str(self.virsotne.stavoklis))

if __name__ == "__main__":
    gm = logs()
    gm.logs.mainloop()
