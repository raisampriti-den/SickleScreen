import streamlit as st

st.set_page_config(page_title="How It Affects Us | SickleScreen", page_icon="🩸", layout="wide")

st.markdown("""
<style>
.block-container { padding-top:1rem; max-width:1200px; }
.hero { background:linear-gradient(135deg,#0f172a,#162d4c); border:1px solid #334155; border-radius:18px; padding:32px; margin:12px 0 22px; }
.hero h1 { color:#f8fafc; margin:.3rem 0; }.hero p,.card p,.card li { color:#cbd5e1; line-height:1.65; }
.eyebrow { color:#60a5fa; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.card { background:#0f172a; border:1px solid #1e293b; border-radius:14px; padding:20px; height:100%; }
.card h3 { color:#f8fafc; font-size:1rem; }
div[data-testid="stPageLink"] a { background:#0f172a; border:1px solid #1e293b; border-radius:8px; justify-content:center; padding:7px 10px; }
</style>
""", unsafe_allow_html=True)

nav = st.columns(5)
for col, path, label, icon in zip(nav,
    ["app.py", "pages/About_Sickle_Cell.py", "pages/How_It_Affects_Us.py", "pages/Symptoms.py", "pages/Prevention_and_Care.py"],
    ["Dashboard", "About", "Impact", "Symptoms", "Care"],
    [":material/home:", ":material/menu_book:", ":material/groups:", ":material/medical_information:", ":material/health_and_safety:"]):
    with col:
        st.page_link(path, label=label, icon=icon)

st.markdown("""
<div class="hero"><div class="eyebrow">People and communities</div>
<h1>How Sickle Cell Affects Us</h1>
<p>Sickle cell disease can affect health, education, work, family life, and emotional wellbeing. Access to quality healthcare, community support, and accurate information can help reduce these challenges and improve quality of life.</p></div>
""", unsafe_allow_html=True)

cols = st.columns(3)
cards = [
    ("Daily life", "People living with sickle cell disease may experience pain episodes, fatigue, medical appointments, and occasional hospital visits that can interrupt normal routines. Symptoms can vary greatly from person to person and may change over time."),
    ("School and work", "Flexible attendance policies, hydration breaks, rest periods, temperature control, and individualized care plans can help students and workers participate safely and successfully."),
    ("Families", "Families often play an important role in managing medications, appointments, emergency situations, and emotional support. Access to clear information and healthcare resources helps families make informed decisions and plan for the future."),
]
for col, (title, body) in zip(cols, cards):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.subheader("Health effects can differ")
left, right = st.columns(2, gap="large")
with left:
    st.markdown("""
    <div class="card"><h3>Possible physical effects</h3>
    <ul><li>Anemia and tiredness</li><li>Episodes of severe pain</li><li>Higher risk of certain infections</li>
    <li>Delayed growth in some children</li><li>Possible complications affecting the lungs, brain, kidneys, eyes, or other organs</li></ul></div>
    """, unsafe_allow_html=True)
with right:
    st.markdown("""
    <div class="card"><h3>Emotional and social effects</h3>
                <p>Not everyone experiences the same symptoms or complications. The severity of sickle cell disease varies between individuals. Some people have mild symptoms, while others may have more frequent or severe complications. This unpredictability can lead to:</p>
    <ul><li>Stress or worry about unpredictable symptoms</li><li>Feeling isolated or misunderstood</li>
    <li>Financial and travel burdens from care</li><li>Stigma related to genetic conditions</li>
    <li>Need for mental health and peer support</li></ul></div>
    """, unsafe_allow_html=True)

st.subheader("How communities can help")
st.markdown("""
1. **Listen and believe people experiencing pain.** Pain severity cannot be judged by appearance alone.
2. **Avoid stigma.** Sickle cell disease is inherited and is nobody's fault.
3. **Support testing and counseling.** Voluntary, confidential testing helps people understand their status.
4. **Make reasonable accommodations.** Access to water, rest, warmth, and medical care can matter.
5. **Know emergency warning signs.** Fast action can save lives.
""")

st.success("A person living with sickle cell disease is more than their diagnosis. Good care, inclusion, and understanding help people learn, work, and thrive.")
st.caption(
    "Educational information only. Content adapted from CDC, NHLBI, WHO, "
    "MedlinePlus, NIH, NHGRI, and American Society of Hematology resources."
)
