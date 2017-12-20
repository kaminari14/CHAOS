import cv2
import numpy as np
bcol=[["" for i in range(12)] for j in range(9)]
l_or=np.array([0,0,0])
U_or=np.array([0,0,0])
l_re=np.array([0,0,0])
U_re=np.array([0,0,0])
l_gr=np.array([0,0,0])
U_gr=np.array([0,0,0])
l_bl=np.array([0,0,0])
U_bl=np.array([0,0,0])
l_wh=np.array([0,0,0])
U_wh=np.array([0,0,0])
l_ye=np.array([0,0,0])
U_ye=np.array([0,0,0])


file=open(".colorinfo", "r")

def scancol():
    for q in ['yellow', 'blue','red','green', 'orange', 'white']:
        print ('scan ', q)
        cap = cv2.VideoCapture(1)
        while True:
            ret, frame = cap.read()
            cv2.rectangle(frame, (200, 100), (440, 340), (255, 0, 0), 5)
            frame=frame[100:340, 200:440]
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('p'):
                break
        _,frame=cap.read()

        cv2.imwrite("test.jpg",frame)
        cap.release()
        cv2.destroyAllWindows()
        img=cv2.imread("cface.jpg")

        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        for c in range(2):
            img_yuv[:, :, c] = cv2.equalizeHist(img_yuv[:, :, c])

        #mask = cv2.inRange(img_yuv, cur_down, cur_up)
        #res = cv2.bitwise_and(img, img, mask=mask)

    return bcol





