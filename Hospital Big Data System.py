import pandas as pd
import numpy as np
import time
import json
import random

print("\n=== HOSPITAL BIG DATA SYSTEM: 5V's ANALYSIS ===\n")

# --- 1. VARIETY: Displaying different data formats ---
print("--- 1. Variety: Handling Diverse Data Formats ---\n")

# Structured (Excel/Database Style)
structured_excel = pd.DataFrame({
    'patient_id': [1001, 1002],
    'age': [45, 30],
    'blood_type': ['A+', 'O-']
})

print("[STRUCTURED - Excel Style]:")
print(structured_excel, "\n")

# Semi-Structured (JSON/Log Style)
semi_structured_log = {
    "timestamp": "2026-02-03T21:45:00Z",
    "event": "Lab_Result_Upload",
    "status": 200
}

print("[SEMI-STRUCTURED - JSON Log]:")
print(json.dumps(semi_structured_log, indent=2), "\n")

# Unstructured (Media/Files Style)
unstructured_data = "FILES: chest_xray_1001.jpg (Image), cardiac_ultrasound.mp4 (Video)"

print("[UNSTRUCTURED - Image/Video]:")
print(unstructured_data, "\n")


# --- 2. VOLUME: Aggregating all Hospital/Clinic data ---
print("--- 2. Volume: Global Hospital Network ---")

total_records = 1_000_000
print(f"Total Database Volume: {total_records} records collected from all clinics.\n")


# --- 3. VELOCITY: High-speed test record generation ---
print("--- 3. Velocity: Real-time Patient Test Stream ---")

for i in range(3):
    print(f"Incoming Test Record {i+1}: Generated at high speed...")
    time.sleep(0.3)

print("Stream Processing Complete.\n")


# --- 4. VERACITY: Accuracy and Trustworthiness ---
print("--- 4. Veracity: Data Validation ---")

raw_data_count = 3
trusted_data_count = 2

print(
    f"Accuracy Check: Filtered {raw_data_count - trusted_data_count} "
    f"untrustworthy record(s).\n"
)


# --- 5. VALUE: Detection and Treatment ---
print("--- 5. Value: Business/Medical Insight ---")

print(
    "Actionable Result: Early disease detection achieved. "
    "Treatment cost reduced by 15%."
)
