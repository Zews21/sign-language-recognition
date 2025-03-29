import cv2
import os
import time
import uuid

IMAGES_PATH = os.path.join('collectedimages')
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    dir_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(dir_path, exist_ok=True)

for label in labels:
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)  # Warm-up time

    try:
        for imgnum in range(number_imgs):
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture image")
                break

            img_name = f"{label}.{uuid.uuid1()}.jpg"
            img_path = os.path.join(IMAGES_PATH, label, img_name)

            cv2.imwrite(img_path, frame)
            cv2.imshow('frame', frame)
            print(f"Images taken: {imgnum}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(2)

    finally:
        cap.release()
        cv2.destroyAllWindows()