#!/usr/bin/env python3
"""
Functions to render final picture
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np

plt.rcParams["figure.figsize"] = (30, 30)


def plot_pentagons(pentagons, fpath):
    """
    Plots a sequence of pentagons and corresponding pentagrams.

    Arguments:
        pentagons: list(tuple(float, float))
            A list of pentagon vertices.
    """
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    for i, points in enumerate(pentagons):
        coords = [(x.real, x.imag) for x in points]

        plt.plot(*zip(*(coords + coords)[3:8]), c="black")

        star_edges = list(zip((coords + coords)[2:], coords[:-1]))
        if i == 0:
            star_edges += [[coords[1], coords[-1]]]

        for star_edge in star_edges:
            plt.plot(
                [star_edge[0][0], star_edge[1][0]],
                [star_edge[0][1], star_edge[1][1]],
                c="black",
                ls="--",
                lw=1,
            )

        perimeter = coords[-3:] + coords[:-2]
        plt.plot(*zip(*perimeter), c="black", ls="-.")

    canvas = FigureCanvasAgg(fig)
    canvas.draw()

    stream, (width, height) = canvas.print_to_buffer()
    img = np.fromstring(stream, np.uint8).reshape((height, width, 4))

    img = _trim_border(img)

    plt.imsave(fpath, img, format="svg")


def _trim_border(img):
    """
    Trims white space border of a numpy image.

    Arguments:
        img: np.array
            Numpy image.

    Returns:
        img: np.array
            Numpy image with no white border space.
    """
    for i in range(img.shape[0]):
        if np.any(img[i, :, :] != 255):
            img = img[i:, :, :]
            break

    for i in range(img.shape[0] - 1, 0, -1):
        if np.any(img[i, :, :] != 255):
            img = img[: i + 1, :, :]
            break

    for i in range(img.shape[1]):
        if np.any(img[:, i, :] != 255):
            img = img[:, i:, :]
            break

    for i in range(img.shape[1] - 1, 0, -1):
        if np.any(img[:, i, :] != 255):
            img = img[:, : i + 1, :]
            break

    return img
