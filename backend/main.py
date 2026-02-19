from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from controllers.faceRecog import face_verification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/verify")
async def verify_face(file: UploadFile = File(...)):
    result = await face_verification(file)
    return result
