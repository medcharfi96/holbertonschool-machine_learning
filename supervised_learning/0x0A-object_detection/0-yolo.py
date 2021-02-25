#!/usr/bin/env python3
""" task 0 """
import tensorflow.keras as K


class Yolo():
    """
    classe yolo
    """
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """
        constructeur parametré
        :param model_path: chemin
        :param classes_path:chemin de nom de classse
        :param class_t: flot
        :param nms_t:flotant
        :param anchors:
        """
        self.model = K.models.load_model(model_path)
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors
        self.class_names = []
        with open(classes_path, 'r') as fichier:
            for l in fichier:
                z = l.strip()
                self.class_names.append(z)
