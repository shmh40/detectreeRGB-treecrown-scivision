import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pooch

# machine learning libraries
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import ColorMode, Visualizer


class DeepForest:
    def __init__(self):
        pass

    def predict(self, image: np.ndarray) -> np.ndarray:
        return image


class DetectreeRGB:
    def __init__(
        self,
        zenodo_source: str = "doi:10.5281/zenodo.5515408/model_final.pth",
        known_hash: str = "md5:24a73ed4422ef4cd4d7d3bfd19bc194a",
    ):

        # define the URL to retrieve the model
        # Pooch can also download based on a DOI from certain providers.
        self.fn = pooch.retrieve(url=zenodo_source, known_hash=known_hash,)

        cfg = get_cfg()

        # If using GPU, hash it out.
        cfg.MODEL.DEVICE = "cpu"

        # model and hyperparameter selection
        cfg.merge_from_file(
            model_zoo.get_config_file(
                "COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml"
            )
        )
        cfg.DATALOADER.NUM_WORKERS = 2
        cfg.SOLVER.IMS_PER_BATCH = 2
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1

        # path to the saved pre-trained model weights
        cfg.MODEL.WEIGHTS = self.fn

        # set confidence threshold at which we predict
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.15

        # Settings for predictions using detectron config
        self.pretrained_model = DefaultPredictor(cfg)

    def show_output(self):

        v = Visualizer(
            self.X[:, :, ::-1], scale=1.5, instance_mode=ColorMode.IMAGE_BW
        )  # remove the colors of unsegmented pixels
        v = v.draw_instance_predictions(self.y["instances"].to("cpu"))
        imagecv2 = cv2.cvtColor(v.get_image()[:, :, :], cv2.COLOR_BGR2RGB)
        plt.imshow(imagecv2)
        plt.show()

    def predict(self, image: np.ndarray) -> np.ndarray:

        # subset RGB bands
        R = image[0]
        G = image[1]
        B = image[2]

        # the rescaling changes according to the values of the image
        rgb = np.dstack((R, G, B))  # BGR for cv2
        rgb_rescaled = 255 * rgb / 65535  # scale to image

        # save this as png
        filepath = os.path.join("sampleImage.png")
        cv2.imwrite(filepath, rgb_rescaled)

        self.X = cv2.imread(filepath)

        self.y = self.pretrained_model(self.X)

        self.show_output()

        return self.y


if __name__ == "__main__":
    pass
