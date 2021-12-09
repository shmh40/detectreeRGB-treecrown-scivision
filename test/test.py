import cv2
import intake
import numpy as np
from detectron2.utils.visualizer import ColorMode, Visualizer
from intake_zenodo_fetcher import download_zenodo_files_for_entry
from IPython.display import display
from PIL import Image

from scivision_treecrown_plugin import DetectreeRGB

# write a catalog YAML file
catalog_file = "../catalog.yaml"

with open(catalog_file, "w") as f:
    f.write(
        """
sources:
  sepilok_rgb:
    driver: rasterio
    description: 'NERC RGB images of Sepilok, Sabah, Malaysia (collection)'
    metadata:
      zenodo_doi: "10.5281/zenodo.5494629"
    args:
      urlpath: "{{ CATALOG_DIR }}/Sep_2014_RGB_602500_646600.tif"
      """
    )

cat_tc = intake.open_catalog(catalog_file)

download_zenodo_files_for_entry(cat_tc["sepilok_rgb"], force_download=False)

tc_rgb = cat_tc["sepilok_rgb"].to_dask()

R = tc_rgb[0]
G = tc_rgb[1]
B = tc_rgb[2]

# stack up the bands and rescale to 0-255 range for cv2

# you will have to change the rescaling depending on the values of your tiff!
rgb = np.dstack((R, G, B))  # BGR for cv2
rgb_rescaled = 255 * rgb / 65535  # scale to image

# save as png
filepath = "tile.png"

cv2.imwrite(filepath, rgb_rescaled)

X = cv2.imread(filepath)

model = DetectreeRGB()
y = model.predict(X)

v = Visualizer(
    X[:, :, ::-1], scale=1.5, instance_mode=ColorMode.IMAGE_BW
)  # remove the colors of unsegmented pixels
v = v.draw_instance_predictions(y["instances"].to("cpu"))
image = cv2.cvtColor(v.get_image()[:, :, :], cv2.COLOR_BGR2RGB)
display(Image.fromarray(image))
