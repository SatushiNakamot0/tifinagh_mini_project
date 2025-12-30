import cv2
import os
import glob

# --- CONFIGURATION ---
SOURCE_DIR = "scans"    # l folder fin 7atiti les images dyali 1.jpeg, 2.jpeg...
OUTPUT_DIR = "dataset"  # l folder li ghadi itrangaw fih l7orouf li tqat3o

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# lista mn 1 l 33
for i in range(1, 34):
    image_path = os.path.join(SOURCE_DIR, f"{i}.jpeg")
    
    # nchof wash l image kayna (ila kanet chi wa7da naqsa)
    if not os.path.exists(image_path):
        # njarbo b .jpg ila makantch b .jpeg
        image_path = os.path.join(SOURCE_DIR, f"{i}.jpg")
        if not os.path.exists(image_path):
            print(f"Image mal9itnach : {image_path}, ghadi nfotouha.")
            continue

    print(f"Traitement de {image_path} (Lettre n°{i})...")
    
    # n3mal folder l had l classe (matalan: dataset/1)
    class_dir = os.path.join(OUTPUT_DIR, str(i))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    # --- TRAITEMENT DYAL L IMAGE ---
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Binarisation (ka7al 3la byad -> byad 3la ka7al)
    # siyeb l threshold (thresh) wla khdam b OTSU
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # nlqa les contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    compteur_lettre = 0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # filtre dial la taille (bach net7aydo les points s3ar wla le bruit)
        if w > 20 and h > 20: 
            # marge dial la sécurité 7da l7arf
            m = 5
            y1 = max(0, y - m)
            y2 = min(img.shape[0], y + h + m)
            x1 = max(0, x - m)
            x2 = min(img.shape[1], x + w + m)
            
            roi = img[y1:y2, x1:x2] # t9ti3
            
            # sauvegarde
            save_path = os.path.join(class_dir, f"{compteur_lettre}.png")
            cv2.imwrite(save_path, roi)
            compteur_lettre += 1
            
    print(f"   -> {compteur_lettre} exemples tkharja.")

print("Extraction salat ! chof l folder 'dataset'.")