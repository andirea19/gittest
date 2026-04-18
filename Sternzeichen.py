from datetime import datetime

def get_zodiac(day, month):
    # Logik für die Sternzeichen
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): return "Wassermann"
    if (month == 2 and day >= 19) or (month == 3 and day <= 20): return "Fische"
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return "Widder"
    if (month == 4 and day >= 20) or (month == 5 and day <= 20): return "Stier"
    if (month == 5 and day >= 21) or (month == 6 and day <= 20): return "Zwillinge"
    if (month == 6 and day >= 21) or (month == 7 and day <= 22): return "Krebs"
    if (month == 7 and day >= 23) or (month == 8 and day <= 22): return "Löwe"
    if (month == 8 and day >= 23) or (month == 9 and day <= 22): return "Jungfrau"
    if (month == 9 and day >= 23) or (month == 10 and day <= 22): return "Waage"
    if (month == 10 and day >= 23) or (month == 11 and day <= 21): return "Skorpion"
    if (month == 11 and day >= 22) or (month == 12 and day <= 21): return "Schütze"
    return "Steinbock"

def main():
    try:
        # Eingabe vom Benutzer
        datum_str = input("Bitte gib dein Geburtsdatum ein (Format: TT.MM.JJJJ): ")
        
        # String in ein datetime-Objekt umwandeln
        geburtstag = datetime.strptime(datum_str, "%d.%m.%Y")
        
        # Wochentag ermitteln (Locale ist hier systemabhängig, meist Englisch)
        # Für deutsche Namen könnte man ein Dictionary nutzen
        wochentage = {
            "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch",
            "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag", 
            "Sunday": "Sonntag"
        }
        wochentag_en = geburtstag.strftime("%A")
        wochentag_de = wochentage[wochentag_en]
        
        # Sternzeichen bestimmen
        sternzeichen = get_zodiac(geburtstag.day, geburtstag.month)
        
        print(f"\nAm {datum_str} war ein {wochentag_de}.")
        print(f"Dein Sternzeichen ist: {sternzeichen}")
        
    except ValueError:
        print("Fehler: Bitte gib das Datum im Format TT.MM.JJJJ ein (z. B. 15.05.1990).")


if __name__ == "__main__":
    main()