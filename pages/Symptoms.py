import streamlit as st

st.set_page_config(page_title="Symptoms | SickleScreen", page_icon="🩸", layout="wide")

st.markdown("""
<style>
.block-container { padding-top:1rem; max-width:1200px; }
.hero { background:linear-gradient(135deg,#0f172a,#35131d); border:1px solid #334155; border-radius:18px; padding:32px; margin:12px 0 22px; }
.hero h1 { color:#f8fafc; margin:.3rem 0; }.hero p,.card p,.card li { color:#cbd5e1; line-height:1.65; }
.eyebrow { color:#fb7185; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.card { background:#0f172a; border:1px solid #1e293b; border-radius:14px; padding:20px; height:100%; }
.card h3 { color:#f8fafc; font-size:1rem; }
.emergency { background:#2b0b12; border:1px solid #ef4444; border-radius:14px; padding:22px; }
.emergency h3 { color:#fca5a5; }
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
<div class="hero"><div class="eyebrow">Recognize the signs</div>
<h1>Symptoms and Warning Signs</h1>
<p>Symptoms of sickle cell disease can vary widely between individuals and may change over time.
While most people with sickle cell trait do not experience symptoms, sickle cell disease can cause
chronic anemia, painful complications, and damage to multiple organs if not properly managed.</p></div>
""", unsafe_allow_html=True)

st.subheader("Common Symptoms of Sickle Cell Disease")
cols = st.columns(3)
items = [
    (
        "Pain Episodes (Pain Crises)",
        "Pain can occur when sickled red blood cells block blood flow through small blood vessels. "
        "Pain episodes may be sudden, severe, and can affect different parts of the body.",
    ),
    (
        "Anemia and Fatigue",
        "Because sickled red blood cells break down more quickly than normal cells, people may "
        "experience tiredness and fatigue, weakness, shortness of breath, or pale skin or inner eyelids.",
    ),
    (
        "Swelling of the Hands and Feet",
        "Painful swelling of the hands and feet, known as dactylitis, may be one of the earliest "
        "signs of sickle cell disease in infants and young children.",
    ),
]
for col, (title, body) in zip(cols, items):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

cols = st.columns(3)
items = [
    (
        "Increased Risk of Infection",
        "Damage to the spleen can reduce the body's ability to fight certain infections, increasing "
        "the risk of serious illness, particularly during childhood.",
    ),
    (
        "Yellowing of the Eyes or Skin",
        "Jaundice may occur because red blood cells break down faster than normal, leading to "
        "increased levels of bilirubin in the body.",
    ),
    (
        "Growth, Development, and Vision Problems",
        "Some children with sickle cell disease may grow more slowly than expected. Changes in blood "
        "flow can also affect the eyes and increase the risk of vision problems.",
    ),
]
for col, (title, body) in zip(cols, items):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

st.markdown("""
<div class="emergency">
<h3>Seek Urgent Medical Care Immediately</h3>
<p>People living with sickle cell disease should receive urgent medical assessment if they experience:</p>
<ul>
<li>Fever, especially in children</li>
<li>Chest pain, difficulty breathing, or severe cough</li>
<li>Signs of stroke, including sudden weakness or numbness, facial drooping, difficulty speaking
or understanding speech, confusion, severe headache, or seizures</li>
<li>Severe pain that cannot be controlled with prescribed treatment</li>
<li>Fainting, extreme drowsiness, or unusual sleepiness</li>
<li>A rapidly enlarging abdomen</li>
<li>A painful erection lasting more than two hours (priapism)</li>
</ul>
<p>Prompt medical attention can help prevent serious complications.</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Sickle Cell Trait: What to Know")
st.write(
    "Most people with sickle cell trait (SCT) do not develop symptoms of sickle cell disease and "
    "live healthy lives without complications."
)
st.write("Rare health problems may occur under extreme conditions such as:")
st.markdown("""
- Severe dehydration
- Very intense physical exertion
- High-altitude environments
- Low-oxygen conditions
""")
st.write(
    "Individuals with sickle cell trait can pass the sickle cell gene to their children. A healthcare "
    "professional or genetic counselor can explain personal risks and inheritance patterns."
)

st.subheader("Important Note")
st.warning(
    "This page is intended for educational purposes only and should not be used to diagnose medical "
    "conditions. If you have concerns about symptoms or health risks, consult a qualified healthcare "
    "professional. For emergency warning signs, seek immediate medical attention."
)