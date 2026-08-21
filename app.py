import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime
from FrontStyle.theme import inject_theme

st.set_page_config(page_title="SickleScreen", page_icon="🩸", layout="wide")

# ─────────────────────────── CSS ───────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base ── */
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.main { background-color: #050816; }
.block-container { padding: 0.75rem 2rem 2rem 2rem; max-width: 100%; }

/* ── Navbar ── */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #0f172a;
    padding: 12px 20px;
    border-radius: 14px;
    margin-bottom: 16px;
    border: 1px solid #1e293b;
}
.navbar-brand { display: flex; align-items: center; gap: 10px; }
.navbar-logo { font-size: 1.5rem; }
.navbar-title { font-size: 1.1rem; font-weight: 700; color: #f8fafc; margin: 0; }
.navbar-sub { font-size: 0.72rem; color: #94a3b8; margin: 0; }
.navbar-links { display: flex; gap: 8px; align-items: center; }
.nav-link {
    color: #94a3b8; text-decoration: none; padding: 6px 14px;
    border-radius: 8px; font-size: 0.85rem; font-weight: 500;
    transition: background 0.2s, color 0.2s;
}
.nav-link:hover { background: #1e293b; color: #f1f5f9; }
.nav-link.active { background: #1e1030; color: #e879f9; }
.nav-link-dropdown { position: relative; display: inline-block; }
.nav-btn-csv {
    background: linear-gradient(135deg, #ec4899, #a855f7);
    color: #fff; border: none; padding: 7px 16px; border-radius: 8px;
    font-size: 0.82rem; font-weight: 600; cursor: pointer;
    display: inline-flex; align-items: center; gap: 6px;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0f172a 60%, #1a0a2e 100%);
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 16px;
    border: 1px solid #1e293b;
    position: relative;
    overflow: hidden;
}
.hero-eyebrow { color: #e879f9; font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 6px; }
.hero-title { color: #f8fafc; font-size: 1.7rem; font-weight: 700; margin: 0 0 6px 0; }
.hero-sub { color: #94a3b8; font-size: 0.88rem; }

/* ── Metric Cards ── */
.metrics-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 12px; margin-bottom: 16px; }
.metric-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 18px 20px;
    display: flex; align-items: center; gap: 14px;
}
.metric-icon {
    width: 44px; height: 44px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem; flex-shrink: 0;
}
.metric-icon.blue { background: #1e3a5f; }
.metric-icon.red  { background: #3b1219; }
.metric-icon.green{ background: #0d2b1e; }
.metric-icon.purple{ background: #2a1a3e; }
.metric-val { font-size: 1.6rem; font-weight: 700; color: #f8fafc; line-height: 1; }
.metric-lbl { font-size: 0.75rem; color: #94a3b8; margin-top: 3px; }

/* ── Section Cards ── */
.section-card {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 22px 24px;
    height: 100%;
}
.section-title { font-size: 1rem; font-weight: 700; color: #f8fafc; margin-bottom: 16px; }

/* ── Form Labels ── */
.form-group-title { font-size: 0.78rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 10px; margin-top: 16px; }

/* ── Computed Index Fields ── */
.index-field {
    background: #0a0f1e;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 10px;
}
.index-field-label { font-size: 0.75rem; color: #64748b; margin-bottom: 3px; }
.index-field-value { font-size: 1.05rem; font-weight: 600; color: #e2e8f0; }
.index-field-unit { font-size: 0.72rem; color: #64748b; margin-left: 4px; }

/* ── Buttons ── */
div[data-testid="stButton"] > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    transition: opacity 0.2s !important;
}
div[data-testid="stButton"] > button:hover { opacity: 0.88 !important; }

/* Screen button */
.screen-btn > div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #ec4899, #a855f7) !important;
    color: white !important;
    border: none !important;
    padding: 12px !important;
    width: 100% !important;
}
/* Reset button */
.reset-btn > div[data-testid="stButton"] > button {
    background: #1e293b !important;
    color: #94a3b8 !important;
    border: 1px solid #334155 !important;
    width: 100% !important;
}

/* ── Result Badges ── */
.result-box {
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-top: 12px;
}
.result-box.low  { background: #061a12; border: 1px solid #16a34a; }
.result-box.mid  { background: #1a1200; border: 1px solid #ca8a04; }
.result-box.high { background: #180610; border: 1px solid #dc2626; }
.result-icon { font-size: 2rem; flex-shrink: 0; }
.result-title { font-size: 1rem; font-weight: 700; }
.result-title.low  { color: #4ade80; }
.result-title.mid  { color: #fbbf24; }
.result-title.high { color: #f87171; }
.result-sub { font-size: 0.78rem; color: #94a3b8; margin-top: 2px; }
.result-text { font-size: 0.82rem; color: #94a3b8; margin-top: 6px; line-height: 1.5; }

/* ── Risk Progress Bar ── */
.risk-bar-wrap { margin-top: 12px; }
.risk-bar-label { display: flex; justify-content: space-between; font-size: 0.78rem; color: #64748b; margin-bottom: 4px; }
.risk-bar-bg { background: #1e293b; border-radius: 99px; height: 8px; }
.risk-bar-fill { height: 8px; border-radius: 99px; }

/* ── History Table ── */
.stDataFrame { border-radius: 10px; overflow: hidden; }
div[data-testid="stDataFrameResizable"] { border: 1px solid #1e293b; border-radius: 10px; }

/* ── Result pill in table ── */
.pill { display:inline-block; padding:3px 10px; border-radius:99px; font-size:0.75rem; font-weight:600; }
.pill-refer   { background:#3b0a0a; color:#f87171; }
.pill-monitor { background:#1a1200; color:#fbbf24; }
.pill-clear   { background:#062010; color:#4ade80; }

/* ── Education Cards ── */
.edu-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:16px; }
.edu-card {
    background:#0f172a; border:1px solid #1e293b; border-radius:14px;
    padding:20px 22px; display:flex; flex-direction:column; gap:8px;
}
.edu-icon { font-size:1.4rem; }
.edu-title { font-size:0.9rem; font-weight:700; color:#f8fafc; }
.edu-desc  { font-size:0.78rem; color:#94a3b8; line-height:1.5; flex:1; }
.edu-link  { color:#e879f9; font-size:0.8rem; font-weight:600; text-decoration:none; cursor:pointer; }

/* ── Footer ── */
.footer { text-align:center; color:#334155; font-size:0.75rem; margin-top:28px; padding:16px; }

/* ── Streamlit overrides ── */
div[data-testid="metric-container"] { background:#0a0f1e; border:1px solid #1e293b; border-radius:10px; padding:12px; }
div[data-testid="stNumberInput"] > div { background:#0a0f1e; border-color:#1e293b; border-radius:10px; }
div[data-testid="stSelectbox"] > div > div { background:#0a0f1e; border-color:#1e293b; border-radius:10px; }
div[data-testid="stTextInput"] > div > div { background:#0a0f1e; border-color:#1e293b; border-radius:10px; }
label { color:#94a3b8 !important; font-size:0.82rem !important; }
h1,h2,h3 { color:#f8fafc !important; }
div[data-testid="stRadio"] > div { gap:4px; }
div[data-testid="stRadio"] label { color:#94a3b8 !important; background:#0f172a; padding:7px 16px; border-radius:8px; border:1px solid #1e293b; font-size:0.85rem !important; }
div[data-testid="stRadio"] label[data-baseweb] { color:#e879f9 !important; background:#1e1030; border-color:#a855f7; }
div[data-testid="stPageLink"] a {
    background:#0f172a; border:1px solid #1e293b; border-radius:8px;
    color:#94a3b8; justify-content:center; padding:7px 12px; text-decoration:none;
}
div[data-testid="stPageLink"] a:hover {
    background:#1e293b; border-color:#a855f7; color:#f1f5f9;
}
</style>
""", unsafe_allow_html=True)
inject_theme()

# ─────────────────────────── SESSION STATE ───────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None
if "page_num" not in st.session_state:
    st.session_state.page_num = 1

# ─────────────────────────── CONFIG ───────────────────────────
referral_data = {
    "Khordha":   {"center": "Capital Hospital, Bhubaneswar",  "phone": "0674-2431257"},
    "Koraput":   {"center": "District Headquarters Hospital",  "phone": "06852-250387"},
    "Sundargarh":{"center": "IGH Rourkela",                   "phone": "0661-2473456"},
    "Cuttack":   {"center": "SCB Medical College",             "phone": "0671-2414355"},
    "Puri":      {"center": "District HQ Hospital, Puri",      "phone": "06752-222153"},
    "Mayurbhanj":{"center": "Shri Ram Chandra Bhanj Medical",  "phone": "06792-252327"},
}

history_file = "patient_history.csv"

ROWS_PER_PAGE = 8

# ─────────────────────────── MODEL (lazy load) ───────────────────────────
@st.cache_resource
def load_model():
    if os.path.exists("sicklescreen_model.pkl"):
        return joblib.load("sicklescreen_model.pkl")
    return None

model = load_model()

# ─────────────────────────── NAVIGATION (Streamlit-native) ───────────────────────────
# These links target the existing Python pages and preserve the dashboard as-is.
nav_cols = st.columns(5, gap="small")
with nav_cols[0]:
    st.page_link("app.py", label="Dashboard", icon=":material/home:")
with nav_cols[1]:
    st.page_link("pages/About_Sickle_Cell.py", label="About Sickle Cell", icon=":material/menu_book:")
with nav_cols[2]:
    st.page_link("pages/How_It_Affects_Us.py", label="How It Affects Us", icon=":material/groups:")
with nav_cols[3]:
    st.page_link("pages/Symptoms.py", label="Symptoms", icon=":material/medical_information:")
with nav_cols[4]:
    st.page_link("pages/Prevention_and_Care.py", label="Prevention & Care", icon=":material/health_and_safety:")

# ─────────────────────────── METRICS ───────────────────────────
def safe_read_csv(path):
    """Read CSV tolerantly — skips malformed rows and handles column mismatches."""
    try:
        return pd.read_csv(path, on_bad_lines="skip")
    except Exception:
        try:
            return pd.read_csv(path, on_bad_lines="skip", engine="python")
        except Exception:
            return pd.DataFrame()

if os.path.exists(history_file):
    h = safe_read_csv(history_file)
    total = len(h)
    high  = len(h[h["Recommendation"] == "REFER"]) if "Recommendation" in h.columns else 0
    low   = len(h[h["Recommendation"] == "CLEAR"]) if "Recommendation" in h.columns else 0
    rate  = round((high / max(total, 1)) * 100, 1)
else:
    total = high = low = rate = 0

# Hero + metrics row
st.markdown(f"""
<div class="hero-banner">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <div>
      <p class="hero-eyebrow">AI-Assisted Screening for</p>
      <p class="hero-title">Sickle Cell Carrier Detection</p>
      <p class="hero-sub">Early detection. Better care. Healthier future.</p>
    </div>
    <div style="font-size:5rem; opacity:0.25; line-height:1;">🩸</div>
  </div>
</div>

<div class="metrics-row">
  <div class="metric-card">
    <div class="metric-icon blue">👥</div>
    <div>
      <div class="metric-val">{total}</div>
      <div class="metric-lbl">Total Screened Patients</div>
    </div>
  </div>
  <div class="metric-card">
    <div class="metric-icon red">🛡️</div>
    <div>
      <div class="metric-val">{high}</div>
      <div class="metric-lbl">High Risk Detected</div>
    </div>
  </div>
  <div class="metric-card">
    <div class="metric-icon green">✅</div>
    <div>
      <div class="metric-val">{low}</div>
      <div class="metric-lbl">Low Risk Detected</div>
    </div>
  </div>
  <div class="metric-card">
    <div class="metric-icon purple">🔄</div>
    <div>
      <div class="metric-val">{rate}%</div>
      <div class="metric-lbl">High Risk Rate</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────── DOWNLOAD CSV ───────────────────────────
if os.path.exists(history_file):
    csv_df = pd.read_csv(history_file)
    csv_bytes = csv_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download CSV",
        data=csv_bytes,
        file_name="patient_history.csv",
        mime="text/csv",
        key="download_csv"
    )

st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

# ─────────────────────────── MAIN LAYOUT ───────────────────────────
left, right = st.columns([1, 1], gap="medium")

# ───── LEFT: Form ─────
with left:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Patient Information & CBC Parameters</p>', unsafe_allow_html=True)

    st.markdown('<p class="form-group-title">Patient Information</p>', unsafe_allow_html=True)
    patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
    district = st.selectbox("District", list(referral_data.keys()))

    st.markdown('<p class="form-group-title">CBC Parameters</p>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        hb  = st.number_input("Hemoglobin Hb (g/dL)",  min_value=0.0, max_value=25.0,  value=12.0, step=0.1, format="%.1f")
        mcv = st.number_input("MCV (Mean Corpuscular Volume) (fL)", min_value=0.0, max_value=150.0, value=80.0, step=0.1, format="%.1f")
        mch = st.number_input("MCH (Mean Corpuscular Hemoglobin) (pg)", min_value=0.0, max_value=50.0, value=27.0, step=0.1, format="%.1f")
    with c2:
        rbc = st.number_input("RBC Count (Red Blood Cells) (million/µL)", min_value=0.1, max_value=10.0, value=4.5, step=0.1, format="%.1f")
        mentzer = round(mcv / rbc, 2) if rbc > 0 else 0.0
        shine   = round(((mcv ** 2) * mch) / 100, 2)

        st.markdown(f"""
        <div class="index-field">
          <div class="index-field-label">Mentzer Index (MCV/RBC)</div>
          <div class="index-field-value">{mentzer}<span class="index-field-unit">ratio</span></div>
        </div>
        <div class="index-field">
          <div class="index-field-label">Shine &amp; Lal Index (MCV² × MCH / 100)</div>
          <div class="index-field-value">{shine}<span class="index-field-unit">index</span></div>
        </div>
        """, unsafe_allow_html=True)

    btn_col1, btn_col2 = st.columns([2, 1])
    with btn_col1:
        screen_clicked = st.button("🔍  Screen Patient", width="stretch", type="primary")
    with btn_col2:
        reset_clicked = st.button("↺  Reset", width="stretch")

    if reset_clicked:
        st.session_state.result = None
        st.rerun()

    if screen_clicked:
        if model is None:
            st.error("⚠️ Model file `sicklescreen_model.pkl` not found. Please place it in the app directory.")
        else:
            patient_df = pd.DataFrame({
                "Hb":              [hb],
                "MCV":             [mcv],
                "MCH":             [mch],
                "RBC":             [rbc],
                "mentzer_index":   [mentzer],
                "shine_lal_index": [shine],
            })
            risk     = model.predict_proba(patient_df)[0][1]
            risk_pct = round(risk * 100, 2)

            if risk < 0.30:
                rec = "CLEAR";   level = "low"
            elif risk < 0.70:
                rec = "MONITOR"; level = "mid"
            else:
                rec = "REFER";   level = "high"

            st.session_state.result = dict(
                risk_pct=risk_pct, rec=rec, level=level,
                patient_name=patient_name, district=district,
                hb=hb, mcv=mcv, mch=mch, rbc=rbc,
                mentzer=mentzer, shine=shine
            )

            # Persist to history
            record = pd.DataFrame({
                "Timestamp":      [datetime.now().strftime("%b %d, %Y %I:%M %p")],
                "Name":           [patient_name or "—"],
                "District":       [district],
                "Hb":             [hb],
                "MCV":            [mcv],
                "MCH":            [mch],
                "RBC":            [rbc],
                "Risk (%)":       [risk_pct],
                "Recommendation": [rec],
            })
            if os.path.exists(history_file):
                record.to_csv(history_file, mode="a", header=False, index=False)
            else:
                record.to_csv(history_file, index=False)
            st.rerun()

    # Result display
    r = st.session_state.result
    if r:
        icons  = {"low": "🛡️", "mid": "⚠️", "high": "🔴"}
        titles = {"low": "LOW RISK", "mid": "MONITOR", "high": "REFER"}
        subs   = {
            "low":  "Sickle Cell Carrier Not Likely",
            "mid":  "Borderline — Follow Up Recommended",
            "high": "High Carrier Risk — Refer Immediately",
        }
        notes  = {
            "low":  "Based on the provided CBC parameters, this individual is not likely to be a sickle cell carrier.",
            "mid":  "Borderline result. Consider repeat testing or specialist referral for confirmation.",
            "high": "High probability of sickle cell carrier status. Immediate referral is strongly advised.",
        }

        level = r["level"]
        bar_colors = {"low": "#16a34a", "mid": "#ca8a04", "high": "#dc2626"}

        st.markdown(f"""
        <p class="form-group-title" style="margin-top:16px;">Prediction Result</p>
        <div class="result-box {level}">
          <div class="result-icon">{icons[level]}</div>
          <div style="flex:1">
            <div class="result-title {level}">{titles[level]}</div>
            <div class="result-sub">{subs[level]}</div>
            <div class="risk-bar-wrap">
              <div class="risk-bar-label">
                <span>Carrier Risk</span>
                <span>{r['risk_pct']}%</span>
              </div>
              <div class="risk-bar-bg">
                <div class="risk-bar-fill" style="width:{min(r['risk_pct'],100)}%; background:{bar_colors[level]};"></div>
              </div>
            </div>
            <div class="result-text">{notes[level]}<br>
              <em>Note: This is an AI-assisted screening. Please refer to a healthcare professional for confirmatory testing.</em>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        center = referral_data.get(r["district"], {})
        if level == "high" and center:
            st.info(f"📍 **Referral Center:** {center['center']}  |  📞 {center['phone']}")

    st.markdown('</div>', unsafe_allow_html=True)

# ───── RIGHT: History Table ─────
with right:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Recent Patient History</p>', unsafe_allow_html=True)

    search_col, _ = st.columns([3, 1])
    with search_col:
        search = st.text_input("Search patients...", placeholder="Search patients...", label_visibility="collapsed")

    if os.path.exists(history_file):
        history_df = safe_read_csv(history_file)
        history_df = history_df.iloc[::-1].reset_index(drop=True)  # newest first

        if search:
            mask = history_df.astype(str).apply(
                lambda col: col.str.contains(search, case=False, na=False)
            ).any(axis=1)
            history_df = history_df[mask].reset_index(drop=True)

        total_rows = len(history_df)
        total_pages = max(1, (total_rows + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        pn = st.session_state.page_num
        pn = max(1, min(pn, total_pages))

        start = (pn - 1) * ROWS_PER_PAGE
        end   = start + ROWS_PER_PAGE
        page_df = history_df.iloc[start:end].copy()

        # Add row index column
        page_df.insert(0, "#", range(start + 1, start + len(page_df) + 1))

        # Rename for display
        display_cols = {
            "#": "#",
            "Name": "Patient Name",
            "District": "District",
            "Hb": "Hb (g/dL)",
            "MCV": "MCV (fL)",
            "MCH": "MCH (pg)",
            "RBC": "RBC (M/µL)",
            "Risk (%)": "Risk (%)",
            "Recommendation": "Result",
            "Timestamp": "Date & Time",
        }
        available_cols = [c for c in display_cols if c in page_df.columns]
        page_df = page_df[available_cols].rename(columns=display_cols)

        st.dataframe(page_df, width="stretch", hide_index=True)

        # Pagination
        st.markdown(f"<div style='color:#64748b; font-size:0.78rem; margin-top:6px;'>Showing {start+1} to {min(end,total_rows)} of {total_rows} entries</div>", unsafe_allow_html=True)

        p_cols = st.columns(8)
        if p_cols[0].button("‹", key="prev_page"):
            st.session_state.page_num = max(1, pn - 1)
            st.rerun()

        for i in range(min(total_pages, 5)):
            pg_n = i + 1
            lbl  = f"**{pg_n}**" if pg_n == pn else str(pg_n)
            if p_cols[i + 1].button(lbl, key=f"pg_{pg_n}"):
                st.session_state.page_num = pg_n
                st.rerun()

        if total_pages > 5:
            p_cols[6].markdown("<span style='color:#64748b'>…</span>", unsafe_allow_html=True)

        if p_cols[7].button("›", key="next_page"):
            st.session_state.page_num = min(total_pages, pn + 1)
            st.rerun()
    else:
        st.markdown("""
        <div style="text-align:center; color:#334155; padding:60px 20px;">
          <div style="font-size:2.5rem; margin-bottom:12px;">📋</div>
          <div style="font-weight:600; color:#64748b;">No patient records yet</div>
          <div style="font-size:0.8rem; color:#334155; margin-top:6px;">Screen a patient to see records here</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────── EDUCATION CARDS ───────────────────────────
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.markdown('<hr style="border-color:#1e293b; margin:0 0 16px 0;">', unsafe_allow_html=True)

edu_cards = [
    ("📖", "About Sickle Cell Anemia",
     "Learn about sickle cell disease, symptoms, causes and prevention.",
     "Learn More →"),
    ("👥", "How It Affects Us",
     "Understand the impact on individuals, families and communities.",
     "Explore →"),
    ("🩺", "Symptoms & Signs",
     "Identify common symptoms and when to seek medical help.",
     "View Symptoms →"),
    ("🛡️", "Prevention & Care",
     "Guidelines for prevention, care and management.",
     "Read More →"),
]

edu_cols = st.columns(4)
for col, (icon, title, desc, link) in zip(edu_cols, edu_cards):
    with col:
        st.markdown(f"""
        <div class="edu-card">
          <div class="edu-icon">{icon}</div>
          <div class="edu-title">{title}</div>
          <div class="edu-desc">{desc}</div>
          <span class="edu-link">{link}</span>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────── FOOTER ───────────────────────────
st.markdown('<div class="footer">© 2025 SickleScreen. All rights reserved.</div>', unsafe_allow_html=True)
