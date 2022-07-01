import np
import torch
import matplotlib.pyplot as plt


def cv2torch_img(x: np.array):
    x = torch.from_numpy(x)
    x = x.permute(2, 0, 1)
    return x


def torch2cv_img(x: torch.Tensor):
    x: np.array = x.numpy()
    x = x.transpose(1, 2, 0)
    return x


def gray2jet(x: np.array):
    colormap = plt.get_cmap('jet')
    x = colormap(x)[..., :3]
    return x


def mk_trimap(f: np.array, b: np.array, threshold_f=0.8, threshold_b=0.4):
    assert f.shape == b.shape
    trimap = np.ones_like(f) * 0.5
    trimap[f > threshold_f] = 1.0
    trimap[b > threshold_b] = 0.0
    return trimap


def overlay(rgb: np.array, gray: np.array, alpha=0.5):
    jet = gray2jet(gray)
    x = alpha * jet + (1 - alpha) * rgb
    return x
