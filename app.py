import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F

# Load model
model = BertForSequenceClassification.from_pretrained("sentiment_model")
tokenizer = BertTokenizer.from_pretrained("sentiment_model")

st.title("🎬 IMDB Sentiment Analysis App")

st.write("Enter a movie review and get sentiment prediction")

# Input
text = st.text_area("Enter your review:")

if st.button("Predict"):
    if text:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)

        pred = outputs.logits.argmax().item()

        # Confidence
        probs = F.softmax(outputs.logits, dim=1)
        confidence = probs.max().item()

        if pred == 1:
            st.success(f"Positive 😊 (Confidence: {round(confidence*100,2)}%)")
        else:
            st.error(f"Negative 😡 (Confidence: {round(confidence*100,2)}%)")
    else:
        st.warning("Please enter some text")