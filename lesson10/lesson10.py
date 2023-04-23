import tkinter as tk
from tkinter import messagebox

class HaiglaVoodikohtadeHaldamine:
    def __init__(self, master):
        self.master = master
        self.master.title("Haigla voodikohtade haldamine")
        self.voodi_arv = 3
        self.patsiendid = []
        self.peamine_menüü()

    def peamine_menüü(self):
        tk.Button(self.master, text="Patsiendi vastuvõtt", command=self.patsiendi_vastuvõtuaken, width=30).pack(pady=5)
        tk.Button(self.master, text="Patsiendi väljasaatmine", command=self.tühjendada_patsiendi_aken, width=30).pack(pady=5)
        tk.Button(self.master, text="Vaata voodi saadavust", command=self.vaata_voodi_saadavus_aken, width=30).pack(pady=5)
        tk.Button(self.master, text="Voodikohtade saadavuse graafik", command=self.voodi_saadavus_graafik_aken, width=30).pack(pady=5)
        tk.Button(self.master, text="Välju", command=self.master.destroy, width=30).pack(pady=5)

    def patsiendi_vastuvõtuaken(self):
        aken = tk.Toplevel(self.master)
        aken.geometry("400x200")
        aken.title("Patsiendi vastuvõtt")

        tk.Label(aken, text="Nimi:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        Nimi_entry = tk.Entry(aken)
        Nimi_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(aken, text="Vanus:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        Vanus_entry = tk.Entry(aken)
        Vanus_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(aken, text="Haigusseisund:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        seisundi_sisestus = tk.Entry(aken)
        seisundi_sisestus.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(aken, text="Submit", command=lambda: self.võtta_patsient_vastu(Nimi_entry.get(), Vanus_entry.get(), seisundi_sisestus.get(), aken)).grid(row=3, columnspan=2, pady=5)

    def võtta_patsient_vastu(self, Nimi, Vanus, seisund, aken):
        if self.voodi_arv > 0:
            self.voodi_arv -= 1
            self.patsiendid.append({"Nimi": Nimi, "Vanus": Vanus, "Haigusseisund": seisund})
            aken.destroy()
        else:
            tk.messagebox.showerror("Viga", "Kõik voodid on hõivatud")

    def tühjendada_patsiendi_aken(self):
        if not self.patsiendid:
            tk.messagebox.showerror("Viga", "Puuduvad patsiendid")
            return
        aken = tk.Toplevel(self.master)
        aken.title("Patsiendi väljasaatmine ")

        patient_Nimis = [p["Nimi"] for p in self.patsiendid]
        patsient_muutuja = tk.StringVar(aken)
        patsient_muutuja.set(patient_Nimis[0])

        tk.OptionMenu(aken, patsient_muutuja, *patient_Nimis).pack(padx=5, pady=5)

        tk.Button(aken, text="Tühjendada", command=lambda: self.tühjendada_patsiendi(patsient_muutuja.get(), aken)).pack(pady=5)

    def tühjendada_patsiendi(self, patient_Nimi, aken):
        for patient in self.patsiendid:
            if patient["Nimi"] == patient_Nimi:
                self.patsiendid.remove(patient)
                self.voodi_arv += 1
                break
        aken.destroy()
        
    def vaata_voodi_saadavus_aken(self):
        aken = tk.Toplevel(self.master)
        aken.geometry("600x300")
        aken.title("Voodi saadavus")

        tk.Label(aken, text=f"Vabad voodid: {self.voodi_arv}").pack(padx=5, pady=5)
        tk.Label(aken, text="Vastuvõetud patsiendid:").pack(padx=5, pady=5)
        patsient_canvas = tk.Canvas(aken, bg="white", width=585, height=200)
        patsient_canvas.pack(padx=5, pady=5)
        if self.patsiendid:
            y = 20
            for patient in self.patsiendid:
                patsient_info = f"Nimi: {patient['Nimi']}, Vanus: {patient['Vanus']}, Haigusseisund: {patient['Haigusseisund']}"
                patsient_canvas.create_text(35, y, text=patsient_info, anchor=tk.W, font=("Arial", 10))
                patsient_canvas.create_line(5, y + 15, 585, y + 15, fill="#c0c0c0")
                y += 30
        else:
            patsient_canvas.create_text(10, 20, text="Patsiente ei ole vastu võetud.", anchor=tk.W)
        patsient_canvas.create_rectangle(5, 5, 585, 200, outline="#c0c0c0", width=2)
        
        
    def voodi_saadavus_graafik_aken(self):
        aken = tk.Toplevel(self.master)
        aken.geometry("600x700")
        aken.title("Voodikohtade saadavuse graafik")

        graafik_canvas = tk.Canvas(aken, bg="white", width=600, height=700)
        graafik_canvas.pack(padx=5, pady=5)

        kogu_voodid = 3
        vabad_voodid = self.voodi_arv
        hõivatud_voodid = kogu_voodid - vabad_voodid

        graafik_canvas.create_rectangle(250, 100, 150, 100 + hõivatud_voodid * 30, fill="red")
        graafik_canvas.create_text(200, 80, text="Hõivatud voodid", font=("Arial", 12))
        graafik_canvas.create_text(200, 130 + hõivatud_voodid * 30, text=str(hõivatud_voodid), font=("Arial", 12))

        graafik_canvas.create_rectangle(450, 100, 350, 100 + vabad_voodid * 30, fill="green")
        graafik_canvas.create_text(400, 80, text="Vabad voodid", font=("Arial", 12))
        graafik_canvas.create_text(400, 130 + vabad_voodid * 30, text=str(vabad_voodid), font=("Arial", 12))

if __name__ == "__main__":
    root = tk.Tk()
    app = HaiglaVoodikohtadeHaldamine(root)
    root.mainloop()