#!/usr/bin/env python3
"""
Complex utility functions for working with pentagons.
"""
import cmath


def create_polygon(num_sides, radius, center):
    """
    Create the vertices of a pentagon.

    Arguments:
        num_sides: int
            Number of sides of polygon.
        radius:
            Radius of circumscribing circle.
        center: complex
            Center of pentagon.

    Returns:
        list(tuple(float, float))
            List of pentagon vertices sorted in anti-clockwise order.
    """
    return [
        center + complex(cmath.rect(radius, x / num_sides * cmath.tau))
        for x in range(num_sides)
    ]


def rotate_points(points, phase_shift):
    """
    Rotate a point about the origin.

    Arguments:
        points: iterable(complex)
            Points to rotate in the complex plane.
        phase_shift:
            Magnitude of rotation in radians.

    Returns:
        rotated_points: list(complex)
            Points rotated about the origin.
    """
    rotated_points = []
    for point in points:
        rad, phase = cmath.polar(point)
        rotated_points.append(cmath.rect(rad, phase + phase_shift))

    return rotated_points
