import joblib
import pandas as pd

# Load trained model
model = joblib.load("sicklescreen_model.pkl")

# Example patient
patient = pd.DataFrame({
    "Hb": [10.5],
    "MCV": [76],
    "MCH": [25],
    "RBC": [4.1]
})

# Feature engineering
patient["mentzer_index"] = patient["MCV"] / patient["RBC"]
patient["shine_lal_index"] = (patient["MCV"] ** 2 * patient["MCH"]) / 100

# Predict
prediction = model.predict(patient)[0]

# Display result
if prediction == 1:
    print("🩸 Screening Result: LIKELY CARRIER")
    print("Recommendation: Refer for confirmatory testing (Hb electrophoresis/HPLC).")
else:
    print("✅ Screening Result: NOT AFFECTED")
    print("No carrier pattern detected based on the model.")