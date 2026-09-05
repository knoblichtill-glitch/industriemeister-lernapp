import streamlit as st
import random
import re
import unicodedata
import json
import os
from pathlib import Path
from datetime import datetime, date, timedelta
from collections import defaultdict, Counter
import hashlib
try:
    import streamlit.components.v1 as components
except Exception:
    components = None

from bwh_daten import (
    BWH_THEMEN,
    KOSTENRECHNUNG_FORMELN, KOSTENRECHNUNG_ZEICHEN,
    MATERIALWIRTSCHAFT_FORMELN, MATERIALWIRTSCHAFT_ZEICHEN,
    MATERIALWIRTSCHAFT_LERNEN,
    ARBEITSENTGELT_FORMELN, ARBEITSENTGELT_LERNEN,
    UNTERNEHMENSFORMEN_LERNEN, ORGANISATION_LERNEN,
    FERTIGUNGSORGANISATION_LERNEN, KAPAZITAETSWIRTSCHAFT_LERNEN,
    UNTERNEHMENSZUSAMMENSCHLUESSE_LERNEN, INVESTITIONSRECHNUNG_LERNEN,
    BETRIEBLICHE_KENNZAHLEN_LERNEN,
)
from bwh_aufgaben import BWH_AUFGABEN
from zib_daten import ZIB_THEMEN, ZIB_LERNBEREICHE
from zib_aufgaben import ZIB_AUFGABEN
from recht_daten import RECHT_THEMEN, RECHT_LERNBEREICHE
from recht_aufgaben import RECHT_AUFGABEN
from mikp_daten import MIKP_THEMEN, MIKP_LERNBEREICHE
from mikp_aufgaben import MIKP_AUFGABEN

st.set_page_config(page_title="Industriemeister Metall LernApp", page_icon="🎓", layout="wide")

# ============================================================
# DESIGN
# ============================================================
st.markdown("""
<style>
:root { --ink:#1f2937; --muted:#667085; --line:#e4e7ec; --panel:#ffffff; --soft:#f8fafc; --accent:#315b7d; }
.block-container {max-width: 1460px; padding-top: 1.45rem; padding-bottom: 3rem;}
[data-testid="stSidebar"] {background:#f7f9fb; border-right:1px solid #e6ebf0;}
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3 {letter-spacing:-.02em;}
h1,h2,h3 {letter-spacing:-.025em; color:var(--ink);}
.hero {padding:22px 24px;border-radius:16px;background:#f7fafc;border:1px solid #dce5ed;margin-bottom:18px;}
.soft-card {padding:16px 18px;border:1px solid var(--line);border-radius:14px;background:#fff;margin:8px 0 14px 0;box-shadow:0 1px 2px rgba(16,24,40,.03);}
.visual-title {font-size:1.05rem;font-weight:700;margin-bottom:10px;}
.kpi {padding:14px;border:1px solid var(--line);border-radius:13px;background:#fff;}
.muted {color:var(--muted);font-size:.92rem;}
.search-hit {padding:13px 15px;border:1px solid var(--line);border-radius:12px;background:#fff;margin:6px 0;}
.merke {padding:14px 16px;border-radius:12px;background:#f3f8f4;border:1px solid #d5e7d8;margin:14px 0;}
.warn-card {padding:14px 16px;border-radius:12px;background:#fff9ed;border:1px solid #eddcb8;margin:14px 0;}
.result-good {padding:15px 17px;border-radius:12px;background:#f2f8f4;border:1px solid #cfe3d3;margin:10px 0;}
.result-mid {padding:15px 17px;border-radius:12px;background:#fff8ea;border:1px solid #ead7a7;margin:10px 0;}
.result-low {padding:15px 17px;border-radius:12px;background:#fff4f2;border:1px solid #edc7c1;margin:10px 0;}
.small-badge {display:inline-block;padding:3px 8px;border-radius:999px;background:#eef2f6;border:1px solid #dce3ea;font-size:.82rem;color:#475467;margin-right:6px;}
div.stButton > button {border-radius:10px;font-weight:600;}
[data-testid="stMetric"] {background:#fff;border:1px solid var(--line);padding:12px 14px;border-radius:12px;}
hr {margin-top:1rem!important;margin-bottom:1rem!important;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATENMODELL
# ============================================================
FACHNAMEN = {
    "BWH": "Betriebswirtschaftliches Handeln",
    "ZIB": "Zusammenarbeit im Betrieb",
    "Recht": "Rechtsbewusstes Handeln",
    "MIKP": "Methoden der Information, Kommunikation und Planung",
    "NTG": "Naturwissenschaftliche und technische Gesetzmäßigkeiten",
}
AUFGABEN = {"BWH": BWH_AUFGABEN, "ZIB": ZIB_AUFGABEN, "Recht": RECHT_AUFGABEN, "MIKP": MIKP_AUFGABEN}

BWH_LERNBEREICHE = {
    "Kostenrechnung": {
        "Fixe und variable Kosten": {
            "Fixkosten": "Fixkosten fallen innerhalb eines bestimmten Beschäftigungsbereichs unabhängig von der Produktionsmenge an.",
            "Beispiele Fixkosten": "Miete, bestimmte Gehälter und Versicherungen.",
            "Variable Kosten": "Variable Kosten verändern sich mit der Produktions- bzw. Absatzmenge.",
            "Beispiele variable Kosten": "Fertigungsmaterial und mengenabhängige Kosten.",
        },
        "Einzel- und Gemeinkosten": {
            "Einzelkosten": "Können einem Kostenträger direkt zugerechnet werden.",
            "Gemeinkosten": "Können einem Kostenträger nicht direkt zugerechnet werden und werden beispielsweise über Zuschlagssätze verteilt.",
        },
        "Deckungsbeitrag": {
            "Definition": "Der Deckungsbeitrag ist der Betrag, der nach Abzug der variablen Kosten zur Deckung der Fixkosten verbleibt.",
            "Stückdeckungsbeitrag": "db = p - kv", "Gesamtdeckungsbeitrag": "DB = db × x",
        },
        "Break-even": {
            "Definition": "Am Break-even-Point sind Erlöse und Gesamtkosten gleich.",
            "Bedeutung": "Es entsteht weder Gewinn noch Verlust.", "Formel": "xBEP = Kf / db",
        },
        "Make-or-buy": {
            "Definition": "Entscheidung zwischen Eigenfertigung und Fremdbezug.",
            "Kostenfaktoren": "Fixkosten der Eigenfertigung, variable Stückkosten und Fremdbezugspreis.",
            "Weitere Faktoren": "Qualität, Kapazität, Know-how, Lieferabhängigkeit und Versorgungssicherheit.",
        },
    },
    "Materialwirtschaft": MATERIALWIRTSCHAFT_LERNEN,
    "Arbeitsentgelt": ARBEITSENTGELT_LERNEN,
    "Unternehmensformen": UNTERNEHMENSFORMEN_LERNEN,
    "Organisation": ORGANISATION_LERNEN,
    "Fertigungsorganisation": FERTIGUNGSORGANISATION_LERNEN,
    "Kapazitätswirtschaft": KAPAZITAETSWIRTSCHAFT_LERNEN,
    "Unternehmenszusammenschlüsse": UNTERNEHMENSZUSAMMENSCHLUESSE_LERNEN,
    "Investitionsrechnung": INVESTITIONSRECHNUNG_LERNEN,
    "Betriebliche Kennzahlen": BETRIEBLICHE_KENNZAHLEN_LERNEN,
}
LERNBEREICHE = {"BWH": BWH_LERNBEREICHE, "ZIB": ZIB_LERNBEREICHE, "Recht": RECHT_LERNBEREICHE, "MIKP": MIKP_LERNBEREICHE}

FORMELBEREICHE = {
    "Kostenrechnung": {"formeln": KOSTENRECHNUNG_FORMELN, "zeichen": KOSTENRECHNUNG_ZEICHEN},
    "Materialwirtschaft": {"formeln": MATERIALWIRTSCHAFT_FORMELN, "zeichen": MATERIALWIRTSCHAFT_ZEICHEN},
    "Arbeitsentgelt": {"formeln": ARBEITSENTGELT_FORMELN, "zeichen": None},
}

# ============================================================
# PERSISTENTER LERNFORTSCHRITT
# ============================================================
PROGRESS_FILE = Path(__file__).with_name("lernfortschritt.json")

def _default_progress():
    return {"version": 1, "items": {}, "activity": {}, "exam_history": []}

def load_progress():
    try:
        if PROGRESS_FILE.exists():
            data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "items" in data:
                return data
    except Exception:
        pass
    return _default_progress()

def save_progress():
    try:
        tmp = PROGRESS_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(st.session_state.progress, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(PROGRESS_FILE)
    except Exception as exc:
        st.session_state["save_warning"] = str(exc)

if "progress" not in st.session_state:
    st.session_state.progress = load_progress()
if "search_open" not in st.session_state:
    st.session_state.search_open = None
if "today_queue" not in st.session_state:
    st.session_state.today_queue = []
if "weak_queue" not in st.session_state:
    st.session_state.weak_queue = []
if "exam" not in st.session_state:
    st.session_state.exam = None

# Einmalige Übernahme eines noch offenen Fortschritts aus älteren App-Versionen.
if st.session_state.get("geloeste_aufgaben") and not st.session_state.progress.get("items"):
    all_by_id = {a["id"]: (f, a) for f, arr in AUFGABEN.items() for a in arr}
    for old_id in st.session_state.get("geloeste_aufgaben", []):
        if old_id in all_by_id:
            old_fach, old_a = all_by_id[old_id]
            st.session_state.progress["items"][old_id] = {
                "fach": old_fach, "thema": old_a.get("thema", ""), "attempts": 1, "correct": 1,
                "confidence": 2, "last_review": datetime.now().isoformat(timespec="seconds"),
                "next_due": (date.today() + timedelta(days=6)).isoformat(),
            }
    save_progress()


def mark_activity():
    key = date.today().isoformat()
    st.session_state.progress.setdefault("activity", {})[key] = st.session_state.progress.setdefault("activity", {}).get(key, 0) + 1


def record_result(a, fach, correct, confidence=None):
    aid = a["id"]
    item = st.session_state.progress.setdefault("items", {}).setdefault(aid, {
        "fach": fach, "thema": a.get("thema", ""), "attempts": 0, "correct": 0,
        "confidence": 0, "last_review": None, "next_due": None,
    })
    item["fach"] = fach
    item["thema"] = a.get("thema", "")
    item["attempts"] = int(item.get("attempts", 0)) + 1
    if correct:
        item["correct"] = int(item.get("correct", 0)) + 1
    if confidence is not None:
        item["confidence"] = int(confidence)
    item["last_review"] = datetime.now().isoformat(timespec="seconds")
    # Einfaches, robustes Spaced-Repetition-Schema
    if not correct or confidence == 0:
        days = 0
    elif confidence == 1:
        days = 2
    elif confidence == 2:
        days = 6
    else:
        days = 10
    item["next_due"] = (date.today() + timedelta(days=days)).isoformat()
    mark_activity()
    save_progress()


def update_confidence(a, fach, confidence, correct=None):
    """Ändert Sicherheit/Wiederholungsabstand, ohne einen Versuch doppelt zu zählen."""
    aid = a["id"]
    item = st.session_state.progress.setdefault("items", {}).setdefault(aid, {
        "fach": fach, "thema": a.get("thema", ""), "attempts": 1, "correct": 1 if correct else 0,
        "confidence": 0, "last_review": datetime.now().isoformat(timespec="seconds"), "next_due": None,
    })
    item["confidence"] = int(confidence)
    if correct is False and item.get("correct", 0) > item.get("attempts", 0):
        item["correct"] = item.get("attempts", 0)
    days = 0 if confidence == 0 else (2 if confidence == 1 else (6 if confidence == 2 else 10))
    item["next_due"] = (date.today() + timedelta(days=days)).isoformat()
    item["last_review"] = datetime.now().isoformat(timespec="seconds")
    save_progress()


def mastery_for_id(aid):
    item = st.session_state.progress.get("items", {}).get(aid)
    if not item or item.get("attempts", 0) == 0:
        return None
    accuracy = item.get("correct", 0) / max(item.get("attempts", 1), 1)
    conf = item.get("confidence", 0) / 3
    return max(0.0, min(1.0, accuracy * 0.75 + conf * 0.25))


def theme_stats(fach):
    grouped = defaultdict(list)
    for a in AUFGABEN.get(fach, []):
        grouped[a.get("thema", "")].append(a)
    out = {}
    for thema, arr in grouped.items():
        vals = [mastery_for_id(a["id"]) for a in arr]
        known = [v for v in vals if v is not None]
        attempts = sum(st.session_state.progress.get("items", {}).get(a["id"], {}).get("attempts", 0) for a in arr)
        out[thema] = {"mastery": (sum(known)/len(known) if known else None), "attempts": attempts, "known": len(known), "total": len(arr)}
    return out


def fach_progress(fach):
    vals = [mastery_for_id(a["id"]) for a in AUFGABEN.get(fach, [])]
    known = [v for v in vals if v is not None]
    return (sum(known)/len(known) if known else 0.0), len(known), len(vals)


def streak_days():
    activity = st.session_state.progress.get("activity", {})
    streak = 0
    d = date.today()
    while activity.get(d.isoformat(), 0) > 0:
        streak += 1
        d -= timedelta(days=1)
    return streak

# ============================================================
# ALLGEMEINE HILFSFUNKTIONEN
# ============================================================
def norm(text):
    text = unicodedata.normalize("NFKD", str(text)).casefold()
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text).split())

def flatten(obj):
    if isinstance(obj, dict): return " ".join(f"{k} {flatten(v)}" for k,v in obj.items())
    if isinstance(obj, (list, tuple, set)): return " ".join(flatten(v) for v in obj)
    return str(obj)


STOPWORDS = {
    "der","die","das","den","dem","des","ein","eine","einer","eines","einem","einen","und","oder","bzw","bzw.","ist","sind","wird","werden","bei","mit","von","zu","zum","zur","im","in","am","an","auf","fur","für","als","auch","durch","bzw","kann","konnen","können","muss","mussen","müssen","soll","sollen","grundsatzlich","grundsätzlich","beispielsweise","weitere","dazu","dabei","je","nach","nicht","nur","bzw"
}

SYNONYM_GROUPS = [
    {"regelmassig","regelmaessig","regelmäßig","wiederholbar","wiederkehrend","gleichartig","gleich","gleiche","standardisiert","wiederholt"},
    {"messbar","messbare","mengenmassig","mengenmaessig","mengenmäßig","quantifizierbar","erfassbar","zahlbar"},
    {"beeinflussen","beeinflussbar","einfluss","steuerbar","selbst","eigenleistung"},
    {"vorgabezeit","vorgabezeiten","normalleistung","normalleistungen","sollzeit","sollzeiten","zeitvorgabe","zeitvorgaben"},
    {"verfugbarkeit","verfuegbarkeit","verfügbarkeit","nutzbar","erreichbar","verfugbar","verfuegbar","zuganglich"},
    {"integritat","integritaet","integrität","korrekt","unverandert","unveraendert","vollstandig","vollständig"},
    {"vertraulichkeit","vertraulich","berechtigt","zugriffsschutz","geheimhaltung"},
    {"backup","backups","datensicherung","sicherung","sicherungen"},
    {"redundant","redundanz","ersatzsystem","ausfallsicherheit"},
    {"authentifizierung","mfa","mehrfaktor","passwort","anmeldung"},
    {"verschluesselung","verschlusselung","verschlüsselung","encrypt"},
    {"abmahnung","abmahnen"}, {"kundigung","kuendigung","kündigung","kundigen","kuendigen"},
    {"schriftform","schriftlich"}, {"mundlich","muendlich","mündlich","telefonisch","telefon"},
    {"betriebsrat","br"}, {"mitbestimmung","mitbestimmungsrecht"}, {"anhoerung","anhörung","anhören","anhoeren"},
    {"gmbh","gesellschaft mit beschrankter haftung","gesellschaft mit beschraenkter haftung"},
    {"ag","aktiengesellschaft"}, {"geschaftsfuhrer","geschaeftsfuehrer","geschäftsführer"}, {"vorstand","aufsichtsrat","hauptversammlung"},
    {"fixkosten","fixe","fix"}, {"variable","variabel","variablekosten"}, {"deckungsbeitrag","db"},
    {"motivation","motivieren","motiviert"}, {"intrinsisch","innerer","innen"}, {"extrinsisch","ausserer","aeusserer","äußerer"},
    {"brainstorming","ideenfindung","ideen"}, {"nutzwertanalyse","nwa"}, {"paarweiser","paarvergleich","paarweisen"},
    {"kritischer","kritisch","kritische"}, {"puffer","gesamtpuffer","gp"}, {"faz","fruhester anfang","fruehester anfang"}, {"fez","fruhestes ende","fruehestes ende"},
]

SYNMAP = {}
for _group in SYNONYM_GROUPS:
    canon = sorted(norm(x) for x in _group if norm(x))[0]
    for _x in _group:
        for _tok in norm(_x).split():
            SYNMAP[_tok] = canon

def _canon_token(tok):
    # kleine Wortstamm-Normalisierung für typische freie Prüfungsformulierungen
    stem_rules = [
        (("messbar","messbare","mengenmess"), "messbar"),
        (("regelmass","regelmaess","wiederhol","wiederkehr","gleichartig","gleiche"), "wiederholbar"),
        (("beeinfluss","steuerbar"), "beeinflussbar"),
        (("vorgabezeit","sollzeit","zeitvorgab"), "vorgabezeit"),
        (("normalleist",), "normalleistung"),
        (("verfug","verfueg","nutzbar","erreichbar"), "verfugbarkeit"),
        (("integrit","korrekt","unverand","unveraend","vollstandig"), "integritat"),
        (("vertraulich","berechtig","zugriffsschutz"), "vertraulichkeit"),
        (("kundig","kuendig"), "kundigung"),
        (("schriftlich","schriftform"), "schriftform"),
        (("mundlich","muendlich","telefon"), "mundlich"),
        (("motiv" ,), "motivation"),
    ]
    for starts, canon in stem_rules:
        if any(tok.startswith(x) for x in starts): return canon
    return SYNMAP.get(tok,tok)

def semantic_tokens(text):
    toks=[]
    for tok in norm(text).split():
        if len(tok) < 2 or tok in STOPWORDS: continue
        toks.append(_canon_token(tok))
    return toks

def _keywords(text, limit=8):
    toks=semantic_tokens(text)
    seen=[]
    for t in toks:
        if t not in seen and (len(t)>=4 or any(ch.isdigit() for ch in t)):
            seen.append(t)
    return seen[:limit]

def _concept_match(user_tokens, solution_text):
    keys=_keywords(solution_text,10)
    if not keys: return 0.0, []
    us=set(user_tokens)
    hits=[k for k in keys if k in us]
    ratio=len(hits)/len(keys)
    # Ein Kernpunkt gilt als erkannt, wenn mindestens ein markanter Fachbegriff getroffen wurde;
    # bei langen Lösungspunkten verlangen wir mehr Überdeckung.
    if len(keys)<=2: score=1.0 if hits else 0.0
    elif len(keys)<=4: score=min(1.0, ratio*1.65)
    else: score=min(1.0, ratio*1.9)
    return score,hits

def evaluate_open_answer(answer, task):
    """Lokale, tolerante Inhaltsbewertung. Kein Online-KI-Dienst; bewertet Kernbegriffe/Synonyme und Teilaspekte."""
    ml=task.get("musterloesung",[])
    points=ml if isinstance(ml,list) else [str(ml)]
    user_tokens=semantic_tokens(answer)
    if not user_tokens:
        return {"score":0,"matched":[],"missing":points,"label":"Noch nicht ausreichend"}
    matched=[]; missing=[]; raw=[]
    for p in points:
        sc,hits=_concept_match(user_tokens,str(p)); raw.append(sc)
        if sc>=0.34: matched.append(str(p))
        else: missing.append(str(p))
    # Prozentwert primär nach erkannten Kernpunkten, mit Teilpunkten bei semantischer Überdeckung.
    if points:
        score=round(100*sum(raw)/len(points))
    else: score=0
    # Kurze Nennen-Aufgaben: Zahl der geforderten Aspekte nicht künstlich durch lange Musterlösung benachteiligen.
    q=norm(task.get("aufgabe",""))
    m=re.search(r"\b(\d+)\b",q)
    expected=int(m.group(1)) if m else None
    if expected is None:
        for word,num in {"eine":1,"einen":1,"zwei":2,"drei":3,"vier":4,"funf":5,"fuenf":5,"sechs":6}.items():
            if re.search(rf"\b{word}\b",q): expected=num; break
    if expected and expected>0 and matched:
        score=max(score, min(100, round(100*min(len(matched),expected)/expected)))
    score=max(0,min(100,score))
    label="Fachlich ausreichend" if score>=80 else ("Teilweise richtig" if score>=40 else "Noch nicht ausreichend")
    return {"score":score,"matched":matched,"missing":missing,"label":label}

def display_key(key):
    mapping = {"erklaerung":"Erklärung", "musterloesung":"Musterlösung", "loesungsweg":"Lösungsweg", "foerderung":"Förderung", "anlaesse":"Anlässe", "bedeutung_fuer_meister":"Bedeutung für den Meister"}
    s = mapping.get(str(key).lower(), str(key).replace("_"," "))
    return s[:1].upper()+s[1:] if s else s

def render_content(value, level=0):
    if isinstance(value, dict):
        for k,v in value.items():
            st.markdown(("### " if level == 0 else "**") + display_key(k) + ("" if level == 0 else "**"))
            render_content(v, level+1)
    elif isinstance(value, list):
        for x in value: st.write(f"• {x}")
    else:
        st.write(value)

def learning_cards(fach, thema=None):
    cards=[]
    for t, area in LERNBEREICHE.get(fach, {}).items():
        if thema and thema != "__ALLE__" and t != thema: continue
        if isinstance(area, dict):
            for title, content in area.items(): cards.append((t,title,content))
    return cards

def priority(fach, thema):
    if fach == "BWH": return BWH_THEMEN.get(thema, {}).get("prioritaet", "")
    src = {"ZIB":ZIB_THEMEN,"Recht":RECHT_THEMEN,"MIKP":MIKP_THEMEN}.get(fach,[])
    for d in src:
        if d.get("name") == thema: return d.get("prioritaet", "")
    return ""

def topic_names(fach):
    if fach == "BWH": return list(BWH_THEMEN.keys())
    return [d["name"] for d in {"ZIB":ZIB_THEMEN,"Recht":RECHT_THEMEN,"MIKP":MIKP_THEMEN}.get(fach,[])]

def type_label(a):
    if a.get("modus") == "gesetzesarbeit": return "Gesetzesarbeit"
    if a.get("typ") == "offen": return "Offene Frage"
    if a.get("typ") == "multiple_choice": return "Multiple Choice"
    return "Rechnen / Methode"

# ============================================================
# VISUELLES LERNEN – ALLE FÄCHER
# ============================================================
def box(text, bg="#eef6ff", border="#b9d6f4"):
    return f"<div style='padding:14px 16px;border:1px solid {border};background:{bg};border-radius:12px;text-align:center;font-weight:650;line-height:1.45'>{text}</div>"
def row(items):
    return "<div style='display:flex;gap:12px;flex-wrap:wrap;align-items:stretch'>" + "".join(f"<div style='flex:1;min-width:150px'>{x}</div>" for x in items) + "</div>"
def flow(items):
    return "<div style='display:flex;gap:7px;align-items:center;flex-wrap:wrap'>" + "".join(f"<div style='flex:1;min-width:145px'>{box(x)}</div>" + ("<div style='font-size:24px'>→</div>" if i < len(items)-1 else "") for i,x in enumerate(items)) + "</div>"
def render_visual_html(content, title=None):
    if title:
        st.markdown(f"### {title}")
    st.markdown(f"<div class='soft-card'>{content}</div>", unsafe_allow_html=True)


def vega_chart(kind, title="Beispiel", categories=None, values=None, x=None, y=None, x_label="", y_label="Wert"):
    """Diagramme ohne matplotlib: nutzt Streamlits eingebautes Vega-Lite."""
    try:
        if kind in ("bar", "line"):
            categories = categories or ["A", "B", "C", "D"]
            values = values or [18, 31, 24, 39]
            data = [{"Kategorie": str(c), "Wert": float(v)} for c, v in zip(categories, values)]
            mark = {"type": "bar", "tooltip": True} if kind == "bar" else {"type": "line", "point": True, "tooltip": True}
            spec = {
                "mark": mark,
                "encoding": {
                    "x": {"field": "Kategorie", "type": "ordinal", "title": x_label or None},
                    "y": {"field": "Wert", "type": "quantitative", "title": y_label},
                    "tooltip": [{"field":"Kategorie"},{"field":"Wert"}]
                },
                "title": title,
                "height": 250,
            }
            st.vega_lite_chart(data, spec, use_container_width=True)
            return
        if kind == "scatter":
            x = x or [1,2,3,4,5,6,7]
            y = y or [2,3,3.5,5.2,5.8,7.1,8.4]
            data = [{"X": float(a), "Y": float(b)} for a,b in zip(x,y)]
            spec = {
                "mark": {"type":"point", "filled":True, "size":90, "tooltip":True},
                "encoding": {
                    "x": {"field":"X", "type":"quantitative", "title": x_label or "Merkmal X"},
                    "y": {"field":"Y", "type":"quantitative", "title": y_label or "Merkmal Y"},
                    "tooltip": [{"field":"X"},{"field":"Y"}]
                },
                "title": title,
                "height": 250,
            }
            st.vega_lite_chart(data, spec, use_container_width=True)
            return
        if kind == "pie":
            categories = categories or ["A","B","C"]
            values = values or [45,30,25]
            data = [{"Kategorie":str(c), "Wert":float(v)} for c,v in zip(categories,values)]
            spec = {
                "mark": {"type":"arc", "innerRadius":35, "tooltip":True},
                "encoding": {
                    "theta": {"field":"Wert", "type":"quantitative"},
                    "color": {"field":"Kategorie", "type":"nominal"},
                    "tooltip": [{"field":"Kategorie"},{"field":"Wert"}]
                },
                "title": title,
                "height": 250,
            }
            st.vega_lite_chart(data, spec, use_container_width=True)
            return
    except Exception:
        # Selbst bei sehr alten Streamlit-Versionen bleibt eine verständliche Darstellung sichtbar.
        if kind == "pie":
            render_visual_html(row([box(f"{c}: {v}") for c,v in zip(categories or [], values or [])]))
        else:
            render_visual_html(row([box(f"{c}: {v}") for c,v in zip(categories or [], values or [])]))


def safe_plot(kind, title="Beispiel"):
    if kind == "bar":
        vega_chart("bar", title, ["A","B","C","D"], [18,31,24,39], y_label="Wert")
    elif kind == "line":
        vega_chart("line", title, ["Jan","Feb","Mär","Apr","Mai"], [20,26,24,34,41], y_label="Wert")
    elif kind == "scatter":
        vega_chart("scatter", title, x=[1,2,3,4,5,6,7], y=[2,3,3.5,5.2,5.8,7.1,8.4], x_label="Merkmal X", y_label="Merkmal Y")
    elif kind == "pie":
        vega_chart("pie", title, ["A","B","C"], [45,30,25])


def abc_visual():
    # bewusst ohne matplotlib, damit es auf der lokalen LernApp immer funktioniert
    data = [
        {"Positionsanteil":0,"Wertanteil":0},{"Positionsanteil":10,"Wertanteil":50},
        {"Positionsanteil":20,"Wertanteil":80},{"Positionsanteil":35,"Wertanteil":88},
        {"Positionsanteil":50,"Wertanteil":93},{"Positionsanteil":60,"Wertanteil":95},
        {"Positionsanteil":80,"Wertanteil":98},{"Positionsanteil":100,"Wertanteil":100},
    ]
    try:
        spec = {
            "layer": [
                {"mark":{"type":"line","point":True,"strokeWidth":3,"tooltip":True},
                 "encoding": {
                     "x":{"field":"Positionsanteil","type":"quantitative","title":"Kumulierter Positionsanteil in %","scale":{"domain":[0,100]}},
                     "y":{"field":"Wertanteil","type":"quantitative","title":"Kumulierter Wertanteil in %","scale":{"domain":[0,100]}},
                     "tooltip":[{"field":"Positionsanteil"},{"field":"Wertanteil"}]
                 }}
            ],
            "title":"Typische ABC-Kurve",
            "height":300,
        }
        st.vega_lite_chart(data, spec, use_container_width=True)
    except Exception:
        st.markdown("**Typische ABC-Verteilung:** A ≈ wenige Positionen mit sehr hohem Wertanteil, B = mittlere Bedeutung, C = viele Positionen mit geringem Einzelwert.")
    c1,c2,c3=st.columns(3)
    with c1: st.info("**A-Güter**\n\nwenige Positionen · hoher Wertanteil · eng steuern")
    with c2: st.info("**B-Güter**\n\nmittlere Positionen · mittlerer Wertanteil · normal steuern")
    with c3: st.info("**C-Güter**\n\nviele Positionen · geringer Einzelwert · vereinfachen")
def generic_visual(fach, thema, titel, content):
    text = norm(f"{thema} {titel} {flatten(content)}")

    # Spezifische, prüfungsrelevante Modelle
    if "abc analyse" in text:
        st.markdown("### Visualisierung")
        abc_visual(); st.caption("A = wenige besonders wichtige Positionen · B = mittlere Bedeutung · C = viele weniger wichtige Positionen."); return
    if "netzplan" in text or "kritisch" in text or "vorwartsrechnung" in text or "ruckwartsrechnung" in text:
        st.markdown("### Visualisierung")
        dot='''digraph { rankdir=LR; node [shape=record, fontname="Arial"]; A [label="{A|Dauer 3|FAZ 0 · FEZ 3|SAZ 0 · SEZ 3|GP 0}", penwidth=3]; B [label="{B|Dauer 4|FAZ 3 · FEZ 7|SAZ 3 · SEZ 7|GP 0}", penwidth=3]; C [label="{C|Dauer 2|FAZ 3 · FEZ 5|SAZ 5 · SEZ 7|GP 2}"]; D [label="{D|Dauer 3|FAZ 7 · FEZ 10|SAZ 7 · SEZ 10|GP 0}", penwidth=3]; A -> B [penwidth=3]; A -> C; B -> D [penwidth=3]; C -> D; }'''
        st.graphviz_chart(dot, use_container_width=True); st.caption("Beispiel: A → B → D ist der kritische Pfad; dort beträgt der Gesamtpuffer 0."); return
    if "flussdiagramm" in text or "ablauf" in text and fach == "MIKP":
        st.markdown("### Visualisierung")
        dot='''digraph { rankdir=TB; node [fontname="Arial"]; S [label="Start",shape=oval]; A [label="Auftrag prüfen",shape=box]; E [label="Alles vollständig?",shape=diamond]; B [label="Bearbeiten",shape=box]; N [label="Fehlende Infos anfordern",shape=box]; Z [label="Ende",shape=oval]; S->A->E; E->B [label="Ja"]; E->N [label="Nein"]; N->A; B->Z; }'''
        st.graphviz_chart(dot, use_container_width=True); st.caption("Oval = Start/Ende · Rechteck = Tätigkeit · Raute = Entscheidung."); return
    if "diagramm" in text or "visualisierung" in text or "haufigkeit" in text or "kennzahl" in text:
        st.markdown("### Visualisierung")
        c1,c2=st.columns(2)
        with c1: safe_plot("bar","Säule/Balken – Vergleich")
        with c2: safe_plot("line","Linie – Entwicklung")
        st.caption("Kreis = Anteile eines Ganzen · Streuung = Zusammenhang zweier Merkmale. Achsen und Einheiten immer beschriften."); return
    if "break even" in text or "deckungsbeitrag" in text:
        st.markdown("### Visualisierung")
        data=[]
        for menge in range(0,101,10):
            data.append({"Menge":menge,"Wert":5000+70*menge,"Art":"Gesamtkosten"})
            data.append({"Menge":menge,"Wert":120*menge,"Art":"Erlöse"})
        try:
            spec={
                "mark":{"type":"line","point":True,"tooltip":True},
                "encoding":{
                    "x":{"field":"Menge","type":"quantitative","title":"Menge"},
                    "y":{"field":"Wert","type":"quantitative","title":"€"},
                    "color":{"field":"Art","type":"nominal"},
                    "tooltip":[{"field":"Art"},{"field":"Menge"},{"field":"Wert"}]
                },
                "title":"Break-even-Prinzip","height":280
            }
            st.vega_lite_chart(data,spec,use_container_width=True)
        except Exception:
            render_visual_html(flow(["Fixkosten + variable Kosten","= Gesamtkosten","Schnittpunkt mit Erlös","= Break-even"]))
        return
    if any(k in text for k in ["forming","storming","norming","performing","gruppenphase"]):
        render_visual_html(flow(["1️⃣ Forming<br><small>Orientierung</small>","2️⃣ Storming<br><small>Konflikt</small>","3️⃣ Norming<br><small>Regeln</small>","4️⃣ Performing<br><small>Leistung</small>"]),"🧩 Gruppenphasen"); return
    if "motivation" in text or "maslow" in text or "herzberg" in text:
        render_visual_html("<div style='max-width:760px;margin:auto'>"+"".join([
            box("🌱 Selbstverwirklichung","#eaf8ee"), box("🏆 Wertschätzung","#eef6ff"), box("🤝 Soziale Bedürfnisse","#fff4df"), box("🛡️ Sicherheit","#f5f1ff"), box("🍽️ Grundbedürfnisse","#fff0f0")]) + "</div>","🎯 Motivation – Bedürfnisebenen"); return
    if "eisberg" in text or "kommunikation" in text or "gesprach" in text or "aktives zuhoren" in text:
        render_visual_html(row([box("🗣️ Sender<br><small>Botschaft + Körpersprache</small>"),box("➡️ Kanal"),box("👂 Empfänger<br><small>Wahrnehmen + deuten</small>"),box("↩️ Rückmeldung")]),"💬 Kommunikation als Kreislauf"); return
    if "konflikt" in text:
        render_visual_html(flow(["⚡ Wahrnehmen","👂 Sichtweisen klären","🧩 Ursachen trennen","💡 Lösungen entwickeln","🤝 Vereinbarung"]),"🤝 Konfliktbearbeitung"); return
    if "fuhrung" in text or "deleg" in text:
        render_visual_html(row([box("🎯 Ziel klären"),box("👤 Können & Wollen einschätzen"),box("🧭 Führungsverhalten wählen"),box("✅ Ergebnis kontrollieren")]),"🧭 Situativ führen"); return
    if "betriebsrat" in text or "mitbestimmung" in text:
        render_visual_html(row([box("ℹ️ Information"),box("💬 Anhörung / Beratung"),box("🤝 Mitwirkung"),box("✋ Mitbestimmung","#fff4df")]),"🏛️ Beteiligungsrechte – zunehmende Stärke"); return
    if "kundigung" in text or "arbeitsvertrag" in text or "beendigung" in text:
        render_visual_html(flow(["📄 Arbeitsverhältnis","⚠️ Kündigungsgrund / Anlass","🧑‍⚖️ Form + Frist + Beteiligung","📬 Zugang","🏁 Beendigung"]),"⚖️ Prüfschema Kündigung"); return
    if "arbeitszeit" in text or "urlaub" in text or "entgeltfortzahlung" in text:
        render_visual_html(row([box("⏱️ Arbeitszeit"),box("☕ Ruhepause"),box("🌙 Ruhezeit"),box("🏖️ Urlaub / Krankheit")]),"🕒 Zeitliche Schutzregeln"); return
    if "tarif" in text or "arbeitskampf" in text:
        render_visual_html(row([box("👥 Gewerkschaft"),box("↔️ Tarifverhandlung"),box("🏭 Arbeitgeber / Verband")]),"🤝 Tarifautonomie"); return
    if "sozialversicherung" in text:
        render_visual_html(row([box("🏥 Kranken"),box("👴 Renten"),box("💼 Arbeitslosen"),box("🧑‍🦽 Pflege"),box("⛑️ Unfall")]),"🛡️ Zweige der Sozialversicherung"); return
    if "arbeitsschutz" in text or "gesundheitsschutz" in text:
        render_visual_html(flow(["S – Substitution","T – Technische Maßnahmen","O – Organisatorische Maßnahmen","P – Persönliche Maßnahmen"]),"🦺 STOP-Prinzip"); return
    if "datenschutz" in text or "datensicherheit" in text:
        render_visual_html(row([box("🔒 Vertraulichkeit"),box("✅ Integrität"),box("🟢 Verfügbarkeit")]),"🔐 Schutzziele"); return
    if "projekt" in text or "magisches dreieck" in text:
        st.markdown("### Visualisierung")
        dot='''graph { layout=neato; overlap=false; node [shape=ellipse,fontname="Arial"]; Q [label="Qualität / Leistung", pos="0,1!"]; Z [label="Zeit / Termine", pos="-1,-1!"]; K [label="Kosten", pos="1,-1!"]; Q--Z; Z--K; K--Q; }'''
        st.graphviz_chart(dot, use_container_width=True); st.caption("Ändert sich eine Ecke, beeinflusst das meist die beiden anderen."); return
    if "nutzwert" in text or "paarweiser vergleich" in text or "entscheidung" in text:
        render_visual_html(flow(["📋 Kriterien","⚖️ Gewichten","⭐ Bewerten","✖️ Teilnutzwerte","➕ Summe","🏆 Entscheidung"]),"⚖️ Nutzwertanalyse"); return
    if "eisenhower" in text:
        render_visual_html("<div style='display:grid;grid-template-columns:1fr 1fr;gap:10px'>"+box("🔥 wichtig + dringend<br>SOFORT","#ffecec")+box("📅 wichtig + nicht dringend<br>TERMINIEREN","#eef6ff")+box("🤝 nicht wichtig + dringend<br>DELEGIEREN","#fff4df")+box("🗑️ nicht wichtig + nicht dringend<br>REDUZIEREN","#f2f2f2")+"</div>","⏳ Eisenhower-Matrix"); return
    if "alpen" in text:
        render_visual_html(flow(["A – Aufgaben","L – Länge schätzen","P – Puffer","E – Entscheidungen","N – Nachkontrolle"]),"🏔️ ALPEN-Methode"); return
    if "pareto" in text:
        render_visual_html(row([box("20 % wichtige Ursachen","#fff4df"),box("➡️"),box("80 % der Wirkung","#eaf8ee")]),"📈 Pareto-Prinzip"); return
    if "organisation" in text or "organigramm" in text:
        st.markdown("### Visualisierung")
        dot='''digraph { rankdir=TB; node [shape=box,fontname="Arial"]; L [label="Unternehmensleitung"]; P [label="Produktion"]; V [label="Vertrieb"]; E [label="Einkauf"]; M [label="Meisterbereich"]; L->P; L->V; L->E; P->M; }'''; st.graphviz_chart(dot,use_container_width=True); return
    if "investition" in text or "amortisation" in text or "kapitalwert" in text:
        render_visual_html(flow(["💸 Auszahlung t₀","📥 Rückflüsse","⏱️ Zeitwert beachten","📊 Verfahren anwenden","✅ Entscheidung"]),"💰 Investitionsrechnung"); return
    if "qualifikation" in text or "kompetenz" in text or "personalentwicklung" in text:
        render_visual_html(row([box("🧠 Fachkompetenz"),box("🛠️ Methodenkompetenz"),box("🤝 Sozialkompetenz"),box("🙋 Selbstkompetenz")]),"🎓 Kompetenzfelder"); return
    if "unternehmensform" in text:
        render_visual_html(row([box("👤 Einzelunternehmen"),box("👥 Personengesellschaft"),box("🏢 Kapitalgesellschaft")]),"🏢 Unternehmensformen – Grundstruktur"); return
    if "fertigung" in text:
        render_visual_html(flow(["📦 Material","⚙️ Bearbeitung 1","🔧 Bearbeitung 2","✅ Prüfung","🚚 Fertigteil"]),"🏭 Fertigungsablauf"); return
    if "kapazitat" in text:
        render_visual_html(row([box("🧑 Personal"),box("⚙️ Maschinen"),box("⏱️ Zeit"),box("📈 Ausbringung")]),"📊 Kapazitätstreiber"); return
    if "arbeitsentgelt" in text or "lohn" in text:
        render_visual_html(row([box("⏱️ Zeitlohn"),box("📦 Akkordlohn"),box("🎯 Prämienlohn")]),"💶 Entgeltformen"); return
    if "material" in text or "beschaffung" in text or "lager" in text:
        render_visual_html(flow(["📋 Bedarf","🛒 Beschaffung","📦 Wareneingang","🏬 Lager","⚙️ Verbrauch"]),"📦 Materialfluss"); return
    # Fallback: Jede Lernkarte hat wenigstens eine inhaltlich neutrale Lernskizze.
    render_visual_html(flow([f"📘 <b>{titel}</b>","🔎 Kernaussage verstehen","🏭 Praxisbezug herstellen","🎓 In Prüfungsantwort übertragen"]),"🧠 Lernbild")


def render_learning_card(fach, thema, titel, content):
    st.caption(f"{fach} · {thema} · Prüfungsrelevanz: {priority(fach,thema) or '—'}")
    st.markdown(f"## {titel}")
    generic_visual(fach,thema,titel,content)
    st.markdown("### Lerninhalt")
    render_content(content)
    st.markdown("<div class='merke'><b>Merksatz:</b> Erst das Prinzip verstehen, dann ein Beispiel nennen und anschließend auf die betriebliche Situation übertragen.</div>",unsafe_allow_html=True)

# ============================================================
# GRAFISCHE MUSTERLÖSUNGEN AUS AUFGABEN
# ============================================================
def task_visual(a):
    vis=a.get("visualisierung")
    if not vis: return
    st.markdown("### 📊 Grafische Musterlösung")
    typ=vis.get("typ")
    if typ=="balken":
        vega_chart("bar",vis.get("titel","Musterdiagramm"),vis.get("kategorien",[]),vis.get("werte",[]),y_label=vis.get("ylabel","Wert"))
    elif typ=="linie":
        vega_chart("line",vis.get("titel","Musterdiagramm"),vis.get("kategorien",[]),vis.get("werte",[]),y_label=vis.get("ylabel","Wert"))
    elif typ=="kreis":
        vega_chart("pie",vis.get("titel","Musterdiagramm"),vis.get("kategorien",[]),vis.get("werte",[]))
    elif typ=="streu":
        vega_chart("scatter",vis.get("titel","Musterdiagramm"),x=vis.get("x",[]),y=vis.get("y",[]),x_label=vis.get("xlabel","x"),y_label=vis.get("ylabel","y"))
    elif typ=="flussdiagramm":
        generic_visual("MIKP","Netzplantechnik und Ablaufplanung","Flussdiagramm",{})
    elif typ=="netzplan":
        generic_visual("MIKP","Netzplantechnik und Ablaufplanung","Netzplan",{})

# ============================================================
# SUCHFUNKTION – DIREKT ÖFFNEN, OPTIONAL ALLE FÄCHER
# ============================================================
def search_ui(current_fach, suffix):
    c1,c2=st.columns([3,1])
    with c1:
        q=st.text_input("🔎 Suche",placeholder="z. B. ABC-Analyse, Motivation, Netzplan, Betriebsrat ...",key=f"search_{current_fach}_{suffix}")
    with c2:
        scope=st.selectbox("Suchbereich",["Aktuelles Fach","Alle Fächer"],key=f"scope_{current_fach}_{suffix}")
    if not q.strip(): return
    nq=norm(q)
    fachliste=[current_fach] if scope=="Aktuelles Fach" else ["BWH","ZIB","Recht","MIKP"]
    cards=[]; tasks=[]
    for f in fachliste:
        for t,title,content in learning_cards(f):
            hay=norm(f"{f} {t} {title} {flatten(content)}")
            if nq in hay or all(w in hay for w in nq.split()): cards.append((f,t,title,content))
        for a in AUFGABEN.get(f,[]):
            hay=norm(flatten(a))
            if nq in hay or all(w in hay for w in nq.split()): tasks.append((f,a))
    if not cards and not tasks:
        st.warning(f"Keine Treffer für **{q}** gefunden."); return
    st.caption(f"{len(cards)+len(tasks)} Treffer – klicke auf **Öffnen**, um den Inhalt direkt vollständig anzuzeigen.")
    shown=0
    for f,t,title,content in cards[:10]:
        cols=st.columns([5,1])
        with cols[0]: st.markdown(f"**📘 {title}** · {f} · {t}")
        with cols[1]:
            if st.button("Öffnen",key=f"open_card_{suffix}_{hashlib.md5((f+t+title).encode()).hexdigest()[:10]}",use_container_width=True):
                st.session_state.search_open=("card",f,t,title)
                st.rerun()
        shown+=1
    for f,a in tasks[:8]:
        cols=st.columns([5,1])
        with cols[0]: st.markdown(f"**{type_label(a)}** · {f} · {a.get('thema','')}  \
{a.get('aufgabe','')[:180]}")
        with cols[1]:
            if st.button("Öffnen",key=f"open_task_{suffix}_{f}_{a['id']}",use_container_width=True):
                st.session_state.search_open=("task",f,a["id"])
                st.rerun()
    if st.session_state.search_open:
        kind,*payload=st.session_state.search_open
        st.divider()
        top=st.columns([5,1])
        with top[0]: st.markdown("### Geöffneter Suchtreffer")
        with top[1]:
            if st.button("✕ Schließen",key=f"close_search_{suffix}",use_container_width=True): st.session_state.search_open=None; st.rerun()
        if kind=="card":
            f,t,title=payload
            match=next((x for x in learning_cards(f) if x[0]==t and x[1]==title),None)
            if match: render_learning_card(f,*match)
        else:
            f,aid=payload
            a=next((x for x in AUFGABEN.get(f,[]) if x["id"]==aid),None)
            if a:
                st.markdown(f"## {a['aufgabe']}"); render_task(a,f,f"search_{suffix}_{f}")
        st.divider()

# ============================================================
# AUFGABEN-RENDERING + ADAPTIVES LERNEN
# ============================================================
def confidence_buttons(a, fach, prefix, known_correct=True):
    st.caption("Wie sicher warst du?")
    c1,c2,c3=st.columns(3)
    with c1:
        if st.button("😕 Nochmal",key=f"{prefix}_conf0_{a['id']}",use_container_width=True): update_confidence(a,fach,0,False); st.toast("Kommt bald wieder.")
    with c2:
        if st.button("🙂 Kann ich",key=f"{prefix}_conf2_{a['id']}",use_container_width=True): update_confidence(a,fach,2,known_correct); st.toast("In einigen Tagen wiederholen.")
    with c3:
        if st.button("🧠 Sicher",key=f"{prefix}_conf3_{a['id']}",use_container_width=True): update_confidence(a,fach,3,known_correct); st.toast("Größerer Wiederholungsabstand.")

def render_task(a, fach, prefix, exam_mode=False):
    aid=a["id"]; typ=a.get("typ","rechnen")

    if typ=="multiple_choice":
        submitted=f"{prefix}_mc_submitted_{aid}"
        correct_key=f"{prefix}_mc_correct_{aid}"
        ans_key=f"{prefix}_mc_{aid}"
        ans=st.radio("Deine Antwort",a.get("antworten",[]),index=None,key=ans_key,disabled=bool(st.session_state.get(submitted)))
        if not st.session_state.get(submitted):
            if st.button("Antwort prüfen" if not exam_mode else "Antwort festhalten",key=f"{prefix}_check_{aid}",type="primary"):
                if ans is None:
                    st.warning("Bitte zuerst eine Antwort auswählen.")
                else:
                    correct=ans==a.get("richtige_antwort")
                    st.session_state[submitted]=True
                    st.session_state[correct_key]=bool(correct)
                    if exam_mode:
                        st.session_state.exam.setdefault("answers",{})[aid]={"correct":bool(correct),"submitted":True}
                    else:
                        record_result(a,fach,bool(correct),1 if correct else 0)
                    st.rerun()
        else:
            if exam_mode:
                st.success("✅ Antwort gespeichert. Die Lösung bleibt bis zum Prüfungsende verborgen.")
            else:
                correct=bool(st.session_state.get(correct_key,False))
                if correct:
                    st.success("✅ Richtig!")
                else:
                    st.error(f"❌ Noch nicht richtig. Richtige Antwort: {a.get('richtige_antwort','')}")
                if a.get("erklaerung"):
                    st.info("💡 " + str(a.get("erklaerung")))
                st.caption("⚠️ Prüfungs-Tipp: Erst den Fachbegriff nennen, dann kurz begründen. Bei vorgegebener Anzahl nur die geforderte Zahl an Antworten geben.")
                confidence_buttons(a,fach,prefix,correct)
                if st.button("↩️ Antwort ändern",key=f"{prefix}_retry_{aid}"):
                    st.session_state.pop(submitted,None); st.session_state.pop(correct_key,None); st.session_state.pop(ans_key,None); st.rerun()
        if not exam_mode and a.get("tipp") and not st.session_state.get(submitted):
            with st.expander("💡 Tipp"):
                st.write(a["tipp"])

    elif typ=="offen":
        submitted=f"{prefix}_submitted_{aid}"
        answer_key=f"{prefix}_open_{aid}"
        eval_key=f"{prefix}_open_eval_{aid}"
        answer=st.text_area("Deine Antwort",height=140,key=answer_key,disabled=bool(st.session_state.get(submitted)),placeholder="Formuliere deine Antwort in eigenen Worten …")
        if not st.session_state.get(submitted):
            if st.button("Antwort auswerten" if not exam_mode else "Antwort festhalten",key=f"{prefix}_submit_{aid}",type="primary"):
                if not str(answer or "").strip():
                    st.warning("Bitte zuerst eine Antwort eingeben.")
                else:
                    st.session_state[submitted]=True
                    if exam_mode:
                        st.session_state.exam.setdefault("answers",{})[aid]={"self_grade":None,"submitted":True,"text":str(answer)}
                    else:
                        ev=evaluate_open_answer(str(answer),a)
                        st.session_state[eval_key]=ev
                        frac=ev["score"]/100
                        record_result(a,fach,ev["score"]>=80,2 if ev["score"]>=80 else (1 if ev["score"]>=40 else 0))
                    st.rerun()
            if not exam_mode and a.get("tipp"):
                with st.expander("Hinweis"):
                    st.write(a["tipp"])
        else:
            if exam_mode:
                st.success("Antwort gespeichert. Musterlösung und Bewertung erscheinen nach Prüfungsende.")
            else:
                ev=st.session_state.get(eval_key) or evaluate_open_answer(str(st.session_state.get(answer_key,"")),a)
                score=ev.get("score",0)
                if score>=80:
                    st.markdown(f"<div class='result-good'><b>Fachlich ausreichend · {score} %</b><br><span class='muted'>Deine Formulierung darf von der Musterlösung abweichen. Entscheidend sind die erkannten Kernpunkte.</span></div>",unsafe_allow_html=True)
                elif score>=40:
                    st.markdown(f"<div class='result-mid'><b>Teilweise richtig · {score} %</b><br><span class='muted'>Wesentliche Punkte sind erkannt, für eine vollständige Prüfungsantwort fehlt noch etwas.</span></div>",unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='result-low'><b>Noch nicht ausreichend · {score} %</b><br><span class='muted'>Einige zentrale Inhalte der Musterlösung wurden noch nicht erkannt.</span></div>",unsafe_allow_html=True)
                if ev.get("matched"):
                    st.markdown("**Erkannte Kernpunkte**")
                    for p in ev["matched"]: st.write(f"✓ {p}")
                if ev.get("missing"):
                    st.markdown("**Für eine vollständigere Antwort ergänzen**")
                    for p in ev["missing"]: st.write(f"• {p}")
                with st.expander("Musterlösung anzeigen",expanded=(score<80)):
                    ml=a.get("musterloesung",[])
                    if isinstance(ml,list):
                        for p in ml: st.write(f"• {p}")
                    else: st.write(ml)
                    task_visual(a)
                st.caption("Die automatische Bewertung arbeitet lokal mit Kernpunkten, Synonymen und Teiltreffern. Bei Grenzfällen zählt weiterhin die fachliche Aussage – nicht der identische Wortlaut.")
                st.caption("Prüfungstipp: Operatoren wie nennen, beschreiben, erläutern und begründen bestimmen die erwartete Antworttiefe.")
                confidence_buttons(a,fach,prefix,score>=80)
                if st.button("Antwort ändern",key=f"{prefix}_open_retry_{aid}"):
                    st.session_state.pop(submitted,None); st.session_state.pop(eval_key,None); st.session_state.pop(answer_key,None); st.rerun()

    else:
        submitted=f"{prefix}_num_submitted_{aid}"
        correct_key=f"{prefix}_num_correct_{aid}"
        answer_key=f"{prefix}_num_{aid}"
        answer=st.number_input("Dein Ergebnis",value=None,step=.01,key=answer_key,disabled=bool(st.session_state.get(submitted)))
        if not st.session_state.get(submitted):
            if st.button("Antwort prüfen" if not exam_mode else "Ergebnis festhalten",key=f"{prefix}_numcheck_{aid}",type="primary"):
                if answer is None:
                    st.warning("Bitte zuerst ein Ergebnis eingeben.")
                else:
                    try:
                        target=float(a.get("ergebnis",0)); value=float(answer)
                    except (TypeError,ValueError):
                        st.error("Für diese Rechenaufgabe ist kein gültiges numerisches Ergebnis hinterlegt.")
                        return
                    tol=max(abs(target)*.001,.01); correct=abs(value-target)<=tol
                    st.session_state[submitted]=True
                    st.session_state[correct_key]=bool(correct)
                    if exam_mode:
                        st.session_state.exam.setdefault("answers",{})[aid]={"correct":bool(correct),"submitted":True,"value":value}
                    else:
                        record_result(a,fach,bool(correct),1 if correct else 0)
                    st.rerun()
        else:
            if exam_mode:
                st.success("✅ Ergebnis gespeichert. Lösung bleibt bis zum Prüfungsende verborgen.")
            else:
                correct=bool(st.session_state.get(correct_key,False))
                if correct:
                    st.success("✅ Richtig!")
                else:
                    st.error(f"❌ Noch nicht richtig. Ergebnis: {a.get('ergebnis')} {a.get('einheit','')}")
                with st.expander("✅ Lösungsweg",expanded=True):
                    if a.get("formel"):
                        st.code(a["formel"],language=None)
                    for p in a.get("loesungsweg",[]):
                        st.write(p)
                    task_visual(a)
                st.caption("⚠️ Prüfungs-Tipp: Rechenweg, Formel, Einheit und Ergebnis nachvollziehbar angeben.")
                confidence_buttons(a,fach,prefix,correct)
                if st.button("↩️ Ergebnis ändern",key=f"{prefix}_num_retry_{aid}"):
                    st.session_state.pop(submitted,None); st.session_state.pop(correct_key,None); st.session_state.pop(answer_key,None); st.rerun()


def build_adaptive_queue(fach, n=18, weakness_only=False):
    today=date.today().isoformat(); scored=[]
    for a in AUFGABEN.get(fach,[]):
        item=st.session_state.progress.get("items",{}).get(a["id"],{})
        mastery=mastery_for_id(a["id"])
        due=item.get("next_due") is None or item.get("next_due")<=today
        attempts=item.get("attempts",0)
        # höher = früher dran
        score=0
        if due: score+=4
        if mastery is None: score+=2
        else: score+=(1-mastery)*6
        score+=min(attempts,3)*.15
        if weakness_only and (mastery is None or mastery>=.65): continue
        scored.append((score,random.random(),a))
    scored.sort(key=lambda x:(-x[0],x[1]))
    chosen=[a for _,_,a in scored[:n]]
    return chosen


def queue_runner(queue_key, fach, title):
    q=st.session_state.get(queue_key,[])
    if not q: return False
    idx_key=f"{queue_key}_idx"; st.session_state.setdefault(idx_key,0)
    idx=min(st.session_state[idx_key],len(q)-1); a=q[idx]
    st.markdown(f"### {title}")
    st.caption(f"Aufgabe {idx+1} von {len(q)} · {a.get('thema','')} · {type_label(a)}")
    st.markdown(f"## {a.get('aufgabe','')}")
    render_task(a,fach,f"{queue_key}_{idx}")
    c1,c2,c3=st.columns([1,1,1])
    with c1:
        if st.button("⬅ Vorherige",disabled=idx<=0,key=f"{queue_key}_prev",use_container_width=True): st.session_state[idx_key]-=1; st.rerun()
    with c2:
        if st.button("Lerneinheit beenden",key=f"{queue_key}_stop",use_container_width=True): st.session_state[queue_key]=[]; st.session_state.pop(idx_key,None); st.rerun()
    with c3:
        if st.button("Nächste ➡",disabled=idx>=len(q)-1,key=f"{queue_key}_next",use_container_width=True): st.session_state[idx_key]+=1; st.rerun()
    return True

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("Industriemeister Metall")
fach=st.sidebar.selectbox("Fach",["BWH","ZIB","Recht","MIKP","NTG"],key="fach_nav")
if st.session_state.get("last_fach") != fach:
    st.session_state.today_queue = []
    st.session_state.weak_queue = []
    st.session_state.search_open = None
    st.session_state["last_fach"] = fach
sections=["Übersicht","Heute lernen","Lernen","Fragen","Schwächen","Prüfung"]
if fach=="BWH": sections.append("Formeln")
if st.session_state.get("bereich_nav") not in sections:
    st.session_state["bereich_nav"] = "Übersicht"
bereich=st.sidebar.radio("Bereich",sections,key="bereich_nav")

if fach!="NTG":
    fp,known,total=fach_progress(fach)
    st.sidebar.divider(); st.sidebar.metric("Beherrschung",f"{fp*100:.0f} %"); st.sidebar.progress(fp)
    st.sidebar.caption(f"{known} von {total} Aufgaben bereits bearbeitet")
    st.sidebar.metric("Lernserie",f"{streak_days()} Tage")
st.sidebar.caption("LernApp Version 4.0 · Study Edition")

st.title("Industriemeister Metall – LernApp")
if fach=="NTG":
    st.info("🚧 NTG ist noch nicht mit Aufgabenmaterial befüllt. BWH, ZIB, Recht und MIKP sind vollständig nutzbar."); st.stop()

current_tasks=AUFGABEN[fach]; fachname=FACHNAMEN[fach]

# ============================================================
# ÜBERSICHT
# ============================================================
if bereich=="Übersicht":
    st.markdown(f"<div class='hero'><h2 style='margin:0'>{fachname}</h2><div class='muted'>Prüfungsorientiert lernen · Schwächen erkennen · gezielt wiederholen</div></div>",unsafe_allow_html=True)
    search_ui(fach,"overview")
    fp,known,total=fach_progress(fach); stats=theme_stats(fach)
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Themen",len(topic_names(fach))); c2.metric("Aufgaben",len(current_tasks)); c3.metric("Bearbeitet",f"{known}/{total}"); c4.metric("Beherrschung",f"{fp*100:.0f} %")
    today_count = st.session_state.progress.get("activity", {}).get(date.today().isoformat(), 0)
    week_count = sum(st.session_state.progress.get("activity", {}).get((date.today()-timedelta(days=i)).isoformat(), 0) for i in range(7))
    h1,h2,h3=st.columns(3); h1.metric("🔥 Lernserie", f"{streak_days()} Tage"); h2.metric("Heute bewertet", today_count); h3.metric("Letzte 7 Tage", week_count)
    st.subheader("🎯 Dein nächster sinnvoller Schritt")
    due=build_adaptive_queue(fach,18)
    weak_count=sum(1 for x in stats.values() if x["mastery"] is not None and x["mastery"]<.65)
    st.info(f"Heute warten **{len(due)} passende Aufgaben** auf dich. Davon stammen möglichst viele aus fälligen Wiederholungen und Schwächen. Aktuell gibt es **{weak_count} erkannte Schwachstellen-Themen**.")
    st.subheader("📊 Themenstand")
    for t in topic_names(fach):
        s=stats.get(t,{"mastery":None,"attempts":0,"known":0,"total":0}); m=s["mastery"]
        label="Noch nicht bewertet" if m is None else f"{m*100:.0f} %"
        cols=st.columns([3,1,1])
        cols[0].markdown(f"**{priority(fach,t) or '➕'} · {t}**")
        cols[1].write(label); cols[2].caption(f"{s['known']}/{s['total']} bearbeitet")
        st.progress(m if m is not None else 0.0)

# ============================================================
# HEUTE LERNEN
# ============================================================
elif bereich=="Heute lernen":
    st.header("Heute lernen")
    search_ui(fach,"today")
    if not st.session_state.today_queue:
        q=build_adaptive_queue(fach,18)
        repeat=sum(1 for a in q if st.session_state.progress.get("items",{}).get(a["id"],{}).get("attempts",0)>0)
        new=len(q)-repeat
        st.markdown(f"<div class='hero'><h3>Deine heutige Lerneinheit</h3><p><b>{len(q)} Aufgaben · ca. 25–35 Minuten</b></p><p>🔁 {repeat} Wiederholungen &nbsp;&nbsp; 🆕 {new} neue/noch nicht bewertete Aufgaben</p></div>",unsafe_allow_html=True)
        if st.button("▶ Lerneinheit starten",type="primary",use_container_width=True): st.session_state.today_queue=q; st.session_state.today_queue_idx=0; st.rerun()
    else:
        queue_runner("today_queue",fach,"🎯 Adaptive Lerneinheit")

# ============================================================
# LERNEN
# ============================================================
elif bereich=="Lernen":
    st.header(f"{fach} – Lernen")
    search_ui(fach,"learn")
    theme=st.selectbox("Thema",["🔀 Alle Themen"]+topic_names(fach),key=f"learn_theme_{fach}")
    cards=learning_cards(fach,"__ALLE__" if theme=="🔀 Alle Themen" else theme)
    if not cards: st.info("Für dieses Thema sind keine Lernkarten vorhanden.")
    else:
        idx=st.number_input("Lernkarte",min_value=1,max_value=len(cards),value=1,step=1,key=f"learn_idx_{fach}_{norm(theme)}")-1
        t,title,content=cards[idx]
        render_learning_card(fach,t,title,content)
        c1,c2=st.columns(2)
        with c1: st.caption(f"Lernkarte {idx+1} von {len(cards)}")
        with c2: st.caption("Tipp: Über die Suche oben gelangst du direkt zu einzelnen Begriffen.")

# ============================================================
# FRAGEN
# ============================================================
elif bereich=="Fragen":
    st.header(f"{fach} – Prüfungstrainer")
    search_ui(fach,"questions")
    theme=st.selectbox("Thema",["🔀 Alle Themen"]+topic_names(fach),key=f"q_theme_{fach}")
    arr=current_tasks if theme=="🔀 Alle Themen" else [a for a in current_tasks if a.get("thema")==theme]
    filters=["Alle","Nur Theorie","Multiple Choice","Offene Fragen"] + (["Rechnen / Methoden"] if any(a.get("typ")=="rechnen" for a in arr) else [])
    flt=st.radio("Aufgabentyp",filters,horizontal=True,key=f"q_filter_{fach}")
    if flt=="Nur Theorie": arr=[a for a in arr if a.get("typ") in ("multiple_choice","offen")]
    elif flt=="Multiple Choice": arr=[a for a in arr if a.get("typ")=="multiple_choice"]
    elif flt=="Offene Fragen": arr=[a for a in arr if a.get("typ")=="offen"]
    elif flt=="Rechnen / Methoden": arr=[a for a in arr if a.get("typ")=="rechnen"]
    if not arr: st.info("Keine Aufgaben für diese Auswahl.")
    else:
        idx=st.number_input("Aufgabe",min_value=1,max_value=len(arr),value=1,step=1,key=f"q_idx_{fach}_{norm(theme)}_{norm(flt)}")-1
        a=arr[idx]; st.caption(f"Aufgabe {idx+1}/{len(arr)} · {a.get('thema')} · {type_label(a)} · {a.get('schwierigkeit','')}")
        st.markdown(f"## {a.get('aufgabe','')}"); render_task(a,fach,f"trainer_{fach}_{idx}")

# ============================================================
# SCHWÄCHEN
# ============================================================
elif bereich=="Schwächen":
    st.header("Meine Schwächen")
    search_ui(fach,"weak")
    stats=theme_stats(fach)
    ranked=[]
    for t,s in stats.items():
        if s["mastery"] is not None: ranked.append((s["mastery"],t,s))
    ranked.sort()
    if not ranked:
        st.info("Noch keine Schwächen erkennbar. Bearbeite zuerst einige Aufgaben; danach entsteht hier automatisch deine persönliche Auswertung.")
    else:
        for m,t,s in ranked:
            icon="🔴" if m<.5 else "🟡" if m<.7 else "🟢"
            st.markdown(f"**{icon} {t} — {m*100:.0f} %**")
            st.progress(m); st.caption(f"{s['known']} von {s['total']} Aufgaben bewertet")
        weak=build_adaptive_queue(fach,15,weakness_only=True)
        if weak and not st.session_state.weak_queue:
            if st.button("▶ Nur meine Schwächen trainieren",type="primary",use_container_width=True): st.session_state.weak_queue=weak; st.session_state.weak_queue_idx=0; st.rerun()
        if st.session_state.weak_queue: queue_runner("weak_queue",fach,"🔥 Schwächentraining")

# ============================================================
# PRÜFUNG
# ============================================================
elif bereich=="Prüfung":
    st.header(f"{fach} – Prüfungssimulation")
    search_ui(fach,"exam")
    if not st.session_state.exam:
        if fach=="MIKP":
            n=6; minutes=90
            st.info("MIKP IHK-nah: **6 Aufgaben · 90 Minuten**. Lösungen und Tipps bleiben bis zum Ende verborgen.")
        else:
            n=min(15,len(current_tasks)); minutes=90
            n=st.selectbox("Anzahl Aufgaben",[x for x in [10,15,20] if x<=len(current_tasks)],index=0)
            minutes=st.selectbox("Zeit",[60,90,120],index=1)
        if st.button("🚀 Prüfung starten",type="primary",use_container_width=True):
            # thematisch breit mischen
            by_theme=defaultdict(list)
            for a in current_tasks: by_theme[a.get("thema","")].append(a)
            chosen=[]
            for t in random.sample(list(by_theme.keys()),min(len(by_theme),n)):
                chosen.append(random.choice(by_theme[t]))
            rest=[a for a in current_tasks if a["id"] not in {x["id"] for x in chosen}]
            if len(chosen)<n: chosen+=random.sample(rest,min(n-len(chosen),len(rest)))
            random.shuffle(chosen)
            st.session_state.exam={"fach":fach,"tasks":[a["id"] for a in chosen],"start":datetime.now().isoformat(),"minutes":minutes,"answers":{},"finished":False}
            st.rerun()
    else:
        exam=st.session_state.exam
        if exam.get("fach")!=fach:
            st.warning(f"Es läuft eine Prüfung in {exam.get('fach')}. Beende sie zuerst.")
        elif not exam.get("finished"):
            start=datetime.fromisoformat(exam["start"]); end=start+timedelta(minutes=exam["minutes"]); remain=max(0,int((end-datetime.now()).total_seconds()))
            mins,secs=divmod(remain,60)
            st.markdown(f"<div class='hero'><b>⏱️ Verbleibende Zeit: {mins:02d}:{secs:02d}</b><br><span class='muted'>Lösungen und Tipps bleiben bis zum Prüfungsende verborgen.</span></div>",unsafe_allow_html=True)
            if components is not None:
                components.html(f"""<div id='timer' style='font-family:Arial;font-size:20px;font-weight:700;padding:8px 0'>⏱️ {mins:02d}:{secs:02d}</div><script>let s={remain}; const el=document.getElementById('timer'); setInterval(()=>{{s=Math.max(0,s-1); const m=Math.floor(s/60); const sec=s%60; el.innerText='⏱️ '+String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0');}},1000);</script>""", height=45)
            tasks=[next(a for a in current_tasks if a["id"]==aid) for aid in exam["tasks"]]
            idx=st.number_input("Prüfungsaufgabe",min_value=1,max_value=len(tasks),value=1,step=1,key=f"exam_idx_{fach}")-1
            a=tasks[idx]; st.caption(f"Aufgabe {idx+1}/{len(tasks)} · {a.get('thema')} · {type_label(a)}")
            st.markdown(f"## {a.get('aufgabe','')}"); render_task(a,fach,f"exam_{fach}_{idx}",exam_mode=True)
            answered=sum(1 for aid in exam["tasks"] if exam.get("answers",{}).get(aid,{}).get("submitted"))
            st.progress(answered/len(tasks)); st.caption(f"{answered}/{len(tasks)} Antworten gespeichert")
            if st.button("🏁 Prüfung beenden und auswerten",type="primary",use_container_width=True): exam["finished"]=True; exam["end"]=datetime.now().isoformat(); save_progress(); st.rerun()
        else:
            tasks=[next(a for a in current_tasks if a["id"]==aid) for aid in exam["tasks"]]
            st.success("🏁 Prüfung beendet – jetzt erfolgt die Auswertung.")
            total_points=100; per=total_points/len(tasks); earned=0
            open_tasks=[]
            for a in tasks:
                ans=exam.get("answers",{}).get(a["id"],{})
                if a.get("typ")=="offen": open_tasks.append(a)
                elif ans.get("correct"): earned+=per
            if open_tasks:
                st.info("Offene Antworten werden jetzt automatisch inhaltlich mit der Musterlösung verglichen. Abweichende Formulierungen und Teiltreffer werden berücksichtigt.")
                for a in open_tasks:
                    ans=exam.get("answers",{}).setdefault(a["id"],{})
                    text=ans.get("text","")
                    ev=evaluate_open_answer(text,a) if text else {"score":0,"matched":[],"missing":a.get("musterloesung",[])}
                    frac=ev.get("score",0)/100
                    ans["self_grade"]=frac
                    ans["auto_score"]=ev.get("score",0)
                    st.markdown(f"### {a.get('thema')} · {a.get('aufgabe')}")
                    st.write(f"**Automatische Einschätzung: {ev.get('score',0)} %**")
                    if ev.get("matched"):
                        st.caption("Erkannt: " + " · ".join(ev.get("matched",[])[:3]))
                    ml=a.get("musterloesung",[])
                    with st.expander("Musterlösung",expanded=False):
                        if isinstance(ml,list):
                            for p in ml: st.write(f"• {p}")
                        else: st.write(ml)
                        task_visual(a)
            # endgültigen Punktestand mit aktuell gesetzten Selbstbewertungen berechnen
            earned=sum(per for a in tasks if a.get("typ")!="offen" and exam.get("answers",{}).get(a["id"],{}).get("correct"))
            for a in open_tasks:
                frac=exam.get("answers",{}).get(a["id"],{}).get("self_grade")
                if frac is not None: earned+=per*frac
            c1,c2=st.columns(2); c1.metric("Punkte",f"{earned:.0f} / 100"); c2.metric("Ergebnis",f"{earned:.0f} %")
            st.progress(min(earned/100,1.0))
            st.subheader("📊 Auswertung nach Themen")
            by=defaultdict(lambda:{"n":0,"points":0.0})
            for a in tasks:
                by[a["thema"]]["n"]+=1
                ans=exam.get("answers",{}).get(a["id"],{})
                frac=ans.get("self_grade") if a.get("typ")=="offen" else (1 if ans.get("correct") else 0)
                if frac is not None: by[a["thema"]]["points"]+=frac
            for t,d in by.items(): st.write(f"**{t}:** {d['points']:.1f} / {d['n']} Aufgabenpunkte")
            if st.button("✅ Ergebnis speichern & neue Prüfung",type="primary",use_container_width=True):
                for a in tasks:
                    ans=exam.get("answers",{}).get(a["id"],{})
                    if a.get("typ")=="offen":
                        frac=ans.get("self_grade")
                        if frac is not None: record_result(a,fach,frac>=.8,2 if frac>=.8 else (1 if frac>=.4 else 0))
                    else: record_result(a,fach,bool(ans.get("correct")),2 if ans.get("correct") else 0)
                st.session_state.progress.setdefault("exam_history",[]).append({"fach":fach,"date":date.today().isoformat(),"score":round(earned,1)})
                save_progress(); st.session_state.exam=None; st.rerun()
            if st.button("🗑️ Prüfung verwerfen",use_container_width=True): st.session_state.exam=None; st.rerun()

# ============================================================
# FORMELN
# ============================================================
elif bereich=="Formeln":
    st.header("BWH – Formelsammlung")
    search_ui(fach,"formula")
    area=st.selectbox("Formelbereich",list(FORMELBEREICHE.keys()))
    data=FORMELBEREICHE[area]
    if data.get("zeichen"):
        with st.expander("🔤 Formelzeichen"):
            for s,b in data["zeichen"].items(): st.write(f"**{s}** = {b}")
    for name,d in data["formeln"].items():
        with st.expander(f"📐 {name}"):
            if isinstance(d,dict):
                if d.get("formel"): st.code(d["formel"],language=None)
                if d.get("erklaerung"): st.write(d["erklaerung"])
            else: st.write(d)

st.divider()
st.caption("Industriemeister Metall LernApp · Version 4.0 Study Edition · Fortschritt wird lokal in lernfortschritt.json gespeichert")
if st.session_state.get("save_warning"):
    st.warning("Der Lernfortschritt konnte nicht dauerhaft gespeichert werden. Die App funktioniert weiter, aber die Daten gelten nur für diese Sitzung.")
