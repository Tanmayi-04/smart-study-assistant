import streamlit as st
import joblib
import json
from utils.model_loader import load_model_and_vectorizer
import os

def show_dashboard():
    st.success(f"✅ Logged in as: {st.session_state['user']} ({st.session_state['branch']})")

    st.title("🧠 Doubt Classifier")
    st.write("Enter your academic doubt below:")

    # Load model and vectorizer
    model, vectorizer, label_encoder = load_model_and_vectorizer()

    # Load resources.json with absolute path
    assets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "resources.json"))
    with open(assets_path, "r") as f:
        resources = json.load(f)

    user_input = st.text_area("Your Doubt", "")
    if st.button("Classify & Recommend"):
        if user_input.strip() == "":
            st.warning("Please enter a doubt.")
        else:
            input_vec = vectorizer.transform([user_input])
            prediction = model.predict(input_vec)[0]
            st.success(f"📌 Predicted Category: **{prediction}**")

            st.markdown("### 📖 Recommended Resources:")
            for link in resources.get(prediction, []):
                if link.endswith(".pdf"):
                    st.markdown(f"- 📄 [Download PDF]({link})")
                else:
                    st.markdown(f"- 🔗 [Open Resource]({link})")

    st.divider()
    st.header("🕒 Focus-Based Study Planner")

    mood = st.selectbox("Mood", ["Energetic", "Okay", "Tired"])
    focus = st.slider("Focus Level (1-5)", 1, 5, 3)
    sleep = st.slider("Sleep (hrs)", 3, 10, 7)

    if st.button("Suggest Study Time"):
        if mood == "Tired" or sleep < 5 or focus < 3:
            st.info("🧘 Short 25-min session with 5-min break.")
        elif focus == 5 and mood == "Energetic":
            st.success("🚀 90-minute deep work session!")
        else:
            st.success("📘 45-min focused session + 10-min break.")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.rerun()
