# ============================================================
# INDUSTRIEMEISTER LERNAPP
# BWH – AUFGABEN
# Version 1.0
# ============================================================


BWH_AUFGABEN = [

    # ========================================================
    # KOSTENRECHNUNG
    # ========================================================

    {
        "id": "KR001",
        "thema": "Kostenrechnung",
        "unterthema": "Stückdeckungsbeitrag",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Ein Produkt wird für 80 € verkauft. "
            "Die variablen Stückkosten betragen 52 €. "
            "Berechnen Sie den Stückdeckungsbeitrag.",
        "gegeben": [
            "Preis p = 80 €",
            "variable Stückkosten kv = 52 €"
        ],
        "gesucht": "Stückdeckungsbeitrag db",
        "formel": "db = p - kv",
        "tipp": "Verkaufspreis minus variable Stückkosten.",
        "ergebnis": 28,
        "einheit": "€/Stück",
        "loesungsweg": [
            "db = p - kv",
            "db = 80 € - 52 €",
            "db = 28 €/Stück"
        ]
    },

    {
        "id": "KR002",
        "thema": "Kostenrechnung",
        "unterthema": "Gesamtdeckungsbeitrag",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Stückdeckungsbeitrag beträgt 28 €. "
            "Es werden 1.500 Stück verkauft. "
            "Berechnen Sie den Gesamtdeckungsbeitrag.",
        "gegeben": [
            "Stückdeckungsbeitrag db = 28 €",
            "Absatzmenge x = 1.500 Stück"
        ],
        "gesucht": "Gesamtdeckungsbeitrag DB",
        "formel": "DB = db × x",
        "tipp": "Stückdeckungsbeitrag mit der Absatzmenge multiplizieren.",
        "ergebnis": 42000,
        "einheit": "€",
        "loesungsweg": [
            "DB = db × x",
            "DB = 28 € × 1.500",
            "DB = 42.000 €"
        ]
    },

    {
        "id": "KR003",
        "thema": "Kostenrechnung",
        "unterthema": "Betriebsergebnis",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Gesamtdeckungsbeitrag beträgt 42.000 €. "
            "Die Fixkosten betragen 31.000 €. "
            "Berechnen Sie das Betriebsergebnis.",
        "gegeben": [
            "DB = 42.000 €",
            "Kf = 31.000 €"
        ],
        "gesucht": "Betriebsergebnis BE",
        "formel": "BE = DB - Kf",
        "tipp": "Fixkosten vom Gesamtdeckungsbeitrag abziehen.",
        "ergebnis": 11000,
        "einheit": "€",
        "loesungsweg": [
            "BE = DB - Kf",
            "BE = 42.000 € - 31.000 €",
            "BE = 11.000 €"
        ]
    },

    {
        "id": "KR004",
        "thema": "Kostenrechnung",
        "unterthema": "Break-even",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Die Fixkosten betragen 60.000 €. "
            "Der Stückdeckungsbeitrag beträgt 30 €. "
            "Berechnen Sie die Break-even-Menge.",
        "gegeben": [
            "Kf = 60.000 €",
            "db = 30 €/Stück"
        ],
        "gesucht": "Break-even-Menge xBEP",
        "formel": "xBEP = Kf / db",
        "tipp": "Fixkosten durch den Stückdeckungsbeitrag teilen.",
        "ergebnis": 2000,
        "einheit": "Stück",
        "loesungsweg": [
            "xBEP = Kf / db",
            "xBEP = 60.000 € / 30 €",
            "xBEP = 2.000 Stück"
        ]
    },

    {
        "id": "KR005",
        "thema": "Kostenrechnung",
        "unterthema": "Variable Gesamtkosten",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Die variablen Stückkosten betragen 18 €. "
            "Es werden 2.500 Stück produziert. "
            "Berechnen Sie die variablen Gesamtkosten.",
        "gegeben": [
            "kv = 18 €/Stück",
            "x = 2.500 Stück"
        ],
        "gesucht": "Variable Gesamtkosten Kv",
        "formel": "Kv = kv × x",
        "tipp": "Variable Stückkosten mit der Menge multiplizieren.",
        "ergebnis": 45000,
        "einheit": "€",
        "loesungsweg": [
            "Kv = kv × x",
            "Kv = 18 € × 2.500",
            "Kv = 45.000 €"
        ]
    },

    {
        "id": "KR006",
        "thema": "Kostenrechnung",
        "unterthema": "Gesamtkosten",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Die Fixkosten betragen 25.000 €. "
            "Die variablen Gesamtkosten betragen 45.000 €. "
            "Berechnen Sie die Gesamtkosten.",
        "gegeben": [
            "Kf = 25.000 €",
            "Kv = 45.000 €"
        ],
        "gesucht": "Gesamtkosten K",
        "formel": "K = Kf + Kv",
        "tipp": "Fixkosten und variable Gesamtkosten addieren.",
        "ergebnis": 70000,
        "einheit": "€",
        "loesungsweg": [
            "K = Kf + Kv",
            "K = 25.000 € + 45.000 €",
            "K = 70.000 €"
        ]
    },


    # ========================================================
    # MATERIALWIRTSCHAFT
    # ========================================================

    {
        "id": "MW001",
        "thema": "Materialwirtschaft",
        "unterthema": "Meldebestand",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der tägliche Verbrauch beträgt 40 Stück. "
            "Die Wiederbeschaffungszeit beträgt 6 Tage. "
            "Der Sicherheitsbestand beträgt 100 Stück. "
            "Berechnen Sie den Meldebestand.",
        "gegeben": [
            "Verbrauch = 40 Stück/Tag",
            "Wiederbeschaffungszeit = 6 Tage",
            "Sicherheitsbestand = 100 Stück"
        ],
        "gesucht": "Meldebestand",
        "formel":
            "Meldebestand = Verbrauch pro Zeiteinheit × Wiederbeschaffungszeit + Sicherheitsbestand",
        "tipp": "Erst den Verbrauch während der Lieferzeit berechnen.",
        "ergebnis": 340,
        "einheit": "Stück",
        "loesungsweg": [
            "Meldebestand = 40 × 6 + 100",
            "Meldebestand = 240 + 100",
            "Meldebestand = 340 Stück"
        ]
    },

    {
        "id": "MW002",
        "thema": "Materialwirtschaft",
        "unterthema": "Sicherheitsbestand",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der durchschnittliche Verbrauch beträgt 35 Stück pro Tag. "
            "Die Sicherheitszeit beträgt 4 Tage. "
            "Berechnen Sie den Sicherheitsbestand.",
        "gegeben": [
            "Ø Verbrauch = 35 Stück/Tag",
            "Sicherheitszeit = 4 Tage"
        ],
        "gesucht": "Sicherheitsbestand",
        "formel":
            "Sicherheitsbestand = Ø Verbrauch pro Tag × Sicherheitszeit",
        "tipp": "Tagesverbrauch mit der Sicherheitszeit multiplizieren.",
        "ergebnis": 140,
        "einheit": "Stück",
        "loesungsweg": [
            "Sicherheitsbestand = 35 × 4",
            "Sicherheitsbestand = 140 Stück"
        ]
    },

    {
        "id": "MW003",
        "thema": "Materialwirtschaft",
        "unterthema": "Durchschnittlicher Lagerbestand",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Anfangsbestand beträgt 800 Stück, "
            "der Endbestand 400 Stück. "
            "Berechnen Sie den durchschnittlichen Lagerbestand.",
        "gegeben": [
            "Anfangsbestand = 800 Stück",
            "Endbestand = 400 Stück"
        ],
        "gesucht": "Ø Lagerbestand",
        "formel":
            "Ø Lagerbestand = (Anfangsbestand + Endbestand) / 2",
        "tipp": "Anfangs- und Endbestand addieren und durch 2 teilen.",
        "ergebnis": 600,
        "einheit": "Stück",
        "loesungsweg": [
            "Ø Lagerbestand = (800 + 400) / 2",
            "Ø Lagerbestand = 600 Stück"
        ]
    },

    {
        "id": "MW004",
        "thema": "Materialwirtschaft",
        "unterthema": "Lagerumschlag",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Jahresverbrauch beträgt 24.000 Stück. "
            "Der durchschnittliche Lagerbestand beträgt 2.000 Stück. "
            "Berechnen Sie den Lagerumschlag.",
        "gegeben": [
            "Verbrauch pro Jahr = 24.000 Stück",
            "Ø Lagerbestand = 2.000 Stück"
        ],
        "gesucht": "Lagerumschlag",
        "formel":
            "Lagerumschlag = Verbrauch pro Jahr / Ø Lagerbestand",
        "tipp": "Jahresverbrauch durch durchschnittlichen Lagerbestand teilen.",
        "ergebnis": 12,
        "einheit": "mal/Jahr",
        "loesungsweg": [
            "Lagerumschlag = 24.000 / 2.000",
            "Lagerumschlag = 12"
        ]
    },

    {
        "id": "MW005",
        "thema": "Materialwirtschaft",
        "unterthema": "Lagerdauer",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Lagerumschlag beträgt 12. "
            "Berechnen Sie die durchschnittliche Lagerdauer.",
        "gegeben": [
            "Lagerumschlag = 12"
        ],
        "gesucht": "Ø Lagerdauer",
        "formel":
            "Ø Lagerdauer = 360 / Lagerumschlag",
        "tipp": "Im kaufmännischen Jahr wird mit 360 Tagen gerechnet.",
        "ergebnis": 30,
        "einheit": "Tage",
        "loesungsweg": [
            "Ø Lagerdauer = 360 / 12",
            "Ø Lagerdauer = 30 Tage"
        ]
    },

    {
        "id": "MW006",
        "thema": "Materialwirtschaft",
        "unterthema": "Lagerreichweite",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der durchschnittliche Lagerbestand beträgt 900 Stück. "
            "Der durchschnittliche Verbrauch beträgt 30 Stück pro Tag. "
            "Berechnen Sie die Lagerreichweite.",
        "gegeben": [
            "Ø Lagerbestand = 900 Stück",
            "Ø Verbrauch = 30 Stück/Tag"
        ],
        "gesucht": "Ø Lagerreichweite",
        "formel":
            "Ø Lagerreichweite = Ø Lagerbestand / Ø Verbrauch pro Tag",
        "tipp": "Lagerbestand durch Tagesverbrauch teilen.",
        "ergebnis": 30,
        "einheit": "Tage",
        "loesungsweg": [
            "Ø Lagerreichweite = 900 / 30",
            "Ø Lagerreichweite = 30 Tage"
        ]
    },

    {
        "id": "MW007",
        "thema": "Materialwirtschaft",
        "unterthema": "Materialverbrauch",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Anfangsbestand beträgt 500 Stück. "
            "Im Laufe des Jahres gehen 3.500 Stück zu. "
            "Der Endbestand beträgt 700 Stück. "
            "Berechnen Sie den Verbrauch.",
        "gegeben": [
            "Anfangsbestand = 500 Stück",
            "Zugänge = 3.500 Stück",
            "Endbestand = 700 Stück"
        ],
        "gesucht": "Verbrauch",
        "formel":
            "Verbrauch = Anfangsbestand + Zugänge - Endbestand",
        "tipp": "Anfangsbestand und Zugänge addieren, Endbestand abziehen.",
        "ergebnis": 3300,
        "einheit": "Stück",
        "loesungsweg": [
            "Verbrauch = 500 + 3.500 - 700",
            "Verbrauch = 3.300 Stück"
        ]
    },

    {
        "id": "MW008",
        "thema": "Materialwirtschaft",
        "unterthema": "Endbestand",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Anfangsbestand beträgt 1.000 Stück. "
            "Die Zugänge betragen 5.000 Stück und die Abgänge 4.600 Stück. "
            "Berechnen Sie den Endbestand.",
        "gegeben": [
            "Anfangsbestand = 1.000 Stück",
            "Zugänge = 5.000 Stück",
            "Abgänge = 4.600 Stück"
        ],
        "gesucht": "Endbestand",
        "formel":
            "Endbestand = Anfangsbestand + Zugänge - Abgänge",
        "tipp": "Bestandsfortschreibung anwenden.",
        "ergebnis": 1400,
        "einheit": "Stück",
        "loesungsweg": [
            "Endbestand = 1.000 + 5.000 - 4.600",
            "Endbestand = 1.400 Stück"
        ]
    },

    {
        "id": "MW009",
        "thema": "Materialwirtschaft",
        "unterthema": "Lagerzinssatz",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Die durchschnittliche Lagerdauer beträgt 72 Tage. "
            "Der Jahreszinssatz beträgt 5 %. "
            "Berechnen Sie den Lagerzinssatz.",
        "gegeben": [
            "Ø Lagerdauer = 72 Tage",
            "Zinssatz = 5 %"
        ],
        "gesucht": "Lagerzinssatz",
        "formel":
            "Lagerzinssatz % = Ø Lagerdauer / 360 × Zinssatz",
        "tipp": "72 durch 360 teilen und mit 5 % multiplizieren.",
        "ergebnis": 1,
        "einheit": "%",
        "loesungsweg": [
            "Lagerzinssatz = 72 / 360 × 5 %",
            "Lagerzinssatz = 1 %"
        ]
    },


    # ========================================================
    # ARBEITSENTGELT
    # ========================================================

    {
        "id": "AE001",
        "thema": "Arbeitsentgelt",
        "unterthema": "Zeitlohn",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Ein Mitarbeiter erhält 18,50 € pro Stunde und arbeitet 8 Stunden. "
            "Berechnen Sie den Zeitlohn.",
        "gegeben": [
            "Stundensatz = 18,50 €",
            "Arbeitszeit = 8 h"
        ],
        "gesucht": "Zeitlohn",
        "formel":
            "Zeitlohn = Stundensatz × Anzahl der geleisteten Stunden",
        "tipp": "Stundensatz mit den Stunden multiplizieren.",
        "ergebnis": 148,
        "einheit": "€",
        "loesungsweg": [
            "Zeitlohn = 18,50 × 8",
            "Zeitlohn = 148,00 €"
        ]
    },

    {
        "id": "AE002",
        "thema": "Arbeitsentgelt",
        "unterthema": "Zeitgradfaktor",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Ein Mitarbeiter erreicht einen Zeitgrad von 125 %. "
            "Berechnen Sie den Zeitgradfaktor.",
        "gegeben": [
            "Zeitgrad = 125 %"
        ],
        "gesucht": "Zeitgradfaktor",
        "formel":
            "Zeitgradfaktor = Zeitgrad / 100",
        "tipp": "Prozentwert durch 100 teilen.",
        "ergebnis": 1.25,
        "einheit": "",
        "loesungsweg": [
            "Zeitgradfaktor = 125 / 100",
            "Zeitgradfaktor = 1,25"
        ]
    },

    {
        "id": "AE003",
        "thema": "Arbeitsentgelt",
        "unterthema": "Akkordrichtsatz",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Akkordgrundlohn beträgt 16 €/h, "
            "der Akkordzuschlag 4 €/h. Berechnen Sie den Akkordrichtsatz.",
        "gegeben": [
            "Akkordgrundlohn = 16 €/h",
            "Akkordzuschlag = 4 €/h"
        ],
        "gesucht": "Akkordrichtsatz",
        "formel":
            "Akkordrichtsatz = Akkordgrundlohn + Akkordzuschlag",
        "tipp": "Beide Lohnbestandteile addieren.",
        "ergebnis": 20,
        "einheit": "€/h",
        "loesungsweg": [
            "Akkordrichtsatz = 16 + 4",
            "Akkordrichtsatz = 20 €/h"
        ]
    },

    {
        "id": "AE004",
        "thema": "Arbeitsentgelt",
        "unterthema": "Akkordlohn",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Akkordrichtsatz beträgt 20 €/h. "
            "Der Zeitgrad beträgt 120 %. "
            "Berechnen Sie den Akkordlohn pro Stunde.",
        "gegeben": [
            "Akkordrichtsatz = 20 €/h",
            "Zeitgrad = 120 %"
        ],
        "gesucht": "Akkordlohn pro Stunde",
        "formel":
            "Akkordlohn pro Stunde = Akkordrichtsatz × Zeitgradfaktor",
        "tipp": "Zuerst den Zeitgradfaktor berechnen.",
        "ergebnis": 24,
        "einheit": "€/h",
        "loesungsweg": [
            "Zeitgradfaktor = 120 / 100 = 1,20",
            "Akkordlohn = 20 × 1,20",
            "Akkordlohn = 24 €/h"
        ]
    },

    {
        "id": "AE005",
        "thema": "Arbeitsentgelt",
        "unterthema": "Stückgeld",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Akkordrichtsatz beträgt 21 €/h. "
            "Die Normalleistung beträgt 30 Stück/h. "
            "Berechnen Sie das Stückgeld.",
        "gegeben": [
            "Akkordrichtsatz = 21 €/h",
            "Normalleistung = 30 Stück/h"
        ],
        "gesucht": "Stückgeld",
        "formel":
            "Stückgeld = Akkordrichtsatz / Normalleistung",
        "tipp": "Akkordrichtsatz durch Normalleistung teilen.",
        "ergebnis": 0.70,
        "einheit": "€/Stück",
        "loesungsweg": [
            "Stückgeld = 21 / 30",
            "Stückgeld = 0,70 €/Stück"
        ]
    },

    {
        "id": "AE006",
        "thema": "Arbeitsentgelt",
        "unterthema": "Geldakkord",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Das Stückgeld beträgt 0,70 €. "
            "Ein Mitarbeiter fertigt 280 Stück. "
            "Berechnen Sie den Bruttolohn.",
        "gegeben": [
            "Stückgeld = 0,70 €/Stück",
            "Leistungsmenge = 280 Stück"
        ],
        "gesucht": "Bruttolohn",
        "formel":
            "Bruttolohn = Leistungsmenge × Stückgeld",
        "tipp": "Stückzahl mit Stückgeld multiplizieren.",
        "ergebnis": 196,
        "einheit": "€",
        "loesungsweg": [
            "Bruttolohn = 280 × 0,70",
            "Bruttolohn = 196 €"
        ]
    },

    {
        "id": "AE007",
        "thema": "Arbeitsentgelt",
        "unterthema": "Vorgabezeit",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Die Normalleistung beträgt 15 Stück pro Stunde. "
            "Berechnen Sie die Vorgabezeit.",
        "gegeben": [
            "Normalleistung = 15 Stück/h"
        ],
        "gesucht": "Vorgabezeit",
        "formel":
            "Vorgabezeit = 60 / Normalleistung",
        "tipp": "Eine Stunde hat 60 Minuten.",
        "ergebnis": 4,
        "einheit": "min/Stück",
        "loesungsweg": [
            "Vorgabezeit = 60 / 15",
            "Vorgabezeit = 4 min/Stück"
        ]
    },

    {
        "id": "AE008",
        "thema": "Arbeitsentgelt",
        "unterthema": "Zeitakkord",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Der Akkordrichtsatz beträgt 24 €/h. "
            "Die Vorgabezeit beträgt 3 Minuten je Stück. "
            "Es werden 180 Stück gefertigt. "
            "Berechnen Sie den Bruttolohn.",
        "gegeben": [
            "Akkordrichtsatz = 24 €/h",
            "Vorgabezeit = 3 min/Stück",
            "Stückzahl = 180"
        ],
        "gesucht": "Bruttolohn",
        "formel":
            "Bruttolohn = Minutenfaktor × Vorgabezeit × Stückzahl",
        "tipp": "Zuerst Minutenfaktor = Akkordrichtsatz / 60.",
        "ergebnis": 216,
        "einheit": "€",
        "loesungsweg": [
            "Minutenfaktor = 24 / 60 = 0,40 €/min",
            "Bruttolohn = 0,40 × 3 × 180",
            "Bruttolohn = 216 €"
        ]
    },

    {
        "id": "AE009",
        "thema": "Arbeitsentgelt",
        "unterthema": "Prämienlohn",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Der Grundlohn beträgt 160 €. "
            "Zusätzlich erhält der Mitarbeiter eine Prämie von 35 €. "
            "Berechnen Sie den Prämienlohn.",
        "gegeben": [
            "Grundlohn = 160 €",
            "Prämie = 35 €"
        ],
        "gesucht": "Prämienlohn",
        "formel":
            "Prämienlohn = Grundlohn + Prämie",
        "tipp": "Grundlohn und Prämie addieren.",
        "ergebnis": 195,
        "einheit": "€",
        "loesungsweg": [
            "Prämienlohn = 160 + 35",
            "Prämienlohn = 195 €"
        ]
    },


    # ========================================================
    # UNTERNEHMENSFORMEN
    # ========================================================

    {
        "id": "UF001",
        "thema": "Unternehmensformen",
        "unterthema": "GmbH",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Wie hoch ist das gesetzliche Mindeststammkapital einer GmbH?",
        "antworten": [
            "10.000 €",
            "25.000 €",
            "50.000 €",
            "100.000 €"
        ],
        "richtige_antwort": "25.000 €",
        "tipp": "Nicht mit dem Grundkapital der AG verwechseln.",
        "erklaerung":
            "Das Mindeststammkapital einer GmbH beträgt 25.000 €."
    },

    {
        "id": "UF002",
        "thema": "Unternehmensformen",
        "unterthema": "AG",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Wie hoch ist das gesetzliche Mindestgrundkapital einer AG?",
        "antworten": [
            "25.000 €",
            "35.000 €",
            "50.000 €",
            "75.000 €"
        ],
        "richtige_antwort": "50.000 €",
        "tipp": "Die AG benötigt mehr Mindestkapital als die GmbH.",
        "erklaerung":
            "Das Mindestgrundkapital einer AG beträgt 50.000 €."
    },

    {
        "id": "UF003",
        "thema": "Unternehmensformen",
        "unterthema": "AG",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welches Organ leitet eine Aktiengesellschaft?",
        "antworten": [
            "Aufsichtsrat",
            "Vorstand",
            "Hauptversammlung",
            "Betriebsrat"
        ],
        "richtige_antwort": "Vorstand",
        "tipp": "Leitung und Überwachung unterscheiden.",
        "erklaerung":
            "Der Vorstand leitet die Aktiengesellschaft."
    },

    {
        "id": "UF004",
        "thema": "Unternehmensformen",
        "unterthema": "AG",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welches Organ überwacht den Vorstand einer AG?",
        "antworten": [
            "Geschäftsführer",
            "Hauptversammlung",
            "Aufsichtsrat",
            "Kommanditist"
        ],
        "richtige_antwort": "Aufsichtsrat",
        "tipp": "Der Name deutet bereits auf Kontrolle hin.",
        "erklaerung":
            "Der Aufsichtsrat überwacht den Vorstand."
    },

    {
        "id": "UF005",
        "thema": "Unternehmensformen",
        "unterthema": "KG",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher Gesellschafter einer KG haftet grundsätzlich unbeschränkt?",
        "antworten": [
            "Kommanditist",
            "Komplementär",
            "Aktionär",
            "Geschäftsführer"
        ],
        "richtige_antwort": "Komplementär",
        "tipp": "Komplementär und Kommanditist nicht verwechseln.",
        "erklaerung":
            "Der Komplementär haftet grundsätzlich unbeschränkt."
    },

    {
        "id": "UF006",
        "thema": "Unternehmensformen",
        "unterthema": "OHG",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Aussage zur OHG ist richtig?",
        "antworten": [
            "Die Gesellschafter haften nur mit ihrer Einlage.",
            "Die Gesellschafter haften grundsätzlich persönlich, unbeschränkt und gesamtschuldnerisch.",
            "Eine OHG benötigt 25.000 € Mindestkapital.",
            "Eine OHG ist eine Kapitalgesellschaft."
        ],
        "richtige_antwort":
            "Die Gesellschafter haften grundsätzlich persönlich, unbeschränkt und gesamtschuldnerisch.",
        "tipp": "Die OHG gehört zu den Personengesellschaften.",
        "erklaerung":
            "Die OHG-Gesellschafter haften grundsätzlich persönlich und unbeschränkt."
    },

    {
        "id": "UF007",
        "thema": "Unternehmensformen",
        "unterthema": "Einzelunternehmen",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Wie haftet ein Einzelunternehmer grundsätzlich?",
        "antworten": [
            "Nur mit dem Betriebsvermögen",
            "Mit Geschäfts- und Privatvermögen",
            "Nur bis 25.000 €",
            "Gar nicht persönlich"
        ],
        "richtige_antwort":
            "Mit Geschäfts- und Privatvermögen",
        "tipp": "Es gibt keine Haftungsbeschränkung wie bei einer GmbH.",
        "erklaerung":
            "Ein Einzelunternehmer haftet grundsätzlich unbeschränkt."
    },

    {
        "id": "UF008",
        "thema": "Unternehmensformen",
        "unterthema": "Kapitalgesellschaften",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche beiden Formen sind Kapitalgesellschaften?",
        "antworten": [
            "OHG und KG",
            "GmbH und AG",
            "KG und GmbH",
            "Einzelunternehmen und OHG"
        ],
        "richtige_antwort":
            "GmbH und AG",
        "tipp": "Stammkapital und Grundkapital.",
        "erklaerung":
            "GmbH und AG sind Kapitalgesellschaften."
    },

    {
        "id": "UF009",
        "thema": "Unternehmensformen",
        "unterthema": "Personengesellschaften",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche beiden Formen sind Personengesellschaften?",
        "antworten": [
            "OHG und KG",
            "GmbH und AG",
            "AG und KG",
            "GmbH und OHG"
        ],
        "richtige_antwort":
            "OHG und KG",
        "tipp": "GmbH und AG gehören zur anderen Gruppe.",
        "erklaerung":
            "OHG und KG gehören zu den Personengesellschaften."
    },

    {
        "id": "UF010",
        "thema": "Unternehmensformen",
        "unterthema": "KG",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Wer übernimmt bei einer KG grundsätzlich die Geschäftsführung?",
        "antworten": [
            "Kommanditist",
            "Komplementär",
            "Aufsichtsrat",
            "Hauptversammlung"
        ],
        "richtige_antwort":
            "Komplementär",
        "tipp": "Denke an die Stellung des persönlich haftenden Gesellschafters.",
        "erklaerung":
            "Die Geschäftsführung liegt grundsätzlich beim Komplementär."
    },


    # ========================================================
    # ORGANISATION
    # ========================================================

    {
        "id": "OR001",
        "thema": "Organisation",
        "unterthema": "Aufbauorganisation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Frage beantwortet hauptsächlich die Aufbauorganisation?",
        "antworten": [
            "Wann wird eine Tätigkeit durchgeführt?",
            "Wer ist für welche Aufgabe zuständig?",
            "Wie hoch sind die Stückkosten?",
            "Wie lange wird Material gelagert?"
        ],
        "richtige_antwort":
            "Wer ist für welche Aufgabe zuständig?",
        "tipp": "Denke an Stellen, Abteilungen und Hierarchien.",
        "erklaerung":
            "Die Aufbauorganisation regelt die dauerhafte Struktur des Unternehmens."
    },

    {
        "id": "OR002",
        "thema": "Organisation",
        "unterthema": "Ablauforganisation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Womit beschäftigt sich die Ablauforganisation hauptsächlich?",
        "antworten": [
            "Mit Rechtsformen",
            "Mit Arbeits- und Prozessabläufen",
            "Mit Aktienkapital",
            "Mit der Lagerbewertung"
        ],
        "richtige_antwort":
            "Mit Arbeits- und Prozessabläufen",
        "tipp": "Ablauf = Reihenfolge eines Prozesses.",
        "erklaerung":
            "Die Ablauforganisation regelt zeitliche, räumliche und sachliche Arbeitsabläufe."
    },

    {
        "id": "OR003",
        "thema": "Organisation",
        "unterthema": "Einliniensystem",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Was kennzeichnet das Einliniensystem?",
        "antworten": [
            "Jeder Mitarbeiter hat mehrere Vorgesetzte.",
            "Jede Stelle erhält Weisungen von einer übergeordneten Stelle.",
            "Es gibt keine Hierarchie.",
            "Nur Stabsstellen dürfen Weisungen erteilen."
        ],
        "richtige_antwort":
            "Jede Stelle erhält Weisungen von einer übergeordneten Stelle.",
        "tipp": "Eine Linie = ein Weisungsweg.",
        "erklaerung":
            "Das Einliniensystem besitzt eindeutige Weisungs- und Unterstellungsverhältnisse."
    },

    {
        "id": "OR004",
        "thema": "Organisation",
        "unterthema": "Mehrliniensystem",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher Nachteil kann beim Mehrliniensystem auftreten?",
        "antworten": [
            "Keine Nutzung von Spezialwissen",
            "Widersprüchliche Anweisungen",
            "Es gibt nur einen Vorgesetzten",
            "Es gibt keine kurzen Informationswege"
        ],
        "richtige_antwort":
            "Widersprüchliche Anweisungen",
        "tipp": "Mehrere Vorgesetzte können unterschiedliche Ziele verfolgen.",
        "erklaerung":
            "Mehrfachunterstellung kann zu Kompetenz- und Weisungskonflikten führen."
    },

    {
        "id": "OR005",
        "thema": "Organisation",
        "unterthema": "Stablinienorganisation",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche typische Aufgabe hat eine Stabsstelle?",
        "antworten": [
            "Sie berät die Leitung.",
            "Sie ist grundsätzlich allen Mitarbeitern weisungsbefugt.",
            "Sie ersetzt die Geschäftsführung.",
            "Sie führt ausschließlich Produktionsarbeiten aus."
        ],
        "richtige_antwort":
            "Sie berät die Leitung.",
        "tipp": "Stab = Spezialwissen zur Unterstützung.",
        "erklaerung":
            "Stabsstellen unterstützen Leitungsstellen beratend."
    },

    {
        "id": "OR006",
        "thema": "Organisation",
        "unterthema": "Funktionale Organisation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Gliederung ist typisch für eine funktionale Organisation?",
        "antworten": [
            "Deutschland, Frankreich, USA",
            "Produkt A, Produkt B, Produkt C",
            "Einkauf, Produktion, Vertrieb, Personal",
            "Privatkunden und Geschäftskunden"
        ],
        "richtige_antwort":
            "Einkauf, Produktion, Vertrieb, Personal",
        "tipp": "Funktion = betriebliche Tätigkeit.",
        "erklaerung":
            "Bei der funktionalen Organisation erfolgt die Gliederung nach betrieblichen Funktionen."
    },

    {
        "id": "OR007",
        "thema": "Organisation",
        "unterthema": "Divisionale Organisation",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welches Beispiel beschreibt eine divisionale Organisation?",
        "antworten": [
            "Einkauf – Produktion – Vertrieb",
            "Produktbereich Maschinen – Produktbereich Anlagen – Produktbereich Service",
            "Vorstand – Meister – Mitarbeiter",
            "Stab – Linie – Betriebsrat"
        ],
        "richtige_antwort":
            "Produktbereich Maschinen – Produktbereich Anlagen – Produktbereich Service",
        "tipp": "Divisionen können nach Produkten, Regionen oder Kunden aufgebaut sein.",
        "erklaerung":
            "Bei der divisionalen Organisation wird nach Objekten gegliedert."
    },

    {
        "id": "OR008",
        "thema": "Organisation",
        "unterthema": "Matrixorganisation",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher typische Nachteil gehört zur Matrixorganisation?",
        "antworten": [
            "Keine Spezialisierung",
            "Konflikte durch Mehrfachunterstellung",
            "Keine Zusammenarbeit zwischen Bereichen",
            "Keine Verantwortung"
        ],
        "richtige_antwort":
            "Konflikte durch Mehrfachunterstellung",
        "tipp": "Zwei Organisationsdimensionen treffen aufeinander.",
        "erklaerung":
            "Die Matrixorganisation kann durch mehrere Weisungsbeziehungen Konflikte verursachen."
    },

    {
        "id": "OR009",
        "thema": "Organisation",
        "unterthema": "Dezentralisation",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher Vorteil spricht für Dezentralisation?",
        "antworten": [
            "Entscheidungen liegen ausschließlich bei der Unternehmensleitung.",
            "Entscheidungen können näher am Problem getroffen werden.",
            "Es entstehen immer einheitlichere Entscheidungen.",
            "Untere Führungsebenen verlieren Kompetenzen."
        ],
        "richtige_antwort":
            "Entscheidungen können näher am Problem getroffen werden.",
        "tipp": "Entscheidungsbefugnis wird nach unten verlagert.",
        "erklaerung":
            "Dezentralisation kann Entscheidungen beschleunigen und Führungskräfte entlasten."
    },

    {
        "id": "OR010",
        "thema": "Organisation",
        "unterthema": "Delegation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was sollte bei einer sinnvollen Delegation gemeinsam übertragen werden?",
        "antworten": [
            "Nur Aufgaben",
            "Nur Verantwortung",
            "Aufgabe, Kompetenz und Verantwortung",
            "Nur Informationen"
        ],
        "richtige_antwort":
            "Aufgabe, Kompetenz und Verantwortung",
        "tipp": "Wer eine Aufgabe übernimmt, braucht auch die notwendigen Befugnisse.",
        "erklaerung":
            "Aufgabe, Kompetenz und Verantwortung müssen miteinander übereinstimmen."
    },


    # ========================================================
    # FERTIGUNGSORGANISATION
    # ========================================================

    {
        "id": "FO001",
        "thema": "Fertigungsorganisation",
        "unterthema": "Werkstattfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was kennzeichnet die Werkstattfertigung?",
        "antworten": [
            "Maschinen werden nach Bearbeitungsreihenfolge angeordnet.",
            "Gleichartige Maschinen werden räumlich zusammengefasst.",
            "Das Produkt bleibt immer am selben Ort.",
            "Die Fertigung ist immer vollautomatisch."
        ],
        "richtige_antwort":
            "Gleichartige Maschinen werden räumlich zusammengefasst.",
        "tipp": "Dreherei, Fräserei, Schleiferei.",
        "erklaerung":
            "Bei der Werkstattfertigung werden Betriebsmittel nach Verrichtungen gruppiert."
    },

    {
        "id": "FO002",
        "thema": "Fertigungsorganisation",
        "unterthema": "Fließfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher Vorteil ist typisch für die Fließfertigung?",
        "antworten": [
            "Sehr lange Transportwege",
            "Kurze Durchlaufzeiten",
            "Sehr hohe Flexibilität bei Einzelstücken",
            "Keine Abhängigkeit zwischen Arbeitsplätzen"
        ],
        "richtige_antwort":
            "Kurze Durchlaufzeiten",
        "tipp": "Der Materialfluss folgt einer festen Reihenfolge.",
        "erklaerung":
            "Die Fließfertigung ermöglicht kurze Wege und meist kurze Durchlaufzeiten."
    },

    {
        "id": "FO003",
        "thema": "Fertigungsorganisation",
        "unterthema": "Reihenfertigung",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Was unterscheidet die Reihenfertigung typischerweise von der Fließfertigung?",
        "antworten": [
            "Die Arbeitsplätze haben keine Reihenfolge.",
            "Es besteht nicht zwingend eine feste zeitliche Taktung.",
            "Es werden ausschließlich Einzelstücke gefertigt.",
            "Das Produkt bleibt ortsfest."
        ],
        "richtige_antwort":
            "Es besteht nicht zwingend eine feste zeitliche Taktung.",
        "tipp": "Reihenfolge ja, fester Takt nicht unbedingt.",
        "erklaerung":
            "Bei der Reihenfertigung ist die räumliche Reihenfolge festgelegt, aber nicht zwingend der Takt."
    },

    {
        "id": "FO004",
        "thema": "Fertigungsorganisation",
        "unterthema": "Baustellenfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Fertigungsform eignet sich besonders für große, ortsfeste Produkte?",
        "antworten": [
            "Baustellenfertigung",
            "Fließfertigung",
            "Massenfertigung",
            "Sortenfertigung"
        ],
        "richtige_antwort":
            "Baustellenfertigung",
        "tipp": "Menschen und Material kommen zum Produkt.",
        "erklaerung":
            "Bei der Baustellenfertigung bleibt das Produkt am Fertigungsort."
    },

    {
        "id": "FO005",
        "thema": "Fertigungsorganisation",
        "unterthema": "Einzelfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Fertigungsart ist für eine kundenspezifische Sondermaschine typisch?",
        "antworten": [
            "Massenfertigung",
            "Einzelfertigung",
            "Sortenfertigung",
            "Fließfertigung"
        ],
        "richtige_antwort":
            "Einzelfertigung",
        "tipp": "Ein individuelles Produkt.",
        "erklaerung":
            "Sondermaschinen werden häufig als Einzelfertigung hergestellt."
    },

    {
        "id": "FO006",
        "thema": "Fertigungsorganisation",
        "unterthema": "Serienfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was kennzeichnet die Serienfertigung?",
        "antworten": [
            "Unbegrenzte Produktion eines identischen Produktes",
            "Begrenzte Stückzahl gleichartiger Produkte",
            "Nur individuelle Einzelprodukte",
            "Das Produkt bleibt grundsätzlich ortsfest"
        ],
        "richtige_antwort":
            "Begrenzte Stückzahl gleichartiger Produkte",
        "tipp": "Nach einer Serie kann eine andere folgen.",
        "erklaerung":
            "Serienfertigung bedeutet die Herstellung einer begrenzten Anzahl gleichartiger Produkte."
    },

    {
        "id": "FO007",
        "thema": "Fertigungsorganisation",
        "unterthema": "Massenfertigung",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welches Merkmal ist typisch für Massenfertigung?",
        "antworten": [
            "Sehr geringe Stückzahlen",
            "Ein Produkt in sehr großer Menge",
            "Ausschließlich Kundenaufträge",
            "Häufige Produktwechsel"
        ],
        "richtige_antwort":
            "Ein Produkt in sehr großer Menge",
        "tipp": "Masse = sehr hohe Stückzahl.",
        "erklaerung":
            "Bei der Massenfertigung wird ein gleichartiges Produkt langfristig in hoher Menge hergestellt."
    },

    {
        "id": "FO008",
        "thema": "Fertigungsorganisation",
        "unterthema": "Gruppenfertigung",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welcher Vorteil kann durch Gruppenfertigung entstehen?",
        "antworten": [
            "Längere Transportwege",
            "Höhere Eigenverantwortung der Gruppe",
            "Keine Zusammenarbeit",
            "Zwingend höhere Zwischenbestände"
        ],
        "richtige_antwort":
            "Höhere Eigenverantwortung der Gruppe",
        "tipp": "Mehrere Arbeitsplätze bilden eine Fertigungsinsel bzw. Gruppe.",
        "erklaerung":
            "Gruppenfertigung kann Eigenverantwortung, Flexibilität und kurze Wege fördern."
    },


    # ========================================================
    # KAPAZITÄTSWIRTSCHAFT
    # ========================================================

    {
        "id": "KA001",
        "thema": "Kapazitätswirtschaft",
        "unterthema": "Kapazitätsauslastung",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Eine Maschine könnte 2.000 Stück pro Woche herstellen. "
            "Tatsächlich werden 1.600 Stück hergestellt. "
            "Berechnen Sie die Kapazitätsauslastung.",
        "gegeben": [
            "Ist-Beschäftigung = 1.600 Stück",
            "verfügbare Kapazität = 2.000 Stück"
        ],
        "gesucht": "Kapazitätsauslastung",
        "formel":
            "Kapazitätsauslastung % = Ist-Beschäftigung / verfügbare Kapazität × 100",
        "tipp": "Ist durch mögliche Kapazität und mal 100.",
        "ergebnis": 80,
        "einheit": "%",
        "loesungsweg": [
            "Kapazitätsauslastung = 1.600 / 2.000 × 100",
            "Kapazitätsauslastung = 80 %"
        ]
    },

    {
        "id": "KA002",
        "thema": "Kapazitätswirtschaft",
        "unterthema": "Engpass",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was versteht man unter einem Kapazitätsengpass?",
        "antworten": [
            "Einen Bereich mit unbegrenzter Kapazität",
            "Einen Bereich, dessen Kapazität den Gesamtprozess begrenzt",
            "Eine zu große Lagerfläche",
            "Eine besonders günstige Maschine"
        ],
        "richtige_antwort":
            "Einen Bereich, dessen Kapazität den Gesamtprozess begrenzt",
        "tipp": "Der Engpass bestimmt den maximal möglichen Durchsatz.",
        "erklaerung":
            "Ein Engpass begrenzt die Leistung des gesamten Produktionssystems."
    },

    {
        "id": "KA003",
        "thema": "Kapazitätswirtschaft",
        "unterthema": "Personalkapazität",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Maßnahme kann kurzfristig die Personalkapazität erhöhen?",
        "antworten": [
            "Überstunden",
            "Reduzierung der Arbeitszeit",
            "Stilllegung einer Schicht",
            "Abbau von Personal"
        ],
        "richtige_antwort":
            "Überstunden",
        "tipp": "Gesucht ist eine kurzfristige Erhöhung.",
        "erklaerung":
            "Überstunden können kurzfristig zusätzliche Personalkapazität bereitstellen."
    },

    {
        "id": "KA004",
        "thema": "Kapazitätswirtschaft",
        "unterthema": "Maschinenkapazität",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Maßnahme kann die Maschinenkapazität kurzfristig erhöhen?",
        "antworten": [
            "Zusätzliche Schicht",
            "Stilllegung der Maschine",
            "Reduzierung der Laufzeit",
            "Verlängerung von Stillstandszeiten"
        ],
        "richtige_antwort":
            "Zusätzliche Schicht",
        "tipp": "Mehr nutzbare Maschinenstunden.",
        "erklaerung":
            "Eine zusätzliche Schicht erhöht die nutzbare Maschinenzeit."
    },

    {
        "id": "KA005",
        "thema": "Kapazitätswirtschaft",
        "unterthema": "Kapazität",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was beschreibt die Kapazität eines Betriebsmittels?",
        "antworten": [
            "Seinen Anschaffungspreis",
            "Sein Leistungsvermögen innerhalb eines Zeitraums",
            "Seinen Restbuchwert",
            "Nur seine elektrische Leistung"
        ],
        "richtige_antwort":
            "Sein Leistungsvermögen innerhalb eines Zeitraums",
        "tipp": "Wie viel kann innerhalb einer bestimmten Zeit geleistet werden?",
        "erklaerung":
            "Kapazität beschreibt das mögliche Leistungsvermögen innerhalb eines Zeitraums."
    },


    # ========================================================
    # UNTERNEHMENSZUSAMMENSCHLÜSSE
    # ========================================================

    {
        "id": "UZ001",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Horizontal",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Zwei Maschinenhersteller derselben Produktionsstufe schließen sich zusammen. "
            "Um welche Richtung handelt es sich?",
        "antworten": [
            "Horizontal",
            "Vertikal",
            "Diagonal",
            "Intern"
        ],
        "richtige_antwort":
            "Horizontal",
        "tipp": "Gleiche Wirtschaftsstufe.",
        "erklaerung":
            "Ein horizontaler Zusammenschluss verbindet Unternehmen derselben Stufe."
    },

    {
        "id": "UZ002",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Vertikal",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Ein Maschinenbauer übernimmt einen wichtigen Zulieferer. "
            "Welche Art des Zusammenschlusses liegt vor?",
        "antworten": [
            "Horizontal",
            "Vertikal",
            "Diagonal",
            "Keine"
        ],
        "richtige_antwort":
            "Vertikal",
        "tipp": "Unterschiedliche Stufen derselben Wertschöpfungskette.",
        "erklaerung":
            "Der Zusammenschluss erfolgt entlang der Wertschöpfungskette."
    },

    {
        "id": "UZ003",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Diagonal",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Unternehmen völlig verschiedener Branchen schließen sich zusammen. "
            "Wie nennt man diese Richtung?",
        "antworten": [
            "Horizontal",
            "Vertikal",
            "Diagonal",
            "Funktional"
        ],
        "richtige_antwort":
            "Diagonal",
        "tipp": "Keine direkte Verbindung in der Wertschöpfungskette.",
        "erklaerung":
            "Bei einem diagonalen Zusammenschluss stammen die Unternehmen aus unterschiedlichen Branchen."
    },

    {
        "id": "UZ004",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Konzern",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Was kennzeichnet einen Konzern?",
        "antworten": [
            "Alle Unternehmen verlieren zwingend ihre rechtliche Selbstständigkeit.",
            "Rechtlich selbstständige Unternehmen stehen unter einheitlicher wirtschaftlicher Leitung.",
            "Es gibt keinerlei wirtschaftliche Verbindung.",
            "Ein Konzern besteht immer nur aus zwei Unternehmen."
        ],
        "richtige_antwort":
            "Rechtlich selbstständige Unternehmen stehen unter einheitlicher wirtschaftlicher Leitung.",
        "tipp": "Rechtlich selbstständig – wirtschaftlich verbunden.",
        "erklaerung":
            "Konzernunternehmen bleiben rechtlich selbstständig, werden aber wirtschaftlich einheitlich geleitet."
    },

    {
        "id": "UZ005",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Fusion",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Was geschieht bei einer Fusion?",
        "antworten": [
            "Unternehmen kooperieren nur lose.",
            "Unternehmen verschmelzen zu einer rechtlichen Einheit.",
            "Unternehmen tauschen lediglich Mitarbeiter.",
            "Es entsteht immer nur ein Kartell."
        ],
        "richtige_antwort":
            "Unternehmen verschmelzen zu einer rechtlichen Einheit.",
        "tipp": "Fusion = Verschmelzung.",
        "erklaerung":
            "Bei einer Fusion werden Unternehmen rechtlich zusammengeführt."
    },

    {
        "id": "UZ006",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Joint Venture",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Was ist ein typischer Vorteil eines Joint Ventures?",
        "antworten": [
            "Risiko und Kapital können geteilt werden.",
            "Es gibt grundsätzlich keine Zusammenarbeit.",
            "Alle beteiligten Unternehmen müssen ihre Existenz aufgeben.",
            "Es darf kein Wissen ausgetauscht werden."
        ],
        "richtige_antwort":
            "Risiko und Kapital können geteilt werden.",
        "tipp": "Gemeinsames Projekt oder Unternehmen.",
        "erklaerung":
            "Joint Ventures ermöglichen die gemeinsame Nutzung von Kapital, Wissen und Risiken."
    },

    {
        "id": "UZ007",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Kooperation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was ist für eine Kooperation typisch?",
        "antworten": [
            "Die beteiligten Unternehmen arbeiten zusammen.",
            "Alle Unternehmen werden vollständig aufgelöst.",
            "Es gibt keine gemeinsamen Ziele.",
            "Die Unternehmen dürfen keine Verträge schließen."
        ],
        "richtige_antwort":
            "Die beteiligten Unternehmen arbeiten zusammen.",
        "tipp": "Kooperation bedeutet Zusammenarbeit.",
        "erklaerung":
            "Bei einer Kooperation verfolgen selbstständige Unternehmen gemeinsame Ziele."
    },

    {
        "id": "UZ008",
        "thema": "Unternehmenszusammenschlüsse",
        "unterthema": "Kartell",
        "schwierigkeit": "Mittel",
        "typ": "multiple_choice",
        "aufgabe":
            "Warum werden Kartelle wettbewerbsrechtlich kritisch betrachtet?",
        "antworten": [
            "Weil sie den Wettbewerb beschränken können.",
            "Weil sie immer staatliche Unternehmen sind.",
            "Weil sie ausschließlich gemeinnützig arbeiten.",
            "Weil sie keinen Einfluss auf Märkte haben."
        ],
        "richtige_antwort":
            "Weil sie den Wettbewerb beschränken können.",
        "tipp": "Absprachen zwischen Wettbewerbern.",
        "erklaerung":
            "Kartellabsprachen können den Wettbewerb erheblich beeinträchtigen."
    },


    # ========================================================
    # INVESTITIONSRECHNUNG
    # ========================================================

    {
        "id": "IR001",
        "thema": "Investitionsrechnung",
        "unterthema": "Gewinn",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Eine Investition erzielt Erlöse von 180.000 €. "
            "Die Kosten betragen 145.000 €. "
            "Berechnen Sie den Gewinn.",
        "gegeben": [
            "Erlöse = 180.000 €",
            "Kosten = 145.000 €"
        ],
        "gesucht": "Gewinn",
        "formel":
            "Gewinn = Erlöse - Kosten",
        "tipp": "Kosten von den Erlösen abziehen.",
        "ergebnis": 35000,
        "einheit": "€",
        "loesungsweg": [
            "Gewinn = 180.000 - 145.000",
            "Gewinn = 35.000 €"
        ]
    },

    {
        "id": "IR002",
        "thema": "Investitionsrechnung",
        "unterthema": "Rentabilität",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Eine Investition erzielt einen Gewinn von 30.000 €. "
            "Das eingesetzte Kapital beträgt 250.000 €. "
            "Berechnen Sie die Rentabilität.",
        "gegeben": [
            "Gewinn = 30.000 €",
            "eingesetztes Kapital = 250.000 €"
        ],
        "gesucht": "Rentabilität",
        "formel":
            "Rentabilität % = Gewinn / eingesetztes Kapital × 100",
        "tipp": "Gewinn durch Kapital und mal 100.",
        "ergebnis": 12,
        "einheit": "%",
        "loesungsweg": [
            "Rentabilität = 30.000 / 250.000 × 100",
            "Rentabilität = 12 %"
        ]
    },

    {
        "id": "IR003",
        "thema": "Investitionsrechnung",
        "unterthema": "Kostenvergleich",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Welche Investition ist bei gleicher Leistung nach der Kostenvergleichsrechnung grundsätzlich günstiger?",
        "antworten": [
            "Die mit den niedrigeren Kosten",
            "Die mit den höheren Kosten",
            "Immer die teurere Maschine",
            "Die mit dem höchsten Personalbedarf"
        ],
        "richtige_antwort":
            "Die mit den niedrigeren Kosten",
        "tipp": "Es werden Kosten verglichen.",
        "erklaerung":
            "Bei gleicher Leistung wird grundsätzlich die kostengünstigere Alternative bevorzugt."
    },

    {
        "id": "IR004",
        "thema": "Investitionsrechnung",
        "unterthema": "Amortisation",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was beschreibt die Amortisationsdauer?",
        "antworten": [
            "Die Zeit bis das eingesetzte Kapital zurückgeflossen ist",
            "Die technische Lebensdauer einer Maschine",
            "Die Lagerdauer eines Materials",
            "Die Ausbildungsdauer eines Mitarbeiters"
        ],
        "richtige_antwort":
            "Die Zeit bis das eingesetzte Kapital zurückgeflossen ist",
        "tipp": "Wann hat sich die Investition zurückgezahlt?",
        "erklaerung":
            "Die Amortisationsdauer beschreibt den Zeitraum des Kapitalrückflusses."
    },


    # ========================================================
    # BETRIEBLICHE KENNZAHLEN
    # ========================================================

    {
        "id": "BK001",
        "thema": "Betriebliche Kennzahlen",
        "unterthema": "Produktivität",
        "schwierigkeit": "Leicht",
        "typ": "rechnen",
        "aufgabe":
            "Ein Mitarbeiter produziert in 8 Stunden 240 Teile. "
            "Berechnen Sie seine Produktivität in Stück pro Stunde.",
        "gegeben": [
            "Output = 240 Stück",
            "Input = 8 Stunden"
        ],
        "gesucht": "Produktivität",
        "formel":
            "Produktivität = Output / Input",
        "tipp": "Stückzahl durch Arbeitsstunden teilen.",
        "ergebnis": 30,
        "einheit": "Stück/h",
        "loesungsweg": [
            "Produktivität = 240 / 8",
            "Produktivität = 30 Stück/h"
        ]
    },

    {
        "id": "BK002",
        "thema": "Betriebliche Kennzahlen",
        "unterthema": "Wirtschaftlichkeit",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Ein Betrieb erzielt einen Ertrag von 150.000 €. "
            "Der Aufwand beträgt 120.000 €. "
            "Berechnen Sie die Wirtschaftlichkeit.",
        "gegeben": [
            "Ertrag = 150.000 €",
            "Aufwand = 120.000 €"
        ],
        "gesucht": "Wirtschaftlichkeit",
        "formel":
            "Wirtschaftlichkeit = Ertrag / Aufwand",
        "tipp": "Ertrag durch Aufwand teilen.",
        "ergebnis": 1.25,
        "einheit": "",
        "loesungsweg": [
            "Wirtschaftlichkeit = 150.000 / 120.000",
            "Wirtschaftlichkeit = 1,25"
        ]
    },

    {
        "id": "BK003",
        "thema": "Betriebliche Kennzahlen",
        "unterthema": "Rentabilität",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Der Gewinn beträgt 40.000 €. "
            "Das eingesetzte Kapital beträgt 500.000 €. "
            "Berechnen Sie die Rentabilität.",
        "gegeben": [
            "Gewinn = 40.000 €",
            "Kapital = 500.000 €"
        ],
        "gesucht": "Rentabilität",
        "formel":
            "Rentabilität % = Gewinn / eingesetztes Kapital × 100",
        "tipp": "Gewinn durch Kapital und mal 100.",
        "ergebnis": 8,
        "einheit": "%",
        "loesungsweg": [
            "Rentabilität = 40.000 / 500.000 × 100",
            "Rentabilität = 8 %"
        ]
    },

    {
        "id": "BK004",
        "thema": "Betriebliche Kennzahlen",
        "unterthema": "Liquidität",
        "schwierigkeit": "Leicht",
        "typ": "multiple_choice",
        "aufgabe":
            "Was versteht man unter Liquidität?",
        "antworten": [
            "Die Fähigkeit, fällige Zahlungsverpflichtungen zu erfüllen",
            "Die Anzahl produzierter Teile",
            "Die Höhe der Abschreibung",
            "Die Zahl der Mitarbeiter"
        ],
        "richtige_antwort":
            "Die Fähigkeit, fällige Zahlungsverpflichtungen zu erfüllen",
        "tipp": "Kann das Unternehmen seine Rechnungen bezahlen?",
        "erklaerung":
            "Liquidität beschreibt die Zahlungsfähigkeit eines Unternehmens."
    }

]


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def aufgaben_nach_thema(thema):
    return [
        aufgabe
        for aufgabe in BWH_AUFGABEN
        if aufgabe["thema"] == thema
    ]


def aufgaben_nach_unterthema(unterthema):
    return [
        aufgabe
        for aufgabe in BWH_AUFGABEN
        if aufgabe["unterthema"] == unterthema
    ]

# ============================================================
# PRÜFUNGSRECHNUNG – ERWEITERUNG
# ============================================================

BWH_AUFGABEN.extend([

    {
        "id": "KR007",
        "thema": "Kostenrechnung",
        "unterthema": "Materialgemeinkostenzuschlag",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Die Materialgemeinkosten betragen 11.600 €. "
            "Das Fertigungsmaterial beträgt 58.000 €. "
            "Berechnen Sie den Materialgemeinkostenzuschlagssatz.",
        "gegeben": [
            "Materialgemeinkosten = 11.600 €",
            "Fertigungsmaterial = 58.000 €"
        ],
        "gesucht": "Materialgemeinkostenzuschlagssatz",
        "formel":
            "MGKZ = Materialgemeinkosten / Fertigungsmaterial × 100",
        "tipp":
            "Gemeinkosten durch die Zuschlagsgrundlage teilen und mit 100 multiplizieren.",
        "ergebnis": 20,
        "einheit": "%",
        "loesungsweg": [
            "MGKZ = 11.600 / 58.000 × 100",
            "MGKZ = 20 %"
        ]
    },

    {
        "id": "KR008",
        "thema": "Kostenrechnung",
        "unterthema": "Fertigungsgemeinkostenzuschlag",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Die Fertigungsgemeinkosten betragen 73.500 €. "
            "Die Fertigungslöhne betragen 42.000 €. "
            "Berechnen Sie den Fertigungsgemeinkostenzuschlagssatz.",
        "gegeben": [
            "Fertigungsgemeinkosten = 73.500 €",
            "Fertigungslöhne = 42.000 €"
        ],
        "gesucht": "Fertigungsgemeinkostenzuschlagssatz",
        "formel":
            "FGKZ = Fertigungsgemeinkosten / Fertigungslöhne × 100",
        "tipp":
            "Die Fertigungslöhne bilden hier die Zuschlagsgrundlage.",
        "ergebnis": 175,
        "einheit": "%",
        "loesungsweg": [
            "FGKZ = 73.500 / 42.000 × 100",
            "FGKZ = 175 %"
        ]
    },

    {
        "id": "KR009",
        "thema": "Kostenrechnung",
        "unterthema": "Materialkosten",
        "schwierigkeit": "Mittel",
        "typ": "rechnen",
        "aufgabe":
            "Für einen Auftrag entstehen 58.000 € Fertigungsmaterial. "
            "Der Materialgemeinkostenzuschlag beträgt 20 %. "
            "Berechnen Sie die Materialkosten.",
        "gegeben": [
            "Fertigungsmaterial = 58.000 €",
            "MGKZ = 20 %"
        ],
        "gesucht": "Materialkosten",
        "formel":
            "Materialkosten = Fertigungsmaterial + Materialgemeinkosten",
        "tipp":
            "Berechne zuerst 20 % von 58.000 €.",
        "ergebnis": 69600,
        "einheit": "€",
        "loesungsweg": [
            "Materialgemeinkosten = 58.000 × 0,20",
            "Materialgemeinkosten = 11.600 €",
            "Materialkosten = 58.000 + 11.600",
            "Materialkosten = 69.600 €"
        ]
    },

    {
        "id": "KR010",
        "thema": "Kostenrechnung",
        "unterthema": "Fertigungskosten",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Die Fertigungslöhne betragen 42.000 €. "
            "Der Fertigungsgemeinkostenzuschlag beträgt 175 %. "
            "Zusätzlich entstehen Sondereinzelkosten der Fertigung von 4.900 €. "
            "Berechnen Sie die Fertigungskosten.",
        "gegeben": [
            "Fertigungslöhne = 42.000 €",
            "FGKZ = 175 %",
            "Sondereinzelkosten der Fertigung = 4.900 €"
        ],
        "gesucht": "Fertigungskosten",
        "formel":
            "Fertigungskosten = Fertigungslöhne + Fertigungsgemeinkosten + Sondereinzelkosten der Fertigung",
        "tipp":
            "Zuerst 175 % von 42.000 € berechnen.",
        "ergebnis": 120400,
        "einheit": "€",
        "loesungsweg": [
            "Fertigungsgemeinkosten = 42.000 × 1,75",
            "Fertigungsgemeinkosten = 73.500 €",
            "Fertigungskosten = 42.000 + 73.500 + 4.900",
            "Fertigungskosten = 120.400 €"
        ]
    },

    {
        "id": "MW010",
        "thema": "Materialwirtschaft",
        "unterthema": "Optimale Bestellmenge",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Der Jahresbedarf beträgt 180.000 Stück. "
            "Die Kosten je Bestellung betragen 50 €. "
            "Der Einstandspreis beträgt 1,50 € je Stück. "
            "Der Lagerhaltungskostensatz beträgt 12 %. "
            "Berechnen Sie die optimale Bestellmenge nach Andler.",
        "gegeben": [
            "xges = 180.000 Stück",
            "kB = 50 €/Bestellung",
            "EP = 1,50 €/Stück",
            "i = 12 % = 0,12"
        ],
        "gesucht": "Optimale Bestellmenge xopt",
        "formel":
            "xopt = √((2 × kB × xges) / (EP × i))",
        "tipp":
            "Den Prozentsatz 12 % als 0,12 einsetzen.",
        "ergebnis": 10000,
        "einheit": "Stück",
        "loesungsweg": [
            "xopt = √((2 × 50 × 180.000) / (1,50 × 0,12))",
            "xopt = √100.000.000",
            "xopt = 10.000 Stück"
        ]
    },

    {
        "id": "KR011",
        "thema": "Kostenrechnung",
        "unterthema": "Make-or-buy",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Bei Eigenfertigung entstehen Fixkosten von 16.200 €. "
            "Die variablen Kosten betragen 89 € je Stück. "
            "Der Fremdbezugspreis beträgt 190 € je Stück. "
            "Berechnen Sie die kritische Menge.",
        "gegeben": [
            "Kf = 16.200 €",
            "kv = 89 €/Stück",
            "pF = 190 €/Stück"
        ],
        "gesucht": "Kritische Menge xkr",
        "formel":
            "xkr = Kf / (pF - kv)",
        "tipp":
            "Fixkosten durch die Differenz aus Fremdbezugspreis und variablen Stückkosten teilen.",
        "ergebnis": 160.40,
        "einheit": "Stück",
        "loesungsweg": [
            "xkr = 16.200 / (190 - 89)",
            "xkr = 16.200 / 101",
            "xkr = 160,40 Stück",
            "Praktisch: Ab 161 Stück ist die Eigenfertigung günstiger."
        ]
    },

    {
        "id": "KR012",
        "thema": "Kostenrechnung",
        "unterthema": "Maschinenstundensatz",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Eine Maschine verursacht jährliche Maschinenkosten von 99.600 €. "
            "Die geplante jährliche Einsatzzeit beträgt 3.000 Stunden. "
            "Berechnen Sie den Maschinenstundensatz.",
        "gegeben": [
            "Maschinenkosten = 99.600 €/Jahr",
            "Einsatzzeit = 3.000 h/Jahr"
        ],
        "gesucht": "Maschinenstundensatz",
        "formel":
            "Maschinenstundensatz = Maschinenkosten pro Jahr / Einsatzzeit pro Jahr",
        "tipp":
            "Jährliche Maschinenkosten durch die Maschinenstunden teilen.",
        "ergebnis": 33.20,
        "einheit": "€/h",
        "loesungsweg": [
            "Maschinenstundensatz = 99.600 / 3.000",
            "Maschinenstundensatz = 33,20 €/h"
        ]
    },

    {
        "id": "KR013",
        "thema": "Kostenrechnung",
        "unterthema": "Fertigungskosten mit Maschinenkosten",
        "schwierigkeit": "Schwer",
        "typ": "rechnen",
        "aufgabe":
            "Für ein Bauteil gelten folgende Daten: "
            "Fertigungslohnkostensatz 24 €/h, Bearbeitungszeit 84 Minuten, "
            "Restfertigungsgemeinkostenzuschlag 120 %, "
            "Maschinenstundensatz 40 €/h und "
            "Sondereinzelkosten der Fertigung 4,08 €. "
            "Berechnen Sie die Fertigungskosten pro Stück.",
        "gegeben": [
            "Fertigungslohnkostensatz = 24 €/h",
            "Bearbeitungszeit = 84 min",
            "Rest-FGKZ = 120 %",
            "Maschinenstundensatz = 40 €/h",
            "SEKF = 4,08 €/Stück"
        ],
        "gesucht": "Fertigungskosten pro Stück",
        "formel":
            "Fertigungskosten = Fertigungslohn + Rest-FGK + Maschinenkosten + SEKF",
        "tipp":
            "84 Minuten entsprechen 1,4 Stunden.",
        "ergebnis": 134,
        "einheit": "€/Stück",
        "loesungsweg": [
            "Bearbeitungszeit = 84 / 60 = 1,4 h",
            "Fertigungslohn = 24 × 1,4 = 33,60 €",
            "Rest-FGK = 33,60 × 1,20 = 40,32 €",
            "Maschinenkosten = 40 × 1,4 = 56,00 €",
            "Fertigungskosten = 33,60 + 40,32 + 56,00 + 4,08",
            "Fertigungskosten = 134,00 €/Stück"
        ]
    }

])

# ============================================================
# BWH THEORIETRAINER – VERSION 1.1
# Wissensfragen + offene IHK-Fragen + Anwendung
# ============================================================

BWH_AUFGABEN.extend([

# ============================================================
# UNTERNEHMENSFORMEN
# ============================================================

{
"id":"TH_UF01",
"thema":"Unternehmensformen",
"unterthema":"GmbH",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Wie hoch ist das Mindeststammkapital einer GmbH?",
"antworten":["1 €","10.000 €","25.000 €","50.000 €"],
"richtige_antwort":"25.000 €",
"tipp":"Nicht mit dem Grundkapital der AG verwechseln.",
"erklaerung":"Das Mindeststammkapital der GmbH beträgt 25.000 €."
},

{
"id":"TH_UF02",
"thema":"Unternehmensformen",
"unterthema":"AG",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Wie hoch ist das Mindestgrundkapital einer AG?",
"antworten":["25.000 €","50.000 €","100.000 €","Kein Mindestkapital"],
"richtige_antwort":"50.000 €",
"tipp":"Die AG benötigt mehr Kapital als die GmbH.",
"erklaerung":"Das Mindestgrundkapital der AG beträgt 50.000 €."
},

{
"id":"TH_UF03",
"thema":"Unternehmensformen",
"unterthema":"OHG",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Welche Aussage zur OHG ist richtig?",
"antworten":[
"Sie benötigt 25.000 € Mindestkapital.",
"Alle Gesellschafter sind Vollhafter.",
"Nur der Geschäftsführer haftet.",
"Sie ist eine Kapitalgesellschaft."
],
"richtige_antwort":"Alle Gesellschafter sind Vollhafter.",
"tipp":"Die OHG ist eine Personengesellschaft.",
"erklaerung":"Bei der OHG sind die Gesellschafter Vollhafter."
},

{
"id":"TH_UF04",
"thema":"Unternehmensformen",
"unterthema":"KG",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Wer ist bei einer KG der Vollhafter?",
"antworten":["Kommanditist","Komplementär","Aktionär","Geschäftsführer"],
"richtige_antwort":"Komplementär",
"tipp":"Komplementär = volle Haftung.",
"erklaerung":"Der Komplementär ist Vollhafter. Der Kommanditist ist Teilhafter."
},

{
"id":"TH_UF05",
"thema":"Unternehmensformen",
"unterthema":"KG",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Wer führt grundsätzlich die Geschäfte einer KG und vertritt sie nach außen?",
"antworten":["Kommanditist","Komplementär","Aufsichtsrat","Hauptversammlung"],
"richtige_antwort":"Komplementär",
"tipp":"Der Vollhafter besitzt hier die zentrale Rolle.",
"erklaerung":"Grundsätzlich übernimmt der Komplementär Geschäftsführung und Außenvertretung."
},

{
"id":"TH_UF06",
"thema":"Unternehmensformen",
"unterthema":"AG",
"schwierigkeit":"Mittel",
"typ":"multiple_choice",
"aufgabe":"Welche drei Organe gehören zur AG?",
"antworten":[
"Vorstand, Aufsichtsrat, Hauptversammlung",
"Geschäftsführer, Betriebsrat, Hauptversammlung",
"Vorstand, Geschäftsführer, Komplementär",
"Aufsichtsrat, Kommanditist, Geschäftsführer"
],
"richtige_antwort":"Vorstand, Aufsichtsrat, Hauptversammlung",
"tipp":"Führen – überwachen – Aktionäre.",
"erklaerung":"Die Organe der AG sind Vorstand, Aufsichtsrat und Hauptversammlung."
},

{
"id":"TH_UF07",
"thema":"Unternehmensformen",
"unterthema":"Rechtsformen",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Unterscheiden Sie Personengesellschaften und Kapitalgesellschaften.",
"tipp":"Gehe besonders auf Personenbezug, Kapital und Haftung ein.",
"musterloesung":[
"Bei Personengesellschaften stehen die beteiligten Personen stärker im Vordergrund.",
"OHG und KG sind typische Personengesellschaften.",
"Bei Kapitalgesellschaften steht das Gesellschaftskapital stärker im Vordergrund.",
"GmbH und AG sind typische Kapitalgesellschaften.",
"Bei Kapitalgesellschaften haftet grundsätzlich die Gesellschaft mit ihrem Gesellschaftsvermögen."
]
},

{
"id":"TH_UF08",
"thema":"Unternehmensformen",
"unterthema":"GmbH und AG",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Unterschiede zwischen GmbH und AG.",
"tipp":"Kapital, Geschäftsführung und Organe.",
"musterloesung":[
"GmbH: Mindeststammkapital 25.000 €; AG: Mindestgrundkapital 50.000 €.",
"GmbH wird durch Geschäftsführer geführt und vertreten.",
"AG wird durch den Vorstand geführt und vertreten.",
"Die AG besitzt Vorstand, Aufsichtsrat und Hauptversammlung."
]
},

{
"id":"TH_UF09",
"thema":"Unternehmensformen",
"unterthema":"GmbH & Co. KG",
"schwierigkeit":"Schwer",
"typ":"offen",
"aufgabe":"Erläutern Sie die Besonderheit einer GmbH & Co. KG.",
"tipp":"Wer übernimmt die Rolle des Komplementärs?",
"musterloesung":[
"Die GmbH & Co. KG besitzt grundsätzlich die Struktur einer KG.",
"Eine GmbH übernimmt die Stellung des Komplementärs.",
"Die GmbH führt grundsätzlich als Komplementär die Geschäfte und vertritt die Gesellschaft.",
"Die persönliche Haftung natürlicher Personen kann dadurch begrenzt werden."
]
},

# ============================================================
# ORGANISATION
# ============================================================

{
"id":"TH_OR01",
"thema":"Organisation",
"unterthema":"Aufbauorganisation",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Womit beschäftigt sich die Aufbauorganisation?",
"antworten":[
"Mit der Struktur und Hierarchie des Unternehmens",
"Nur mit Produktionszeiten",
"Nur mit Lagerbeständen",
"Mit der Lohnberechnung"
],
"richtige_antwort":"Mit der Struktur und Hierarchie des Unternehmens",
"tipp":"WER macht WAS?",
"erklaerung":"Die Aufbauorganisation regelt unter anderem Stellen, Abteilungen, Aufgaben, Kompetenzen und Hierarchien."
},

{
"id":"TH_OR02",
"thema":"Organisation",
"unterthema":"Ablauforganisation",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Womit beschäftigt sich die Ablauforganisation?",
"antworten":[
"Mit Arbeits- und Geschäftsprozessen",
"Nur mit Hierarchieebenen",
"Mit Rechtsformen",
"Mit der Kapitalbeschaffung"
],
"richtige_antwort":"Mit Arbeits- und Geschäftsprozessen",
"tipp":"WIE, WANN und WO?",
"erklaerung":"Die Ablauforganisation regelt Arbeitsabläufe sowie deren zeitliches und räumliches Zusammenwirken."
},

{
"id":"TH_OR03",
"thema":"Organisation",
"unterthema":"Organisation",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Erklären Sie den Unterschied zwischen Aufbauorganisation und Ablauforganisation.",
"tipp":"Struktur gegenüber Prozess.",
"musterloesung":[
"Die Aufbauorganisation befasst sich mit Struktur und Hierarchie.",
"Sie bildet Stellen und Abteilungen und ordnet Aufgaben und Kompetenzen zu.",
"Die Ablauforganisation befasst sich mit den Prozessen.",
"Sie regelt insbesondere Reihenfolge, Ort und Zeit der Tätigkeiten."
]
},

{
"id":"TH_OR04",
"thema":"Organisation",
"unterthema":"Dokumentation",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Möglichkeiten zur Dokumentation der Aufbauorganisation.",
"tipp":"Denke an Darstellung von Hierarchie und Stellen.",
"musterloesung":[
"Organigramm",
"Stellenplan",
"Stellenbeschreibung"
]
},

{
"id":"TH_OR05",
"thema":"Organisation",
"unterthema":"Dokumentation",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Möglichkeiten zur Dokumentation der Ablauforganisation.",
"tipp":"Wie können Prozesse dokumentiert werden?",
"musterloesung":[
"Arbeitsanweisung",
"Ablaufdiagramm",
"Softwarehandbuch"
]
},

{
"id":"TH_OR06",
"thema":"Organisation",
"unterthema":"Einliniensystem",
"schwierigkeit":"Mittel",
"typ":"multiple_choice",
"aufgabe":"Was kennzeichnet das Einliniensystem?",
"antworten":[
"Ein Mitarbeiter hat grundsätzlich einen direkten Vorgesetzten.",
"Jeder Mitarbeiter erhält von beliebig vielen Stellen Weisungen.",
"Es existieren keine Hierarchieebenen.",
"Es gibt ausschließlich Projektleiter."
],
"richtige_antwort":"Ein Mitarbeiter hat grundsätzlich einen direkten Vorgesetzten.",
"tipp":"Der Name sagt es bereits: eine Linie.",
"erklaerung":"Beim Einliniensystem bestehen eindeutige Weisungswege."
},

{
"id":"TH_OR07",
"thema":"Organisation",
"unterthema":"Matrixorganisation",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie jeweils zwei Vor- und Nachteile einer Matrixorganisation.",
"tipp":"Spezialwissen gegen Abstimmungsaufwand.",
"musterloesung":[
"Vorteil: Spezialwissen verschiedener Bereiche wird zusammengeführt.",
"Vorteil: unterschiedliche Sichtweisen werden berücksichtigt.",
"Nachteil: hoher Abstimmungsbedarf.",
"Nachteil: Kompetenz- und Weisungskonflikte können entstehen."
]
},

# ============================================================
# FERTIGUNGSORGANISATION
# ============================================================

{
"id":"TH_FO01",
"thema":"Fertigungsorganisation",
"unterthema":"Werkstattfertigung",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Nach welchem Prinzip werden Maschinen bei der Werkstattfertigung angeordnet?",
"antworten":["Verrichtungsprinzip","Flussprinzip","Objektprinzip","Kapitalprinzip"],
"richtige_antwort":"Verrichtungsprinzip",
"tipp":"Gleichartige Tätigkeiten werden zusammengefasst.",
"erklaerung":"Bei der Werkstattfertigung werden gleichartige Betriebsmittel räumlich zusammengefasst."
},

{
"id":"TH_FO02",
"thema":"Fertigungsorganisation",
"unterthema":"Reihenfertigung",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was kennzeichnet die Reihenfertigung?",
"antworten":[
"Arbeitsplätze sind in der Reihenfolge der Arbeitsgänge angeordnet.",
"Alle gleichen Maschinen stehen zusammen.",
"Jedes Produkt wird nur einmal hergestellt.",
"Es gibt keine festgelegte Reihenfolge."
],
"richtige_antwort":"Arbeitsplätze sind in der Reihenfolge der Arbeitsgänge angeordnet.",
"tipp":"Das Werkstück folgt einer festgelegten Reihenfolge.",
"erklaerung":"Die Reihenfertigung folgt dem Flussprinzip, jedoch ohne zwingende Taktbindung."
},

{
"id":"TH_FO03",
"thema":"Fertigungsorganisation",
"unterthema":"Werkstattfertigung",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie jeweils zwei Vor- und Nachteile der Werkstattfertigung.",
"tipp":"Flexibilität gegenüber Transport und Durchlaufzeit.",
"musterloesung":[
"Vorteil: hohe Flexibilität bei wechselnden Produkten.",
"Vorteil: universell einsetzbare Maschinen.",
"Vorteil: Ausweichmöglichkeiten bei Maschinenausfall.",
"Nachteil: längere Transportwege.",
"Nachteil: längere Durchlaufzeiten.",
"Nachteil: höherer Platzbedarf."
]
},

{
"id":"TH_FO04",
"thema":"Fertigungsorganisation",
"unterthema":"Fließfertigung",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie zwei Vorteile und zwei Nachteile der Fließfertigung.",
"tipp":"Hohe Produktivität, aber geringe Flexibilität.",
"musterloesung":[
"Vorteil: kurze Transportwege.",
"Vorteil: kurze Durchlaufzeiten und hohe Produktivität.",
"Nachteil: geringe Flexibilität.",
"Nachteil: Störungen können große Teile des Fertigungsablaufs beeinträchtigen."
]
},

{
"id":"TH_FO05",
"thema":"Fertigungsorganisation",
"unterthema":"Fertigungsarten",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Unterscheiden Sie Einzel-, Serien- und Massenfertigung.",
"tipp":"Entscheidend sind Wiederholung und Stückzahl.",
"musterloesung":[
"Einzelfertigung: einmalige bzw. sehr geringe Stückzahl eines Produkts.",
"Serienfertigung: begrenzte Anzahl gleicher Produkte wird als Serie hergestellt.",
"Massenfertigung: gleichartiges Produkt wird über längere Zeit in sehr großer Menge hergestellt."
]
},

# ============================================================
# MATERIALWIRTSCHAFT
# ============================================================

{
"id":"TH_MW01",
"thema":"Materialwirtschaft",
"unterthema":"Bedarfsarten",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was versteht man unter Primärbedarf?",
"antworten":[
"Bedarf an verkaufsfähigen Endprodukten, Ersatzteilen und Handelswaren",
"Nur Bedarf an Rohstoffen",
"Nur Bedarf an Schmierstoffen",
"Den Sicherheitsbestand"
],
"richtige_antwort":"Bedarf an verkaufsfähigen Endprodukten, Ersatzteilen und Handelswaren",
"tipp":"Primär = Ausgangspunkt der Bedarfsplanung.",
"erklaerung":"Der Primärbedarf umfasst insbesondere den Bedarf an verkaufsfähigen Erzeugnissen."
},

{
"id":"TH_MW02",
"thema":"Materialwirtschaft",
"unterthema":"Bedarfsarten",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Unterscheiden Sie Primär-, Sekundär- und Tertiärbedarf.",
"tipp":"Endprodukt – Bauteile – Hilfs-/Betriebsstoffe.",
"musterloesung":[
"Primärbedarf: Bedarf an verkaufsfähigen Endprodukten, Ersatzteilen und Handelswaren.",
"Sekundärbedarf: Bedarf an Rohstoffen, Einzelteilen und Baugruppen zur Herstellung des Primärbedarfs.",
"Tertiärbedarf: Bedarf an Hilfs- und Betriebsstoffen sowie weiteren Produktionshilfsmitteln."
]
},

{
"id":"TH_MW03",
"thema":"Materialwirtschaft",
"unterthema":"Lager",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie zwei Vorteile und zwei Nachteile eines hohen Lagerbestands.",
"tipp":"Versorgungssicherheit gegenüber Kosten.",
"musterloesung":[
"Vorteil: hohe Liefer- und Produktionsbereitschaft.",
"Vorteil: Schutz vor Lieferverzögerungen.",
"Nachteil: hohe Kapitalbindung.",
"Nachteil: höhere Lagerkosten.",
"Nachteil: Risiko von Schwund, Verderb oder Veralterung."
]
},

{
"id":"TH_MW04",
"thema":"Materialwirtschaft",
"unterthema":"Sicherheitsbestand",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Welchen Hauptzweck hat der Sicherheitsbestand?",
"antworten":[
"Absicherung gegen Verbrauchsschwankungen und Lieferverzögerungen",
"Erhöhung des Verkaufspreises",
"Berechnung des Arbeitslohns",
"Erhöhung der Maschinenleistung"
],
"richtige_antwort":"Absicherung gegen Verbrauchsschwankungen und Lieferverzögerungen",
"tipp":"Er ist eine Reserve.",
"erklaerung":"Der Sicherheitsbestand schützt vor unvorhergesehenen Fehlmengen."
},

{
"id":"TH_MW05",
"thema":"Materialwirtschaft",
"unterthema":"Optimale Bestellmenge",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Erläutern Sie den Zielkonflikt bei der optimalen Bestellmenge.",
"tipp":"Bestellkosten gegen Lagerhaltungskosten.",
"musterloesung":[
"Kleine Bestellmengen führen zu vielen Bestellungen und damit höheren Bestellkosten.",
"Große Bestellmengen führen zu höheren durchschnittlichen Lagerbeständen und damit höheren Lagerhaltungskosten.",
"Die optimale Bestellmenge soll die Summe dieser Kosten minimieren."
]
},

# ============================================================
# ARBEITSENTGELT
# ============================================================

{
"id":"TH_AE01",
"thema":"Arbeitsentgelt",
"unterthema":"Zeitlohn",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Wann eignet sich Zeitlohn besonders?",
"antworten":[
"Wenn Qualität und Sorgfalt wichtiger sind und Leistung schwer messbar ist",
"Nur bei vollautomatischen Maschinen",
"Wenn ausschließlich die Stückzahl zählt",
"Nur bei Serienfertigung"
],
"richtige_antwort":"Wenn Qualität und Sorgfalt wichtiger sind und Leistung schwer messbar ist",
"tipp":"Zeit statt Stückzahl.",
"erklaerung":"Beim Zeitlohn wird die Arbeitszeit vergütet. Er eignet sich daher besonders bei schwer messbarer Leistung."
},

{
"id":"TH_AE02",
"thema":"Arbeitsentgelt",
"unterthema":"Akkordlohn",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Voraussetzungen für die Einführung von Akkordentlohnung.",
"tipp":"Messbarkeit und Beeinflussbarkeit der Leistung.",
"musterloesung":[
"Die Arbeit muss regelmäßig bzw. wiederholbar sein.",
"Die Leistung muss mengenmäßig messbar sein.",
"Der Beschäftigte muss seine Leistung beeinflussen können.",
"Vorgabezeiten bzw. Normalleistungen müssen festgelegt werden können."
]
},

{
"id":"TH_AE03",
"thema":"Arbeitsentgelt",
"unterthema":"Prämienlohn",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Größen, an die eine Prämie gekoppelt werden kann.",
"tipp":"Nicht nur Menge zählt.",
"musterloesung":[
"Menge bzw. Leistung",
"Qualität",
"Materialeinsparung",
"Termineinhaltung",
"Maschinennutzung"
]
},

{
"id":"TH_AE04",
"thema":"Arbeitsentgelt",
"unterthema":"Lohnformen",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie jeweils einen Vorteil und einen Nachteil des Akkordlohns.",
"tipp":"Leistungsanreiz gegenüber Leistungsdruck.",
"musterloesung":[
"Vorteil: hoher Leistungsanreiz.",
"Vorteil: Leistung und Entgelt stehen in engem Zusammenhang.",
"Nachteil: erhöhter Leistungsdruck.",
"Nachteil: Qualität kann zugunsten der Menge leiden."
]
},

# ============================================================
# KAPAZITÄTSWIRTSCHAFT
# ============================================================

{
"id":"TH_KA01",
"thema":"Kapazitätswirtschaft",
"unterthema":"Kapazität",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was versteht man unter betrieblicher Kapazität?",
"antworten":[
"Das Leistungsvermögen innerhalb eines bestimmten Zeitraums",
"Den Verkaufspreis eines Produktes",
"Den Lagerbestand",
"Das Stammkapital"
],
"richtige_antwort":"Das Leistungsvermögen innerhalb eines bestimmten Zeitraums",
"tipp":"Wie viel kann geleistet werden?",
"erklaerung":"Kapazität beschreibt das Leistungsvermögen beispielsweise einer Maschine oder einer Belegschaft."
},

{
"id":"TH_KA02",
"thema":"Kapazitätswirtschaft",
"unterthema":"Kapazitätsengpass",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie vier mögliche Maßnahmen bei einem kurzfristigen Kapazitätsengpass.",
"tipp":"Personal, Arbeitszeit, Fremdvergabe.",
"musterloesung":[
"Überstunden",
"Zusatzschichten",
"Arbeitszeitverlagerung",
"Fremdvergabe",
"Zusätzliche Mitarbeiter",
"Verbesserung der Anlagenverfügbarkeit"
]
},

{
"id":"TH_KA03",
"thema":"Kapazitätswirtschaft",
"unterthema":"Überkapazität",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie drei Maßnahmen bei einer Überkapazität.",
"tipp":"Wenn mehr Kapazität vorhanden ist als benötigt.",
"musterloesung":[
"Abbau von Überstunden",
"Kurzarbeit",
"Personalverlagerung",
"Zusätzliche Aufträge beschaffen",
"Nicht benötigte Betriebsmittel vorübergehend stilllegen"
]
},

# ============================================================
# UNTERNEHMENSZUSAMMENSCHLÜSSE
# ============================================================

{
"id":"TH_UZ01",
"thema":"Unternehmenszusammenschlüsse",
"unterthema":"Kooperation",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was kennzeichnet eine Kooperation?",
"antworten":[
"Unternehmen arbeiten zusammen und bleiben grundsätzlich selbstständig.",
"Alle Unternehmen verlieren zwingend ihre rechtliche Selbstständigkeit.",
"Es wird immer eine AG gegründet.",
"Ein Unternehmen wird zwingend aufgelöst."
],
"richtige_antwort":"Unternehmen arbeiten zusammen und bleiben grundsätzlich selbstständig.",
"tipp":"Zusammenarbeit ohne vollständige Aufgabe der Selbstständigkeit.",
"erklaerung":"Bei einer Kooperation arbeiten Unternehmen zusammen, bleiben aber grundsätzlich selbstständig."
},

{
"id":"TH_UZ02",
"thema":"Unternehmenszusammenschlüsse",
"unterthema":"Konzern",
"schwierigkeit":"Mittel",
"typ":"multiple_choice",
"aufgabe":"Was kennzeichnet einen Konzern?",
"antworten":[
"Rechtlich selbstständige Unternehmen unter einheitlicher Leitung",
"Nur zwei Privatpersonen arbeiten zusammen",
"Alle Unternehmen sind vollständig unabhängig",
"Es handelt sich um eine Lohnform"
],
"richtige_antwort":"Rechtlich selbstständige Unternehmen unter einheitlicher Leitung",
"tipp":"Rechtlich selbstständig – wirtschaftlich verbunden.",
"erklaerung":"Ein Konzern umfasst mehrere rechtlich selbstständige Unternehmen unter einheitlicher Leitung."
},

{
"id":"TH_UZ03",
"thema":"Unternehmenszusammenschlüsse",
"unterthema":"Fusion",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was geschieht bei einer Fusion?",
"antworten":[
"Unternehmen verschmelzen miteinander.",
"Nur die Arbeitszeit wird verändert.",
"Ein Lager wird vergrößert.",
"Unternehmen vereinbaren ausschließlich Liefertermine."
],
"richtige_antwort":"Unternehmen verschmelzen miteinander.",
"tipp":"Verschmelzung.",
"erklaerung":"Bei einer Fusion werden Unternehmen miteinander verschmolzen."
},

{
"id":"TH_UZ04",
"thema":"Unternehmenszusammenschlüsse",
"unterthema":"Joint Venture",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie zwei mögliche Vorteile eines Joint Ventures.",
"tipp":"Risiko, Kapital und Wissen.",
"musterloesung":[
"Risiken können zwischen den Partnern geteilt werden.",
"Kapitalbedarf kann gemeinsam getragen werden.",
"Know-how der Partner kann kombiniert werden.",
"Neue Märkte können leichter erschlossen werden."
]
},

{
"id":"TH_UZ05",
"thema":"Unternehmenszusammenschlüsse",
"unterthema":"Outsourcing",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Nennen Sie zwei Vorteile und zwei Nachteile des Outsourcings.",
"tipp":"Kernkompetenzen gegenüber Abhängigkeit.",
"musterloesung":[
"Vorteil: Konzentration auf Kernkompetenzen.",
"Vorteil: Nutzung externen Spezialwissens.",
"Vorteil: mögliche Kostensenkung.",
"Nachteil: Abhängigkeit vom externen Anbieter.",
"Nachteil: möglicher Know-how-Verlust.",
"Nachteil: Qualitäts- und Terminrisiken."
]
},

# ============================================================
# INVESTITION / KENNZAHLEN
# ============================================================

{
"id":"TH_IR01",
"thema":"Investitionsrechnung",
"unterthema":"Investitionsarten",
"schwierigkeit":"Mittel",
"typ":"offen",
"aufgabe":"Unterscheiden Sie Ersatz-, Erweiterungs- und Rationalisierungsinvestition.",
"tipp":"Ersetzen – vergrößern – wirtschaftlicher machen.",
"musterloesung":[
"Ersatzinvestition: ein vorhandenes Betriebsmittel wird ersetzt.",
"Erweiterungsinvestition: die vorhandene Kapazität wird erhöht.",
"Rationalisierungsinvestition: Abläufe sollen wirtschaftlicher werden bzw. Kosten sinken."
]
},

{
"id":"TH_BK01",
"thema":"Betriebliche Kennzahlen",
"unterthema":"Produktivität",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was beschreibt die Produktivität?",
"antworten":[
"Das mengenmäßige Verhältnis von Output zu Input",
"Die Zahlungsfähigkeit",
"Nur den Gewinn",
"Das Mindestkapital"
],
"richtige_antwort":"Das mengenmäßige Verhältnis von Output zu Input",
"tipp":"Produktivität betrachtet Mengen.",
"erklaerung":"Produktivität = Output / Input."
},

{
"id":"TH_BK02",
"thema":"Betriebliche Kennzahlen",
"unterthema":"Liquidität",
"schwierigkeit":"Leicht",
"typ":"multiple_choice",
"aufgabe":"Was bedeutet Liquidität?",
"antworten":[
"Fähigkeit, fällige Zahlungsverpflichtungen fristgerecht zu erfüllen",
"Anzahl produzierter Teile",
"Höhe des Stammkapitals",
"Anzahl der Mitarbeiter"
],
"richtige_antwort":"Fähigkeit, fällige Zahlungsverpflichtungen fristgerecht zu erfüllen",
"tipp":"Kann das Unternehmen seine Rechnungen bezahlen?",
"erklaerung":"Liquidität bezeichnet die Zahlungsfähigkeit eines Unternehmens."
},

# ============================================================
# GEMISCHTE IHK-ANWENDUNGSFRAGEN
# ============================================================

{
"id":"TH_IHK01",
"thema":"Unternehmensformen",
"unterthema":"Anwendung",
"schwierigkeit":"Schwer",
"typ":"offen",
"aufgabe":"Ein Unternehmen soll als Kapitalgesellschaft gegründet werden. Vergleichen Sie GmbH und AG hinsichtlich Mindestgründungskapital, Geschäftsführung und Außenvertretung.",
"tipp":"25.000 € gegen 50.000 €.",
"musterloesung":[
"GmbH: Mindeststammkapital 25.000 €.",
"GmbH: Geschäftsführung und Außenvertretung durch Geschäftsführer.",
"AG: Mindestgrundkapital 50.000 €.",
"AG: Geschäftsführung und Außenvertretung durch Vorstand."
]
},

{
"id":"TH_IHK02",
"thema":"Organisation",
"unterthema":"Anwendung",
"schwierigkeit":"Schwer",
"typ":"offen",
"aufgabe":"Ein Unternehmen möchte seine Organisation dokumentieren. Nennen Sie jeweils zwei geeignete Dokumentationsformen für Aufbau- und Ablauforganisation und beschreiben Sie kurz deren Informationsgehalt.",
"tipp":"Organigramm/Stellenbeschreibung und Arbeitsanweisung/Ablaufdiagramm.",
"musterloesung":[
"Aufbauorganisation – Organigramm: zeigt Hierarchie, Abteilungen und Stellen.",
"Aufbauorganisation – Stellenbeschreibung: zeigt Aufgaben, Anforderungen und Einordnung einer Stelle.",
"Ablauforganisation – Arbeitsanweisung: beschreibt die Reihenfolge von Arbeitsschritten.",
"Ablauforganisation – Ablaufdiagramm: stellt Prozesse und deren Ablauf grafisch dar."
]
},

{
"id":"TH_IHK03",
"thema":"Fertigungsorganisation",
"unterthema":"Anwendung",
"schwierigkeit":"Schwer",
"typ":"offen",
"aufgabe":"Ein Betrieb fertigt häufig wechselnde Produkte in kleinen Stückzahlen. Begründen Sie, warum eine Werkstattfertigung geeignet sein kann, und nennen Sie zwei Nachteile.",
"tipp":"Flexibilität ist hier entscheidend.",
"musterloesung":[
"Die Werkstattfertigung besitzt eine hohe Flexibilität bei wechselnden Produkten.",
"Universell einsetzbare Maschinen können für unterschiedliche Aufträge genutzt werden.",
"Nachteile sind beispielsweise längere Transportwege.",
"Weiterer Nachteil sind längere Durchlaufzeiten bzw. höherer Platzbedarf."
]
},

{
"id":"TH_IHK04",
"thema":"Arbeitsentgelt",
"unterthema":"Anwendung",
"schwierigkeit":"Schwer",
"typ":"offen",
"aufgabe":"Ein Unternehmen möchte von Zeitlohn auf Akkordlohn umstellen. Erläutern Sie drei Voraussetzungen, die dafür erfüllt sein sollten.",
"tipp":"Die Leistung muss sinnvoll messbar und beeinflussbar sein.",
"musterloesung":[
"Der Arbeitsablauf muss regelmäßig bzw. wiederholbar sein.",
"Die Leistung muss mengenmäßig messbar sein.",
"Der Beschäftigte muss seine Leistung beeinflussen können.",
"Es müssen geeignete Vorgabezeiten bzw. Normalleistungen bestimmt werden können."
]
}

])