import joblib
import pandas as pd

# Load trained model
model = joblib.load("sicklescreen_best_model.pkl")

# Example patient
patient = pd.DataFrame({
    "Hb": [10.5],
    "MCV": [76],
    "MCH": [25],
    "RBC": [4.1],
})

# Feature engineering
patient["mentzer_index"] = patient["MCV"] / patient["RBC"]
patient["shine_lal_index"] = (patient["MCV"] ** 2 * patient["MCH"]) / 100

# Predict carrier status (1 = likely carrier, 0 = not affected)
prediction = model.predict(patient)[0]
prob = model.predict_proba(patient)[0][1]

print(f"Carrier Risk: {prob * 100:.1f}%")

# Display result
if prediction == 1:
    print("Screening Result: LIKELY CARRIER")
    print("Recommendation: Refer for confirmatory testing (Hb electrophoresis/HPLC).")
else:
    print("Screening Result: NOT AFFECTED")
    print("No carrier pattern detected based on the model.")
