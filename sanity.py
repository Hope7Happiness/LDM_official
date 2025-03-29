import numpy as np

data = np.load('./data/celebahq/114512.npy')
assert data.shape == (1024, 1024, 3), 'Get shape: {}'.format(data.shape)
assert data.dtype == np.uint8, 'Get dtype: {}'.format(data.dtype)

# visualize the image
from PIL import Image
import os

img = (data)
os.makedirs('tmp', exist_ok=True)
img.save('tmp/example.png')