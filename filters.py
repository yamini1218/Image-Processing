#all OpenCV functions
import cv2
from PIL import ImageFilter, ImageEnhance
from utils import pil_to_np, np_to_pil, ensure_rgb, to_grayscale_np, validate_thresholds, brightness_factor, sharpness_factor, contrast_factor

def apply_filters(image, blur, sharpness, bright, contrast, edge, gray, thresh1, thresh2):

    if blur > 0:
        image = apply_blur(image, blur)

    if sharpness != 0.0:
        image = apply_sharpness(image, sharpness)

    if bright != 0:
        image = apply_brightness(image, bright)

    if contrast != 0.0:
        image = apply_contrast(image, contrast)

    if gray:
        image = apply_grayscale(image)

    if edge and validate_thresholds(thresh1, thresh2):
        image = apply_edge(image, thresh1, thresh2)

    return image


def apply_blur(image, blur):
    return image.filter(ImageFilter.GaussianBlur(radius=blur))


def apply_sharpness(image, sharpness):
    enhancer = ImageEnhance.Sharpness(image)
    factor = sharpness_factor(sharpness)
    return enhancer.enhance(factor)


def apply_brightness(image, bright):
    enhancer = ImageEnhance.Brightness(image)
    factor = brightness_factor(bright)
    return enhancer.enhance(factor)


def apply_contrast(image, contrast):
    enhancer = ImageEnhance.Contrast(image)
    factor = contrast_factor(contrast)
    return enhancer.enhance(factor)


def apply_edge(image, thresh1, thresh2):
    image = ensure_rgb(image)
    img_np = pil_to_np(image)
    gray = to_grayscale_np(img_np)
    edges = cv2.Canny(gray, thresh1, thresh2)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return np_to_pil(edges_rgb)


def apply_grayscale(image):
    return image.convert("L")
