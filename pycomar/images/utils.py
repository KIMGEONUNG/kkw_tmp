import numpy as np
import torch
from torchvision.transforms import ToPILImage, ToTensor
import matplotlib.pyplot as plt
from PIL import Image
from os.path import exists
from typing import List
# from warnings import warn


def cvimg2torchimg(x: np.array):
    assert isinstance(x, np.array)
    x = torch.from_numpy(x) / 255.0
    x = x.permute(2, 0, 1)[::-1, ...]
    return x


def torchimg2cvimg(x: torch.Tensor):
    assert isinstance(x, torch.Tensor)
    x: np.array = (x.numpy() * 255).astype('uint8')
    x = x.transpose(1, 2, 0)[..., ::-1]
    return x


# def cv2torch_img(x: np.array):
#     warn('This method \'%s\' is deprecated' % cv2torch_img.__name__,
#             DeprecationWarning, stacklevel=2)
#     assert isinstance(x, np.array)
#     x = torch.from_numpy(x)
#     x = x.permute(2, 0, 1)
#     return x
#
#
# def torch2cv_img(x: torch.Tensor):
#     warn('This method \'%s\' is deprecated' % torch2cv_img.__name__,
#             DeprecationWarning, stacklevel=2)
#     assert isinstance(x, torch.Tensor)
#     x: np.array = x.numpy()
#     x = x.transpose(1, 2, 0)
#     return x


def gray2jet(x: np.array):
    assert isinstance(x, np.array)
    colormap = plt.get_cmap('jet')
    x = colormap(x)[..., :3]
    return x


def mk_trimap(f: np.array, b: np.array, threshold_f=0.8, threshold_b=0.4):
    assert isinstance(f, np.array)
    assert isinstance(b, np.array)
    assert f.shape == b.shape
    trimap = np.ones_like(f) * 0.5
    trimap[f > threshold_f] = 1.0
    trimap[b > threshold_b] = 0.0
    return trimap


def overlay(rgb: np.array, gray: np.array, alpha=0.5):
    assert isinstance(rgb, np.array)
    assert isinstance(gray, np.array)
    jet = gray2jet(gray)
    x = alpha * jet + (1 - alpha) * rgb
    return x


def cv2pil(x):
    """
    We assume that a range of values is 0 to 1.
    """
    return Image.fromarray((x[..., :3]).astype('uint8'))


def torch2pil(x):
    """
    We assume that a range of values is 0 to 1.
    """
    return ToPILImage()(x.detach().cpu())


def show_img(x):
    """
    We assume that a range of values is 0 to 1.
    """
    if isinstance(x, np.ndarray):
        im = cv2pil(x)
        im.show()

    if isinstance(x, torch.Tensor):
        im = torch2pil(x)
        im.show()


def show3plt(xs: List[torch.Tensor]):
    import matplotlib.pyplot as plt

    plt.rcParams["figure.figsize"] = (20, 20)

    num_img = len(xs)
    num_edge = int(num_img ** 0.5)

    for i in len(xs):
        plt.subplot(num_edge, num_edge, i + 1)
        plt.imshow(ToPILImage()(xs[i]))

    plt.tight_layout()
    plt.show()
    plt.clear()


def load_img(path: str):
    assert exists(path)
    return ToTensor()(Image.open(path))


if __name__ == '__main__':
    # x = torch.randn(3, 100, 100)
    # show_img(x)
    x = np.random.randn(100, 100, 3)
    show_img(x)
    torchimg2cvimg(torch.randn(3,10,10))
