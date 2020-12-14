import face_recognition
import cv2

#环境安装
#先安装pip install dlib
#然后安装 pip install face_recognition
#不安装上面的没办法安装face_recognition
#感觉自己的识别效果不怎么样所以我也就当着一个娱乐效果

#获取一个网络摄像头(0)或者你有多个摄像头的话可以更改
video_capture = cv2.VideoCapture(1)

#谨记这个地方加载的图像必须有头像可以识别出来不然没有图像的话下面obama_face_encoding = face_recognition.face_encodings(obama_image)[0]会报列表下标溢出
#加载样本图片让机器学习识别。
obama_image = face_recognition.load_image_file("../图片/1.jpg")#可修改地址信息
#这里是加载显示的头像这里我只用一个头像显示所以写了0
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#加载第二个样本图让机器学习识别。
biden_image = face_recognition.load_image_file("../图片/3.jpg")#可修改地址信息
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

#创建已知脸部编码的数组及其名称
known_face_encodings = [
	obama_face_encoding,
	biden_face_encoding
]

known_face_names=[
	"*****",
	"123456"
]
#初始化数据变量
face_locations = []
face_encodings = []
face_names=[]
process_this_frame=True

while True:
	#抓取一帧视频
	ret,frame =video_capture.read()
	#将视频帧调整为1/4大小以进行更快的人脸识别处理
	small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy=0.25)
	#将bgr颜色转换到rgb
	rgb_small_frame = small_frame[:,:,::-1]
		
	#只处理每隔一帧视频
	if process_this_frame:
		#查找当前视频帧中的所有面部和面部编码
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
		
		face_names=[]
		for face_encoding in face_encodings:
			#查看人脸是否与已知人脸匹配
			matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
			name="Unknown"
			
			#如果在已知的编码中找到匹配，只需使用第一个匹配即可。
			if True in matches:
				first_match_index = matches.index(True)
				name = known_face_names[first_match_index]
				
			face_names.append(name)
			
	process_this_frame = not process_this_frame
	#显示结果
	for (top,right,bottom,left),name in zip(face_locations,face_names):
		top *=4
		right *=4
		bottom *=4
		left *=4
		#标记脸部
		cv2.rectangle(frame,(left,top),(right,bottom),(55,255,155),2)
		#在脸下画个有名字标签
		cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
	#展示图片
	cv2.imshow('Video',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
video_capture.release()
cv2.detoryAllWindows()