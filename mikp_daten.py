MIKP_THEMEN = [
    {"name":"Informations- und Datenmanagement","prioritaet":"🔥 Sehr hoch","beschreibung":"Datenerfassung, Stammdaten/Bewegungsdaten, Datenbanken, ERP, Datenschutz und Datensicherheit."},
    {"name":"Projektmanagement","prioritaet":"🔥 Sehr hoch","beschreibung":"Projektphasen, Ziele, Projektstruktur, Ablauf-, Termin-, Ressourcen-, Informations- und Risikoplanung."},
    {"name":"Netzplantechnik und Ablaufplanung","prioritaet":"🔥 Sehr hoch","beschreibung":"Netzplan, kritischer Pfad, Pufferzeiten, Flussdiagramme und Ablaufdarstellungen."},
    {"name":"Präsentation und Medieneinsatz","prioritaet":"🔥 Sehr hoch","beschreibung":"Präsentationen vorbereiten, Medien auswählen, Visualisierung, Online-Präsentationen und Bewertungskriterien."},
    {"name":"Kommunikation und Moderation","prioritaet":"🔥 Sehr hoch","beschreibung":"Gesprächsführung, aktives Zuhören, Fragetechniken, Konfliktgespräche und Moderation."},
    {"name":"Statistik, Kennzahlen und Diagramme","prioritaet":"🔥 Sehr hoch","beschreibung":"Häufigkeiten, Prozentrechnung, Mittelwerte, Kennzahlen sowie Auswahl, Erstellung und Interpretation von Diagrammen."},
    {"name":"Entscheidungs- und Kreativitätstechniken","prioritaet":"⭐ Hoch","beschreibung":"Brainstorming, schriftliche Ideenfindung, Nutzwertanalyse, paarweiser Vergleich und ABC-Analyse."},
    {"name":"Zeit- und Selbstmanagement","prioritaet":"⭐ Hoch","beschreibung":"Priorisierung, Zeitmanagementmethoden und strukturierte Arbeitsplanung."},
]

MIKP_LERNBEREICHE = {
"Informations- und Datenmanagement": {
    "Stamm- und Bewegungsdaten": {"Stammdaten":"Relativ konstante Grunddaten, z. B. Artikelnummer, Mitarbeiterstammdaten oder Lieferantendaten.","Bewegungsdaten":"Entstehen durch betriebliche Vorgänge, z. B. Auftrag, Buchung, Wareneingang oder Arbeitszeit.","Prüfungstipp":"Begriff erklären und immer ein betriebliches Beispiel nennen."},
    "Datenbanken und ERP": {"Datenbank":"Strukturierte Sammlung von Daten, die gespeichert, gesucht, verknüpft und ausgewertet werden können.","ERP":"Verknüpft betriebliche Bereiche und stellt gemeinsame Daten für Planung und Steuerung bereit.","Auswertungen":["Filtern und Sortieren","Abfragen und Berichte","Kennzahlen und Statistiken"]},
    "Datensicherheit": {"Verfügbarkeit":"Daten und Systeme stehen bei Bedarf zur Verfügung.","Integrität":"Daten sind vollständig, korrekt und vor unbemerkter Veränderung geschützt.","Vertraulichkeit":"Nur berechtigte Personen erhalten Zugriff.","Maßnahmen":["Berechtigungskonzept","Backups","Firewall und Virenschutz","Updates","Verschlüsselung","Redundanz"]},
    "Datenschutz": {"Ziel":"Schutz personenbezogener Daten und der betroffenen Personen.","Organisatorisch":["Zugriffsrechte festlegen","Mitarbeiter schulen","Lösch- und Aufbewahrungsregeln","Vertraulichkeitsverpflichtung"],"Technisch":["Passwörter/MFA","Verschlüsselung","Zugriffsschutz","Protokollierung"]},
},
"Projektmanagement": {
    "Magisches Dreieck": {"Ziele":["Leistung/Qualität","Zeit/Termin","Kosten"],"Zusammenhang":"Ändert sich ein Ziel, beeinflusst das häufig mindestens ein weiteres Ziel."},
    "Projektphasen": {"Typischer Ablauf":["Definition","Planung","Realisierung/Steuerung","Abschluss"],"Merke":"Je nach Modell können Bezeichnungen abweichen; wichtig ist die logische Reihenfolge."},
    "Planungsschritte": {"Strukturplanung":"Projekt in Teilaufgaben und Arbeitspakete zerlegen.","Ablaufplanung":"Abhängigkeiten und Reihenfolge festlegen.","Terminplanung":"Dauern, Termine, Puffer und kritischen Pfad bestimmen.","Ressourcenplanung":"Personal, Technik und Material zuordnen.","Informationsplanung":"Festlegen, wer welche Information wann, wie und von wem erhält."},
    "Risikoanalyse": {"Vorgehen":["Risiken identifizieren","Eintrittswahrscheinlichkeit und Auswirkung bewerten","Risiken priorisieren","Maßnahmen planen und überwachen"],"Mögliche Risiken":["Termin","Kosten","Personal","Technik","Qualität","Lieferkette"]},
    "Lastenheft": {"Bedeutung":"Beschreibt aus Sicht des Auftraggebers, WAS gefordert wird.","Nutzen":"Klare Anforderungen, Vergleichbarkeit von Angeboten und weniger spätere Missverständnisse."},
},
"Netzplantechnik und Ablaufplanung": {
    "Netzplan-Grundlagen": {"FAZ":"Frühester Anfangszeitpunkt","FEZ":"Frühester Endzeitpunkt","SAZ":"Spätester Anfangszeitpunkt","SEZ":"Spätester Endzeitpunkt","GP":"Gesamtpuffer = SAZ − FAZ bzw. SEZ − FEZ"},
    "Kritischer Pfad": {"Definition":"Kette der Vorgänge mit Gesamtpuffer 0.","Bedeutung":"Eine Verzögerung eines kritischen Vorgangs verzögert ohne Gegenmaßnahme das gesamte Projekt."},
    "Vorwärtsrechnung": {"Regel":"FAZ eines Vorgangs = größter FEZ seiner Vorgänger; FEZ = FAZ + Dauer."},
    "Rückwärtsrechnung": {"Regel":"SEZ eines Vorgangs = kleinster SAZ seiner Nachfolger; SAZ = SEZ − Dauer."},
    "Flussdiagramm": {"Symbole":{"Start/Ende":"Oval bzw. abgerundete Form","Tätigkeit":"Rechteck","Entscheidung":"Raute","Fluss":"Pfeil"},"Vorteile":["schneller Überblick","Transparenz","Standardisierung","Fehler und Optimierungspotenziale werden sichtbar"]},
},
"Präsentation und Medieneinsatz": {
    "Vorbereitung": {"Schritte":["Ziel festlegen","Zielgruppe analysieren","Inhalte auswählen und strukturieren","Medien auswählen","Zeit planen","Raum und Technik prüfen","Probe durchführen"]},
    "Aufbau": {"Einstieg":"Interesse wecken, Ziel und Nutzen nennen.","Hauptteil":"Kernaussagen logisch und verständlich vermitteln.","Schluss":"Ergebnisse zusammenfassen, Fragen klären, nächsten Schritt nennen."},
    "Visualisierung": {"Grundsätze":["wenig Text","große lesbare Schrift","einheitliche Gestaltung","passende Diagrammart","Achsen und Einheiten beschriften","Grafiken nur mit Aussage"]},
    "Online-Präsentation": {"Typische Fehler":["Technik nicht testen","zu kleine Schrift","Folien vorlesen","monotone Stimme","keine Aktivierung","Ablenkungen im Hintergrund"]},
},
"Kommunikation und Moderation": {
    "Aktives Zuhören": {"Merkmale":["ausreden lassen","Blickkontakt und zugewandte Haltung","paraphrasieren","offene Rückfragen","Gefühle/Inhalte spiegeln","zusammenfassen"]},
    "Fragetechniken": {"Offene Fragen":"regen ausführliche Antworten an.","Geschlossene Fragen":"ermöglichen kurze, eindeutige Antworten.","Alternativfragen":"bieten Auswahlmöglichkeiten.","Rückfragen":"klären Verständnis und Details."},
    "Konfliktgespräch": {"Grundsätze":["sachlich bleiben","beide Seiten anhören","Ich-Botschaften","konkrete Beobachtungen statt Vorwürfe","gemeinsame Lösung suchen","Vereinbarung festhalten"]},
    "Moderation": {"Phasen":["Vorbereiten","Einsteigen","Thema bearbeiten/Ideen sammeln","Ergebnisse bewerten","Maßnahmen vereinbaren","Nachbereiten"],"Dokumente":["Auftrag","Einladung","Handout","Moderationskarten/Notizen","Protokoll","Ergebnisbericht"]},
},
"Statistik, Kennzahlen und Diagramme": {
    "Prozentuale Veränderung": {"Formel":"(Neuer Wert − Alter Wert) / Alter Wert × 100 %","Deutung":"Positives Ergebnis = Steigerung, negatives Ergebnis = Reduzierung."},
    "Häufigkeiten": {"Absolute Häufigkeit":"Anzahl der Beobachtungen.","Relative Häufigkeit":"Anteil an der Gesamtzahl.","Kumulierte Häufigkeit":"Aufsummierte Häufigkeit bis zu einer Ausprägung."},
    "Diagrammauswahl": {"Säule/Balken":"Kategorien vergleichen.","Linie":"Entwicklung über eine geordnete Zeitachse.","Kreis":"Anteile eines Ganzen bei wenigen Kategorien.","Streuung/Korrelation":"Zusammenhang zweier zahlenmäßiger Merkmale."},
    "Diagrammregeln": {"Checkliste":["aussagekräftiger Titel","Achsen beschriften","Einheiten angeben","sinnvolle Skalierung","Legende bei mehreren Reihen","Werte korrekt übertragen"]},
},
"Entscheidungs- und Kreativitätstechniken": {
    "Brainstorming": {"Regeln":["Kritik während der Sammlung vermeiden","Quantität vor Qualität","Ideen anderer aufgreifen","ungewöhnliche Ideen zulassen","erst danach bewerten"]},
    "Schriftliche Ideenfindung": {"Ablauf":["Problem/Ziel erklären","Teilnehmer schreiben Ideen auf","Ideen weitergeben/ergänzen","Ergebnisse sammeln","strukturieren","bewerten"]},
    "Paarweiser Vergleich": {"Prinzip":"Kriterien werden jeweils paarweise verglichen. Wichtigere Kriterien erhalten mehr Punkte; daraus werden Gewichtungen abgeleitet."},
    "Nutzwertanalyse": {"Ablauf":["Kriterien festlegen","Gewichten","Alternativen bewerten","Bewertung × Gewichtung","Teilnutzwerte addieren","höchsten Gesamtnutzwert beurteilen"]},
    "ABC-Analyse": {"A":"wenige Positionen mit hohem Wertanteil – hohe Aufmerksamkeit.","B":"mittlere Bedeutung.","C":"viele Positionen mit geringem Wertanteil – vereinfachte Steuerung möglich."},
},
"Zeit- und Selbstmanagement": {
    "Eisenhower-Prinzip": {"Wichtig + dringend":"sofort selbst erledigen.","Wichtig + nicht dringend":"terminieren.","Nicht wichtig + dringend":"delegieren, wenn möglich.","Nicht wichtig + nicht dringend":"reduzieren oder streichen."},
    "ALPEN-Methode": {"A":"Aufgaben notieren","L":"Länge/Dauer schätzen","P":"Pufferzeiten reservieren","E":"Entscheidungen über Prioritäten treffen","N":"Nachkontrolle"},
    "Pareto-Prinzip": {"Kernaussage":"Ein relativ kleiner Anteil der Ursachen kann einen großen Anteil der Wirkung erzeugen. Es dient als Denkmodell zur Priorisierung, nicht als starres Naturgesetz."},
}
}
