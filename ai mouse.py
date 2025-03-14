import cv2
import mediapipe as mp
import pyautogui
cap =cv2.VideoCapture(0)
hand_dector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
s_width,s_higth=pyautogui.size()
index_y=0
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_heigth , frame_weight,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output =hand_dector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    #print(hands)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_weight)
                y=int(landmark.y*frame_heigth)
                #print(x,y)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,255,255))
                    index_x=s_width/frame_weight*x
                    index_y=s_higth/frame_heigth*y
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,255,255))
                    thumb_x=s_width/frame_weight*x
                    thumb_y=s_higth/frame_heigth*y
                    print(abs(index_y-thumb_y))
                    if abs(index_y-thumb_y)<50:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Ai mouse',frame)
    cv2.waitKey(1)