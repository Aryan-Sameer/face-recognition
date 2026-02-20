import cv2
import numpy as np

def enhance_image(frame):
    # 1. Apply Gamma Correction (Values > 1.0 brighten the image)
    # 1.5 to 2.5 is usually the sweet spot for very dark rooms
    gamma = 2.0
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    frame = cv2.LUT(frame, table)

    # 2. Convert to LAB color space
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # 3. Apply a more aggressive CLAHE
    # Increased clipLimit to 5.0 for deeper contrast
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
    l = clahe.apply(l)

    # 4. Normalize the L channel (ensures full range of brightness)
    l = cv2.normalize(l, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Merge channels back
    limg = cv2.merge((l, a, b))
    enhanced_frame = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    return enhanced_frame

