import qrcode
from tkinter import *
import cv2
import numpy as np
from pyzbar.pyzbar import decode
w=Tk()
#b2=Button()
e=Entry(w,width=50)
e.pack()
e.insert(0,"enter name:")
e1=Entry(w,width=50)
e1.pack()
e1.insert(0,"enter number")
def gen():
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    data=e1.get()
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save(e.get()+".png")
def sca():
    cap=cv2.VideoCapture(0)
    cap.set(3,700)
    cap.set(4,500)
    with open('qrlist.txt') as f:
        mydl=f.read().splitlines()
    #print(mydl)
    while(1):
        s,img=cap.read()
        for barcode in decode(img):
            mydata=barcode.data.decode('utf-8')
            #print(mydata)
            """
            if((mydata) in mydl):
                op='Authorized'
                myc=(0,255,0)
            else:
                op='unAuthorized'
                myc=(0,0,255)
            """
            pts=np.array([barcode.polygon],np.int32)
            pts=pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(0,255,0),5)
            pts2=barcode.rect
            cv2.putText(img,mydata,(10,50),cv2.FONT_ITALIC,0.9,(0,0,255),2)
        cv2.imshow('result',img)
        if(cv2.waitKey(20) & 0xFF==ord("q")):
            break
           
    cv2.destroyAllWindows()

    
b1=Button(w,text="generate",command=gen).pack()
b2=Button(w,text="scan",command=sca).pack()

    

w.mainloop()
