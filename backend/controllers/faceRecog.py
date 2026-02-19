from deepface import DeepFace
import numpy as np
import os

DB_PATH = "./my_db" 
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

async def face_verification(file):
    
    print(f"Received file: {file.filename}")
    temp_path = "temp_frame.jpg"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    try:
        results = DeepFace.find(
            img_path=temp_path, 
            db_path=DB_PATH, 
            enforce_detection=False,
            model_name="VGG-Face"
        )

        if len(results) > 0 and not results[0].empty:
            print(f"Match found: {results[0].iloc[0]['identity']}")
            match_path = results[0].iloc[0]['identity']
            name = os.path.basename(match_path).split('.')[0]
            return {"success": True, "faces": [{"name": name}]}

        print("no match found")
        return {"success": False, "faces": []}

    except Exception as e:
        print(f"Error: {e}")
        return {"success": False, "faces": [], "error": str(e)}
