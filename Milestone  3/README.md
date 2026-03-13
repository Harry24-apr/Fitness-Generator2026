# AI Fitness Analyzer – Personalized Fitness Plan Generator

## Project Overview

AI Fitness Analyzer is a web-based application that provides users with a personalized fitness plan based on their profile information. The system collects user details such as age, weight, height, and fitness goals to generate customized workout recommendations.

To ensure secure access, the application implements a login system with OTP (One-Time Password) verification. This two-step authentication process allows only verified users to access the fitness dashboard and generate their personalized fitness plans.

This project is developed as part of the Infosys Internship Program and is deployed on Hugging Face Spaces.

---

## Features

User Registration (Signup)  
Users can create an account using their email ID and password.

Secure Login System  
Users log in using their registered credentials which are verified from the database.

OTP Verification  
After successful login, a 6-digit OTP is generated and sent to the user's registered email address.

Two-Step Authentication  
Users must enter the correct OTP before accessing the application dashboard.

Personalized Fitness Plan Generator  
After authentication, the system analyzes the user's fitness profile and generates customized workout and fitness recommendations.

Dashboard Access  
Only authenticated users with successful OTP verification can access the fitness analyzer dashboard.

---

## System Workflow

1. User signs up using email and password.
2. User information is stored securely in the database.
3. User logs in with registered credentials.
4. The system verifies email and password.
5. If login is successful:
   - A 6-digit OTP is generated.
   - OTP is sent to the user's email.
6. User enters the OTP in the verification page.
7. If OTP is valid, the user is redirected to the dashboard.
8. The user enters fitness details and receives a personalized fitness plan.

---

## Project Structure

AI_Fitness_Analyzer

app.py  
templates  
    signup.html  
    login.html  
    otp_verification.html  
    dashboard.html  

static  
    css  
    images  

database  
    users.db  

README.md

---

## Technologies Used

Python  
Flask  
SQLite Database  
HTML  
CSS  
SMTP Email Service  
Machine Learning / AI Fitness Analysis Logic  

---

## Security Features

Email-based user authentication  
OTP-based two-step verification  
Restricted dashboard access  
Secure credential validation

---

## Deployment

This application is deployed using Hugging Face Spaces.

Space Link:  
https://huggingface.co/spaces/Infosysprojectwork/AI_Fitness_Analyzer

---

## How to Run Locally

1. Clone the repository

git clone https://huggingface.co/spaces/Infosysprojectwork/AI_Fitness_Analyzer

2. Navigate to the project directory

cd AI_Fitness_Analyzer

3. Install required libraries

pip install flask

4. Run the application

python app.py

5. Open in browser

https://huggingface.co/spaces/Infosysprojectwork/AI_Fitness_Analyzer

---

## Future Improvements

Integration with wearable fitness devices  
Advanced AI-based fitness recommendations  
Nutrition and diet plan generator  
Workout progress tracking  
Mobile application support

---

## Author

Reddypogu Harry Joen  
B.E Electrical and Electronics Engineering  
RMK Engineering College  

Infosys Virtual Internship Project
