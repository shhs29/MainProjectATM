import cv2
import time
from threading import Thread

class Video:
    def __init__(self):       
        self.camara1 = cv2.VideoCapture(0)
        self.iniciar_video=True
        self.estoy_vivo=True
        self.thread = Thread(target=self.mantiene_vivo, args=())
        self.thread.daemon = True
        self.thread.start()

    def mantiene_vivo(self):
        self.inicia_video()
        while self.estoy_vivo:
            time.sleep(10) 

    def detener(self):
        self.iniciar_video=False

    def inicia_video(self):
        print("Iniciando")

        self.iniciar_video=True

        self.camara1.open(0)

        while self.iniciar_video:

            ret1,captura1= self.camara1.read() 
            if(ret1):
                cv2.imshow('img',captura1)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                self.iniciar_video=False
                self.detener()
                break    
        cv2.destroyAllWindows() 
        self.camara1.release()

ObjVideo = Video()
time.sleep(10) 
print("Finish 1")
ObjVideo.detener() 
time.sleep(10) 
ObjVideo.inicia_video()
time.sleep(10)
print("Finish 2")
ObjVideo.detener() 
time.sleep(10) 
ObjVideo.inicia_video()
