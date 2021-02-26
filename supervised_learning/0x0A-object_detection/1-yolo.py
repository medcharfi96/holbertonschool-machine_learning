#!/usr/bin/env python3
""" task 1 """
import tensorflow._api.v1.keras as K
import numpy as np
import tensorflow as tf


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

            box_confidences.append(tf.math.sigmoid(zz[..., 4, np.newaxis]))

            box_class_probs.append(tf.math.sigmoid(zz[..., 5:]))

        for i, bx in enumerate(boxes):
            grid_height, grid_width, anchor_boxes, _ = bx.shape

            c = np.zeros((grid_height, grid_width, anchor_boxes), dtype=int)

            Tx = (bx[..., 0])
            Ty = (bx[..., 1])
            Tw = (bx[..., 2])
            Th = (bx[..., 3])

            indx_y = np.arange(grid_height).reshape(grid_height, 1, 1)
            Cy = c + indx_y

            indx_x = np.arange(grid_width).reshape(1, grid_width, 1)
            Cx = c + indx_x

            bx = (tf.math.sigmoid(Tx) + Cx) / grid_width
            by = (tf.math.sigmoid(Ty) + Cy) / grid_height

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

            bx[..., :0] = x1 * img_width
            bx[..., 1:1] = y1 * img_height
            bx[..., 2:2] = x2 * img_width
            bx[..., 3:3] = y2 * img_height

        return boxes, box_confidences, box_class_probs
