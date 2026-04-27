# 🎬 IMDB Sentiment Analysis App

## 📌 Project Overview

This project is a Natural Language Processing (NLP) based web application that analyzes movie reviews and predicts whether the sentiment is **Positive 😊** or **Negative 😡**.

The application uses a fine-tuned **BERT (Bidirectional Encoder Representations from Transformers)** model and is deployed using **Streamlit** for real-time predictions.

---

## 🚀 Live Demo

🚀 **Access the deployed application:**
👉 https://sentiment-analysis-app-jl7kgk48mpzdam3rfhaoay.streamlit.app/

---

## 🚀 Features

* 🎯 Classifies movie reviews into Positive or Negative sentiment
* ⚡ Real-time prediction using deep learning model
* 🧠 Uses BERT transformer model for high accuracy
* 📊 Displays prediction with confidence score
* 🎨 Clean and interactive UI using Streamlit
* ☁️ Deployed on cloud

---

## 🧠 Machine Learning Model

### Model Type:

Deep Learning (NLP)

### Architecture:

**BERT (bert-base-uncased)**

### Frameworks Used:

* Hugging Face Transformers
* PyTorch

### Model Details:

* Tokenization using `BertTokenizer`
* Max sequence length: 128
* Padding and truncation applied
* Custom PyTorch Dataset (`IMDbDataset`) used
* Fine-tuned on IMDB dataset

---

## 📊 Model Performance

The model was evaluated using standard classification metrics:

| Class        | Precision | Recall | F1-Score | Support |
| ------------ | --------- | ------ | -------- | ------- |
| Negative (0) | 0.85      | 0.85   | 0.85     | 189     |
| Positive (1) | 0.86      | 0.87   | 0.87     | 211     |

### Overall Performance:

* **Accuracy:** 86%
* **Macro Average F1-Score:** 0.86
* **Weighted Average F1-Score:** 0.86

The model demonstrates balanced performance across both classes with minimal bias and maintains a good balance between precision and recall.

---

## 📥 Input

* Movie review text

## 📤 Output

* Sentiment:

  * Positive 😊
  * Negative 😡
* Confidence Score (%)

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* Hugging Face Transformers
* PyTorch
* Scikit-learn

---

## 📂 Project Structure

```
sentiment-analysis-app/
│── app.py
│── requirements.txt
│── sentiment_model/
```

---

## ⚙️ Installation & Run Locally

```bash
git clone https://github.com/textgithum/sentiment-analysis-app.git
cd sentiment-analysis-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud**.

Due to large model size, the trained model is hosted on **Hugging Face Hub**, which allows efficient loading during runtime without exceeding GitHub file size limits.

---

## 🎯 Use Cases

* 🎬 Movie review analysis
* 📊 Social media sentiment analysis
* 🛒 Product review classification
* 🎓 NLP learning project

---

## 📸 Screenshots

<img width="949" height="866" alt="image" src="https://github.com/user-attachments/assets/302d3bce-63b1-4679-9bb7-985c836297d6" />


---

## 👩‍💻 Author

**Nikki Ram**
B.E. Artificial Intelligence & Machine Learning
Savitribai Phule Pune University

---

## ⭐ Future Improvements

* Add multi-class sentiment (Neutral, Mixed)
* Improve accuracy with larger dataset
* Add visualization dashboard
* Deploy using Docker

---

