# app.py
import tkinter as tk
from tkinter import messagebox
from logic import get_zodiac, get_weekday_info # Importiert deine Logik!

def starte_zauber():
    result_label.config(text="🌙✨ Berechne ... ✨🌙")
    root.update()
    root.after(1000, berechne_action)

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
farbe_blau = "#89CFF0"  # Baby Blue
farbe_pink = "#FFB7C5"  # Soft Pink

root = tk.Tk()
root.title("GeburtstagsTool von Mandy & Andi")
root.geometry("300x250")
root.configure(bg=farbe_blau) # Hintergrund der App in Blau

# UI-Elemente
tk.Label(root, text="Geburtstag (TT.MM.JJJJ):", bg=farbe_blau).pack(pady=10)

entry = tk.Entry(root)
entry.pack()

# Button in Pink
btn = tk.Button(root, text="Analysieren", command=berechne_action, bg=farbe_pink, font=("Arial", 10, "bold"))
btn.pack(pady=20)

# Ergebnis-Label
result_label = tk.Label(root, text="", bg=farbe_blau, font=("Arial", 11, "bold"))
result_label.pack()

root.mainloop()