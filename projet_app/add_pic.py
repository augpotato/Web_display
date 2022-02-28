import cv2
import numpy as np
import streamlit as st

def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new

def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)


    #当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    #这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加

    yy1 = 0
    yy2 = png_img.shape[0]
    xx1 = 0
    xx2 = png_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > jpg_img.shape[1]:
        xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
        x2 = jpg_img.shape[1]
    if y2 > jpg_img.shape[0]:
        yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
        y2 = jpg_img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_jpg = 1 - alpha_png

    # 开始叠加
    for c in range(0, 3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg * jpg_img[y1:y2, x1:x2, c]) + (alpha_png * png_img[yy1:yy2, xx1:xx2, c]))
    return jpg_img


img_png=cv2.imread('1.png',cv2.IMREAD_UNCHANGED)
st.title('example')
uploaded_file = st.file_uploader("上传一张图片",type=["jpg", "png", "bmp", "jpeg"])

if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_jpg = cv2.imdecode(file_bytes, 1)
    img_jpg = cv2.resize(img_jpg,(300,300))
    # 设置叠加位置坐标
    x1 = 0
    y1 = 0
    x2 = x1 + img_png.shape[1]
    y2 = y1 + img_png.shape[0]

    # 开始叠加
    res_img = merge_img(img_jpg, img_png, y1, y2, x1, x2)


    # 展示图片
    st.image(res_img, channels="BGR")
    cv2.imwrite('test.jpg', res_img)











