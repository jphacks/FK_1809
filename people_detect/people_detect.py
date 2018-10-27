import cv2
import numpy as np 
import datetime
import subprocess
from chainercv.links import SSD300
from chainercv.datasets import voc_bbox_label_names
from datetime import datetime

model = SSD300(n_fg_class=len(voc_bbox_label_names), pretrained_model='voc0712')
last_shot_time = datetime.now()

def crop_human(img):
    input_img = img.transpose(2, 0, 1)
    bboxes, labels, score = model.predict([input_img])
    
    if 14 in labels[0]:# labels[14] is human
        img = img
        print(bboxes)
        bbox = [int(i) for i in bboxes[0][0]]
        cropped_img = img[bbox[0]:bbox[2], bbox[1]:bbox[3], :]
        return cropped_img, score[0][0]
    
    return np.array([]), 0

def use_chainercv(frame):
    cropped_img, score = crop_human(frame)
    if len(cropped_img) > 0:
        h, w, c = cropped_img.shape
    print('Score: ' + str(score))

    if h > 0 and w > 0:
        cv2.imshow('cropped', cropped_img)
    else:
        pass
        
    cv2.imshow('img', frame)

def use_cascade(frame, face_cascade):
    global last_shot_time
    save_path = '../people_detect/outputs/'

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    # Create clf use Hog feature and SVM
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParam = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}

    human, r = hog.detectMultiScale(gray, **hogParam)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    margin = 1

    '''
    for (mx, my, mw, mh) in human:
        cv2.rectangle(frame, (mx, my), (mx + mw, my + mh), (0, 0, 200), 3)
        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)
    '''

    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)

    for (mx, my, mw, mh) in human:
        cv2.rectangle(frame, (mx, my), (mx + mw, my + mh), (0, 0, 200), 3)

    if len(human) > 0 and len(faces) > 0:
        mx = human[0][0]
        my = human[0][1]
        mw = human[0][2]
        mh = human[0][3]

        fx = faces[0][0]
        fy = faces[0][1]
        fw = faces[0][2]
        fh = faces[0][3]

        if (mx < fx) and (my - int(fh/margin) < fy) and (mx + mw > fx + fw) and (my + mh > fy + fh):
            dst = frame[my:my+mh, mx:mx+mw]
            print(str(my-int(fh/margin)) +", "+ str(my+mh) +", "+ str(mx) +", "+ str(mx+mw))
            if (True or (datetime.now() - last_shot_time).total_seconds() > 5): 
                cv2.imwrite(save_path + now + ".jpg", dst)
                last_shot_time = datetime.now()
                subprocess.Popen(["./bin/rails", "image:import[" + save_path + now + '.jpg]'])

            #print('mx: '+str(mx).rjust(4)+'\t'+' my: '+str(my).rjust(4)+'\t'
            #        +' mw: '+str(mw).rjust(4)+'\t'+' mh: '+str(mh).rjust(4)+'\t'
            #        +' fx: '+str(fx).rjust(4)+'\t'+' fy: '+str(fy).rjust(4)+'\t'
            #        +' fw: '+str(fw).rjust(4)+'\t'+' fh: '+str(fh).rjust(4))

    cv2.imshow('cascade', frame)

def main():
    cap = cv2.VideoCapture(0)
    #cap.set(cv2.CAP_PROP_FPS, 2)
    cap.set(3,640)
    cap.set(4,480)

    # Read cascade file
    face_cascade = cv2.CascadeClassifier('../people_detect/haarcascade_frontalface_default.xml')

    while(cap.isOpened()):
        # Get camera image
        ret, frame = cap.read()

        #use_chainercv(frame)
        use_cascade(frame, face_cascade)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
