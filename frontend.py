import streamlit as st

# ------------------------------
# Title & Description
# ------------------------------
st.set_page_config(page_title="AI Prescription Verification", layout="centered")
st.title("💊 AI Medical Prescription Verification")
st.write("Verify prescriptions using AI-powered analysis (IBM Watson + Hugging Face).")

# ------------------------------
# Patient Details
# ------------------------------
st.header("👤 Patient Details")
age = st.number_input("Enter Patient Age", min_value=0, max_value=120, step=1)
gender = st.radio("Select Gender", ["Male", "Female", "Other"])

# ------------------------------
# Drug Details
# ------------------------------
st.header("💊 Drug Details")
drug_name = st.text_input("Enter Drug Name")
dosage = st.text_input("Enter Dosage (e.g., 500mg, 1-0-1)")
frequency = st.selectbox("Frequency", ["Once a day", "Twice a day", "Thrice a day", "As prescribed"])

# ------------------------------
# Submit Button
# ------------------------------
if st.button("✅ Verify Prescription"):
    if drug_name and age > 0:
        st.success("Prescription submitted successfully!")
        st.info(f"""
        **Entered Details:**
        - Patient Age: {age}  
        - Gender: {gender}  
        - Drug: {drug_name}  
        - Dosage: {dosage if dosage else "Not provided"}  
        - Frequency: {frequency}  
        """)
        st.warning("⚠️ Backend integration pending: Drug interaction, dosage validation, and alternatives.")
    else:
        st.error("⚠️ Please fill all fields before submitting.")

