import streamlit as st
import random

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Fitness Profile", page_icon="🏋️")

# =========================
# BMI Functions
# =========================
def calculate_bmi(height_cm, weight_kg):
    h = height_cm / 100
    return round(weight_kg / (h * h), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# =========================
# Exercise Database
# =========================
beginner_exercises = [
    "Push-Ups", "Bodyweight Squats", "Plank",
    "Lunges", "Glute Bridge", "Jump Rope",
    "Dumbbell Rows", "Shoulder Press",
    "Resistance Band Pull", "Mountain Climbers"
]

# =========================
# UI
# =========================
st.title("🏋️ Professional Fitness Planner")

name = st.text_input("Name")
height = st.number_input("Height (cm)", min_value=0.0)
weight = st.number_input("Weight (kg)", min_value=0.0)

fitness_level = st.radio(
    "Fitness Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Generate 5-Day Plan"):

    if not name or height <= 0 or weight <= 0:
        st.error("Please enter valid details")
    else:

        bmi = calculate_bmi(height, weight)
        category = bmi_category(bmi)

        st.success(f"{name} | BMI: {bmi} ({category})")

        # =========================
        # Intensity based on BMI
        # =========================
        if category == "Underweight":
            reps = "10-12"
            rest = "60 sec"
        elif category == "Normal":
            reps = "12-15"
            rest = "45 sec"
        else:
            reps = "8-10"
            rest = "75 sec"

        # =========================
        # Generate 5-Day Plan
        # =========================
        for day in range(1, 6):

            st.subheader(f"Day {day}")

            exercises = random.sample(beginner_exercises, 5)

            for i, ex in enumerate(exercises, 1):
                st.write(f"""
{i}. Exercise: {ex}
   Sets: 3
   Reps: {reps}
   Rest: {rest}
""")
