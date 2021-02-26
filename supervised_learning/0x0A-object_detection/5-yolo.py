#!/usr/bin/env python3
""" task 1 """
import cv2
import glob
import tensorflow.keras as K
import numpy as np


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
        with open(classes_path, 'r') as fichier:
            for l in fichier:
                z = l.strip()
                self.class_names = [z]

    def sigmoid(self, X):
        """ sigmoid function"""
        return (1 / (1 + np.exp(-X)))

    def process_outputs(self, outputs, image_size):
        """
        des
        """

        img_height, img_width = image_size

        boxes = []
        box_confidences = []
        box_class_probs = []
        for zz in outputs:

            boxes.append(zz[..., 0:4])

            box_confidences.append(self.sigmoid(zz[..., 4:5]))

            box_class_probs.append(self.sigmoid((zz[..., 5:])))

        for i, bx in enumerate(boxes):
            grid_h, grid_w, anchor_boxes, _ = bx.shape

            Tx = bx[..., 0]
            Ty = bx[..., 1]
            Tw = bx[..., 2]
            Th = bx[..., 3]

            Cy = np.indices((grid_h, grid_w, anchor_boxes))[0]

            Cx = np.indices((grid_h, grid_w, anchor_boxes))[1]

            bbx = self.sigmoid(Tx) + Cx
            bby = self.sigmoid(Ty) + Cy

            bx = bbx / grid_w
            by = bby / grid_h
            pw = self.anchors[i, :, 0]
            ph = self.anchors[i, :, 1]
            bw = pw * np.exp(Tw)
            bw = bw / self.model.input.shape[1].value
            bh = ph * np.exp(Th)
            bh = bh / self.model.input.shape[2].value

            x1 = bx - bw / 2
            x2 = x1 + bw
            y1 = by - bh / 2
            y2 = y1 + bh

            x11 = x1 * img_width
            x22 = x2 * img_width
            y11 = y1 * img_height
            y22 = y2 * img_height

            bx[..., 0] = x11
            bx[..., 1] = y11
            bx[..., 2] = x22
            bx[..., 3] = y22

        return boxes, box_confidences, box_class_probs

    @staticmethod
    def load_images(folder_path):
        """ function that load all images of folder_path
        return list of images and list ofimage_path"""
        images = []
        pth = folder_path + '/*'
        image_paths = glob.glob(pth)
        for img in image_paths:
            images.append(cv2.imread(img, 3))
        return images, image_paths

    def preprocess_images(self, images):
        """

        :param images:
        :return:
        """
        lpmg = []
        lpmg_tll = []
        input_w = self.model.input.shape[1].value
        input_h = self.model.input.shape[2].value

        for img in images:
            img_taille = img.shape[:-1]
            lpmg_tll.append(img_taille)
            dim = (input_w, input_h)
            fnl = cv2.resize(img,
                             dim,
                             interpolation=cv2.INTER_CUBIC)
            pimage = fnl / 255
            lpmg.append(pimage)

        pimages = np.array(lpmg)
        image_shapes = np.stack(lpmg_tll, axis=0)
        return pimages, image_shapes
