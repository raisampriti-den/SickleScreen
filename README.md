# 🩸 SickleScreen
### AI-Assisted Sickle Cell Carrier Screening for Frontline Health Workers

> *"Identify sickle cell carriers in 60 seconds — using blood reports they already have."*

---

## 📌 The Problem

Sickle cell disease is one of the most prevalent genetic disorders in India, disproportionately affecting tribal communities in Odisha, Chhattisgarh, Madhya Pradesh, Maharashtra, and Gujarat. India accounts for roughly **14% of the global sickle cell burden**, with an estimated 10–15 million carriers nationwide.

Despite the Government of India's **National Sickle Cell Anaemia Elimination Mission (2047)**, early detection at the community level remains broken:

- ASHA workers — the first point of contact in tribal health — **have no digital screening tool**
- Confirmatory testing (HPLC / Hb electrophoresis) is only available at district hospitals, often hours away
- Standard CBC reports are generated at PHCs but **never analyzed for carrier risk**
- Carriers are routinely missed until they have affected children

**SickleScreen bridges that gap.**

---

## 💡 What Is SickleScreen?

SickleScreen is a **mobile-first Streamlit application** that takes standard CBC (Complete Blood Count) values — which are routinely collected at Primary Health Centres — and runs them through a trained Random Forest model to produce a **carrier probability score** in seconds.

It is designed to be used by ASHA workers and PHC staff with **no medical AI expertise required**. The output is a simple three-tier recommendation:

| Risk Score | Status | Action |
|---|---|---|
| < 30% | 🟢 **CLEAR** | Low likelihood of carrier status |
| 30–70% | 🟡 **MONITOR** | Retest recommended |
| > 70% | 🔴 **REFER IMMEDIATELY** | Refer for HPLC / Hb electrophoresis |

The app also surfaces the **nearest government HPLC referral centre** with a contact number, based on the patient's district.

---

## 🧬 How It Works — The Science

Sickle cell trait carriers typically show a **distinct CBC signature** compared to healthy individuals:

| Parameter | Normal Range | Carrier Pattern |
|---|---|---|
| Hemoglobin (Hb) | 12–16 g/dL | Mildly reduced (~9–11 g/dL) |
| MCV | 80–100 fL | Microcytic (~70–85 fL) |
| MCH | 27–32 pg | Reduced (~22–27 pg) |
| RBC Count | 4–5.5 M/µL | Often low-normal (~3.5–4.2) |

Beyond raw CBC values, SickleScreen engineers two clinically validated hematological indices:

- **Mentzer Index** = MCV / RBC — helps differentiate sickle trait from iron deficiency anaemia
- **Shine-Lal Index** = (MCV² × MCH) / 100 — a composite discriminant index for microcytic anaemias

These 6 features together power the Random Forest classifier.

---

## 🧠 The ML Pipeline

### Data
- **500 synthetic samples** generated from published Indian clinical literature (250 normal, 250 carriers)
- CBC distributions modeled from mean ± SD values reported in ICMR studies and peer-reviewed Indian hematology journals
- Dataset saved as `sicklescreen_raw_data.csv`

### Model
- **Algorithm:** Random Forest Classifier (100 estimators, `random_state=42`)
- **Train/Test Split:** 80% / 20%, stratified
- **Target Metric:** Carrier Sensitivity (Recall) — chosen because false negatives (missing a carrier) are clinically worse than false positives
- **Benchmark:** The model is validated against the **69% multicenter sensitivity benchmark** from published Indian sickle cell screening studies
- **Output:** `sicklescreen_model.pkl` (serialized via `joblib`)

### Feature Importance
The model assigns highest importance to MCV, MCH, and the Shine-Lal Index — consistent with clinical literature indicating microcytic indices as strongest discriminants.

---

## 🗂️ Project Structure

```
SickleScreen/
│
├── app.py                      # Main Streamlit application
├── samfile1.py                 # ML training pipeline (data gen → model export)
├── samfile2.py                 # Standalone inference/prediction script
│
├── sicklescreen_model.pkl      # Trained Random Forest model
├── sicklescreen_raw_data.csv   # Synthetic training dataset (500 samples)
├── patient_history.csv         # Auto-generated screening log
│
├── .venv/                      # Virtual environment
└── README.md
```

---

## 🖥️ Application Walkthrough

### Screen 1 — Patient Information
- Enter patient name
- Select district (Khordha, Koraput, Sundargarh, Cuttack — expandable)

### Screen 2 — CBC Input
- Enter four standard CBC values: **Hb, MCV, MCH, RBC Count**
- All values are available on any standard CBC report printed at a PHC

### Screen 3 — Risk Score + Recommendation
- Model computes carrier probability
- Displays percentage score and colour-coded recommendation (Clear / Monitor / Refer)

### Screen 4 — Referral Centre
- Automatically surfaces the nearest government HPLC centre for the selected district
- Shows centre name and direct phone number

### Screen 5 — Patient History Log
- All screenings are appended to `patient_history.csv`
- Last 100 records displayed in-app for the health worker's reference

---

## 🏥 Referral Database (Current Coverage)

| District | Referral Centre | Contact |
|---|---|---|
| Khordha | Capital Hospital, Bhubaneswar | 0674-2431257 |
| Koraput | District Headquarters Hospital | 06852-250387 |
| Sundargarh | IGH Rourkela | 0661-2473456 |
| Cuttack | SCB Medical College | 0671-2414355 |

> Planned expansion: Maharashtra, Madhya Pradesh, Chhattisgarh, Gujarat — covering the full tribal sickle cell belt.

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/SickleScreen.git
cd SickleScreen

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install streamlit pandas scikit-learn joblib numpy

# 4. (Optional) Retrain the model from scratch
python samfile1.py

# 5. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## 🧪 Validation

To test the model against known carrier CBC profiles from published literature, run the inference script:

```bash
python samfile2.py
```

This loads a sample patient with known carrier-range CBC values (`Hb: 10.5, MCV: 76, MCH: 25, RBC: 4.1`) and prints the carrier probability and recommendation.

For formal validation, 5–10 published case studies of confirmed sickle cell trait carriers were run through the model to verify correct flagging — consistent with the >69% sensitivity threshold.

---

## 🗺️ Roadmap

| Phase | Feature | Status |
|---|---|---|
| ✅ Week 1 | Synthetic dataset generation + feature engineering | Done |
| ✅ Week 2 | Random Forest model training + evaluation | Done |
| ✅ Week 3 | Streamlit app + referral database | Done |
| 🔄 Week 4 | Multilingual support (Hindi, Odia, Marathi) via IndicTrans2 | In Progress |
| 🔜 Week 5 | PDF report generation for doctors | Planned |
| 🔜 Week 5 | Expanded referral database (5-state coverage) | Planned |
| 🔜 Week 6 | Field validation with real PHC CBC data | Planned |

---

## 🌐 Multilingual Support (Planned)

Using [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) — an open-source, free translation API built for Indian languages — SickleScreen will support:
- **Hindi** (primary target)
- **Odia** (Odisha tribal belt)
- **Marathi** (Maharashtra coverage)

This makes the tool usable by ASHA workers who are not comfortable with English-language interfaces.

---

## 🎯 Impact Potential

- **~900,000 ASHA workers** operate across India's rural and tribal areas
- Sickle cell belt states — Odisha, Chhattisgarh, MP, Maharashtra, Gujarat — have the highest unmet screening burden
- SickleScreen aligns directly with the **National Sickle Cell Anaemia Elimination Mission 2047** launched by the Government of India
- Every PHC already generates CBC reports — SickleScreen adds **zero cost and zero new tests** to the workflow

---

## 👥 Team

| Name | Role |
|---|---|
| **[Sampriti Halder]** | Biology domain, dataset research, referral database, validation, ML pipeline |
| **[Duradarshee Chinara]** |Backend logic, Streamlit interface, PDF generation |

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- ICMR and Indian Journal of Hematology for published CBC reference ranges
- [AI4Bharat](https://ai4bharat.iitm.ac.in/) for IndicTrans2 multilingual support
- Government of India — National Sickle Cell Anaemia Elimination Mission 2047

---

*Built for Samsung Solve for Tomorrow 2026 — using technology to serve frontline health workers in tribal India.*
