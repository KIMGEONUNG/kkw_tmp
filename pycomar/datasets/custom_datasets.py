import torch.utils.data as data
from torchvision.datasets.folder import default_loader
from typing import Tuple, Any, Optional, Callable, List, Dict
from imagenet_index import IMAGENET_INDEX
import os


class ImageNetIndexDataset(data.Dataset):

  def __init__(
      self,
      root: str,
      transform: Optional[Callable] = None,
      target_transform: Optional[Callable] = None,
      post_processings: Optional[List[Callable]] = None,
  ) -> None:

    self.root = os.path.expanduser(root)
    self.loader = default_loader

    self.allowed_extensions = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm',
                               '.tif', '.tiff', '.webp')
    self.samples = self.make_dataset(self.root, IMAGENET_INDEX)
    self.targets = [s[1] for s in self.samples]

    self.transform = transform
    self.target_transform = target_transform
    self.additional_processings = post_processings

  def make_dataset(
      self,
      directory: str,
      class_to_idx: [Dict[str, int]],
  ) -> List[Tuple[str, int]]:
    directory = os.path.expanduser(directory)

    instances = []
    for target_class in sorted(class_to_idx.keys()):
      class_index = class_to_idx[target_class]
      target_dir = os.path.join(directory, target_class)
      if not os.path.isdir(target_dir):
        continue
      for root, _, fnames in sorted(os.walk(target_dir, followlinks=True)):
        for fname in sorted(fnames):
          if self.is_valid_file(fname):
            path = os.path.join(root, fname)
            item = path, class_index
            instances.append(item)

    return instances

  def is_valid_file(self, filename: str) -> bool:
    return filename.lower().endswith(self.allowed_extensions)

  def __getitem__(self, index: int) -> Tuple[Any, Any]:
    path, target = self.samples[index]
    sample = self.loader(path)
    if self.transform is not None:
      sample = self.transform(sample)
    if self.target_transform is not None:
      target = self.target_transform(target)

    if self.additional_processings is not None:
      samples = [p(sample) for p in self.additional_processings]

    return tuple([sample] + samples + [target])

  def __len__(self) -> int:
    return len(self.samples)
