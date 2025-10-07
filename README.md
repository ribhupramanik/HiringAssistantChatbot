# 💼 TalentScout Hiring Assistant Chatbot

## 🚀 Project Overview

**TalentScout Hiring Assistant** is an interactive AI-powered chatbot built using **Streamlit** and **OpenAI GPT models** to automate the **initial stages of technical recruitment**.  
The chatbot conducts structured conversations with candidates — collecting personal details, understanding their technical stack, and generating tailored interview questions dynamically.  

The primary goal is to **streamline candidate screening**, reduce manual workload for recruiters, and provide an engaging first-round experience.

---

## ⚙️ Installation Instructions

Follow these steps to set up and run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Hiring-Assistant-Chatbot.git
cd Hiring-Assistant-Chatbot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
✅ Make sure your `.env` file is listed in `.gitignore` to prevent accidental uploads to GitHub.

### 6️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 💡 Usage Guide

1. Launch the Streamlit app.  
2. The assistant greets you and starts the interview process.  
3. Provide your **name**, **email**, and **technical stack**.  
4. The chatbot generates **customized technical interview questions** based on your input.  
5. Once the session concludes, the assistant thanks you for your time.

> 🧠 Example prompt flow:
> ```
> 👋 Hi! I'm TalentScout, your hiring assistant.
> Please share your name, email, and tech stack.
> ```
> → *User responds:* “I’m John, email is john@example.com, and I work with Python, Django, and React.”
>
> → *Chatbot responds with relevant technical questions.*

---

## 🧩 Technical Details

| Component | Description |
|------------|-------------|
| **Frontend Framework** | [Streamlit](https://streamlit.io/) for creating the interactive web interface |
| **Language** | Python 3.10+ |
| **AI Model** | `gpt-3.5-turbo` (OpenAI API) |
| **Environment Management** | `python-dotenv` for secure API key handling |
| **Core Libraries** | `openai`, `streamlit`, `pandas`, `dotenv` |
| **Project Structure** |  
```
├── app.py                 # Streamlit application (main interface)
├── utils.py               # Chat model handler (OpenAI API interaction)
├── prompts.py             # Prompt templates for system and model messages
├── requirements.txt       # Dependencies
├── .env                   # API key (ignored in Git)
└── README.md
```

### ⚙️ Architectural Decisions

- **Session State:** Used `st.session_state` to maintain message history and flow between user and assistant.  
- **Hidden System Prompts:** System-level instructions are never displayed to the user; they only guide model behavior internally.  
- **Step-Based Conversation Flow:**  
  - Step 1: Greeting  
  - Step 2: Candidate Information Collection  
  - Step 3: Technical Question Generation  
  - Step 4: Completion  

This ensures logical progression and avoids prompt leakage.

---

## ✍️ Prompt Design

The chatbot uses three structured system prompts to guide conversation:

1. **`greeting_prompt()`**  
   Introduces the assistant’s role and ensures a professional, friendly tone.

2. **`info_collection_prompt()`**  
   Guides the model to request candidate details like name, email, and technical stack.

3. **`tech_question_prompt(tech_stack)`**  
   Instructs the model to generate technical interview questions relevant to the provided stack.

> **Prompt Strategy:**  
> Each prompt is crafted to be **contextually aware** yet **modular**, allowing fine-tuned control over conversation flow while keeping system instructions hidden from the candidate.

---

## 🧠 Challenges & Solutions

| Challenge | Solution |
|------------|-----------|
| **1. System prompts appearing in chat** | Restructured chat flow and used hidden prompts only in backend (not appended to visible chat). |
| **2. Chat order mismatches in Streamlit** | Rendered entire chat history *before* new input handling to preserve order and prevent duplication. |
| **3. OpenAI API version compatibility issue (`ChatCompletion` deprecated)** | Updated to new `client.chat.completions.create()` syntax compatible with OpenAI ≥1.0.0. |
| **4. API key exposure risk** | Implemented `.env` with `python-dotenv` and added `.env` to `.gitignore`. |
| **5. Maintaining conversation flow** | Used `st.session_state` with custom `step` logic to control multi-stage dialogue progression. |

---

## 🌟 Future Improvements

- Add database integration for storing candidate responses.
- Include feedback/rating mechanism for generated questions.
- Enable recruiter dashboard for viewing candidate interactions.
- Integrate with applicant tracking systems (ATS).

---

## 👨‍💻 Author
**Ribhu Pramanik**  

