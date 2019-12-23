import cv2
import numpy as np
import sqlite3

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("Subjects.db")
    cmd="SELECT * FROM Subjects WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Subjects SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Subjects(ID,Name) Values("+str(Id)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
        
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

id=raw_input('Enter user id: ')
name=raw_input('Enter user name: ')
insertOrUpdate(id,name)

sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataSet/user."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if (sampleNum>50):
        break
cam.release()
cv2.destroyAllWindows()
