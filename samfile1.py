# =====================================================================
# SICKLESCREEN: STEP 3 - MODEL GENERATION & TRAINING PIPELINE (WEEK 1)
# =====================================================================

import joblib
import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

try:
    from xgboost import XGBClassifier
except ImportError:
    XGBClassifier = None

# ---------------------------------------------------------------------
# STEP 1: Generate Synthetic Dataset
# ---------------------------------------------------------------------

np.random.seed(42)
n_samples = 250

# Class 0: Healthy Controls
normal_df = pd.DataFrame({
    "Hb": np.random.normal(13.50, 1.20, n_samples),
    "MCV": np.random.normal(90.00, 5.00, n_samples),
    "MCH": np.random.normal(29.00, 2.00, n_samples),
    "RBC": np.random.normal(4.50, 0.40, n_samples),
    "is_carrier": 0,
})

# Class 1: Sickle Cell Trait Carriers
carrier_df = pd.DataFrame({
    "Hb": np.random.normal(9.31, 2.25, n_samples),
    "MCV": np.random.normal(78.52, 12.17, n_samples),
    "MCH": np.random.normal(26.30, 6.56, n_samples),
    "RBC": np.random.normal(3.72, 0.88, n_samples),
    "is_carrier": 1,
})

# Combine datasets
raw_data = pd.concat([normal_df, carrier_df]).reset_index(drop=True)

# Save dataset
raw_data.to_csv("sicklescreen_raw_data.csv", index=False)

print("Step 1: Synthetic data successfully generated and saved.")

# ---------------------------------------------------------------------
# STEP 2: Load Data & Feature Engineering
# ---------------------------------------------------------------------

df = pd.read_csv("sicklescreen_raw_data.csv")

# Mentzer Index = MCV / RBC
df["mentzer_index"] = df["MCV"] / df["RBC"]

# Shine-Lal Index = (MCV^2 * MCH) / 100
df["shine_lal_index"] = ((df["MCV"] ** 2) * df["MCH"]) / 100

print("Step 2: Feature engineering completed.")

# ---------------------------------------------------------------------
# STEP 3: Train-Test Split
# ---------------------------------------------------------------------

X = df.drop("is_carrier", axis=1)
y = df["is_carrier"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

print("Step 3: Dataset split completed.")

# ---------------------------------------------------------------------
# STEP 4: Compare Models
# ---------------------------------------------------------------------

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
    ),
    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("svm", CalibratedClassifierCV(
            estimator=SVC(
                kernel="rbf",
                class_weight="balanced",
                random_state=42,
            ),
            cv=3,
        )),
    ]),
}

if XGBClassifier is not None:
    models["XGBoost"] = XGBClassifier(
        n_estimators=100,
        learning_rate=0.05,
        max_depth=3,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=42,
    )
else:
    print("XGBoost not installed, so Random Forest and SVM will be compared.")
    print("To include XGBoost, run this inside the project folder:")
    print(r".\.venv\Scripts\python.exe -m pip install xgboost")

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
results = []

print("Step 4: Training and comparing models.")

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    sensitivity = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    cv_auc = cross_val_score(model, X, y, cv=cv, scoring="roc_auc")

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Sensitivity/Recall": sensitivity,
        "F1 Score": f1,
        "AUC-ROC": auc,
        "CV AUC Mean": cv_auc.mean(),
        "CV AUC Std": cv_auc.std(),
    })

    print(f"\n--- {name} PERFORMANCE REPORT ---")
    print(classification_report(y_test, y_pred, target_names=["Normal", "Carrier"]))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print(f"AUC-ROC: {auc:.3f}")
    print(f"5-Fold CV AUC: {cv_auc.mean():.3f} +/- {cv_auc.std():.3f}")

# ---------------------------------------------------------------------
# STEP 5: Select and Save Best Model
# ---------------------------------------------------------------------

results_df = pd.DataFrame(results).sort_values(by="AUC-ROC", ascending=False)
best_model_name = results_df.iloc[0]["Model"]
best_model = models[best_model_name]
best_sensitivity = results_df.iloc[0]["Sensitivity/Recall"] * 100

print("\n--- MODEL COMPARISON ---")
print(results_df.to_string(index=False))

print(f"\nBest model by AUC-ROC: {best_model_name}")
print(f"Best model carrier sensitivity: {best_sensitivity:.2f}%")

if best_sensitivity >= 69.0:
    print("SUCCESS: Best model sensitivity beats the 69.0% benchmark.")
else:
    print("FAILED: Adjust synthetic boundaries to reduce false negatives.")

joblib.dump(best_model, "sicklescreen_best_model.pkl")
joblib.dump(best_model, "sicklescreen_model.pkl")

print("Step 5: Best model exported as 'sicklescreen_best_model.pkl'.")
print("Pipeline completed successfully.")

# ---------------------------------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------------------------------

rf_model = models["Random Forest"]
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_,
}).sort_values(by="Importance", ascending=False)

print("\n--- RANDOM FOREST FEATURE IMPORTANCE ---")
print(importance.to_string(index=False))
