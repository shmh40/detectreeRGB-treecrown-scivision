import urllib.request

import numpy as np

# machine learning libraries
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor


class DeepForest:
    def __init__(self):
        pass

    def predict(self, image: np.ndarray) -> np.ndarray:
        return image


class DetectreeRGB:
    def __init__(self, model_source: str = "zenodo"):
        # define the URL to retrieve the model
        if model_source == "zenodo":
            fn = "model_final.pth"
            url = f"https://zenodo.org/record/5515408/files/{fn}?download=1"
            urllib.request.urlretrieve(url, fn)

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
        cfg.MODEL.WEIGHTS = fn

        # set confidence threshold at which we predict
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.15

        # Settings for predictions using detectron config
        self.pretrained_model = DefaultPredictor(cfg)

    def predict(self, image: np.ndarray) -> np.ndarray:

        y = self.pretrained_model(image)
        return y


if __name__ == "__main__":
    pass
