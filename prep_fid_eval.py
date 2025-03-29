import bisect
import numpy as np
import albumentations
from PIL import Image
from torch.utils.data import Dataset, ConcatDataset
import os
from tqdm import trange

# class ConcatDatasetWithIndex(ConcatDataset):
#     """Modified from original pytorch code to return dataset idx"""
#     def __getitem__(self, idx):
#         if idx < 0:
#             if -idx > len(self):
#                 raise ValueError("absolute value of index should not exceed dataset length")
#             idx = len(self) + idx
#         dataset_idx = bisect.bisect_right(self.cumulative_sizes, idx)
#         if dataset_idx == 0:
#             sample_idx = idx
#         else:
#             sample_idx = idx - self.cumulative_sizes[dataset_idx - 1]
#         return self.datasets[dataset_idx][sample_idx], dataset_idx


class ImagePaths(Dataset):
    def __init__(self, paths, size=None, random_crop=False, labels=None):
        self.size = size
        self.random_crop = random_crop

        self.labels = dict() if labels is None else labels
        self.labels["file_path_"] = paths
        self._length = len(paths)

        if self.size is not None and self.size > 0:
            self.rescaler = albumentations.SmallestMaxSize(max_size = self.size)
            if not self.random_crop:
                self.cropper = albumentations.CenterCrop(height=self.size,width=self.size)
            else:
                self.cropper = albumentations.RandomCrop(height=self.size,width=self.size)
            self.preprocessor = albumentations.Compose([self.rescaler, self.cropper])
        else:
            self.preprocessor = lambda **kwargs: kwargs

    def __len__(self):
        return self._length

    def preprocess_image(self, image_path):
        image = Image.open(image_path)
        if not image.mode == "RGB":
            image = image.convert("RGB")
        image = np.array(image).astype(np.uint8)
        image = self.preprocessor(image=image)["image"]
        image = (image/127.5 - 1.0).astype(np.float32)
        return image

    def __getitem__(self, i):
        example = dict()
        example["image"] = self.preprocess_image(self.labels["file_path_"][i])
        for k in self.labels:
            example[k] = self.labels[k][i]
        return example


# class NumpyPaths(ImagePaths):
#     def preprocess_image(self, image_path):
#         image = np.load(image_path)
#         image = Image.fromarray(image, mode="RGB")
#         image = np.array(image).astype(np.uint8)
#         image = self.preprocessor(image=image)["image"]
#         assert image.dtype == np.uint8, f"{image.dtype=}"
#         # image = (image/127.5 - 1.0).astype(np.float32)
#         return image
    
root = './data/ffhq'
with open("data/ffhqtrain.txt", "r") as f:
    relpaths = f.read().splitlines()
paths = [os.path.join(root, relpath) for relpath in relpaths]
data = ImagePaths(paths=paths, size=256, random_crop=False)
# data = NumpyPaths(paths=paths, size=256, random_crop=False)

out_dir = './eval_fid/ffhq256_ref'
os.makedirs(out_dir, exist_ok=True)

import concurrent.futures

def worker_fn(i, example, out_dir):
    image = example['image']
    image = (image + 1.0) * 127.5
    image = image.astype(np.uint8)
    image = Image.fromarray(image, mode='RGB')
    image.save(f'{out_dir}/{i:05d}.png')

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    futures = [executor.submit(worker_fn, i, data[i], out_dir) for i in trange(len(data))]
    concurrent.futures.wait(futures)


## sanity: validation
# root = './data/celebahq'
# with open("data/celebahqvalidation.txt", "r") as f:
#     relpaths = f.read().splitlines()
# paths = [os.path.join(root, relpath) for relpath in relpaths]
# data = NumpyPaths(paths=paths, size=256, random_crop=False)

# out_dir = './eval_fid/celeba256_ref_valid_sanity'
# os.makedirs(out_dir, exist_ok=True)

# import concurrent.futures

# def worker_fn(i, example, out_dir):
#     image = example['image']
#     image = Image.fromarray(image, mode='RGB')
#     image.save(f'{out_dir}/{i:05d}.png')

# with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
#     futures = [executor.submit(worker_fn, i, data[i], out_dir) for i in trange(len(data))]
#     concurrent.futures.wait(futures)