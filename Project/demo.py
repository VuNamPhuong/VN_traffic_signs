import streamlit as st
import numpy as np
import os
import cv2 as cv
import pandas as pd
import time
from take_traffic_sign import crop_image
from ultralytics import YOLO, RTDETR
from PIL import Image

yolov11 = YOLO('Project/yolov11l_best.pt') # 'model_yolov11.pt'
detr = RTDETR('Project/detr-l_best.pt') #'model_detr.pt'
yolov8 = YOLO('Project/yolov8l_best.pt') #'model_yolov8.pt'

st.header("Phân loại biển báo giao thông")
st.markdown("---")
model_option=["Comparision", 'YOLOv11', 'RT-DETR', 'YOLOv8']
model_chosen = st.sidebar.selectbox("Model: ", model_option)

label=["cấm", "nguy hiểm","chỉ dẫn","phụ","hiệu lệnh"]
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png', 'gif','webp'])

def predict(img):
    st.write("Model used: ", model_chosen)

    if model_chosen =="YOLOv11":
        pred = yolov11.predict(img, show_labels=True, save=True, imgsz=320, conf=0.5)
        for r in pred:
            r.show()
            for box in r.boxes:
                label_name = label[int(box.cls)]
                conf_score = float(box.conf)
                st.write("Biển báo ", label_name, " với độ chính xác: ", conf_score)

    elif model_chosen =="RT-DETR":
        pred = detr.predict(img, show_labels=True, save=True, imgsz=320, conf=0.5)
        for r in pred:
            r.show()
            for box in r.boxes:
                label_name = label[int(box.cls)]
                conf_score = float(box.conf)
                st.write("Biển báo ", label_name, " với độ chính xác: ", conf_score)

    elif model_chosen == "YOLOv8":
        pred = yolov8.predict(img, show_labels=True, save=True, imgsz=320, conf=0.3)
        for r in pred:
            r.show()
            for box in r.boxes:
                label_name = label[int(box.cls)]
                conf_score = float(box.conf)
                st.write("Biển báo ", label_name, " với độ chính xác: ", conf_score)

    elif model_chosen == "Comparision":
        st_time = time.time()
        pred_yv11 = yolov11.predict(img, save=True, conf=0.6)
        for r in pred_yv11:
            r.show()
        end_time = time.time()
        rt_yolov11 = end_time - st_time

        st_time = time.time()
        pred_detr = detr.predict(img, save=True, conf=0.6)
        for r in pred_detr:
            r.show()
        end_time = time.time()
        rt_detr = end_time-st_time

        st_time = time.time()
        pred_yv8 = yolov8.predict(img, save=True, conf=0.6)
        for r in pred_yv8:
            r.show()
        end_time = time.time()
        rt_yolov8 = end_time-st_time

        dictionary = {}
        dictionary["RUNTIME (s)"] = [str(rt_yolov11),str(rt_detr),str(rt_yolov8)]
        print(dictionary)

        df = pd.DataFrame(dictionary)
        new_index = ['YOLOv11', 'RT-DETR', 'YOLOv8']
        df.index = new_index
        st.table(df)

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img)
    submit=st.button(label="Classify")

    if submit: 
        predict(img)