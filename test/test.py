import numpy as np

from detectreeRGB_treecrown_scivision import DetectreeRGB

# create synthetic image
X = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)

model = DetectreeRGB()
y = model.predict(X)
print(y["instances"])


# test with scivision
# from scivision.io import load_dataset
# from intake_zenodo_fetcher import download_zenodo_files_for_entry
#
# cat = load_dataset(
#     ".scivision/data.yaml"
# )
#
# download_zenodo_files_for_entry(cat["sepilok_rgb"], force_download=False)
#
# tc_rgb = cat["sepilok_rgb"].to_dask()
#
# y = model.predict(tc_rgb)
