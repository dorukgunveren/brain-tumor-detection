# brain-tumor-detection
Brain tumor detection usin yolov8n.pt trained on custom dataset with Roboflow and Google Colab. Detects Brain Tumor

This project utilizes the YOLOv8n detection model, trained on a custom brain MRI dataset, to detect and localize brain tumors in medical images. The model processes MRI scans to identify and locate brain tumors. It can make predictions on individual MRI images and provide bounding box coordinates along with confidence scores for detected tumors.


## brain-tumor-detection.py

This script uses a YOLOv8n model alongside OpenCV to perform single-image inference on brain MRI scans. It loads a brain MRI image, runs detection using a trained YOLOv8 model, and identifies the presence of brain tumors.

The script reads the image with OpenCV, processes it with the YOLOv8 model, extracts detection results, and returns the predicted tumor presence based on the model's output.

## Model and Training Results

The trained model and evaluation outputs  can be accessed from the following Google Drive link:

🔗 https://drive.google.com/drive/folders/1C8LwRcASgRTuIjwnmMlm83s3HxL1B75_?usp=sharing

## Dataset

The model was trained on a custom brain MRI dataset containing one class: Tumor.
You can access the dataset via Roboflow using the link below:

🔗 https://app.roboflow.com/doruk-gunveren/brain-tumor-detection-15wyz/1



## Dependencies

This project requires the following Python packages. It is recommended to install them in a virtual environment using the `requirements.txt` file included in the repository.
