import streamlit as st
import numpy as np
import pickle
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model
model = load_model("nextwordmodel.keras")

# Load tokenizer
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

# Load max_len
max_len = pickle.load(open("max_len.pkl", "rb"))

# Title
st.title("Next Word Prediction App")

# Input text
input_text = st.text_input("Enter a sentence:")

# Prediction function
def predict_next_word(text):
    for i in range(10):
       token_text = tokenizer.texts_to_sequences([text])[0]
       padded_token_text = pad_sequences([token_text], maxlen=max_len-1, padding='pre')
       pos = np.argmax(model.predict(padded_token_text))
       
       for word,index in tokenizer.word_index.items():
          if index == pos:
             text = text + " " + word

    return text                    

# Button
if st.button("Predict"):
    if input_text:
        result = predict_next_word(input_text)
        st.write("Next word:", result)
    else:
        st.write("Please enter some text")