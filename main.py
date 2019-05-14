#!/usr/bin/env python3
"""
Generates a figure of The Lute of Pythagoras.
"""
import argparse
import cmath

from src.renderer import plot_pentagons
from src.complex_util import create_polygon, rotate_points


def main(num_pentagrams, fpath):
    """
    Create a Lute of Pythagoras image.

    Arguments:
        num_pentagrams: int
            Number of pentagons to subsequently nest.
        fpath: str
            File path to save image to.
    """
    pentagons = []
    center = complex(0, 0)
    radius = 1

    for _ in range(num_pentagrams):
        vertices = create_polygon(5, radius, center)
        pentagons.append(vertices)

        center += cmath.rect(radius, cmath.pi)
        mag, _ = cmath.polar(center - vertices[-2])
        radius *= mag / radius

    pentagons = [rotate_points(x, cmath.tau / 10) for x in pentagons]

    plot_pentagons(pentagons, fpath)


def parse_arguments():
    """
    Main CLI for interfacing with Lute of Pythagoras drawing application.

    Returns:
        argparse.Namespace
            Argparse namespace containg CLI inputs.
    """
    parser = argparse.ArgumentParser(
        description=("Lute of Pythagoras draw application.")
    )

    parser.add_argument(
        "num_pentagrams", type=int, help=("Number of pentagons to subsequently nest.")
    )
    parser.add_argument("fpath", type=str, help="File path to save image to")

    return parser.parse_args()


def assert_argument_vals(args):
    """
    Various asserts to enforce CLI arguments passed are valid.

    Arguments:
        args: argparse.Namespace
            Argparse namespace containg CLI inputs.
    """
    assert args.num_pentagrams >= 1, "Invalid amount of pentagrams passed."


if __name__ == "__main__":
    ARGS = parse_arguments()

    assert_argument_vals(ARGS)

    main(ARGS.num_pentagrams, ARGS.fpath)
