from pandas import DataFrame
from joblib import load
from starlette.responses import JSONResponse

from schemas.personality import Personality

model = load("ml_models/introvert-extrovert-rfc.joblib")
MODEL_VERSION = '1.0.0'
class_labels = model.classes_.tolist()


def bool_to_str(val: bool) -> str:
    return "Yes" if val else "No"


def predict_personality(data):
    try:
        input_dict = data.model_dump()

        # Convert booleans to integers (0/1)
        for key, value in input_dict.items():
            if isinstance(value, bool):
                input_dict[key] = bool_to_str(input_dict[key])

        input_df = DataFrame([input_dict])

        res = model.predict(input_df)
        probabilities = model.predict_proba(input_df)[0]
        confidence = max(probabilities)
        class_probs = {label: round(prob * 100, 2) for label, prob in zip(class_labels, probabilities)}
        personality = Personality.EXTROVERT if res[0] == 0 else Personality.INTROVERT


        return {
            "personality": personality,
            "confidence": confidence,
            "class_probs": class_probs
        }
    except Exception as e:
        print(e)
        return {"error": str(e), "status_code": 500}