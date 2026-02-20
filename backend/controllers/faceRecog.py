from deepface import DeepFace
import numpy as np
import os
import cv2
from utils.enhance_image import enhance_image

DB_PATH = "./my_db" 
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

async def face_verification(file):
    print(f"Received file: {file.filename}")
    temp_path = "temp_frame.jpg"

    content = await file.read()
    with open(temp_path, "wb") as f:
        f.write(content)

    frame = cv2.imread(temp_path)
    if frame is None:
        return {"success": False, "error": "Could not read uploaded image"}

    enhanced_frame = enhance_image(frame)

    try:
        results = DeepFace.find(
            img_path=enhanced_frame,
            db_path=DB_PATH, 
            enforce_detection=True,
            model_name="VGG-Face"
        )

        if len(results) > 0 and not results[0].empty:
            match_path = results[0].iloc[0]['identity']
            name = os.path.basename(match_path).split('.')[0]
            print(f"Match found: {name}")
            return {"success": True, "faces": [{"name": name}]}

        print("no match found")
        return {"success": False, "faces": []}

    except Exception as e:
        print(f"DeepFace Error: {e}")
        return {"success": False, "error": str(e)}
