import streamlit as st
import pandas as pd
import joblib
import os

# =====================================================

# PAGE CONFIG

# =====================================================

st.set_page_config(
page_title="SickleScreen",
page_icon="🩸",
layout="centered"
)

# =====================================================

# LOAD MODEL

# =====================================================

model = joblib.load("sicklescreen_model.pkl")

# =====================================================

# REFERRAL DATABASE

# =====================================================

referral_data = {
"Khordha": {
"center": "Capital Hospital, Bhubaneswar",
"phone": "0674-2431257"
},
"Koraput": {
"center": "District Headquarters Hospital",
"phone": "06852-250387"
},
"Sundargarh": {
"center": "IGH Rourkela",
"phone": "0661-2473456"
},
"Cuttack": {
"center": "SCB Medical College",
"phone": "0671-2414355"
}
}

# =====================================================

# HEADER

# =====================================================

st.title("🩸 SickleScreen")
st.write("AI-assisted screening tool for sickle cell carrier detection")

# =====================================================

# PATIENT DETAILS

# =====================================================

st.subheader("Patient Information")

patient_name = st.text_input("Patient Name")

district = st.selectbox(
"District",
list(referral_data.keys())
)

# =====================================================

# CBC INPUTS

# =====================================================

st.subheader("CBC Parameters")

hb = st.number_input(
"Hemoglobin (Hb)",
min_value=0.0,
max_value=25.0,
value=12.0
)

mcv = st.number_input(
"MCV",
min_value=0.0,
max_value=150.0,
value=80.0
)

mch = st.number_input(
"MCH",
min_value=0.0,
max_value=50.0,
value=27.0
)

rbc = st.number_input(
"RBC Count",
min_value=0.1,
max_value=10.0,
value=4.5
)

# =====================================================

# SCREENING BUTTON

# =====================================================

if st.button("Screen Patient"):

    patient = pd.DataFrame({
        "Hb": [hb],
        "MCV": [mcv],
        "MCH": [mch],
        "RBC": [rbc]
    })

    patient["mentzer_index"] = (
        patient["MCV"] / patient["RBC"]
    )

    patient["shine_lal_index"] = (
        patient["MCV"] ** 2 * patient["MCH"]
    ) / 100

    risk = model.predict_proba(patient)[0][1]

    st.subheader(
        f"Carrier Risk: {risk * 100:.1f}%"
    )

    if risk < 0.30:
        recommendation = "CLEAR"
        st.success(
            "🟢 CLEAR\n\nLow likelihood of carrier status."
        )

    elif risk < 0.70:
        recommendation = "MONITOR"
        st.warning(
            "🟡 MONITOR\n\nRetesting recommended."
        )

    else:
        recommendation = "REFER"
        st.error(
            "🔴 REFER IMMEDIATELY\n\nFurther testing recommended."
        )

    # Referral Center

    center = referral_data[district]

    st.subheader("Nearest Referral Center")

    st.write(
        f"**Center:** {center['center']}"
    )

    st.write(
        f"**Phone:** {center['phone']}"
    )

    # Save History

    history_record = pd.DataFrame({
        "Name": [patient_name],
        "District": [district],
        "Hb": [hb],
        "MCV": [mcv],
        "MCH": [mch],
        "RBC": [rbc],
        "Risk (%)": [round(risk * 100, 2)],
        "Recommendation": [recommendation]
    })

    history_file = "patient_history.csv"

    if os.path.exists(history_file):

        history_record.to_csv(
            history_file,
            mode="a",
            header=False,
            index=False
        )

    else:

        history_record.to_csv(
            history_file,
            index=False
        )


# =====================================================

# HISTORY SECTION

# =====================================================

if os.path.exists("patient_history.csv"):

    st.subheader("Recent Patient History")

    history_df = pd.read_csv(
        "patient_history.csv"
    )

    st.dataframe(
        history_df.tail(100),
        use_container_width=True
    )