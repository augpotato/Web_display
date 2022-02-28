import cv2
import numpy as np
import streamlit as st
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image

model = models.load_model("cats_and_dogs_small_214.h5")
st.title('example')
uploaded_file = st.file_uploader("上传一张图片",type=["jpg", "png", "bmp", "jpeg"])
a=''
if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    # 展示图片
    st.image(opencv_image, channels="BGR")
    cv2.imwrite('test.jpg', opencv_image)

    img_dir='test.jpg'
    img = image.load_img(img_dir, target_size=(150,150))
    img_data = image.img_to_array(img)

    img_data = np.expand_dims(img_data, axis=0)
    img_data /= 255
    r = model.predict(img_data)
    if r <0.5:
        a="cat"
    else:
        a="dog"
    st.text(f"result is:{a}")








