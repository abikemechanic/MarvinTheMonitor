import cv2 as cv
import imagezmq
import numpy as np
import threading


class ImageZMQController:
    def __init__(self):
        self.image_dict = {}
        self.hub = imagezmq.ImageHub()
        self.server_name = 'ImageZMQ_Hub'
        self.image_thread = threading.Thread(target=self.run_server, daemon=True)
        self.image_thread.start()

    def run_server(self):
        print('starting zmq server')
        with imagezmq.ImageHub(open_port='tcp://*555') as image_hub:
            while 1:
                recv_name, jpg_buffer = image_hub.recv_jpg()
                self.image_dict[recv_name] = jpg_buffer
                image_hub.send_reply(b'OK')


class ImageStorage:
    def __init__(self):
        self.img_hub = ImageZMQController()

    def get_image_dict(self):
        return self.img_hub.image_dict
