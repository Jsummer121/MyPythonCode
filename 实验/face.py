import cv2

#加载图片
#img = cv2.imread('1.jpg')

#加载人脸模型
face = cv2.CascadeClassifier('E:\python-summer-1\haarcascade_frontalface_alt2.xml')

#打开摄像头capture
capture = cv2.VideoCapture(0)

#获取摄像头的实时画面
while True:
    #拿到每一帧画面
    ret,image = capture.read()

    #图像灰度处理
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#检测人脸
faces = face.detectMultiScale(gray)

#标记人脸
for (x,y,w,h) in faces:
    #图片 坐标原点 矩形宽搞 线宽
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

#创建显示窗口
cv2.imshow('window',image)

#暂停窗口
cv2.waitKey(0)

#销毁窗口
cv2.destroyAllWindows()