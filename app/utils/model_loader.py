import joblib
import os

def load_model_and_vectorizer():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    model_dir = os.path.join(base_dir, "doubt_classifier")

    print("DEBUG: __file__ =", __file__)
    print("DEBUG: base_dir =", base_dir)
    print("DEBUG: model_dir =", model_dir)

    model_path = os.path.join(model_dir, "doubt_classifier_model.pkl")
    vectorizer_path = os.path.join(model_dir, "vectorizer.pkl")
    label_encoder_path = os.path.join(model_dir, "label_encoder.pkl")

    print("Loading model from:", model_path)
    print("Loading vectorizer from:", vectorizer_path)
    print("Loading label encoder from:", label_encoder_path)

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    label_encoder = joblib.load(label_encoder_path)

    return model, vectorizer, label_encoder
