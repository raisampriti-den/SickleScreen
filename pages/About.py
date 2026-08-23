import streamlit as st

from FrontStyle.theme import inject_theme


st.set_page_config(page_title="About | SickleScreen", page_icon="🩸", layout="wide")
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
      <div class="eyebrow">About SickleScreen</div>
      <h1>Clearer screening, informed next steps.</h1>
      <p>SickleScreen is an AI-assisted educational screening tool that uses CBC parameters to help identify patterns that may need confirmatory testing and clinical review.</p>
    </div>
    <div class="card"><h3>Designed to support—not replace—care</h3><p>Results are intended to guide conversations with qualified healthcare professionals. They are not a diagnosis and should always be confirmed with appropriate laboratory testing.</p></div>
    """,
    unsafe_allow_html=True,
)
