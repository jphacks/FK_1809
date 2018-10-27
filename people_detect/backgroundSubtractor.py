import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # save a picture when this program start
        if count == 0:
            copyframe = frame.copy()

        fgmask = fgbg.apply(copyframe)
        fgmask = fgbg.apply(frame)

        cv2.imshow("frame", fgmask)
        
        count = 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
