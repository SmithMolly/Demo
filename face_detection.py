import cv2

def detect():
# 将识别的算法库函数换掉
#filename =  'C:/Users/zhao1/Desktop/show/test/example/1.jpg'
    casvade_face='F:/python/test/cascades/haarcascade_frontalface_default.xml'
    # casvade_eye='C:/Users/zhao1/Desktop/show/test/cascades/haarcascade_eye.xml'
    eye_glasses='F:/python/test/cascades/haarcascade_eye_tree_eyeglasses.xml'

    face_cascade=cv2.CascadeClassifier(casvade_face)
    # eye_cascade=cv2.CascadeClassifier(casvade_eye)
    eye_glass_cascade=cv2.CascadeClassifier(eye_glasses)
    camera= cv2.VideoCapture(0)

    while(True):
        # 文件来自摄像头读取内容
        ret, frame=camera.read()#获摄像头得每一帧
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#把每一帧进行灰度处理
        faces = face_cascade.detectMultiScale(gray, 1.3, 5,0)#把灰度图片传给haar进行灰度处理，返回值是人脸左上角坐标，宽度和高度


        for (x,y,w,h) in faces:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

            roi_gray=gray[y:y+h,x:x+w]
            roi_color = img[y:y + h, x:x + w]
            glass = eye_glass_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (20, 20))
            for (gx, gy, gw, gh) in glass:
                cv2.rectangle(roi_color, (gx, gy), (gx + gw, gy + gh), (0, 255, 0), 2)
            # eyes=eye_cascade.detectMultiScale(roi_gray, 1.03, 5,0,(40,40))
            # for (ex,ey,ew,eh) in eyes:
            #     cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()
if __name__ =="__main__":
    detect()