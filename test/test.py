import numpy as np

from scivision_treecrown_plugin import DetectreeRGB

# create synthetic image
X = np.random.randint(255, size=(900, 800, 3), dtype=np.uint8)

model = DetectreeRGB()
y = model.predict(X)
print(y["instances"])


# test with scivision
# from intake_zenodo_fetcher import download_zenodo_files_for_entry
# from scivision.io import load_dataset
#
# cat = load_dataset(
#     "https://github.com/acocac/scivision-forest-datasets/drone_tropics.yml"
# )
#
# download_zenodo_files_for_entry(cat["sepilok_rgb"], force_download=False)
#
# tc_rgb = cat["sepilok_rgb"].to_dask()
#
# y = model.predict(tc_rgb)
