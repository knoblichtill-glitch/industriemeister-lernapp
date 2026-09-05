# ============================================================
# ZIB DATEN
# Industriemeister Metall - Basisqualifikationen
# Zusammenarbeit im Betrieb
# ============================================================

ZIB_THEMEN = [
    {
        "name": "Führung und Führungsverhalten",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Führungsstile, Führungsverhalten, situatives Führen sowie fachliche und disziplinarische Führung."
    },
    {
        "name": "Kommunikation und Mitarbeitergespräche",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Gesprächsführung, Mitarbeitergespräche, aktives Zuhören, Fragetechniken und Gesprächsstörungen."
    },
    {
        "name": "Gruppen und Teams",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Gruppenentwicklung, Rollen, Zusammenarbeit und Aufgaben des Meisters in Arbeitsgruppen."
    },
    {
        "name": "Konflikte",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Konfliktursachen, Auswirkungen und Möglichkeiten der Konfliktbewältigung."
    },
    {
        "name": "Motivation",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Motivation von Mitarbeitern, Bedürfnisse, Anerkennung und Gestaltung motivierender Arbeitsbedingungen."
    },
    {
        "name": "Personalentwicklung und Beurteilung",
        "prioritaet": "🔴 Sehr hoch",
        "beschreibung": "Mitarbeiterbeurteilung, Beurteilungsfehler, Qualifizierungsmaßnahmen und Personalentwicklung."
    },
    {
        "name": "Sozialverhalten und Persönlichkeit",
        "prioritaet": "🟠 Hoch",
        "beschreibung": "Persönlichkeitsentwicklung, Sozialverhalten und Einflussfaktoren auf menschliches Verhalten."
    },
    {
        "name": "Qualifikationen",
        "prioritaet": "🟠 Hoch",
        "beschreibung": "Schlüsselqualifikationen sowie fachliche, methodische und soziale Kompetenzen."
    },
    {
        "name": "Betriebsklima und Zusammenarbeit",
        "prioritaet": "🟠 Hoch",
        "beschreibung": "Zusammenarbeit, Arbeitsbedingungen, Betriebsklima und Integration von Mitarbeitern."
    },
    {
        "name": "Besondere Führungssituationen",
        "prioritaet": "🟡 Mittel",
        "beschreibung": "Veränderungsprozesse, virtuelle Teams und besondere betriebliche Führungssituationen."
    },
]


# ============================================================
# 1. FÜHRUNG UND FÜHRUNGSVERHALTEN
# ============================================================

FUEHRUNG_LERNEN = {

    "Führung": {
        "definition":
            "Führung bedeutet, das Verhalten von Mitarbeitern zielgerichtet zu beeinflussen, "
            "damit betriebliche Ziele erreicht werden.",

        "merkmale": [
            "Führung richtet sich auf Menschen und deren Verhalten.",
            "Führung verfolgt betriebliche Ziele.",
            "Führung beinhaltet Kommunikation.",
            "Führung erfordert Motivation und Koordination.",
            "Das Führungsverhalten muss zur jeweiligen Situation passen."
        ],

        "merksatz":
            "Führung = Menschen so beeinflussen und unterstützen, dass gemeinsame Ziele erreicht werden."
    },

    "Führungsaufgaben des Industriemeisters": {
        "definition":
            "Der Industriemeister übernimmt neben fachlichen Aufgaben auch Führungs- und Koordinationsaufgaben.",

        "merkmale": [
            "Mitarbeiter informieren",
            "Aufgaben übertragen",
            "Arbeitsabläufe koordinieren",
            "Mitarbeiter motivieren",
            "Leistungen kontrollieren",
            "Mitarbeiter beurteilen",
            "Konflikte erkennen und bearbeiten",
            "Mitarbeiter fördern",
            "Ziele vereinbaren",
            "Zusammenarbeit unterstützen"
        ],

        "merksatz":
            "Der Meister organisiert nicht nur Arbeit – er führt Menschen."
    },

    "Situative Führung": {
        "definition":
            "Bei der situativen Führung wird das Führungsverhalten an die jeweilige Situation "
            "und an die zu führenden Mitarbeiter angepasst.",

        "einflussfaktoren": [
            "Kenntnisse und Fähigkeiten des Mitarbeiters",
            "Erfahrung des Mitarbeiters",
            "Motivation und Engagement",
            "Persönlichkeit",
            "Art und Schwierigkeit der Aufgabe",
            "Zeitdruck",
            "Gefahrensituation",
            "betriebliche Rahmenbedingungen"
        ],

        "beispiel":
            "Ein erfahrener und zuverlässiger Mitarbeiter kann selbstständig arbeiten. "
            "Ein neuer Mitarbeiter benötigt dagegen zunächst mehr Anleitung und Kontrolle.",

        "merksatz":
            "Nicht jeder Mitarbeiter und nicht jede Situation benötigt denselben Führungsstil."
    },

    "Fachliche Führung": {
        "definition":
            "Fachliche Führung bezieht sich vor allem auf die operativen und fachlichen Aufgaben.",

        "merkmale": [
            "Arbeitsaufgaben koordinieren",
            "fachliche Anweisungen geben",
            "Arbeitsprozesse begleiten",
            "Arbeitsergebnisse sicherstellen",
            "fachliche Unterstützung geben"
        ],

        "hinweis":
            "Eine rein fachliche Führungskraft verfügt nicht zwingend über disziplinarische Weisungsbefugnisse."
    },

    "Disziplinarische Führung": {
        "definition":
            "Disziplinarische Führung umfasst personelle und arbeitsrechtliche Führungsbefugnisse.",

        "beispiele": [
            "Personalentscheidungen",
            "Abmahnungen",
            "Mitarbeiterentwicklung",
            "Gehaltsfragen",
            "Einstellungen",
            "Kündigungen"
        ],

        "merksatz":
            "Fachlich = Wie wird gearbeitet? | Disziplinarisch = personelle Führungsverantwortung."
    }
}


# ============================================================
# 2. KOMMUNIKATION UND MITARBEITERGESPRÄCHE
# ============================================================

KOMMUNIKATION_LERNEN = {

    "Mitarbeitergespräch": {
        "definition":
            "Ein Mitarbeitergespräch ist ein gezielt vorbereitetes Gespräch zwischen Führungskraft "
            "und Mitarbeiter zu einem bestimmten betrieblichen oder persönlichen Anlass.",

        "anlaesse": [
            "Beurteilungsgespräch",
            "Jahresgespräch",
            "Kritikgespräch",
            "Konfliktgespräch",
            "Zielvereinbarungsgespräch",
            "Disziplinargespräch",
            "Probezeitgespräch",
            "Versetzungs- oder Beförderungsgespräch",
            "Personalentwicklungsgespräch",
            "Krankenrückkehrgespräch",
            "Bewerbungs- oder Einstellungsgespräch"
        ],

        "merksatz":
            "Vor jedem Gespräch müssen Anlass und Ziel klar sein."
    },

    "Gesprächsvorbereitung": {
        "merkmale": [
            "Gesprächsziel festlegen",
            "Informationen und Fakten sammeln",
            "ausreichend Zeit einplanen",
            "störungsfreien Raum auswählen",
            "Gesprächsstruktur vorbereiten",
            "Unterlagen bereithalten"
        ]
    },

    "Gesprächsverlauf": {
        "phasen": [
            "Gespräch freundlich eröffnen",
            "Anlass und Ziel erklären",
            "Sachverhalt darstellen",
            "Mitarbeiter zu Wort kommen lassen",
            "aktiv zuhören und Fragen stellen",
            "gemeinsam Lösungen bzw. Maßnahmen entwickeln",
            "Ergebnisse zusammenfassen",
            "Vereinbarungen dokumentieren",
            "Gespräch positiv beenden"
        ]
    },

    "Negativer Gesprächsverlauf": {
        "ursachen": [
            "schlechte Vorbereitung",
            "fehlende Gesprächsziele",
            "mangelndes Einfühlungsvermögen",
            "Mitarbeiter nicht ausreden lassen",
            "fehlendes aktives Zuhören",
            "ungeeignete Fragetechniken",
            "unsystematisches Vorgehen",
            "störende Gesprächsumgebung",
            "zu wenig Zeit",
            "Kritik an der Person statt an der Sache"
        ]
    },

    "Aktives Zuhören": {
        "definition":
            "Aktives Zuhören bedeutet, dem Gesprächspartner aufmerksam zuzuhören und ihm zu zeigen, "
            "dass seine Aussagen verstanden werden sollen.",

        "merkmale": [
            "ausreden lassen",
            "Blickkontakt halten",
            "gezielt nachfragen",
            "Gesagtes zusammenfassen",
            "Gefühle und Sichtweise berücksichtigen",
            "nicht vorschnell bewerten"
        ],

        "merksatz":
            "Aktiv zuhören heißt nicht nur schweigen, sondern Verständnis sichtbar machen."
    }
}


# ============================================================
# 3. GRUPPEN UND TEAMS
# ============================================================

GRUPPEN_LERNEN = {

    "Forming": {
        "definition":
            "Forming ist die Orientierungs- und Kennenlernphase einer Gruppe.",

        "merkmale": [
            "Unsicherheit",
            "vorsichtiges Verhalten",
            "Höflichkeit",
            "gegenseitiges Kennenlernen",
            "Orientierung",
            "erste Rollensuche"
        ],

        "rolle_meister":
            "Orientierung geben, Ziele erklären und Sicherheit schaffen."
    },

    "Storming": {
        "definition":
            "Storming ist die Konflikt- und Auseinandersetzungsphase.",

        "merkmale": [
            "Konflikte werden sichtbar",
            "unterschiedliche Meinungen treffen aufeinander",
            "Macht- und Positionskämpfe",
            "Rollen werden ausgehandelt",
            "Spannungen innerhalb der Gruppe"
        ],

        "rolle_meister":
            "Konflikte moderieren, Regeln verdeutlichen und die Zusammenarbeit fördern."
    },

    "Norming": {
        "definition":
            "Norming ist die Organisations- und Regelungsphase.",

        "merkmale": [
            "Regeln entstehen",
            "Aufgaben werden verteilt",
            "Rollen werden akzeptiert",
            "Kompromisse werden gefunden",
            "Zusammengehörigkeitsgefühl wächst"
        ],

        "rolle_meister":
            "Eigenverantwortung fördern und gemeinsame Regeln unterstützen."
    },

    "Performing": {
        "definition":
            "Performing ist die leistungsfähige Arbeitsphase.",

        "merkmale": [
            "Gruppe arbeitet weitgehend selbstständig",
            "Aufgabenverteilung funktioniert",
            "Zusammenarbeit ist stabil",
            "Gruppenziele stehen im Vordergrund",
            "hohe Leistungsfähigkeit"
        ],

        "rolle_meister":
            "Verantwortung übertragen und überwiegend unterstützend eingreifen."
    },

    "Gruppenphasen": {
        "reihenfolge": [
            "1. Forming",
            "2. Storming",
            "3. Norming",
            "4. Performing"
        ],

        "merksatz":
            "Forming → Storming → Norming → Performing"
    },

    "Aufgaben des Meisters bei Gruppenarbeit": {
        "merkmale": [
            "Ziele festlegen",
            "Aufgaben koordinieren",
            "Mitarbeiter informieren",
            "Rahmenbedingungen schaffen",
            "Konflikte bearbeiten",
            "Mitarbeiter motivieren",
            "Ergebnisse kontrollieren",
            "Zusammenarbeit fördern"
        ]
    },

    "Teamarbeit fördern": {
        "werte": [
            "Respekt",
            "Toleranz",
            "Vertrauen",
            "Hilfsbereitschaft",
            "Fairness",
            "Offenheit",
            "Zuverlässigkeit",
            "gegenseitige Wertschätzung"
        ]
    }
}


# ============================================================
# 4. KONFLIKTE
# ============================================================

KONFLIKTE_LERNEN = {

    "Konflikt": {
        "definition":
            "Ein Konflikt entsteht, wenn unterschiedliche Interessen, Ziele, Erwartungen, "
            "Meinungen oder Verhaltensweisen aufeinandertreffen und als unvereinbar erlebt werden.",

        "merksatz":
            "Unterschiedliche Interessen allein sind noch kein Problem – entscheidend ist der Umgang damit."
    },

    "Konfliktursachen": {
        "ursachen": [
            "mangelnde Kommunikation",
            "Missverständnisse",
            "unterschiedliche Ziele",
            "unterschiedliche Interessen",
            "unklare Aufgabenverteilung",
            "Kompetenzüberschneidungen",
            "Informationsmangel",
            "Konkurrenzdenken",
            "persönliche Antipathien",
            "unterschiedliche Arbeitsweisen",
            "ungerechte Behandlung",
            "Über- oder Unterforderung"
        ]
    },

    "Auswirkungen von Konflikten": {
        "negative_folgen": [
            "Produktivität sinkt",
            "Betriebsklima verschlechtert sich",
            "Motivation sinkt",
            "Fehler können zunehmen",
            "Fehlzeiten können steigen",
            "Informationsaustausch verschlechtert sich",
            "Zusammenarbeit wird erschwert"
        ],

        "positive_chancen": [
            "Probleme werden sichtbar",
            "Veränderungen können angestoßen werden",
            "neue Lösungen können entstehen",
            "Regeln und Zuständigkeiten können verbessert werden"
        ]
    },

    "Konfliktbewältigung": {
        "massnahmen": [
            "Konflikt frühzeitig erkennen",
            "Konfliktparteien anhören",
            "Ursachen ermitteln",
            "sachlich bleiben",
            "gemeinsame Interessen herausarbeiten",
            "Lösungsmöglichkeiten entwickeln",
            "Vereinbarungen treffen",
            "Umsetzung kontrollieren",
            "bei Bedarf Mediation einsetzen"
        ]
    }
}


# ============================================================
# 5. MOTIVATION
# ============================================================

MOTIVATION_LERNEN = {

    "Motivation": {
        "definition":
            "Motivation beschreibt die Beweggründe, die einen Menschen zu einem bestimmten Verhalten veranlassen.",

        "betriebliche_bedeutung": [
            "Leistungsbereitschaft fördern",
            "Arbeitszufriedenheit erhöhen",
            "Eigeninitiative unterstützen",
            "Mitarbeiterbindung stärken",
            "Zusammenarbeit verbessern"
        ]
    },

    "Intrinsische Motivation": {
        "definition":
            "Die Motivation entsteht aus der Tätigkeit selbst.",

        "beispiele": [
            "Interesse an der Aufgabe",
            "Freude an der Arbeit",
            "Verantwortung",
            "persönliche Herausforderung",
            "Erfolgserlebnis"
        ]
    },

    "Extrinsische Motivation": {
        "definition":
            "Die Motivation entsteht durch äußere Anreize.",

        "beispiele": [
            "Lohn",
            "Prämien",
            "Beförderung",
            "Lob",
            "Status",
            "Vermeidung negativer Konsequenzen"
        ]
    },

    "Motivationsmaßnahmen des Meisters": {
        "massnahmen": [
            "Anerkennung und Lob",
            "interessante Aufgaben",
            "Verantwortung übertragen",
            "Mitarbeiter beteiligen",
            "klare Ziele vereinbaren",
            "Weiterbildung ermöglichen",
            "gute Arbeitsbedingungen schaffen",
            "regelmäßiges Feedback",
            "gerechte Behandlung"
        ]
    },

    "Selbstwertgefühl": {
        "definition":
            "Das Selbstwertgefühl beschreibt die Bewertung, die ein Mensch seiner eigenen Person beimisst.",

        "foerderung": [
            "Wertschätzung zeigen",
            "Leistungen anerkennen",
            "Mitarbeiter ernst nehmen",
            "Verantwortung übertragen",
            "realistische Ziele setzen",
            "Erfolgserlebnisse ermöglichen",
            "konstruktives Feedback geben"
        ]
    }
}


# ============================================================
# 6. PERSONALENTWICKLUNG UND BEURTEILUNG
# ============================================================

PERSONALENTWICKLUNG_LERNEN = {

    "Personalentwicklung": {
        "definition":
            "Personalentwicklung umfasst Maßnahmen zur Erhaltung, Verbesserung und Erweiterung "
            "der Qualifikationen und Kompetenzen von Mitarbeitern.",

        "ziele": [
            "Mitarbeiter auf neue Aufgaben vorbereiten",
            "Fachwissen erweitern",
            "Führungskräftenachwuchs entwickeln",
            "Motivation erhöhen",
            "Mitarbeiter langfristig binden",
            "Anpassung an technische und organisatorische Veränderungen"
        ]
    },

    "Job Rotation": {
        "definition":
            "Planmäßiger Wechsel zwischen verschiedenen Arbeitsplätzen oder Aufgaben.",

        "ziele": [
            "Kenntnisse erweitern",
            "Flexibilität erhöhen",
            "einseitige Belastung reduzieren",
            "Vertretungsmöglichkeiten verbessern"
        ]
    },

    "Job Enlargement": {
        "definition":
            "Erweiterung des Aufgabenbereichs um zusätzliche Tätigkeiten auf vergleichbarem Anforderungsniveau.",

        "merksatz":
            "Mehr Aufgaben auf gleicher Ebene."
    },

    "Job Enrichment": {
        "definition":
            "Erweiterung einer Tätigkeit um anspruchsvollere Aufgaben sowie zusätzliche Verantwortung.",

        "merksatz":
            "Mehr Verantwortung und höherwertige Aufgaben."
    },

    "Mitarbeiterbeurteilung": {
        "definition":
            "Bei der Mitarbeiterbeurteilung werden Leistung, Verhalten und gegebenenfalls Potenzial "
            "eines Mitarbeiters anhand festgelegter Kriterien bewertet.",

        "ziele": [
            "Leistungsstand feststellen",
            "Stärken und Schwächen erkennen",
            "Entwicklungsmöglichkeiten ableiten",
            "Personalentscheidungen unterstützen",
            "Weiterbildungsbedarf feststellen",
            "Feedback geben"
        ]
    },

    "Beurteilungsfehler": {
        "arten": [
            "Überstrahlungseffekt",
            "Mildefehler",
            "Strengefehler",
            "Tendenz zur Mitte",
            "Kontrastfehler",
            "Vorurteile",
            "Pauschalurteile",
            "Klischeevorstellungen"
        ],

        "merksatz":
            "Eine Beurteilung soll sich auf beobachtbares Verhalten und nachvollziehbare Kriterien stützen."
    },

    "Überstrahlungseffekt": {
        "definition":
            "Ein besonders auffälliges positives oder negatives Merkmal beeinflusst die gesamte Beurteilung."
    },

    "Tendenz zur Mitte": {
        "definition":
            "Die Führungskraft vermeidet besonders gute oder schlechte Bewertungen und bewertet überwiegend durchschnittlich."
    },

    "Mildefehler": {
        "definition":
            "Mitarbeiter werden systematisch zu positiv beurteilt."
    },

    "Kontrastfehler": {
        "definition":
            "Der Mitarbeiter wird nicht objektiv, sondern im Vergleich mit einer anderen Person oder mit der Führungskraft selbst bewertet."
    }
}


# ============================================================
# 7. SOZIALVERHALTEN UND PERSÖNLICHKEIT
# ============================================================

SOZIALVERHALTEN_LERNEN = {

    "Sozialverhalten": {
        "definition":
            "Sozialverhalten beschreibt das Verhalten eines Menschen gegenüber anderen Menschen "
            "und innerhalb sozialer Gruppen.",

        "betriebliche_beispiele": [
            "Teamfähigkeit",
            "Hilfsbereitschaft",
            "Rücksichtnahme",
            "Kommunikationsverhalten",
            "Zuverlässigkeit",
            "Umgang mit Konflikten",
            "Einhaltung gemeinsamer Regeln"
        ]
    },

    "Einflussfaktoren auf Verhalten": {
        "faktoren": [
            "Familie und Erziehung",
            "Schule und Ausbildung",
            "Freundeskreis",
            "Berufserfahrung",
            "Vorgesetzte",
            "Kollegen",
            "betriebliche Kultur",
            "positive und negative Erfahrungen",
            "gesellschaftliches Umfeld"
        ]
    },

    "Persönlichkeitsentwicklung": {
        "definition":
            "Die Persönlichkeit eines Menschen entwickelt sich durch Anlage, Umwelt, Erziehung "
            "sowie persönliche Lebens- und Berufserfahrungen.",

        "bedeutung_fuer_meister":
            "Mitarbeiter reagieren aufgrund unterschiedlicher Erfahrungen und Persönlichkeiten "
            "nicht alle gleich. Dies muss bei der Führung berücksichtigt werden."
    }
}


# ============================================================
# 8. QUALIFIKATIONEN
# ============================================================

QUALIFIKATIONEN_LERNEN = {

    "Schlüsselqualifikationen": {
        "definition":
            "Schlüsselqualifikationen sind fach- und berufsübergreifende Fähigkeiten, "
            "die in unterschiedlichen Situationen eingesetzt werden können.",

        "beispiele": [
            "Teamfähigkeit",
            "Kommunikationsfähigkeit",
            "Kooperationsfähigkeit",
            "Toleranz",
            "Fairness",
            "Hilfsbereitschaft",
            "Selbstständigkeit",
            "Problemlösungsfähigkeit"
        ]
    },

    "Fachkompetenz": {
        "definition":
            "Fähigkeit, berufliche Aufgaben aufgrund fachlicher Kenntnisse und Fertigkeiten sachgerecht zu lösen."
    },

    "Sozialkompetenz": {
        "definition":
            "Fähigkeit, mit anderen Menschen angemessen zusammenzuarbeiten und soziale Situationen erfolgreich zu bewältigen.",

        "beispiele": [
            "Teamfähigkeit",
            "Konfliktfähigkeit",
            "Kommunikationsfähigkeit",
            "Empathie"
        ]
    },

    "Methodenkompetenz": {
        "definition":
            "Fähigkeit, geeignete Methoden und Vorgehensweisen zur Lösung von Aufgaben und Problemen einzusetzen.",

        "beispiele": [
            "Problemlösungstechniken",
            "Planung",
            "Informationsbeschaffung",
            "Präsentationstechniken"
        ]
    },

    "Schlüsselqualifikationen fördern": {
        "massnahmen": [
            "Gruppenarbeit einsetzen",
            "Verantwortung übertragen",
            "Projektarbeit ermöglichen",
            "Mitarbeiter an Entscheidungen beteiligen",
            "Aufgabenwechsel ermöglichen",
            "Feedback geben"
        ]
    }
}


# ============================================================
# 9. BETRIEBSKLIMA UND ZUSAMMENARBEIT
# ============================================================

BETRIEBSKLIMA_LERNEN = {

    "Betriebsklima": {
        "definition":
            "Das Betriebsklima beschreibt die von den Mitarbeitern wahrgenommene Qualität "
            "der sozialen Beziehungen und der Zusammenarbeit im Unternehmen.",

        "positive_einflussfaktoren": [
            "gute Kommunikation",
            "gegenseitiger Respekt",
            "gerechte Behandlung",
            "Anerkennung",
            "Vertrauen",
            "klare Zuständigkeiten",
            "gute Arbeitsbedingungen",
            "konstruktive Konfliktlösung"
        ]
    },

    "Folgen eines schlechten Betriebsklimas": {
        "folgen": [
            "sinkende Motivation",
            "sinkende Produktivität",
            "höhere Fehlzeiten",
            "mehr Konflikte",
            "höhere Fluktuation",
            "schlechtere Zusammenarbeit",
            "geringere Mitarbeiterbindung"
        ]
    },

    "Zusammenarbeit fördern": {
        "massnahmen": [
            "Informationen offen weitergeben",
            "gemeinsame Ziele schaffen",
            "Teamarbeit fördern",
            "Konflikte früh bearbeiten",
            "Mitarbeiter beteiligen",
            "Verantwortlichkeiten klären",
            "gegenseitige Unterstützung fördern",
            "Leistungen anerkennen"
        ]
    }
}


# ============================================================
# 10. BESONDERE FÜHRUNGSSITUATIONEN
# ============================================================

BESONDERE_FUEHRUNGSSITUATIONEN_LERNEN = {

    "Veränderungsprozesse": {
        "definition":
            "Betriebliche Veränderungen können bei Mitarbeitern Unsicherheit und Widerstand auslösen.",

        "massnahmen_meister": [
            "frühzeitig informieren",
            "Gründe für Veränderungen erklären",
            "Mitarbeiter beteiligen",
            "Ängste und Bedenken ernst nehmen",
            "Qualifizierungsmaßnahmen anbieten",
            "Erfahrungswissen nutzen",
            "Feedback ermöglichen",
            "Veränderungen nachvollziehbar begleiten"
        ]
    },

    "Integration neuer Mitarbeiter": {
        "massnahmen": [
            "Mitarbeiter vorstellen",
            "Aufgaben und Zuständigkeiten erklären",
            "betriebliche Regeln erläutern",
            "Ansprechpartner benennen",
            "Einarbeitung organisieren",
            "Team aktiv einbeziehen",
            "regelmäßige Rückmeldungen geben",
            "Konflikte früh erkennen"
        ]
    },

    "Virtuelle Teams": {
        "herausforderungen": [
            "fehlende räumliche Nähe",
            "erschwerter Vertrauensaufbau",
            "Gefahr sozialer Isolation",
            "Missverständnisse durch virtuelle Kommunikation",
            "schwierigerer Überblick über Arbeitsstände",
            "geringere persönliche Interaktion"
        ],

        "massnahmen": [
            "regelmäßige virtuelle Besprechungen",
            "klare Ziele und Teilziele",
            "Arbeitsstände transparent machen",
            "Erreichbarkeit vereinbaren",
            "geeignete Kommunikationssysteme bereitstellen",
            "Mitarbeiter in Systeme einweisen",
            "regelmäßiges Feedback"
        ]
    }
}


# ============================================================
# SAMMLUNG ALLER ZIB-LERNBEREICHE
# ============================================================

ZIB_LERNBEREICHE = {
    "Führung und Führungsverhalten": FUEHRUNG_LERNEN,
    "Kommunikation und Mitarbeitergespräche": KOMMUNIKATION_LERNEN,
    "Gruppen und Teams": GRUPPEN_LERNEN,
    "Konflikte": KONFLIKTE_LERNEN,
    "Motivation": MOTIVATION_LERNEN,
    "Personalentwicklung und Beurteilung": PERSONALENTWICKLUNG_LERNEN,
    "Sozialverhalten und Persönlichkeit": SOZIALVERHALTEN_LERNEN,
    "Qualifikationen": QUALIFIKATIONEN_LERNEN,
    "Betriebsklima und Zusammenarbeit": BETRIEBSKLIMA_LERNEN,
    "Besondere Führungssituationen": BESONDERE_FUEHRUNGSSITUATIONEN_LERNEN
}