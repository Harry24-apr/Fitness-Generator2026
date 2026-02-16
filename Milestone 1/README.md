# 🏋️ Fitness Profile & BMI Calculator App

## 📌 Objective of the Milestone

The objective of this milestone is to design and develop a Streamlit-based Fitness Profile application that:

- Collects user personal information
- Calculates Body Mass Index (BMI)
- Categorizes BMI according to health standards
- Demonstrates input validation and logical processing
- Deploys the application using Streamlit / Hugging Face Spaces
- Publishes the project on GitHub with proper documentation

This milestone focuses on combining UI design, backend logic, validation, and deployment skills.

---

## 🧮 BMI Formula Explanation

BMI (Body Mass Index) is a measure used to determine whether a person has a healthy body weight for their height.

### Formula:

\[
BMI = \frac{Weight\ (kg)}{(Height\ (meters))^2}
\]

### Steps Used in Application:

1. Convert height from centimeters to meters:

   Height (m) = Height (cm) / 100

2. Apply BMI formula:

   BMI = Weight (kg) / (Height in meters)^2

3. Round BMI to two decimal places.

---

## 📊 BMI Categories

| BMI Range        | Category      |
|------------------|--------------|
| Less than 18.5   | Underweight  |
| 18.5 – 24.9      | Normal       |
| 25 – 29.9        | Overweight   |
| 30 and above     | Obese        |

---

## ⚙️ Steps Performed

### 1️⃣ Form Creation
- Created a Streamlit form to collect:
  - Name (Required)
  - Height (cm)
  - Weight (kg)
  - Fitness Goal
  - Available Equipment (Multiple selection)
  - Fitness Level

---

### 2️⃣ Input Validation
- Checked that Name is not empty.
- Ensured height and weight are positive values.
- Prevented zero or negative input.
- Displayed error messages when validation fails.

---

### 3️⃣ BMI Logic Implementation
- Converted height from cm to meters.
- Calculated BMI using formula.
- Rounded BMI to 2 decimal places.
- Classified BMI into health categories.
- Displayed user name along with BMI and category.

---

### 4️⃣ Deployment
- Developed application using Streamlit.
- Created requirements.txt file.
- Uploaded project to GitHub.
- Deployed application on Hugging Face Spaces.

---

## 🚀 Technologies Used

- Python
- Streamlit
- GitHub
- Hugging Face Spaces

---

## 👤 Author

REDDYPOGU HARRY JOEN 
B.E. Electrical and Electronics Engineering  

