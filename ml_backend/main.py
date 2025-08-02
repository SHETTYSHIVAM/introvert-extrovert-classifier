from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from schemas.personality import ModelOutput, ModelInput
from ml_models.predict import predict_personality, MODEL_VERSION, model
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") # for humans
async def root():
    return {"detail": "A Personality Introvert-Extrovert Prediction Model"}


@app.post("/predict", response_model=ModelOutput)
async def predict(data: ModelInput):
    output =  predict_personality(data)
    if "personality" in output:
        return JSONResponse(output, status_code=200)
    else:
        raise HTTPException(status_code=500, detail="Prediction failed")

@app.get("/health")  # for machines (AWS/Kubernetes) (required)
async def health():
    return {
        "status": "ok",
        "version": MODEL_VERSION,
        "model_is_loaded": model is not None,
    }
