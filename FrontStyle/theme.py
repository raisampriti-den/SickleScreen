"""Shared presentation layer for SickleScreen's Streamlit pages."""

import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


def inject_theme():
    """Apply the common visual system and the Google Translate website widget."""
    image_path = Path(__file__).with_name("background.jpeg")
    background = base64.b64encode(image_path.read_bytes()).decode("ascii")

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
        :root {{ color-scheme: dark; }}
        html, body, [class*="css"] {{ font-family:'DM Sans',sans-serif; }}
        [data-testid="stAppViewContainer"] {{
          background:linear-gradient(110deg,rgba(2,9,24,.87),rgba(6,14,34,.76)),url("data:image/jpeg;base64,{background}") center/cover fixed no-repeat;
          animation:biomedicalDrift 42s ease-in-out infinite;
        }}
        [data-testid="stAppViewContainer"]::before {{
          content:""; position:fixed; inset:0; pointer-events:none; z-index:0;
          background:radial-gradient(circle at 82% 12%,rgba(44,196,222,.12),transparent 28%),radial-gradient(circle at 9% 86%,rgba(138,16,44,.14),transparent 30%);
          animation:ambientGlow 18s ease-in-out infinite alternate;
        }}
        @keyframes ambientGlow {{ to {{ opacity:.56; transform:scale(1.04); }} }}
        @keyframes biomedicalDrift {{ 0%,100% {{ background-position:center center; }} 50% {{ background-position:52% 48%; }} }}
        .stMainBlockContainer, [data-testid="stHeader"], [data-testid="stSidebar"] {{ position:relative; z-index:1; }}
        .block-container {{ max-width:1240px; padding:1.15rem 2rem 2.5rem; }}
        [data-testid="stHeader"] {{ background:transparent; }}
        .stApp {{ color:#dceafa; }}
        h1,h2,h3 {{ font-family:'Manrope',sans-serif !important; color:#f5fbff !important; letter-spacing:-.025em; }}
        h2 {{ font-size:1.35rem !important; margin-top:1.55rem !important; }}
        p,li,[data-testid="stMarkdownContainer"] {{ color:#c2d2e4; }}
        .navbar {{ display:flex; align-items:center; justify-content:space-between; gap:18px; background:linear-gradient(120deg,rgba(8,21,44,.82),rgba(13,31,59,.58)); border:1px solid rgba(147,205,232,.2); border-radius:18px; padding:14px 20px; margin-bottom:12px; box-shadow:0 16px 38px rgba(0,0,0,.23), inset 0 1px rgba(255,255,255,.09); backdrop-filter:blur(18px); }}
        .navbar-brand {{ display:flex; align-items:center; gap:12px; }}
        .navbar-logo {{ font-size:1.4rem; filter:drop-shadow(0 0 9px rgba(255,70,102,.45)); }}
        .navbar-title {{ font-family:'Manrope',sans-serif; font-size:1.18rem; font-weight:800; color:#f7fdff; margin:0; letter-spacing:-.02em; }}
        .navbar-sub {{ color:#a8bfd3; font-size:.76rem; margin:1px 0 0; }}
        .hero,.hero-banner {{ background:linear-gradient(125deg,rgba(10,29,57,.83),rgba(12,32,60,.52)); border:1px solid rgba(132,205,230,.24); border-radius:20px; padding:30px 32px; margin:12px 0 22px; box-shadow:0 18px 44px rgba(0,0,0,.22), inset 0 1px rgba(255,255,255,.09); backdrop-filter:blur(17px); overflow:hidden; position:relative; }}
        .hero::after,.hero-banner::after {{ content:""; position:absolute; inset:0; pointer-events:none; background:linear-gradient(110deg,transparent 40%,rgba(106,220,255,.06),transparent 62%); }}
        .hero h1,.hero-title {{ color:#f8fdff !important; font-family:'Manrope',sans-serif; font-size:clamp(1.55rem,3vw,2.1rem); font-weight:800; margin:.3rem 0; }}
        .hero p,.hero-sub {{ color:#bfd1e2 !important; line-height:1.65; max-width:780px; }}
        .eyebrow,.hero-eyebrow,.form-group-title {{ color:#70d7ee !important; font-size:.72rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase; }}
        .metrics-row {{ gap:14px; }}
        .metric-card,.section-card,.card {{ background:linear-gradient(145deg,rgba(11,28,54,.82),rgba(9,22,45,.62)); border:1px solid rgba(146,205,234,.19); border-radius:16px; box-shadow:0 12px 30px rgba(0,0,0,.17),inset 0 1px rgba(255,255,255,.08); backdrop-filter:blur(15px); }}
        .metric-card,.card {{ transition:transform .25s ease,border-color .25s ease,background .25s ease; }}
        .metric-card:hover,.card:hover {{ transform:translateY(-3px); border-color:rgba(106,218,241,.44); background:linear-gradient(145deg,rgba(14,38,69,.89),rgba(9,25,51,.72)); }}
        .card {{ padding:21px; height:100%; }} .card h3 {{ font-size:1rem; margin-top:0; }} .card p,.card li {{ line-height:1.65; }}
        .understand-visual {{ display:block; width:min(100%,1000px); margin:0 auto 1.8rem; border:1px solid rgba(116,211,236,.36); border-radius:18px; box-shadow:0 18px 46px rgba(0,0,0,.3),0 0 28px rgba(61,190,219,.12),inset 0 1px rgba(255,255,255,.14); }}
        .understand-copy {{ max-width:900px; margin:0 auto; }} .support-panel {{ padding:0 0 1rem; }} .support-panel h2 {{ margin:1.15rem 0 .35rem !important; font-size:1.12rem !important; }} .support-panel p {{ max-width:700px; margin:.25rem 0; line-height:1.62; }}
        .care-flow {{ display:flex; align-items:center; flex-wrap:wrap; gap:9px; margin:1.2rem 0 .7rem; color:#e6f8ff; font-weight:600; }} .care-flow span {{ padding:8px 11px; border-radius:999px; background:rgba(13,49,78,.58); border:1px solid rgba(116,211,236,.24); box-shadow:inset 0 1px rgba(255,255,255,.09); }} .care-flow b {{ color:#65d8ee; font-weight:500; }}
        .important-note {{ margin:1.35rem auto .7rem; max-width:900px; padding:15px 18px; border-left:3px solid #68d9ee; border-radius:0 13px 13px 0; background:rgba(9,42,65,.58); color:#dff7ff; line-height:1.6; }}
        .section-card {{ padding:23px 24px; }} .section-title {{ color:#f4fbff; font-family:'Manrope',sans-serif; font-weight:700; font-size:1.04rem; }}
        .metric-icon {{ border:1px solid rgba(139,219,240,.22); box-shadow:inset 0 1px rgba(255,255,255,.16),0 0 16px rgba(56,195,221,.08); }}
        .metric-icon.blue,.metric-icon.purple {{ background:rgba(24,105,136,.28); }} .metric-icon.red {{ background:rgba(138,24,54,.34); }} .metric-icon.green {{ background:rgba(18,108,91,.3); }}
        .metric-val {{ color:#f5fcff; }} .metric-lbl,.index-field-label {{ color:#9bb4ca; }}
        .index-field {{ background:rgba(3,15,35,.52); border-color:rgba(125,195,224,.17); border-radius:12px; }} .index-field-value {{ color:#e6f8ff; }}
        div[data-testid="stButton"] > button, div[data-testid="stDownloadButton"] > button {{ background:linear-gradient(135deg,#0e7da0,#145e95 55%,#8d153f) !important; color:#f8fdff !important; border:1px solid rgba(154,223,243,.35) !important; border-radius:11px !important; box-shadow:inset 0 1px rgba(255,255,255,.18),0 8px 18px rgba(1,18,42,.24); font-weight:700 !important; transition:transform .2s ease,filter .2s ease !important; }}
        div[data-testid="stButton"] > button:hover,div[data-testid="stDownloadButton"] > button:hover {{ transform:translateY(-2px); filter:brightness(1.14); }}
        div[data-testid="stTextInput"] input,div[data-testid="stNumberInput"] input,div[data-testid="stSelectbox"] [data-baseweb="select"] > div {{ background:rgba(4,18,40,.7) !important; color:#eaf6ff !important; border-color:rgba(119,201,232,.3) !important; border-radius:10px !important; }}
        div[data-testid="stTextInput"] input:focus,div[data-testid="stNumberInput"] input:focus {{ border-color:#5ed2ec !important; box-shadow:0 0 0 2px rgba(94,210,236,.13) !important; }}
        label,[data-testid="stWidgetLabel"] p {{ color:#b6cbdb !important; font-size:.82rem !important; }}
        div[data-testid="stPageLink"] a {{ background:rgba(8,25,49,.7); border:1px solid rgba(134,202,229,.17); border-radius:10px; color:#b7d1e4; justify-content:center; padding:8px 10px; transition:all .2s ease; }}
        div[data-testid="stPageLink"] a:hover {{ background:rgba(19,76,105,.68); border-color:rgba(102,214,240,.5); color:#fff; transform:translateY(-1px); }}
        .result-box,.emergency {{ backdrop-filter:blur(14px); }} .result-box.low {{ background:rgba(5,71,62,.63); border-color:rgba(65,211,166,.55); }} .result-box.mid {{ background:rgba(91,67,9,.58); border-color:rgba(243,191,64,.58); }} .result-box.high,.emergency {{ background:rgba(91,16,37,.65); border-color:rgba(244,100,126,.58); }}
        .risk-bar-bg {{ background:rgba(1,12,30,.72); border:1px solid rgba(126,198,226,.12); height:9px; overflow:hidden; }} .risk-bar-fill {{ box-shadow:0 0 14px currentColor; }}
        .stDataFrame,div[data-testid="stDataFrameResizable"] {{ border:1px solid rgba(130,202,229,.23) !important; border-radius:13px !important; overflow:hidden; }}
        [data-testid="stAlert"] {{ background:rgba(9,31,57,.78); border:1px solid rgba(134,202,229,.25); border-radius:13px; backdrop-filter:blur(12px); }}
        details {{ background:rgba(8,27,52,.68); border:1px solid rgba(126,195,222,.2); border-radius:12px; padding:4px 12px; }}
        #google_translate_element {{ display:flex; align-items:center; min-height:26px; margin-left:auto; }}
        .goog-te-gadget {{ color:transparent !important; font-size:0 !important; }} .goog-te-gadget select {{ background:rgba(7,27,54,.82); color:#d8f2fc; border:1px solid rgba(128,211,239,.36); border-radius:8px; padding:5px 8px; font:600 .75rem 'DM Sans',sans-serif; outline:none; }}
        .goog-te-banner-frame.skiptranslate,iframe.goog-te-banner-frame,iframe.VIpgJd-ZVi9od-ORHb-OEVmcd {{ display:none !important; }} body {{ top:0 !important; }} .skiptranslate {{ font-size:0; }}
        @media(max-width:720px) {{ .block-container {{ padding: .8rem 1rem 2rem; }} .navbar {{ align-items:flex-start; flex-direction:column; }} #google_translate_element {{ margin-left:0; }} .hero,.hero-banner {{ padding:22px; }} .metrics-row {{ grid-template-columns:1fr 1fr; }} .care-flow {{ align-items:flex-start; flex-direction:column; }} .care-flow b {{ transform:rotate(90deg); margin-left:13px; }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="navbar"><div class="navbar-brand"><span class="navbar-logo">&#10010;</span><div><p class="navbar-title">SickleScreen</p><p class="navbar-sub">AI-assisted sickle-cell screening from CBC parameters</p></div></div><div id="google_translate_element" aria-label="Select website language"></div></div>',
        unsafe_allow_html=True,
    )
    components.html(
        """
        <script>
        const doc = window.parent.document;
        if (!doc.getElementById('google-translate-script')) {
          window.parent.googleTranslateElementInit = function () {
            const target = doc.getElementById('google_translate_element');
            if (target && !target.hasChildNodes() && window.parent.google && window.parent.google.translate) {
              new window.parent.google.translate.TranslateElement({pageLanguage:'en', autoDisplay:false}, 'google_translate_element');
            }
          };
          const script = doc.createElement('script');
          script.id = 'google-translate-script';
          script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
          doc.head.appendChild(script);
        } else if (window.parent.googleTranslateElementInit) { window.parent.googleTranslateElementInit(); }
        </script>
        """,
        height=0,
    )
