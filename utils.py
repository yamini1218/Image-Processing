#Helper Functions
import numpy as np
from PIL import Image

def pil_to_np(image):
    return np.array(image)


def np_to_pil(arr):
    return Image.fromarray(arr)


def ensure_rgb(image):
    if image.mode != "RGB":
        return image.convert("RGB")
    return image


def to_grayscale_np(image_np):
    import cv2
    return cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)


def validate_thresholds(t1, t2):
    if t1 is None or t2 is None:
        return False
    return t1 < t2


def brightness_factor(bright):
    return (bright + 100) / 100


def sharpness_factor(value):
    return 1.0 + value


def contrast_factor(value):
    return 1.0 + value