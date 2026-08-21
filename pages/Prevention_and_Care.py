import streamlit as st
from FrontStyle.theme import inject_theme

st.set_page_config(page_title="Prevention and Care | SickleScreen", page_icon="🩸", layout="wide")

st.markdown("""
<style>
.block-container { padding-top:1rem; max-width:1200px; }
.hero { background:linear-gradient(135deg,#0f172a,#103426); border:1px solid #334155; border-radius:18px; padding:32px; margin:12px 0 22px; }
.hero h1 { color:#f8fafc; margin:.3rem 0; }.hero p,.card p,.card li { color:#cbd5e1; line-height:1.65; }
.eyebrow { color:#4ade80; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.card { background:#0f172a; border:1px solid #1e293b; border-radius:14px; padding:20px; height:100%; }
.card h3 { color:#f8fafc; font-size:1rem; }
div[data-testid="stPageLink"] a { background:#0f172a; border:1px solid #1e293b; border-radius:8px; justify-content:center; padding:7px 10px; }
</style>
""", unsafe_allow_html=True)
inject_theme()

nav = st.columns(5)
for col, path, label, icon in zip(nav,
    ["app.py", "pages/About_Sickle_Cell.py", "pages/How_It_Affects_Us.py", "pages/Symptoms.py", "pages/Prevention_and_Care.py"],
    ["Dashboard", "About", "Impact", "Symptoms", "Care"],
    [":material/home:", ":material/menu_book:", ":material/groups:", ":material/medical_information:", ":material/health_and_safety:"]):
    with col:
        st.page_link(path, label=label, icon=icon)

st.markdown("""
<div class="hero"><div class="eyebrow">Living well</div>
<h1>Prevention and Care</h1>
<p>Symptoms of sickle cell disease can vary widely between individuals and may change over time. While most people with sickle cell trait do not experience symptoms, sickle cell disease can cause chronic anemia, painful complications, and damage to multiple organs if not properly managed.</p></div>
""", unsafe_allow_html=True)

st.subheader("Everyday care")
cols = st.columns(3)
items = [
    ("Stay hydrated", "Drink water regularly, especially during hot weather, illness, travel, or physical activity. Ask a clinician about individual fluid needs."),
    ("Avoid extremes", "Sudden temperature changes, extreme heat or cold, high altitude, and overexertion may trigger problems for some people."),
    ("Build a care plan", "Keep regular appointments, know emergency warning signs, and carry important health information when possible."),
]
for col, (title, body) in zip(cols, items):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.subheader("Medical care may include")
left, right = st.columns(2, gap="large")
with left:
    st.markdown("""
    <div class="card"><h3>Prevention and monitoring</h3>
    <ul><li>Recommended vaccinations and infection prevention</li><li>Routine blood and organ-health checks</li>
    <li>Stroke-risk screening for eligible children</li><li>Eye, kidney, and other specialist checks when advised</li></ul></div>
    """, unsafe_allow_html=True)
with right:
    st.markdown("""
    <div class="card"><h3>Treatment options</h3>
    <ul><li>Medicines that reduce pain episodes or other complications</li><li>Pain management and treatment of infections</li>
    <li>Blood transfusion for selected situations</li><li>For some patients, transplant or gene-based therapy may be considered</li></ul></div>
    """, unsafe_allow_html=True)

st.info("Medicines, supplements, transfusions, and other treatments must be chosen and monitored by qualified healthcare professionals. Never start or stop prescribed treatment based on this page.")

st.subheader("Planning for families")
st.write(
    "Voluntary sickle cell testing can help people learn whether they have disease, trait, or neither. "
    "Genetic counseling can explain how genes may be passed to children and support informed, non-directive decisions."
)

with st.expander("Simple appointment checklist"):
    st.markdown("""
    - Bring a current medicine list and recent test results.
    - Mention new pain, fever, breathing difficulty, fatigue, or other changes.
    - Ask which vaccines, screenings, and follow-up tests are due.
    - Ask for a written pain and emergency plan.
    - Discuss pregnancy, travel, exercise, or school/work needs in advance.
    """)

st.error("Fever, chest pain, breathing difficulty, stroke signs, severe uncontrolled pain, or unusual sleepiness require urgent medical assessment.")
st.info(
    "Pain crises occur when sickled red blood cells obstruct small blood vessels, reducing oxygen delivery to tissues."
)
st.caption(
    "Educational information only. Content adapted from CDC, NHLBI, WHO, "
    "MedlinePlus, NIH, NHGRI, and American Society of Hematology resources."
)
