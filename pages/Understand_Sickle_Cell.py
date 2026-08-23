import base64
from pathlib import Path

import streamlit as st

from FrontStyle.theme import inject_theme


st.set_page_config(page_title="Understand Sickle Cell | SickleScreen", page_icon="🩸", layout="wide")
inject_theme()

nav = st.columns(4, gap="small")
for col, path, label, icon in zip(
    nav,
    ["app.py", "pages/Understand_Sickle_Cell.py", "app.py", "pages/About.py"],
    ["Screen", "Understand", "History", "About"],
    [":material/bloodtype:", ":material/genetics:", ":material/monitoring:", ":material/info:"],
):
    with col:
        st.page_link(path, label=label, icon=icon)

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">Visual medical guide</div>
      <h1>Understand Sickle Cell</h1>
      <p>See how sickle cell disease affects red blood cells, why complications can occur, and where screening fits in.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

infographic_path = Path(__file__).with_name("About_sickle.png")
infographic = base64.b64encode(infographic_path.read_bytes()).decode("ascii")
st.markdown(
    f'<img class="understand-visual" src="data:image/png;base64,{infographic}" alt="Sickle cell disease visual guide">',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="understand-copy">
      <div class="support-panel">
        <h2>What is sickle cell disease?</h2>
        <p>Sickle cell disease is an inherited blood disorder in which red blood cells can become rigid and sickle-shaped, affecting blood flow and oxygen delivery.</p>
        <h2>Why screening matters</h2>
        <p>CBC parameters can help identify patterns that may warrant further evaluation, but screening alone cannot confirm sickle cell disease.</p>
        <h2>What happens next?</h2>
        <div class="care-flow"><span>CBC screening</span><b>→</b><span>Possible risk identified</span><b>→</b><span>Confirmatory laboratory testing</span><b>→</b><span>Healthcare professional</span></div>
      </div>
    </div>
    <div class="important-note"><strong>Important.</strong> SickleScreen is an educational screening aid, not a diagnostic test. Screening results should be discussed with a qualified healthcare professional and confirmed using appropriate laboratory testing.</div>
    """,
    unsafe_allow_html=True,
)

with st.expander("References & Sources"):
    st.markdown(
        """
        - Centers for Disease Control and Prevention (CDC) — Sickle Cell Disease.
        - National Heart, Lung, and Blood Institute (NHLBI) — Sickle Cell Disease.
        - World Health Organization (WHO) — Sickle-cell disease resources.
        - MedlinePlus — Sickle Cell Disease.
        - American Society of Hematology (ASH) — Sickle Cell Disease Resources.
        - National Institutes of Health (NIH) and National Human Genome Research Institute (NHGRI) — genetics and inheritance information.
        """
    )
