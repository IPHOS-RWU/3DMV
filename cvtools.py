import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(*images, titles=None, cols=None, size=5):
    n = len(images)

    if titles is None:
        titles = [""] * n

    if cols is None:
        cols = min(n, 3)

    rows = int(np.ceil(n / cols))

    fig, axes = plt.subplots(
        rows, cols,
        figsize=(cols * size, rows * size),
        squeeze=False
    )

    for ax, img, title in zip(axes.flat, images, titles):

        if img is None:
            ax.axis("off")
            continue

        if img.ndim == 2:
            ax.imshow(img, cmap="gray")

        elif img.ndim == 3 and img.shape[2] == 3:
            ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        elif img.ndim == 3 and img.shape[2] == 4:
            ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA))

        else:
            ax.imshow(img)

        ax.set_title(title)
        ax.axis("off")

    for ax in axes.flat[n:]:
        ax.axis("off")

    plt.tight_layout()
    plt.show()