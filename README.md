# Next-Word-Prediction
# 🔮 Next Word Prediction using Bidirectional LSTM

## 📌 Overview
This project is a Deep Learning based **Next Word Prediction System** developed using a **Bidirectional LSTM** model in Natural Language Processing (NLP).  
The model predicts the most probable next word based on previously entered words, similar to autocomplete systems used in chatbots, virtual assistants, and search engines.

The project also includes a deployed interactive web application using Streamlit.

---

# 🚀 Features
✔ Next Word Prediction using Deep Learning  
✔ Bidirectional LSTM Architecture  
✔ Context-Aware Text Generation  
✔ Streamlit Web Application  
✔ Multi-word Sentence Generation  
✔ NLP-based Sequential Learning  

---

# 🧠 Problem Statement
Modern applications such as chatbots, virtual assistants, and autocomplete systems require intelligent language models to generate meaningful and context-aware text predictions. Traditional systems fail to understand sequential word relationships effectively, leading to inaccurate suggestions and reduced user experience.

This project addresses the problem by building a Bidirectional LSTM-based Next Word Prediction system capable of learning contextual relationships from textual data.

---

# 🎯 Objectives
- Build a Next Word Prediction model using Bidirectional LSTM
- Learn contextual and sequential relationships between words
- Generate meaningful and accurate next-word suggestions
- Develop an interactive NLP application using Streamlit

---

# 📂 Dataset
- **Dataset Source:** Project Gutenberg Text Dataset
- **Dataset Type:** Text Dataset (`.txt`)
- **Domain:** Natural Language Text Data

### Dataset Statistics
- Total Words:27587
- Vocabulary Size:4201
- Total Input Sequences:26043

---

# ⚙️ Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- Natural Language Processing (NLP)

---

# 🔄 Project Workflow

```text
Text Dataset
     ↓
Tokenization
     ↓
N-Gram Sequence Generation
     ↓
Padding
     ↓
Bidirectional LSTM Model
     ↓
Next Word Prediction
     ↓
Streamlit Deployment


# 📁 Project Structure

next-word-prediction/
│
├── app.py                     # Streamlit web application
├── Nextwordprediction.ipynb   # Model training notebook
├── nextwordmodel.keras        # Trained deep learning model
├── tokenizer.pkl              # Saved tokenizer object
├── max_len.pkl                # Maximum sequence length
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Ignored files and folders
│
└── outputs/
    └── screenshots/           # Application output screenshots

---------

# ⚙️ Setup

Install all required dependencies:

pip install -r requirements.txt


## ▶️ Run the Application

Start the Streamlit application:

streamlit run app.py


---

# 📸 Screenshots

## 🔹 Streamlit App
![App Screenshot](screenshots/"C:\Users\ssvmj\OneDrive\Innomatics\Data Science\Module 8 NLP\Assignments\Nextword_prediction\outputs\prediction1.png")

---

## 🔹 Prediction Output
![Prediction Screenshot](screenshots/"C:\Users\ssvmj\OneDrive\Innomatics\Data Science\Module 8 NLP\Assignments\Nextword_prediction\outputs\prediction2.png")

---

---

# ☁️ Deployment

The Next Word Prediction application was deployed using Streamlit and AWS EC2 for cloud-based access.