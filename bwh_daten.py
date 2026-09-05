# ============================================================
# INDUSTRIEMEISTER METALL – BWH
# LERNDATEN VERSION 1.1
# Schwerpunkt: Theorie + IHK-Prüfungswissen
# ============================================================


# ============================================================
# THEMENÜBERSICHT
# ============================================================

BWH_THEMEN = {

    "Kostenrechnung": {
        "prioritaet": "🔴 Sehr hoch",
        "unterthemen": [
            "Kostenarten",
            "Fixe und variable Kosten",
            "Einzel- und Gemeinkosten",
            "Deckungsbeitrag",
            "Break-even",
            "BAB",
            "Zuschlagskalkulation",
            "Maschinenstundensatz",
            "Make-or-buy"
        ]
    },

    "Materialwirtschaft": {
        "prioritaet": "🔴 Sehr hoch",
        "unterthemen": [
            "Aufgaben der Materialwirtschaft",
            "Bedarfsarten",
            "Beschaffung",
            "Lagerhaltung",
            "Sicherheitsbestand",
            "Meldebestand",
            "Lagerkennzahlen",
            "Optimale Bestellmenge"
        ]
    },

    "Arbeitsentgelt": {
        "prioritaet": "🔴 Sehr hoch",
        "unterthemen": [
            "Zeitlohn",
            "Akkordlohn",
            "Prämienlohn",
            "Normalleistung",
            "Leistungsgrad",
            "Zeitgrad",
            "Voraussetzungen für Akkord"
        ]
    },

    "Unternehmensformen": {
        "prioritaet": "🔴 Sehr hoch",
        "unterthemen": [
            "Personengesellschaften",
            "Kapitalgesellschaften",
            "OHG",
            "KG",
            "GmbH",
            "AG",
            "UG",
            "GmbH & Co. KG",
            "Haftung",
            "Geschäftsführung",
            "Mindestkapital"
        ]
    },

    "Organisation": {
        "prioritaet": "🔴 Sehr hoch",
        "unterthemen": [
            "Aufbauorganisation",
            "Ablauforganisation",
            "Stelle und Abteilung",
            "Organigramm",
            "Stellenbeschreibung",
            "Einliniensystem",
            "Mehrliniensystem",
            "Stabliniensystem",
            "Matrixorganisation"
        ]
    },

    "Fertigungsorganisation": {
        "prioritaet": "🟠 Hoch",
        "unterthemen": [
            "Werkstattfertigung",
            "Reihenfertigung",
            "Fließfertigung",
            "Gruppenfertigung",
            "Einzelfertigung",
            "Serienfertigung",
            "Massenfertigung"
        ]
    },

    "Kapazitätswirtschaft": {
        "prioritaet": "🟠 Hoch",
        "unterthemen": [
            "Kapazität",
            "Kapazitätsauslastung",
            "Kapazitätsengpass",
            "Überkapazität",
            "Personelle Maßnahmen",
            "Technische Maßnahmen"
        ]
    },

    "Unternehmenszusammenschlüsse": {
        "prioritaet": "🟠 Hoch",
        "unterthemen": [
            "Kooperation",
            "Konzentration",
            "Kartell",
            "Konzern",
            "Fusion",
            "Joint Venture",
            "Outsourcing"
        ]
    },

    "Investitionsrechnung": {
        "prioritaet": "🟡 Mittel",
        "unterthemen": [
            "Investition",
            "Investitionsgründe",
            "Kostenvergleich",
            "Gewinnvergleich",
            "Rentabilität",
            "Amortisation"
        ]
    },

    "Betriebliche Kennzahlen": {
        "prioritaet": "🟡 Mittel",
        "unterthemen": [
            "Produktivität",
            "Wirtschaftlichkeit",
            "Rentabilität",
            "Liquidität"
        ]
    }
}


# ============================================================
# KOSTENRECHNUNG
# ============================================================

KOSTENRECHNUNG_ZEICHEN = {
    "Kf": "Fixkosten",
    "kv": "variable Stückkosten",
    "Kv": "variable Gesamtkosten",
    "K": "Gesamtkosten",
    "p": "Preis je Stück",
    "x": "Absatz- bzw. Produktionsmenge",
    "db": "Stückdeckungsbeitrag",
    "DB": "Gesamtdeckungsbeitrag",
    "BE": "Betriebsergebnis"
}


KOSTENRECHNUNG_FORMELN = {

    "Variable Gesamtkosten": {
        "formel": "Kv = kv × x",
        "erklaerung": "Variable Stückkosten multipliziert mit der Menge."
    },

    "Gesamtkosten": {
        "formel": "K = Kf + Kv",
        "erklaerung": "Fixkosten und variable Gesamtkosten ergeben die Gesamtkosten."
    },

    "Stückdeckungsbeitrag": {
        "formel": "db = p - kv",
        "erklaerung": "Der Stückdeckungsbeitrag trägt zur Deckung der Fixkosten bei."
    },

    "Gesamtdeckungsbeitrag": {
        "formel": "DB = db × x",
        "erklaerung": "Stückdeckungsbeitrag multipliziert mit der Absatzmenge."
    },

    "Betriebsergebnis": {
        "formel": "BE = DB - Kf",
        "erklaerung": "Positiv = Gewinn, negativ = Verlust."
    },

    "Break-even-Menge": {
        "formel": "xBEP = Kf / db",
        "erklaerung": "Absatzmenge, bei der weder Gewinn noch Verlust entsteht."
    },

    "Break-even-Umsatz": {
        "formel": "UBEP = p × xBEP",
        "erklaerung": "Umsatz an der Gewinnschwelle."
    }
}


# ============================================================
# MATERIALWIRTSCHAFT – FORMELN
# ============================================================

MATERIALWIRTSCHAFT_ZEICHEN = {
    "xges": "Gesamtbedarf",
    "xopt": "optimale Bestellmenge",
    "nopt": "optimale Anzahl der Bestellungen"
}


MATERIALWIRTSCHAFT_FORMELN = {

    "Sekundärbedarf": {
        "formel": "Sekundärbedarf = Primärbedarf × Stücklistenmenge",
        "erklaerung": "Bedarf an Rohstoffen, Bauteilen und Baugruppen."
    },

    "Nettobedarf": {
        "formel": "Nettobedarf = Bruttobedarf + Zusatzbedarf - Lagerbestand - offene Bestellungen",
        "erklaerung": "Tatsächlich noch zu beschaffende Menge."
    },

    "Meldebestand": {
        "formel": "Meldebestand = Verbrauch pro Zeiteinheit × Wiederbeschaffungszeit + Sicherheitsbestand",
        "erklaerung": "Bei Erreichen des Meldebestands wird eine Bestellung ausgelöst."
    },

    "Durchschnittlicher Lagerbestand": {
        "formel": "Ø Lagerbestand = (Anfangsbestand + Endbestand) / 2",
        "erklaerung": "Vereinfachte Berechnung."
    },

    "Lagerumschlag": {
        "formel": "Lagerumschlag = Verbrauch pro Jahr / Ø Lagerbestand",
        "erklaerung": "Zeigt, wie oft sich der durchschnittliche Lagerbestand pro Jahr erneuert."
    },

    "Durchschnittliche Lagerdauer": {
        "formel": "Ø Lagerdauer = 360 / Lagerumschlag",
        "erklaerung": "Durchschnittliche Verweildauer des Materials im Lager."
    },

    "Lagerreichweite": {
        "formel": "Ø Lagerreichweite = Ø Lagerbestand / Ø Verbrauch pro Tag",
        "erklaerung": "Zeigt, wie viele Tage der Bestand durchschnittlich reicht."
    },

    "Optimale Bestellanzahl": {
        "formel": "nopt = xges / xopt",
        "erklaerung": "Gesamtbedarf geteilt durch optimale Bestellmenge."
    }
}


# ============================================================
# MATERIALWIRTSCHAFT – THEORIE
# ============================================================

MATERIALWIRTSCHAFT_LERNEN = {

    "Aufgabe der Materialwirtschaft": {
        "Definition":
            "Die Materialwirtschaft stellt sicher, dass die benötigten Materialien "
            "in richtiger Art, Menge und Qualität, zum richtigen Zeitpunkt, "
            "am richtigen Ort und möglichst wirtschaftlich zur Verfügung stehen.",

        "Ziele":
            "Hohe Lieferbereitschaft, geringe Beschaffungskosten, geringe Lagerbestände, "
            "geringe Kapitalbindung und Sicherstellung der Produktion.",

        "Merken":
            "Zu wenig Material gefährdet die Produktion – zu viel Material verursacht Lager- und Kapitalbindungskosten."
    },

    "Primärbedarf": {
        "Definition":
            "Bedarf an verkaufsfähigen Endprodukten, Ersatzteilen und Handelswaren.",

        "Beispiel":
            "Ein Unternehmen plant die Produktion von 1.000 Getrieben. "
            "Die 1.000 Getriebe gehören zum Primärbedarf."
    },

    "Sekundärbedarf": {
        "Definition":
            "Bedarf an Rohstoffen, Einzelteilen und Baugruppen, die zur Herstellung des Primärbedarfs benötigt werden.",

        "Beispiel":
            "Für jedes Getriebe werden vier Zahnräder benötigt. Die Zahnräder gehören zum Sekundärbedarf."
    },

    "Tertiärbedarf": {
        "Definition":
            "Bedarf an Hilfs- und Betriebsstoffen sowie Verschleißwerkzeugen, "
            "die für die Produktion benötigt werden.",

        "Beispiele":
            "Schmierstoffe, Reinigungsmittel oder Hilfsstoffe."
    },

    "Bruttobedarf und Nettobedarf": {
        "Bruttobedarf":
            "Gesamter Materialbedarf für einen bestimmten Zeitraum.",

        "Nettobedarf":
            "Der nach Berücksichtigung vorhandener Bestände und erwarteter Zugänge tatsächlich zu beschaffende Bedarf.",

        "Merken":
            "Brutto = gesamter Bedarf. Netto = was tatsächlich noch beschafft werden muss."
    },

    "Sicherheitsbestand": {
        "Definition":
            "Reservebestand, der unvorhergesehene Verbrauchsschwankungen oder Lieferverzögerungen absichern soll.",

        "Folge eines hohen Sicherheitsbestands":
            "Höhere Lieferbereitschaft, aber gleichzeitig höhere Lager- und Kapitalbindungskosten."
    },

    "Meldebestand": {
        "Definition":
            "Bestandsmenge, bei deren Erreichen eine neue Bestellung ausgelöst werden muss.",

        "Merken":
            "Der Meldebestand berücksichtigt den Verbrauch während der Wiederbeschaffungszeit und den Sicherheitsbestand."
    },

    "Hohe Lagerbestände": {
        "Vorteile":
            "Hohe Lieferbereitschaft, geringeres Risiko von Produktionsstillständen, größere Unabhängigkeit von Lieferverzögerungen.",

        "Nachteile":
            "Hohe Kapitalbindung, Lagerkosten, Platzbedarf, Schwund-, Verderb- und Veralterungsrisiko."
    },

    "Niedrige Lagerbestände": {
        "Vorteile":
            "Geringere Kapitalbindung und geringere Lagerkosten.",

        "Nachteile":
            "Höheres Risiko von Fehlmengen und Produktionsunterbrechungen."
    },

    "Optimale Bestellmenge": {
        "Ziel":
            "Gesamtkosten aus Bestellkosten und Lagerhaltungskosten minimieren.",

        "Zusammenhang":
            "Große Bestellmengen senken die Anzahl der Bestellungen, erhöhen aber den durchschnittlichen Lagerbestand.",

        "Merken":
            "Kleine Bestellmenge = hohe Bestellkosten. Große Bestellmenge = hohe Lagerhaltungskosten."
    }
}


# ============================================================
# ARBEITSENTGELT – FORMELN
# ============================================================

ARBEITSENTGELT_FORMELN = {

    "Zeitlohn": {
        "formel": "Zeitlohn = Stundensatz × Anzahl der geleisteten Stunden",
        "erklaerung": "Entlohnung nach Arbeitszeit."
    },

    "Zeitgradfaktor": {
        "formel": "Zeitgradfaktor = Zeitgrad / 100",
        "erklaerung": "Umrechnung des Zeitgrades in einen Faktor."
    },

    "Akkordlohn pro Stunde": {
        "formel": "Akkordlohn pro Stunde = Akkordrichtsatz × Zeitgradfaktor",
        "erklaerung": "Entgelt steigt proportional zur Leistung."
    },

    "Akkordrichtsatz": {
        "formel": "Akkordrichtsatz = Akkordgrundlohn + Akkordzuschlag",
        "erklaerung": "Entgelt bei Normalleistung."
    },

    "Minutenfaktor": {
        "formel": "Minutenfaktor = Akkordrichtsatz / 60",
        "erklaerung": "Akkordrichtsatz je Minute."
    },

    "Stückgeld": {
        "formel": "Stückgeld = Akkordrichtsatz / Normalleistung",
        "erklaerung": "Entgelt je hergestelltem Stück."
    },

    "Vorgabezeit": {
        "formel": "Vorgabezeit = 60 / Normalleistung",
        "erklaerung": "Vorgabezeit je Stück."
    },

    "Prämienlohn": {
        "formel": "Prämienlohn = Grundlohn + Prämie",
        "erklaerung": "Grundentgelt plus zusätzliche leistungsabhängige Prämie."
    }
}


# ============================================================
# ARBEITSENTGELT – THEORIE
# ============================================================

ARBEITSENTGELT_LERNEN = {

    "Zeitlohn": {
        "Definition":
            "Beim Zeitlohn richtet sich das Entgelt hauptsächlich nach der geleisteten Arbeitszeit.",

        "Geeignet":
            "Wenn Leistung schwer messbar ist oder Qualität und Sorgfalt wichtiger als eine hohe Stückzahl sind.",

        "Vorteile Arbeitnehmer":
            "Planbares Einkommen und geringerer Leistungsdruck.",

        "Nachteile Unternehmen":
            "Geringerer direkter Leistungsanreiz.",

        "Typische Bereiche":
            "Wartung, Instandhaltung, Kontroll- oder Überwachungstätigkeiten."
    },

    "Akkordlohn": {
        "Definition":
            "Leistungsabhängige Entgeltform. Eine höhere Leistung führt grundsätzlich zu einem höheren Entgelt.",

        "Vorteile":
            "Hoher Leistungsanreiz und gute Zuordnung zwischen Leistung und Entgelt.",

        "Nachteile":
            "Leistungsdruck, mögliche Qualitätsprobleme und höhere körperliche Belastung.",

        "Merken":
            "Akkord eignet sich besonders für regelmäßig wiederkehrende und mengenmäßig messbare Arbeiten."
    },

    "Voraussetzungen für Akkordarbeit": {
        "Voraussetzungen":
            "Arbeitsablauf muss wiederholbar sein; Leistung muss messbar sein; "
            "Arbeitsablauf muss vom Beschäftigten beeinflussbar sein; "
            "Vorgabezeiten müssen nachvollziehbar sein.",

        "Mitbestimmung":
            "Bei der Einführung der Akkordentlohnung ist die Beteiligung des Betriebsrats zu beachten."
    },

    "Normalleistung": {
        "Definition":
            "Leistung, die von einem geeigneten und eingearbeiteten Beschäftigten bei normaler Anstrengung dauerhaft erreicht werden kann.",

        "Merken":
            "Normalleistung entspricht grundsätzlich 100 %."
    },

    "Prämienlohn": {
        "Definition":
            "Grundlohn plus zusätzliche Prämie für bestimmte messbare Leistungen.",

        "Prämien können sich beziehen auf":
            "Menge, Qualität, Materialeinsparung, Termineinhaltung oder Maschinennutzung.",

        "Vorteil":
            "Nicht nur die produzierte Menge kann belohnt werden."
    }
}


# ============================================================
# UNTERNEHMENSFORMEN – AUSFÜHRLICH
# ============================================================

UNTERNEHMENSFORMEN_LERNEN = {

    "Grundentscheidung Rechtsform": {
        "Wichtige Kriterien":
            "Haftung, Kapitalbedarf, Mindestgründungskapital, Geschäftsführung, "
            "Außenvertretung, Finanzierungsmöglichkeiten und Mitspracherechte.",

        "Prüfungsmerker":
            "Bei einem Rechtsformenvergleich immer systematisch dieselben Kriterien gegenüberstellen."
    },

    "Personengesellschaften": {
        "Definition":
            "Bei Personengesellschaften stehen die beteiligten Personen und ihre persönliche Zusammenarbeit im Vordergrund.",

        "Typische Formen":
            "OHG und KG.",

        "Mindestgründungskapital":
            "Für OHG und KG besteht keine gesetzliche Vorgabe für ein Mindestgründungskapital.",

        "Haftung":
            "Je nach Rechtsform können Gesellschafter persönlich und unbeschränkt haften.",

        "Prüfungsmerker":
            "Personengesellschaft = Personen und persönliche Haftung spielen eine besonders wichtige Rolle."
    },

    "Kapitalgesellschaften": {
        "Definition":
            "Bei Kapitalgesellschaften steht das Gesellschaftskapital stärker im Vordergrund.",

        "Typische Formen":
            "GmbH, AG und UG (haftungsbeschränkt).",

        "Haftung":
            "Die Gesellschaft haftet grundsätzlich mit ihrem Gesellschaftsvermögen.",

        "Prüfungsmerker":
            "Kapitalgesellschaften besitzen vorgeschriebene Kapital- und Organisationsstrukturen."
    },

    "OHG – Offene Handelsgesellschaft": {
        "Art":
            "Personengesellschaft.",

        "Mindestgründungskapital":
            "Keine gesetzliche Mindestkapitalvorgabe.",

        "Geschäftsführung":
            "Grundsätzlich sind die Gesellschafter zur Geschäftsführung berechtigt.",

        "Außenvertretung":
            "Grundsätzlich durch die Gesellschafter.",

        "Haftung":
            "Die Gesellschafter sind Vollhafter.",

        "Bedeutung Vollhafter":
            "Persönliche und grundsätzlich unbeschränkte Haftung.",

        "Prüfungsmerker":
            "OHG: Alle Gesellschafter sind Vollhafter."
    },

    "KG – Kommanditgesellschaft": {
        "Art":
            "Personengesellschaft.",

        "Mindestgründungskapital":
            "Keine gesetzliche Mindestkapitalvorgabe.",

        "Gesellschafter":
            "Komplementär und Kommanditist.",

        "Komplementär":
            "Vollhafter. Führt grundsätzlich die Geschäfte und vertritt die KG nach außen.",

        "Kommanditist":
            "Teilhafter; seine Haftung ist auf seine Einlage begrenzt.",

        "Prüfungsmerker":
            "KG = mindestens ein Vollhafter (Komplementär) und mindestens ein Teilhafter (Kommanditist)."
    },

    "GmbH – Gesellschaft mit beschränkter Haftung": {
        "Art":
            "Kapitalgesellschaft.",

        "Mindeststammkapital":
            "25.000 €.",

        "Geschäftsführung":
            "Geschäftsführer.",

        "Außenvertretung":
            "Geschäftsführer.",

        "Haftung":
            "Die Gesellschaft haftet mit dem Gesellschaftsvermögen.",

        "Stimmrecht":
            "Grundsätzlich nach Anteil am Stammkapital.",

        "Prüfungsmerker":
            "GmbH = 25.000 € Stammkapital + Geschäftsführer."
    },

    "AG – Aktiengesellschaft": {
        "Art":
            "Kapitalgesellschaft.",

        "Mindestgrundkapital":
            "50.000 €.",

        "Geschäftsführung":
            "Vorstand.",

        "Außenvertretung":
            "Vorstand.",

        "Organe":
            "Vorstand, Aufsichtsrat und Hauptversammlung.",

        "Stimmrecht":
            "Grundsätzlich nach Anteil am Grundkapital.",

        "Haftung":
            "Die AG haftet mit dem Gesellschaftsvermögen.",

        "Prüfungsmerker":
            "AG = 50.000 € Grundkapital; Vorstand führt, Aufsichtsrat überwacht, Hauptversammlung vertritt die Aktionäre."
    },

    "UG (haftungsbeschränkt)": {
        "Art":
            "Kapitalgesellschaft.",

        "Mindestgründungskapital":
            "In den vorliegenden IHK-Lösungshinweisen: 1 € je Gesellschafter.",

        "Geschäftsführung":
            "Geschäftsführer.",

        "Haftung":
            "Haftungsbeschränkung auf das Gesellschaftsvermögen.",

        "Merken":
            "Nicht mit der klassischen GmbH und deren 25.000 € Stammkapital verwechseln."
    },

    "GmbH & Co. KG": {
        "Grundidee":
            "Sonderform der KG, bei der eine GmbH die Stellung des Komplementärs übernimmt.",

        "Vorteil":
            "Die persönliche Haftung natürlicher Personen kann dadurch begrenzt werden.",

        "Geschäftsführung":
            "Grundsätzlich führt die GmbH als Komplementär die Geschäfte und vertritt die GmbH & Co. KG.",

        "Prüfungsmerker":
            "KG-Struktur + GmbH als Komplementär."
    },

    "OHG vs. KG": {
        "OHG":
            "Alle Gesellschafter sind Vollhafter.",

        "KG":
            "Komplementär = Vollhafter; Kommanditist = Teilhafter.",

        "Gemeinsamkeit":
            "Beide zählen zu den Personengesellschaften und besitzen keine gesetzliche Mindestkapitalvorgabe."
    },

    "GmbH vs. AG": {
        "GmbH":
            "25.000 € Mindeststammkapital; Geschäftsführung durch Geschäftsführer.",

        "AG":
            "50.000 € Mindestgrundkapital; Geschäftsführung durch Vorstand.",

        "AG-Organe":
            "Vorstand, Aufsichtsrat, Hauptversammlung.",

        "Prüfungsmerker":
            "Diese Unterschiede unbedingt auswendig können."
    }
}


# ============================================================
# ORGANISATION – AUSFÜHRLICH
# ============================================================

ORGANISATION_LERNEN = {

    "Aufbauorganisation": {
        "Definition":
            "Regelt die Struktur und Hierarchie des Unternehmens.",

        "Inhalt":
            "Bildung von Stellen und Abteilungen sowie Zuordnung von Aufgaben, Kompetenzen und Verantwortlichkeiten.",

        "Frage":
            "WER macht WAS?",

        "Dokumentation":
            "Organigramm, Stellenplan, Stellenbeschreibung.",

        "Merken":
            "Aufbauorganisation = Struktur des Unternehmens."
    },

    "Ablauforganisation": {
        "Definition":
            "Regelt die Arbeits- und Geschäftsprozesse.",

        "Inhalt":
            "Reihenfolge, Zeit, Ort und Zusammenwirken von Menschen, Betriebsmitteln und Arbeitsgegenständen.",

        "Frage":
            "WIE, WANN und WO wird eine Aufgabe erledigt?",

        "Dokumentation":
            "Arbeitsanweisung, Ablaufdiagramm oder Softwarehandbuch.",

        "Merken":
            "Ablauforganisation = Prozesse des Unternehmens."
    },

    "Organigramm": {
        "Definition":
            "Grafische Darstellung der Aufbauorganisation.",

        "Zeigt":
            "Hierarchie, Abteilungen, Instanzen, Stabsstellen und ausführende Stellen."
    },

    "Stellenplan": {
        "Definition":
            "Übersicht über die im Unternehmen vorhandenen bzw. vorgesehenen Stellen.",

        "Nutzen":
            "Zeigt, welche Stellen zur Verfügung stehen."
    },

    "Stellenbeschreibung": {
        "Definition":
            "Beschreibung einer konkreten Stelle innerhalb der Organisation.",

        "Typische Inhalte":
            "Aufgaben, Kompetenzen, Verantwortung, Anforderungen sowie organisatorische Einordnung.",

        "Merken":
            "Stellenbeschreibung beschreibt die Stelle – nicht die konkrete Person."
    },

    "Einliniensystem": {
        "Prinzip":
            "Jeder Mitarbeiter erhält Weisungen grundsätzlich von genau einer übergeordneten Stelle.",

        "Vorteile":
            "Klare Zuständigkeiten und eindeutige Weisungswege.",

        "Nachteile":
            "Lange Informations- und Entscheidungswege; starke Belastung der Vorgesetzten.",

        "Merken":
            "Ein Mitarbeiter – ein direkter Vorgesetzter."
    },

    "Mehrliniensystem": {
        "Prinzip":
            "Ein Mitarbeiter kann Weisungen von mehreren spezialisierten Vorgesetzten erhalten.",

        "Vorteile":
            "Kurze Wege und Nutzung von Spezialwissen.",

        "Nachteile":
            "Kompetenzüberschneidungen und widersprüchliche Anweisungen möglich."
    },

    "Stabliniensystem": {
        "Prinzip":
            "Einliniensystem wird durch beratende Stabsstellen ergänzt.",

        "Stab":
            "Unterstützt und berät eine Instanz.",

        "Vorteil":
            "Entlastung der Leitung und Nutzung von Expertenwissen.",

        "Problem":
            "Konflikte zwischen Linie und Stab sind möglich."
    },

    "Matrixorganisation": {
        "Prinzip":
            "Überlagerung von zwei Organisationsdimensionen, beispielsweise Funktionen und Produkte.",

        "Beispiel":
            "Produktmanager und Funktionsmanager wirken gemeinsam an Entscheidungen mit.",

        "Vorteile":
            "Spezialwissen verschiedener Bereiche wird zusammengeführt.",

        "Nachteile":
            "Hoher Abstimmungsbedarf und mögliche Kompetenzkonflikte.",

        "Merken":
            "Matrix = zwei sich überschneidende Weisungs-/Entscheidungsdimensionen."
    }
}


# ============================================================
# FERTIGUNGSORGANISATION
# ============================================================

FERTIGUNGSORGANISATION_LERNEN = {

    "Werkstattfertigung": {
        "Prinzip":
            "Gleichartige Maschinen und Arbeitsplätze werden räumlich zusammengefasst.",

        "Organisationsprinzip":
            "Verrichtungsprinzip.",

        "Vorteile":
            "Hohe Flexibilität, universell einsetzbare Maschinen und Ausweichmöglichkeiten bei Maschinenausfall.",

        "Nachteile":
            "Längere Transportwege, längere Durchlaufzeiten, höherer Platzbedarf und teilweise schlechtere Kapazitätsauslastung.",

        "Geeignet":
            "Besonders bei wechselnden Produkten und kleineren Stückzahlen.",

        "Merken":
            "Werkstattfertigung = Maschinen nach gleicher Tätigkeit gruppiert."
    },

    "Reihenfertigung": {
        "Prinzip":
            "Betriebsmittel werden in der Reihenfolge der notwendigen Arbeitsschritte angeordnet.",

        "Organisationsprinzip":
            "Flussprinzip.",

        "Kennzeichen":
            "Keine zwingende Taktbindung.",

        "Vorteil":
            "Kürzere Transportwege als bei der Werkstattfertigung.",

        "Merken":
            "Reihenfolge stimmt mit dem Fertigungsablauf überein."
    },

    "Fließfertigung": {
        "Prinzip":
            "Arbeitsplätze sind entsprechend dem Arbeitsablauf angeordnet und die Arbeitsgänge sind zeitlich aufeinander abgestimmt.",

        "Vorteile":
            "Kurze Transportwege, kurze Durchlaufzeiten und hohe Produktivität.",

        "Nachteile":
            "Geringe Flexibilität, hohe Störanfälligkeit der gesamten Linie und häufig hohe Investitionen.",

        "Geeignet":
            "Große Stückzahlen und standardisierte Produkte."
    },

    "Gruppenfertigung": {
        "Prinzip":
            "Maschinen unterschiedlicher Art werden für eine bestimmte Teile- oder Produktgruppe zusammengefasst.",

        "Ziel":
            "Vorteile von Werkstatt- und Flussfertigung miteinander verbinden."
    },

    "Einzelfertigung": {
        "Definition":
            "Ein Produkt wird einmalig oder in sehr geringer Stückzahl hergestellt.",

        "Beispiele":
            "Sondermaschine oder individuell geplante Anlage.",

        "Kennzeichen":
            "Hohe Individualität und meist hoher Planungsaufwand."
    },

    "Serienfertigung": {
        "Definition":
            "Eine begrenzte Stückzahl gleicher Produkte wird wiederholt hergestellt.",

        "Beispiel":
            "Eine Serie von 5.000 gleichen Bauteilen."
    },

    "Massenfertigung": {
        "Definition":
            "Ein gleichartiges Produkt wird über einen langen Zeitraum in sehr großer Menge hergestellt.",

        "Vorteil":
            "Hohe Spezialisierung und niedrige Stückkosten möglich.",

        "Nachteil":
            "Geringe Flexibilität."
    }
}


# ============================================================
# KAPAZITÄTSWIRTSCHAFT
# ============================================================

KAPAZITAETSWIRTSCHAFT_LERNEN = {

    "Kapazität": {
        "Definition":
            "Leistungsvermögen eines Betriebsmittels, Mitarbeiters oder Betriebes innerhalb eines bestimmten Zeitraums.",

        "Beispiele":
            "Maschinenstunden, Mitarbeiterstunden oder Stück pro Schicht."
    },

    "Kapazitätsauslastung": {
        "Definition":
            "Verhältnis der tatsächlich genutzten Kapazität zur verfügbaren Kapazität.",

        "formel":
            "Kapazitätsauslastung = Ist-Beschäftigung / verfügbare Kapazität × 100"
    },

    "Kapazitätsengpass": {
        "Definition":
            "Die benötigte Leistung ist größer als die vorhandene Kapazität.",

        "Mögliche Maßnahmen":
            "Überstunden, Zusatzschichten, Fremdvergabe, zusätzliche Mitarbeiter, zusätzliche Maschinen oder organisatorische Verbesserungen."
    },

    "Überkapazität": {
        "Definition":
            "Vorhandene Kapazität wird nicht vollständig benötigt.",

        "Mögliche Maßnahmen":
            "Kurzarbeit, Abbau von Überstunden, Personalverlagerung, zusätzliche Aufträge oder Stilllegung nicht benötigter Betriebsmittel."
    },

    "Personelle Kapazitätsanpassung": {
        "Kurzfristig":
            "Überstunden, Zusatzschichten oder Arbeitszeitverlagerung.",

        "Langfristig":
            "Neueinstellungen, Qualifizierung oder Personalabbau."
    },

    "Technische Kapazitätsanpassung": {
        "Möglichkeiten":
            "Zusätzliche Maschinen, Automatisierung, Modernisierung, Fremdvergabe oder Verbesserung der Anlagenverfügbarkeit."
    }
}


# ============================================================
# UNTERNEHMENSZUSAMMENSCHLÜSSE
# ============================================================

UNTERNEHMENSZUSAMMENSCHLUESSE_LERNEN = {

    "Warum Unternehmen zusammenarbeiten": {
        "Ziele":
            "Kosten senken, Marktposition verbessern, Know-how nutzen, Risiken teilen, neue Märkte erschließen oder Beschaffung und Absatz sichern."
    },

    "Kooperation": {
        "Definition":
            "Zusammenarbeit rechtlich und grundsätzlich wirtschaftlich selbstständiger Unternehmen.",

        "Merken":
            "Unternehmen arbeiten zusammen, bleiben aber selbstständig."
    },

    "Konzentration": {
        "Definition":
            "Unternehmen verlieren einen Teil oder ihre gesamte wirtschaftliche bzw. rechtliche Selbstständigkeit.",

        "Merken":
            "Stärkere Bindung als bei einer Kooperation."
    },

    "Kartell": {
        "Grundidee":
            "Unternehmen stimmen bestimmte wirtschaftliche Verhaltensweisen miteinander ab.",

        "Wichtig":
            "Kartelle können den Wettbewerb beschränken und unterliegen deshalb wettbewerbsrechtlichen Grenzen."
    },

    "Konzern": {
        "Definition":
            "Mehrere rechtlich selbstständige Unternehmen werden unter einer einheitlichen Leitung zusammengefasst.",

        "Merken":
            "Rechtlich selbstständig – wirtschaftlich unter gemeinsamer Leitung."
    },

    "Fusion": {
        "Definition":
            "Unternehmen verschmelzen miteinander.",

        "Folge":
            "Mindestens ein beteiligtes Unternehmen verliert seine bisherige rechtliche Selbstständigkeit."
    },

    "Joint Venture": {
        "Definition":
            "Gemeinschaftliches Unternehmen, das von mindestens zwei Partnerunternehmen getragen wird.",

        "Vorteile":
            "Risiko, Kapitalbedarf und Know-how können geteilt werden.",

        "Typischer Zweck":
            "Erschließung neuer Märkte oder gemeinsame Durchführung größerer Projekte."
    },

    "Outsourcing": {
        "Definition":
            "Bisher intern erbrachte Leistungen werden an externe Unternehmen vergeben.",

        "Vorteile":
            "Konzentration auf Kernkompetenzen, mögliche Kostensenkung und Nutzung externen Spezialwissens.",

        "Nachteile":
            "Abhängigkeit vom Dienstleister, Know-how-Verlust, Qualitätsrisiken und schwierige Rückführung.",

        "Merken":
            "Outsourcing kann kurzfristig entlasten, schafft aber Abhängigkeiten."
    }
}


# ============================================================
# INVESTITIONSRECHNUNG
# ============================================================

INVESTITIONSRECHNUNG_LERNEN = {

    "Investition": {
        "Definition":
            "Langfristige Bindung finanzieller Mittel mit dem Ziel eines zukünftigen wirtschaftlichen Nutzens.",

        "Beispiele":
            "Maschinen, Anlagen, Gebäude, Fahrzeuge oder Software."
    },

    "Investitionsgründe": {
        "Arten":
            "Ersatzinvestition, Erweiterungsinvestition, Rationalisierungsinvestition und Neuinvestition.",

        "Ersatzinvestition":
            "Ein vorhandenes Betriebsmittel wird ersetzt.",

        "Erweiterungsinvestition":
            "Kapazität wird erhöht.",

        "Rationalisierungsinvestition":
            "Kosten oder Bearbeitungszeiten sollen reduziert werden."
    },

    "Kostenvergleich": {
        "Ziel":
            "Alternative mit den niedrigeren Kosten bestimmen.",

        "Beachten":
            "Fixe und variable Kosten können zu unterschiedlichen Ergebnissen bei verschiedenen Beschäftigungsmengen führen."
    },

    "Gewinnvergleich": {
        "formel":
            "Gewinn = Erlöse - Kosten",

        "Ziel":
            "Alternative mit dem höheren erwarteten Gewinn bestimmen."
    },

    "Rentabilität": {
        "formel":
            "Rentabilität = Gewinn / eingesetztes Kapital × 100",

        "Bedeutung":
            "Zeigt die Verzinsung des eingesetzten Kapitals."
    },

    "Amortisation": {
        "Definition":
            "Zeitraum, nach dem das investierte Kapital durch Rückflüsse wieder zurückgewonnen wurde.",

        "Merken":
            "Je kürzer die Amortisationszeit, desto schneller fließt das eingesetzte Kapital zurück."
    }
}


# ============================================================
# BETRIEBLICHE KENNZAHLEN
# ============================================================

BETRIEBLICHE_KENNZAHLEN_LERNEN = {

    "Produktivität": {
        "Definition":
            "Mengenmäßiges Verhältnis von Output zu Input.",

        "formel":
            "Produktivität = Output / Input",

        "Beispiel":
            "Produzierte Stückzahl je Arbeitsstunde.",

        "Merken":
            "Produktivität betrachtet Mengen."
    },

    "Wirtschaftlichkeit": {
        "Definition":
            "Wertmäßiges Verhältnis von Ertrag zu Aufwand.",

        "formel":
            "Wirtschaftlichkeit = Ertrag / Aufwand",

        "Bewertung":
            "Über 1 = wirtschaftlich; 1 = ausgeglichen; unter 1 = unwirtschaftlich.",

        "Merken":
            "Wirtschaftlichkeit betrachtet Werte."
    },

    "Rentabilität": {
        "Definition":
            "Zeigt den Erfolg im Verhältnis zum eingesetzten Kapital.",

        "formel":
            "Rentabilität = Gewinn / eingesetztes Kapital × 100",

        "Merken":
            "Rentabilität wird in Prozent angegeben."
    },

    "Liquidität": {
        "Definition":
            "Fähigkeit eines Unternehmens, seine fälligen Zahlungsverpflichtungen fristgerecht zu erfüllen.",

        "Folge mangelnder Liquidität":
            "Ein Unternehmen kann trotz vorhandener Vermögenswerte in Zahlungsschwierigkeiten geraten.",

        "Merken":
            "Liquidität = Zahlungsfähigkeit."
    }
}