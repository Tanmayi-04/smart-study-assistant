import streamlit as st
import joblib
import json

# Load study resources
with open("../assets/resources.json", "r") as f:
    resources = json.load(f)

# Load model and vectorizer
model = joblib.load("../doubt_classifier/doubt_classifier_model.pkl")
vectorizer = joblib.load("../doubt_classifier/vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Smart Study Assistant", layout="centered")
st.title("🧠 Doubt Classifier")
st.write("Enter your academic doubt below and get an instant category.")

# Input box
user_input = st.text_area("Your Doubt", "")

if st.button("Classify & Recommend"):
    if user_input.strip() == "":
        st.warning("Please enter a doubt.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]

        st.success(f"📌 Predicted Category: **{prediction}**")

        # Show relevant study resources
        st.markdown("### 📖 Recommended Resources:")
        for link in resources.get(prediction, []):
            if link.endswith(".pdf"):
                st.markdown(f"- 📄 [Download PDF]({link})")
            else:
                st.markdown(f"- 🔗 [Open Resource]({link})")
st.markdown("---")
st.header("🕒 Focus-Based Study Planner")

# Input: mood, focus, sleep
mood = st.selectbox("How do you feel right now?", ["Energetic", "Okay", "Tired"])
focus = st.slider("How focused are you? (1 = Distracted, 5 = Fully Focused)", 1, 5, 3)
sleep = st.slider("How many hours did you sleep last night?", 3, 10, 7)

if st.button("Suggest Study Time"):
    if mood == "Tired" or sleep < 5 or focus < 3:
        st.info("🧘 You seem low on energy. Try a short 25-minute study session with a 5-minute break.")
    elif focus == 5 and mood == "Energetic":
        st.success("🚀 You're in peak focus mode! Go for a 90-minute deep work session.")
    else:
        st.success("📘 Try a 45-minute focused study session followed by a 10-minute break.")

