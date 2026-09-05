# ============================================================
# INDUSTRIEMEISTER LERNAPP
# RECHT – DATEN
# Rechtsbewusstes Handeln
# Version 1.0
# ============================================================

RECHT_THEMEN = [
    {
        "name": "Arbeitsvertrag und Beendigung",
        "prioritaet": "🔥 Sehr hoch",
        "beschreibung": "Arbeitsvertrag, Form, Befristung, Kündigung, Kündigungsfristen, Kündigungsschutz und Arbeitszeugnis."
    },
    {
        "name": "Arbeitszeit, Urlaub und Entgeltfortzahlung",
        "prioritaet": "🔥 Sehr hoch",
        "beschreibung": "Arbeitszeitgesetz, Teilzeit, Urlaub, Krankheit und Entgeltfortzahlung."
    },
    {
        "name": "Betriebsverfassung und Mitbestimmung",
        "prioritaet": "🔥 Sehr hoch",
        "beschreibung": "Betriebsrat, Beteiligungsrechte, Mitbestimmung, Betriebsvereinbarung und Einigungsstelle."
    },
    {
        "name": "Tarifrecht und Arbeitskampf",
        "prioritaet": "🔥 Sehr hoch",
        "beschreibung": "Tarifvertrag, Tarifbindung, Öffnungsklausel, Rangfolge der Rechtsquellen, Streik und Friedenspflicht."
    },
    {
        "name": "Sozialversicherung und Unfallversicherung",
        "prioritaet": "⭐ Hoch",
        "beschreibung": "Zweige und Träger der Sozialversicherung, Berufsgenossenschaft, Arbeits- und Wegeunfälle."
    },
    {
        "name": "Arbeits- und Gesundheitsschutz",
        "prioritaet": "🔥 Sehr hoch",
        "beschreibung": "Arbeitsschutzorganisation, Gefährdungsbeurteilung, Unterweisung und relevante Regelwerke."
    },
    {
        "name": "Besondere Personengruppen und Ausbildung",
        "prioritaet": "⭐ Hoch",
        "beschreibung": "Mutterschutz, Schwerbehinderung, Jugendliche und Auszubildende."
    },
    {
        "name": "Umweltrecht",
        "prioritaet": "⭐ Hoch",
        "beschreibung": "Umweltprinzipien, Emission/Immission, Kreislaufwirtschaft und wichtige Umweltgesetze."
    },
    {
        "name": "Datenschutz und allgemeine Rechtsgrundlagen",
        "prioritaet": "➕ Mittel",
        "beschreibung": "Datenschutz im Beschäftigungsverhältnis sowie grundlegende Rechtsbegriffe und Zuständigkeiten."
    },
]

RECHT_LERNBEREICHE = {
    "Arbeitsvertrag und Beendigung": {
        "Arbeitsvertrag": {
            "Grundsatz": "Ein unbefristeter Arbeitsvertrag kann grundsätzlich formfrei zustande kommen. Besondere Formvorschriften können sich aber aus Gesetzen oder anderen Regelungen ergeben.",
            "Wichtige Normen": "§ 611a BGB; bei Befristung insbesondere § 14 Abs. 4 TzBfG; bei Kündigungen § 623 BGB.",
            "Prüfungstipp": "Bei Formfragen immer trennen: Ist der Vertrag selbst wirksam? Gibt es zusätzlich eine Nachweis- oder Dokumentationspflicht?"
        },
        "Kündigung": {
            "Ordentliche Kündigung": "Prüfe Kündigungsfrist, Form, Kündigungsschutz und besondere Schutzvorschriften.",
            "Schriftform": "Kündigungen bedürfen grundsätzlich der Schriftform (§ 623 BGB).",
            "Kündigungsfrist": "§ 622 BGB ist ein zentraler Ausgangspunkt. Tarifvertragliche Abweichungen können zulässig sein.",
            "Prüfungsschema": "1. Form → 2. Frist → 3. allgemeiner Kündigungsschutz → 4. besonderer Kündigungsschutz → 5. Beteiligung des Betriebsrates."
        },
        "Arbeitszeugnis": {
            "Einfaches Zeugnis": "Enthält insbesondere Art und Dauer der Tätigkeit.",
            "Qualifiziertes Zeugnis": "Enthält zusätzlich Aussagen zu Leistung und Verhalten.",
            "Prüfungstipp": "Unzulässige bzw. besonders sensible Angaben nicht ungefragt in das Zeugnis aufnehmen."
        }
    },
    "Arbeitszeit, Urlaub und Entgeltfortzahlung": {
        "Arbeitszeit": {
            "Kernfragen": "Dauer der täglichen Arbeitszeit, Ausgleichszeiträume, Ruhezeiten sowie Mitbestimmung des Betriebsrates.",
            "Wichtig": "Arbeitszeitrecht und Betriebsverfassungsrecht werden in Prüfungen häufig miteinander kombiniert.",
            "Prüfungstipp": "Nicht nur ArbZG prüfen: Bei Lage und Verteilung der Arbeitszeit oft zusätzlich § 87 BetrVG."
        },
        "Teilzeit": {
            "Kernnorm": "§ 8 TzBfG.",
            "Prüfungsschema": "Betriebsgröße, Beschäftigungsdauer, rechtzeitiges Verlangen und entgegenstehende betriebliche Gründe prüfen.",
            "Prüfungstipp": "Bei Aufgaben zu Teilzeit werden häufig ausdrücklich Rechtsgrundlagen verlangt."
        },
        "Urlaub und Krankheit": {
            "Urlaub": "Gesetzlicher Mindesturlaub richtet sich nach dem BUrlG; bei Teilzeiträumen kann eine anteilige Betrachtung relevant sein.",
            "Entgeltfortzahlung": "Bei Krankheit ist insbesondere das EFZG wichtig.",
            "Wartezeit": "Für die Entgeltfortzahlung ist die gesetzliche Wartezeit zu beachten."
        }
    },
    "Betriebsverfassung und Mitbestimmung": {
        "Mitbestimmung": {
            "Kernnorm": "§ 87 BetrVG ist einer der wichtigsten Paragraphen für die Prüfung.",
            "Typische Themen": "Beginn/Ende der Arbeitszeit, Verteilung auf Wochentage, Mehrarbeit, technische Überwachung und weitere soziale Angelegenheiten.",
            "Prüfungstipp": "Erst fragen: Gibt es einen Betriebsrat? Dann prüfen, ob ein Mitbestimmungsrecht besteht."
        },
        "Betriebsvereinbarung": {
            "Grundsatz": "Betriebsvereinbarungen werden zwischen Arbeitgeber und Betriebsrat geschlossen.",
            "Tarifsperre": "§ 77 Abs. 3 BetrVG beachten: tariflich geregelte oder üblicherweise tariflich geregelte Arbeitsbedingungen sind grundsätzlich gesperrt.",
            "Form": "Die Betriebsvereinbarung ist schriftlich niederzulegen."
        },
        "Personelle Maßnahmen": {
            "Einstellungen": "In Unternehmen mit entsprechendem Betriebsrat können Beteiligungsrechte nach § 99 BetrVG bestehen.",
            "Prüfungstipp": "Bei Einstellungen, Versetzungen, Eingruppierungen und Umgruppierungen immer an § 99 BetrVG denken."
        }
    },
    "Tarifrecht und Arbeitskampf": {
        "Rangfolge": {
            "Merksatz": "Höhere Rechtsquellen gehen grundsätzlich niedrigeren vor; günstigere Regelungen können im Arbeitsrecht eine besondere Rolle spielen.",
            "Typische Reihenfolge": "Europarecht → Grundgesetz → Gesetze → Tarifvertrag → Betriebsvereinbarung → Arbeitsvertrag → Weisungsrecht.",
        },
        "Tarifvertrag": {
            "Form": "Tarifverträge sind schriftlich abzuschließen.",
            "Öffnungsklausel": "Eine Öffnungsklausel erlaubt unter bestimmten Voraussetzungen betriebliche Abweichungen vom Tarifvertrag.",
            "Tarifbindung": "Prüfe, ob Arbeitgeber und Arbeitnehmer tarifgebunden sind und ob der Tarifvertrag räumlich, fachlich und persönlich gilt."
        },
        "Arbeitskampf": {
            "Streik": "Ein rechtmäßiger Streik setzt u. a. ein tariflich regelbares Ziel, Gewerkschaftsbezug, Verhältnismäßigkeit und Beachtung der Friedenspflicht voraus.",
            "Friedenspflicht": "Während eines ungekündigt geltenden Tarifvertrags sind Kampfmaßnahmen über die geregelten Gegenstände grundsätzlich ausgeschlossen."
        }
    },
    "Sozialversicherung und Unfallversicherung": {
        "Sozialversicherung": {
            "Zweige": "Kranken-, Pflege-, Renten-, Arbeitslosen- und Unfallversicherung.",
            "Träger": "Krankenkassen/Pflegekassen, Deutsche Rentenversicherung, Bundesagentur für Arbeit und Berufsgenossenschaften/Unfallkassen.",
            "Prüfungstipp": "Zweig und Träger sicher zuordnen können."
        },
        "Berufsgenossenschaft": {
            "Prävention": "Arbeitsunfälle, Berufskrankheiten und arbeitsbedingte Gesundheitsgefahren verhüten.",
            "Leistung": "Nach Eintritt eines Versicherungsfalls Rehabilitation und ggf. Entschädigungsleistungen.",
            "Arbeits- und Wegeunfall": "Beide können Versicherungsfälle der gesetzlichen Unfallversicherung sein; für betriebliche Beitragsbetrachtungen kann die Unterscheidung relevant sein."
        }
    },
    "Arbeits- und Gesundheitsschutz": {
        "Verantwortung": {
            "Arbeitgeber": "Der Arbeitgeber trägt die grundsätzliche Verantwortung für Sicherheit und Gesundheitsschutz.",
            "Führungskraft": "Aufgaben können übertragen werden; Verantwortung und Pflichten müssen dann im übertragenen Bereich wahrgenommen werden."
        },
        "Gefährdungsbeurteilung": {
            "Zweck": "Gefährdungen systematisch ermitteln und bewerten sowie geeignete Schutzmaßnahmen ableiten.",
            "Aktualisierung": "Insbesondere bei Änderungen von Arbeitsverfahren, Arbeitsmitteln, Stoffen, Erkenntnissen oder nach Unfällen/Ereignissen.",
            "Beteiligte": "Je nach Betrieb z. B. Führungskräfte, Fachkraft für Arbeitssicherheit, Betriebsarzt, Betriebsrat, Sicherheitsbeauftragte und Beschäftigte."
        },
        "Regelwerke": {
            "Beispiele": "ArbSchG, ASiG, BetrSichV, GefStoffV, ArbStättV sowie DGUV-Regelwerk.",
            "Prüfungstipp": "Nicht nur Gesetze auswendig lernen, sondern wissen, welches Regelwerk für welchen Sachverhalt zuständig ist."
        }
    },
    "Besondere Personengruppen und Ausbildung": {
        "Schwangerschaft": {
            "Kündigungsschutz": "Schwangere genießen besonderen Kündigungsschutz; zentral ist § 17 MuSchG.",
            "Prüfungstipp": "Zeitpunkt der Schwangerschaft, Kenntnis des Arbeitgebers und Mitteilungsfristen im Sachverhalt genau lesen."
        },
        "Schwerbehinderung": {
            "Kündigung": "Vor der Kündigung eines schwerbehinderten Menschen ist grundsätzlich die Zustimmung des Integrationsamtes erforderlich (§ 168 SGB IX).",
            "Zusatzurlaub": "Schwerbehinderte Menschen können zusätzlichen Urlaub nach § 208 SGB IX haben."
        },
        "Auszubildende und Jugendliche": {
            "Berufsschule": "Freistellung und Anrechnung der Berufsschulzeit sind zentrale Prüfungsthemen.",
            "Normen": "Insbesondere BBiG und JArbSchG.",
            "Prüfungstipp": "Alter des Auszubildenden beachten, weil dadurch zusätzliche Schutzvorschriften gelten können."
        }
    },
    "Umweltrecht": {
        "Umweltprinzipien": {
            "Vorsorgeprinzip": "Umweltbelastungen möglichst bereits vor ihrem Eintritt verhindern.",
            "Verursacherprinzip": "Der Verursacher soll die Kosten der Vermeidung und Beseitigung von Umweltbelastungen tragen.",
            "Kooperationsprinzip": "Behörden, Unternehmen und Öffentlichkeit wirken beim Umweltschutz zusammen.",
            "Gemeinlastprinzip": "Kann kein Verursacher herangezogen werden, kann die Allgemeinheit Kosten tragen."
        },
        "Emission und Immission": {
            "Emission": "Von einer Anlage ausgehende Einwirkungen, z. B. Geräusche, Luftverunreinigungen oder Wärme.",
            "Immission": "Einwirkungen, die auf Menschen, Tiere, Pflanzen, Sachen oder Umweltgüter treffen.",
            "Kernnorm": "Begriffsbestimmungen finden sich im BImSchG."
        },
        "Abfallhierarchie": {
            "Reihenfolge": "Vermeidung → Vorbereitung zur Wiederverwendung → Recycling → sonstige Verwertung → Beseitigung.",
            "Kernnorm": "§ 6 KrWG."
        },
        "Wichtige Gesetze": {
            "Beispiele": "BImSchG, KrWG, WHG, BNatSchG sowie einschlägige Verordnungen.",
        }
    },
    "Datenschutz und allgemeine Rechtsgrundlagen": {
        "Beschäftigtendaten": {
            "Grundsatz": "Beschäftigtendaten dürfen nicht beliebig verarbeitet werden. Es braucht eine Rechtsgrundlage oder eine andere zulässige Grundlage.",
            "Rechte": "Typische Betroffenenrechte sind Auskunft, Berichtigung und unter Voraussetzungen Löschung.",
            "Prüfungstipp": "Bei Datenschutzfragen zwischen Datenart, Rechtsgrundlage der Verarbeitung und Rechten der betroffenen Person trennen."
        },
        "Arbeitsgerichtsbarkeit": {
            "Zuständigkeit": "Arbeitsrechtliche Streitigkeiten werden regelmäßig vor der Arbeitsgerichtsbarkeit ausgetragen.",
            "Prüfungstipp": "In Aufgaben wird gern nach sachlich und örtlich zuständigem Gericht sowie der Besetzung gefragt."
        }
    }
}

RECHT_GESETZE = {
    "BGB": ["§ 611a Arbeitsvertrag", "§ 622 Kündigungsfristen", "§ 623 Schriftform der Kündigung"],
    "TzBfG": ["§ 8 Verringerung der Arbeitszeit", "§ 14 Abs. 4 Schriftform der Befristung"],
    "BetrVG": ["§ 77 Betriebsvereinbarung", "§ 87 Mitbestimmung in sozialen Angelegenheiten", "§ 99 personelle Einzelmaßnahmen"],
    "TVG": ["§ 1 Tarifvertrag und Form", "§ 4 Wirkung der Rechtsnormen"],
    "MuSchG": ["§ 17 Kündigungsverbot"],
    "SGB IX": ["§ 168 Zustimmung des Integrationsamtes", "§ 208 Zusatzurlaub"],
    "BBiG": ["§ 15 Freistellung, Anrechnung", "§§ 10-11 Berufsausbildungsvertrag"],
    "ArbSchG": ["§ 5 Beurteilung der Arbeitsbedingungen"],
    "KrWG": ["§ 6 Abfallhierarchie"],
    "BImSchG": ["§ 3 Begriffsbestimmungen zu Emissionen/Immissionen"],
}
