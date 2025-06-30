import streamlit as st
from transformers import pipeline

# Load the chatbot model once
@st.cache_resource

def load_model():
    return pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

chatbot = load_model()

# Streamlit app UI
st.set_page_config(page_title="HR Model Chatbot", page_icon="🤖")
st.title("🤖 HR Model Explainer Chatbot")

st.markdown("""
Welcome! Ask me anything about the employee absenteeism prediction model. 
This model uses features like **BMI**, **workload**, **reason for absence**, and more to predict absenteeism level (High/Low).
It was trained using **XGBoost**, and explained with **SHAP** for transparency.
""")

# Text input
user_question = st.text_input("Ask a question:", placeholder="e.g. What features are most important?")

# Add model context
context = """
The model predicts employee absenteeism (High or Low) using an XGBoost classifier. 
Top important features from SHAP analysis include:
- Reason for absence
- Transportation expense
- Daily workload
- BMI
- Age

It helps HR understand which factors contribute most to absenteeism.
"""

if user_question:
    full_prompt = f"You are an AI HR assistant. Explain the model based on this context:\n\n{context}\n\nQuestion: {user_question}\n\nAnswer:"
    with st.spinner("Thinking..."):
        response = chatbot(full_prompt, max_length=300, do_sample=True)[0]['generated_text']
        answer = response.split("Answer:")[-1].strip()
        st.success(answer)