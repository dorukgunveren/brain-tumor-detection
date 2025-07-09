import cv2 as cv
from ultralytics import YOLO


img_p = r"path"
model_p = r"path"

img = cv.imread(img_p)
model = YOLO(model_p)

results = model(img)[0]

threshold = 0.5

for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result

    x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)
 
    class_name = results.names[class_id]

    text = f"{class_name}:%{int(score * 100)}"


    if score > threshold:
        cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
        cv.putText(img, text, (x1, y1-10), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


cv.imshow("New Window", img)
cv.waitKey(0)