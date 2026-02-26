📌 Objective of the Milestone

The objective of this milestone is to build an AI-powered fitness application that:

Collects user personal and fitness details

Calculates BMI and determines BMI category

Uses a Large Language Model (LLM) to generate a structured 5-day workout plan

Ensures the workout plan is safe, professional, and easy to follow

Deploys the application using Hugging Face Spaces

Demonstrates practical usage of prompt engineering and model inference

This milestone focuses on integrating AI model inference with Streamlit UI and deploying a real-world application.

🤖 Model Name Used

The following Hugging Face model is used:

google/flan-t5-base
Why this model?

Instruction-tuned model

Good for structured text generation

Lightweight enough for deployment

Works well for prompt-based task generation

🧠 Prompt Design Explanation

Prompt engineering plays a major role in controlling AI output.

The prompt was designed to:

Clearly divide the workout into Day 1 to Day 5

Include:

Exercise name

Sets

Reps

Rest period

Adjust intensity based on BMI category

Avoid unsafe exercises for beginners

Keep output professional and structured

Prevent extra explanations or unwanted text

Example Prompt Logic
You are a certified professional fitness trainer.

Create a STRICT 5-DAY workout plan.

Rules:
1. Divide clearly into Day 1 to Day 5.
2. Include exercise name.
3. Include sets and reps.
4. Include rest period.
5. Adjust intensity based on BMI category.
6. Avoid unsafe exercises for beginners.
7. Keep the plan professional and easy to follow.

This structured prompt ensures consistent AI output.

⚙️ Steps Performed
1️⃣ Model Loading

Loaded tokenizer and model using Hugging Face Transformers:

AutoTokenizer.from_pretrained()
AutoModelForSeq2SeqLM.from_pretrained()

Used Streamlit caching to avoid repeated loading.

2️⃣ Prompt Creation

User input collected:

Name

Gender

Height & Weight

Fitness Goal

Fitness Level

Available Equipment

BMI calculated and added to prompt context.

Prompt dynamically generated using user details.

3️⃣ Inference Testing

Tokenized prompt using:

tokenizer(prompt, return_tensors="pt")

Generated response using:

model.generate()

Decoded output to produce final workout plan.

4️⃣ Output Validation

Ensured:

5-day structure

Exercise details included

Professional formatting

🏋️ Sample Generated Output
Day 1: Upper Body Strength
1. Exercise: Push-Ups
   Sets: 3
   Reps: 12
   Rest: 60 sec

2. Exercise: Dumbbell Rows
   Sets: 3
   Reps: 10
   Rest: 60 sec
...

Day 2: Lower Body
1. Exercise: Bodyweight Squats
   Sets: 3
   Reps: 15
   Rest: 45 sec
...
🚀 Hugging Face Space Deployment

🔗 Live Application Link:

https://huggingface.co/spaces/YOUR-USERNAME/YOUR-SPACE-NAME

(Replace with your actual deployment link)

🧰 Technologies Used

Python

Streamlit

Hugging Face Transformers

PyTorch

Hugging Face Spaces

GitHub
## 👤 Author

**REDDYPPOGU HARRY JOEN**  
B.E. Electrical and Electronics Engineering  
AI & Automation Enthusiast
