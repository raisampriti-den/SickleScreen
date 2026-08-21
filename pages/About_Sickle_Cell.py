import streamlit as st
from FrontStyle.theme import inject_theme

st.set_page_config(page_title="About Sickle Cell | SickleScreen", page_icon="🩸", layout="wide")

st.markdown("""
<style>
.block-container { padding-top: 1rem; max-width: 1200px; }
.hero { background:linear-gradient(135deg,#0f172a,#2a103d); border:1px solid #334155;
border-radius:18px; padding:32px; margin:12px 0 22px; }
.eyebrow { color:#e879f9; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.hero h1 { color:#f8fafc; margin:.3rem 0; }
.hero p { color:#cbd5e1; max-width:760px; }
.card { background:#0f172a; border:1px solid #1e293b; border-radius:14px; padding:20px; height:100%; }
.card h3 { color:#f8fafc; font-size:1rem; }
.card p, .card li { color:#cbd5e1; line-height:1.65; }
.fact { color:#e879f9; font-weight:700; }
div[data-testid="stPageLink"] a { background:#0f172a; border:1px solid #1e293b; border-radius:8px;
justify-content:center; padding:7px 10px; }
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
<div class="hero">
  <div class="eyebrow">Education center</div>
  <h1>About Sickle Cell</h1>
  <p>Sickle cell disease is an inherited blood disorder. Understanding the difference between
  sickle cell disease and sickle cell trait helps families make informed health decisions.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")
with left:
    st.markdown("""
    <div class="card">
      <h3>What happens in the blood?</h3>
      <p>Red blood cells normally stay flexible and round so they can move easily through blood
      vessels. In sickle cell disease, abnormal hemoglobin can make some cells hard, sticky, and
      sickle-shaped. These cells can break down early and sometimes block blood flow.</p>
      <p>Repeated blockage of blood flow may cause pain episodes, increase the risk of infection, and damage organs over time. Early breakdown of red blood cells can cause anemia.</p>
    </div>
    """, unsafe_allow_html=True)
with right:
    st.markdown("""
    <div class="card">
      <h3>Disease and trait are different</h3>
      <p><span class="fact">Sickle cell disease (SCD)</span> occurs when a person inherits two
      abnormal hemoglobin genes, one from each parent. Symptoms and severity vary.</p>
      <p><span class="fact">Sickle cell trait (SCT)</span> Sickle cell trait (SCT) usually occurs when a person inherits one sickle hemoglobin gene (HbS) and one normal hemoglobin gene (HbA). Most people with trait do not have symptoms, but they can pass
      the gene to their children.</p>
    </div>
    """, unsafe_allow_html=True)

st.subheader("How it is inherited")
st.write(
    "Sickle cell conditions are inherited; they are not contagious. When both parents have "
    "sickle cell trait, each pregnancy has a 25% chance of sickle cell disease, a 50% chance "
    "of sickle cell trait, and a 25% chance of neither. These probabilities apply to each pregnancy independently"
)

st.subheader("Testing and diagnosis")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>Screening</h3><p>Screening tests identify individuals who may be at risk and who could benefit from confirmatory laboratory testing. Screening alone cannot diagnose sickle cell disease or sickle cell trait.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>Confirmatory testing</h3><p>Hemoglobin electrophoresis, HPLC, or other laboratory testing can identify hemoglobin types.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>Genetic counseling</h3><p>A trained professional can explain results, inheritance, and reproductive choices without stigma.</p></div>', unsafe_allow_html=True)

with st.expander("Common myths and facts"):
    st.markdown("""
    - **Myth:** Sickle cell disease spreads between people. **Fact:** It is inherited and is not contagious.
    - **Myth:** Sickle cell trait and disease are the same. **Fact:** They have different gene patterns and health effects.
    - **Myth:** A person with sickle cell disease cannot live a full life. **Fact:** Regular care and modern treatment can greatly improve health and quality of life.
    """)

st.info("Educational information only. SickleScreen is not a diagnostic test. Discuss screening or laboratory results with a qualified healthcare professional.")
st.caption(
    "Educational information only. Content adapted from CDC, NHLBI, WHO, "
    "MedlinePlus, NIH, NHGRI, and American Society of Hematology resources."
)
st.markdown("""
### References

1. Centers for Disease Control and Prevention (CDC). *Sickle Cell Disease (SCD)*.
   https://www.cdc.gov/sickle-cell

2. National Heart, Lung, and Blood Institute (NHLBI). *Sickle Cell Disease*.
   https://www.nhlbi.nih.gov/health/sickle-cell-disease

3. World Health Organization (WHO). *Sickle-cell disease fact sheets and global health resources*.
   https://www.who.int

4. MedlinePlus. *Sickle Cell Disease*.
   https://medlineplus.gov/sicklecelldisease.html

5. American Society of Hematology (ASH). *Sickle Cell Disease Resources*.
   https://www.hematology.org

6. National Institutes of Health (NIH). *Genetics and inheritance information for Sickle Cell Disease*.
   https://www.nih.gov

7. National Human Genome Research Institute (NHGRI). *Learning About Sickle Cell Disease*.
   https://www.genome.gov
""")
