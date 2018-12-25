# import os
# import numpy
# from PIL import Image, ImageDraw
# 导入所需要的CV2模块
import cv2
# from keras.models import load_model
# 采用默认的人脸分类器haarcascade_frontalface_default.xml
# 检查带眼镜的眼睛haarcascade_eye_tree_eyeglasses.xml
filename =  'F:/python/test/example/1.jpg'
casvade_face_name='F:/python/test/cascades/haarcascade_frontalface_default.xml'
eye_glasses='F:/python/test/cascades/haarcascade_eye_tree_eyeglasses.xml'

#定义了detect函数
def detect(filename) :
    face_cascade=cv2.CascadeClassifier(casvade_face_name)#人脸检测
    eye_glass_cascade=cv2.CascadeClassifier(eye_glasses)#带眼镜的人眼检测
    # 通过CV2imread加载图片，并把它转换为灰度图片
    img=cv2.imread(filename)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.2,3)
    for (x,y,w,h) in faces:
        # cv2.rectangle用来允许通过坐标绘制矩形,x,y表示左上角的坐标，w和h表示人脸矩形的宽度和高度
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        #print(roi_gray)
        roi_color = img[y:y + h, x:x + w]
        glass=eye_glass_cascade.detectMultiScale(roi_gray,1.03,5,0,(40,40))
        for (gx, gy, gw, gh) in glass:
            cv2.rectangle(roi_color, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)
        # font = cv2.FONT_HERSHEY_SIMPLEX  # 使用默认字体
        # img = cv2.putText(faces, 'man', (roi_gray[0][0], roi_gray[0][1]), font, 1.2, (255, 255, 255), 2)  # 添加文字，1.2表示字体大小，（0,40）是初始的位置，
        #     # 保存
    cv2.namedWindow('find')
    cv2.imshow('face',img)
    cv2.imwrite('F:/python/test/人脸.jpg ',img)
    cv2.waitKey(0)
detect(filename)
