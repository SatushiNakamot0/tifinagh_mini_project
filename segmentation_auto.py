import cv2
import os
import numpy as np

# --- CONFIGURATION ---
SOURCE_DIR = "scans"    # l folder fin 7atit les images dyali 1.jpeg, 2.jpeg...
OUTPUT_DIR = "dataset"  # l folder li ghadi itrangaw fih l7orouf li tqat3o
TARGET_SIZE = 32        # la taille finale dial kol 7arf (32x32 pixels)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# lista mn 1 l 33
for i in range(1, 34):
    # nchof wash l image kayna (ila kanet chi wa7da naqsa)
    image_path = os.path.join(SOURCE_DIR, f"{i}.jpeg")
    if not os.path.exists(image_path):
        # njarbo b .jpg ila makantch b .jpeg
        image_path = os.path.join(SOURCE_DIR, f"{i}.jpg")
        if not os.path.exists(image_path):
            print(f"Image mal9itnach : lettre {i}, ghadi nfotouha.")
            continue

    print(f"Traitement de la lettre {i}...")
    
    # n3mal folder l had l classe (matalan: dataset/1)
    class_dir = os.path.join(OUTPUT_DIR, str(i))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    # --- TRAITEMENT DYAL L IMAGE ---
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Binarisation (ka7al 3la byad -> byad 3la ka7al)
    # THRESH_BINARY_INV : kay7awel l byad (warqa) l ka7al (0)
    # w l ka7al (stylo) l byad (255)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # nlqa les contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    compteur_lettre = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # filtre dial la taille (bach net7aydo les points sghar wla le bruit)
        if w > 20 and h > 20: 
            # marge dial la sécurité 7da l7arf
            m = 5
            y1 = max(0, y - m)
            y2 = min(thresh.shape[0], y + h + m)
            x1 = max(0, x - m)
            x2 = min(thresh.shape[1], x + w + m)
            
            # (l image invertie) 
            roi = thresh[y1:y2, x1:x2]
            
            # --- PREPROCESSING: RESIZE W CENTERING ---
            # n7asbo la taille dial l7arf
            h_roi, w_roi = roi.shape
            
            # n7asbo l aspect ratio bach ma ndeformioch l7arf
            if h_roi > w_roi:
                # l7arf tawil (vertical)
                new_h = TARGET_SIZE - 4  # nkhalliw chwiya d marge
                new_w = int(w_roi * (new_h / h_roi))
            else:
                # l7arf 3arid (horizontal)
                new_w = TARGET_SIZE - 4
                new_h = int(h_roi * (new_w / w_roi))
            
            # resize l7arf
            resized = cv2.resize(roi, (new_w, new_h), interpolation=cv2.INTER_AREA)
            
            # n3mlo image jdida b fond ka7al (32x32)
            centered = np.zeros((TARGET_SIZE, TARGET_SIZE), dtype=np.uint8)
            
            # n7asbo fين nحطو l7arf bach ikoun f west
            y_offset = (TARGET_SIZE - new_h) // 2
            x_offset = (TARGET_SIZE - new_w) // 2
            
            # نحطو l7arf f west dial l image
            centered[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
            
            # sauvegarde (daba kol image 32x32 w l7arf f west)
            save_path = os.path.join(class_dir, f"{compteur_lettre}.png")
            cv2.imwrite(save_path, centered)
            compteur_lettre += 1
            
    print(f"   -> {compteur_lettre} exemples tkharja (32x32, centered, fond ka7al).")

print("Extraction salat ! chof l folder 'dataset'.")