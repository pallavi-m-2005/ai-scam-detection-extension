import joblib

model = joblib.load("model.pkl")

def predict(features):

    result = model.predict([features])

    return result[0]
