import cv2
import numpy as np
import os 

def do_everything():
    v = open("namesofviolators.txt", 'w')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Aditya', "Rohan", "Kohav"] 
    # Initialize and start realtime video capture
    
    for pic in sorted(os.listdir("Violators")):
        img = cv2.imread("Violators/" + pic) 
        # Define min window size to be recognized as a face
        
        minW = img.shape[0]
        minH = img.shape[1]
        #ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            #cv2.putText(
            #            img, 
            #            str(id), 
            #            (x+5,y-5), 
            #            font, 
            #            1, 
            #            (255,255,255), 
            #            2
            #           )
            #cv2.putText(
            #            img, 
            #            str(confidence), 
            #            (x+5,y+h-5), 
            #            font, 
            #            1, 
            #            (255,255,0), 
            #            1
            #           )  
        v.write(str(id) + "\n") 
        
     
