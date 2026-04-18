# app.py
import tkinter as tk
from tkinter import messagebox
from logic import get_zodiac, get_weekday_info # Importiert deine Logik!

def starte_zauber():
    result_label.config(text="🌙✨ Berechne ... ✨🌙")
    root.update()
    root.after(1000, berechne_action)
# ich möchte hier den zweiten button sichtbar machen 
    reset_btn.pack(pady=10)  # Zeigt den 2. Button an, wenn die Berechnung gestartet wird


def berechne_action():
   
    eingabe = entry.get()
    try:
        wochentag, datum = get_weekday_info(eingabe)
        sternzeichen = get_zodiac(datum.day, datum.month)
        
        # Text aktualisieren
        result_label.config(text=f"Wochentag: {wochentag}\nSternzeichen: {sternzeichen}")
    except:
        messagebox.showerror("Fehler", "Bitte Format TT.MM.JJJJ eingeben!")

# Farben definieren
farbe_blau = "#89CFF0"  # Babyblau hihi
farbe_pink = "#FFB7C5"  # Soft Pink

root = tk.Tk()
root.title("GeburtstagsTool von Mandy & Andi & Linda")
root.geometry("400x350")
root.configure(bg=farbe_blau) 

# UI-Elemente
tk.Label(root, text="Gib deinen Geburtstag an! ✨ (TT.MM.JJJJ):", bg=farbe_blau).pack(pady=10)

entry = tk.Entry(root)
entry.pack()

# Button in Pink
btn = tk.Button(root, text="Analysieren", command=starte_zauber, bg=farbe_pink, font=("Arial", 10, "bold"))
btn.pack(pady=20)

# Ergebnis-Label
result_label = tk.Label(root, text="", bg=farbe_blau, font=("Arial", 11, "bold"))
result_label.pack()

# ich möchte einen Button, der alles neu startet, damit ich ein neues Datum eingeben kann, ohne die App zu schließen.
def reset_app():
    entry.delete(0, tk.END)  
    result_label.config(text="")  
# ist es sinnvoll den button unsichtbar zu machen, bis er beim zaubern sichtbar wird? Ja, das ist eine gute Idee, damit die Benutzeroberfläche sauber bleibt, bis der Button benötigt wird. Hier ist die aktualisierte Version des Codes, die den Reset-Button zunächst unsichtbar macht?

reset_btn = tk.Button(root, text="Neu starten", command=reset_app, bg=farbe_pink, font=("Arial", 10, "bold"))
reset_btn.pack(pady=10)
reset_btn.pack_forget()  # Versteckt den Button zu Beginn

root.mainloop()


