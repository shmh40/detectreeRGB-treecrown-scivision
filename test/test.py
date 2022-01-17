import cv2
import numpy as np
from PIL import Image

from scivision_treecrown_plugin import DetectreeRGB

# save as png
filepath = "tile.png"

rgb = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)

img = Image.fromarray(rgb)
img.save(filepath)

X = cv2.imread(filepath)

model = DetectreeRGB()
y = model.predict(X)
print(y["instances"])
