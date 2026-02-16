import streamlit as st
from transformers import pipeline
st.set_page_config(page_title="Fitness Profile", page_icon="🏋️", layout="centered")
def load_model():
    return pipeline(
        "text-generation",
        model="google/flan-t5-base"
    )
 
generator = load_model()
st.title("🏋️ Personalized Fitness Profile")

st.markdown("---")

# =========================
# 1️⃣ Personal Information
# =========================
st.header("1. Personal Information")

name = st.text_input("Name *")

height_cm = st.number_input("Height (in centimeters) *", min_value=0.0, format="%.2f")
weight_kg = st.number_input("Weight (in kilograms) *", min_value=0.0, format="%.2f")

# =========================
# 2️⃣ Fitness Details
# =========================
st.header("2. Fitness Details")

fitness_goal = st.selectbox(
    "Fitness Goal",
    ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

equipment = st.multiselect(
    "Available Equipment (Multiple selection allowed)",
    ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment"]
)

fitness_level = st.radio(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

st.markdown("---")

# =========================
if st.button("Submit Profile"):
 
    if not name:
        st.error("Please enter your name.")
 
    elif not equipment:
        st.error("Please select at least one equipment option.")
 
    elif bmi is None:
        st.error("Please enter valid height and weight.")
 
    else:
        st.success("✅ Profile Submitted Successfully!")
 
        bmi_status = bmi_category(bmi)
        equipment_list = ", ".join(equipment)
 
        prompt = f"""
        Generate a 5-day structured workout plan.
 
        User Details:
        Name: {name}
        Gender: {gender}
        BMI: {bmi:.2f} ({bmi_status})
        Goal: {goal}
        Fitness Level: {fitness_level}
        Available Equipment: {equipment_list}
 
        Requirements:
        - Include warmup
        - Include exercises with sets and reps
        - Include rest time
        - Adjust intensity based on BMI and fitness level
        - Keep it structured day-wise
        """
 
        with st.spinner("Generating your AI workout plan..."):
            result = generator(prompt, max_new_tokens=400)[0]["generated_text"]
 
        st.subheader("🏋️ Your Personalized Workout Plan")
        st.write(result)
