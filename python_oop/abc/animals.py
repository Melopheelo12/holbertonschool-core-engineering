#!/usr/bin/env python3
"""Module définissant Shape, Circle, Rectangle et shape_info."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique."""

    @abstractmethod
    def area(self) -> float:
        """Retourne l'aire de la forme."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        """Retourne le périmètre de la forme."""
        raise NotImplementedError


class Circle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe représentant un rectangle."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d'une forme.

    Utilise le duck typing (aucun isinstance).
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
